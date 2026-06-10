from dataclasses import dataclass
from typing import Dict, List, Optional

from antlr4.Token import Token
from antlr4.error.ErrorListener import ErrorListener

from ANTLR4_generated.ArnoldCParser import ArnoldCParser
from ANTLR4_generated.ArnoldCVisitor import ArnoldCVisitor


@dataclass
class Diagnostic:
    severity: str
    line: int
    column: int
    message: str
    hint: Optional[str] = None


@dataclass
class FunctionInfo:
    name: str
    arity: int
    returns_value: bool
    line: int
    column: int


TOKEN_DESCRIPTIONS = {
    ArnoldCParser.START: "`IT'S SHOWTIME` - początek programu",
    ArnoldCParser.END: "`YOU HAVE BEEN TERMINATED` - koniec programu",
    ArnoldCParser.PRINT: "`TALK TO THE HAND` - wypisanie wartości",
    ArnoldCParser.DECLARE: "`HEY CHRISTMAS TREE` - deklaracja zmiennej",
    ArnoldCParser.SET_INIT: "`YOU SET US UP` - wartość początkowa",
    ArnoldCParser.ASSIGN_VAR_START: "`GET TO THE CHOPPER` - początek przypisania",
    ArnoldCParser.ASSIGN_VAR_VALUE: "`HERE IS MY INVITATION` - pierwszy operand przypisania",
    ArnoldCParser.ASSIGN_VAR_END: "`ENOUGH TALK` - koniec przypisania",
    ArnoldCParser.IF: "`BECAUSE I'M GOING TO SAY PLEASE` - instrukcja if",
    ArnoldCParser.ELSE: "`BULLSHIT` - gałąź else",
    ArnoldCParser.ENDIF: "`YOU HAVE NO RESPECT FOR LOGIC` - koniec if",
    ArnoldCParser.WHILE: "`STICK AROUND` - pętla while",
    ArnoldCParser.ENDWHILE: "`CHILL` - koniec while",
    ArnoldCParser.FUNC_START: "`LISTEN TO ME VERY CAREFULLY` - początek funkcji",
    ArnoldCParser.FUNC_END: "`HASTA LA VISTA, BABY` - koniec funkcji",
    ArnoldCParser.CALL: "`DO IT NOW` - wywołanie funkcji",
    ArnoldCParser.CALL_ASSIGN: "`GET YOUR ASS TO MARS` - zapis wyniku funkcji",
    ArnoldCParser.RETURN: "`I'LL BE BACK` - return",
    ArnoldCParser.NUMBER: "liczba",
    ArnoldCParser.STRING: "napis w cudzysłowie",
    ArnoldCParser.IDENTIFIER: "nazwa zmiennej lub funkcji",
    Token.EOF: "koniec pliku",
}


class ArnoldCErrorListener(ErrorListener):
    def __init__(self, diagnostics: List[Diagnostic]):
        super().__init__()
        self.diagnostics = diagnostics

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if recognizer.__class__.__name__.endswith("Lexer"):
            self._add_lexer_error(line, column, msg)
            return

        token_type = offendingSymbol.type if offendingSymbol is not None else None
        token_text = offendingSymbol.text if offendingSymbol is not None else ""
        expected = self._expected_tokens(recognizer)

        if token_type == ArnoldCParser.ERROR_TOKEN:
            message = "Użyto specjalnego tokenu błędu."
            hint = "Usuń `WHAT THE FUCK DID I DO WRONG`; ten tekst istnieje tylko jako jawny marker błędu."
        elif token_type == Token.EOF:
            message = "Nieoczekiwany koniec pliku."
            hint = self._hint_for_expected(expected) or "Sprawdź, czy domknięto program, funkcję, pętlę albo instrukcję warunkową."
        else:
            message = f"Nieoczekiwany token `{token_text}`."
            hint = self._hint_for_expected(expected)

        self.diagnostics.append(Diagnostic("error", line, column, message, hint))

    def _add_lexer_error(self, line: int, column: int, msg: str):
        fragment = msg.split(":", 1)[1].strip() if ":" in msg else msg
        self.diagnostics.append(
            Diagnostic(
                "error",
                line,
                column,
                f"Nieznany znak lub fragment programu {fragment}.",
                "Sprawdź literówkę w słowie kluczowym, nazwie albo niedomknięty napis.",
            )
        )

    def _expected_tokens(self, recognizer):
        try:
            return recognizer.getExpectedTokens()
        except Exception:
            return None

    def _hint_for_expected(self, expected) -> Optional[str]:
        if expected is None:
            return None

        important_tokens = [
            ArnoldCParser.START,
            ArnoldCParser.END,
            ArnoldCParser.SET_INIT,
            ArnoldCParser.ASSIGN_VAR_VALUE,
            ArnoldCParser.ASSIGN_VAR_END,
            ArnoldCParser.ENDIF,
            ArnoldCParser.ENDWHILE,
            ArnoldCParser.FUNC_END,
            ArnoldCParser.CALL,
            ArnoldCParser.NUMBER,
            ArnoldCParser.STRING,
            ArnoldCParser.IDENTIFIER,
        ]
        matches = [
            TOKEN_DESCRIPTIONS[token_type]
            for token_type in important_tokens
            if self._contains(expected, token_type)
        ]

        if not matches:
            return None
        if len(matches) == 1:
            return f"Oczekiwano: {matches[0]}."
        return "Oczekiwano jednego z: " + ", ".join(matches[:5]) + "."

    def _contains(self, expected, token_type: int) -> bool:
        try:
            return expected.contains(token_type)
        except AttributeError:
            return token_type in expected


class SemanticAnalyzer(ArnoldCVisitor):
    def __init__(self):
        self.diagnostics: List[Diagnostic] = []
        self.functions: Dict[str, FunctionInfo] = {}
        self.scopes: List[Dict[str, object]] = []
        self.current_function: Optional[FunctionInfo] = None
        self.current_function_has_value_return = False

    def visitProgram(self, ctx):
        self._collect_functions(ctx.funcDecl())

        for func_ctx in ctx.funcDecl():
            self.visit(func_ctx)

        self._push_scope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self._pop_scope()
        return None

    def visitFuncDecl(self, ctx):
        name_token = ctx.IDENTIFIER().getSymbol()
        function = self.functions.get(name_token.text)
        previous_function = self.current_function
        previous_return_state = self.current_function_has_value_return

        self.current_function = function
        self.current_function_has_value_return = False
        self._push_scope()

        for arg in ctx.funcArg():
            self._declare_variable(arg.IDENTIFIER().getSymbol(), "argument funkcji")

        for stmt in ctx.statement():
            self.visit(stmt)

        if function is not None and function.returns_value and not self.current_function_has_value_return:
            self._add_error(
                name_token,
                f"Funkcja `{function.name}` deklaruje zwracanie wartości, ale nie ma `I'LL BE BACK` z wartością.",
                "Dodaj return z operandem albo usuń `GIVE THESE PEOPLE AIR`.",
            )

        self._pop_scope()
        self.current_function = previous_function
        self.current_function_has_value_return = previous_return_state
        return None

    def visitDeclaration(self, ctx):
        self._check_operand(ctx.initValue())
        self._declare_variable(ctx.IDENTIFIER().getSymbol(), "zmienna")
        return None

    def visitAssignment(self, ctx):
        self._require_variable(ctx.IDENTIFIER().getSymbol(), "przypisanie")
        self._check_operand(ctx.operand())
        for operation in ctx.operation():
            self._check_operation(operation)
        return None

    def visitPrintStmt(self, ctx):
        if ctx.IDENTIFIER() is not None:
            self._require_variable(ctx.IDENTIFIER().getSymbol(), "wypisanie")
        return None

    def visitIfStmt(self, ctx):
        self._check_operand(ctx.operand())

        self._push_scope()
        for child in ctx.children[2:-1]:
            if child.getText() == "BULLSHIT":
                self._pop_scope()
                self._push_scope()
            elif child.__class__.__name__ == "StatementContext":
                self.visit(child)
        self._pop_scope()
        return None

    def visitWhileStmt(self, ctx):
        self._check_operand(ctx.operand())
        self._push_scope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self._pop_scope()
        return None

    def visitReturnStmt(self, ctx):
        has_value = ctx.operand() is not None
        if has_value:
            self._check_operand(ctx.operand())

        if self.current_function is None:
            return None

        if self.current_function.returns_value:
            if has_value:
                self.current_function_has_value_return = True
            else:
                self._add_error(
                    ctx.start,
                    f"Funkcja `{self.current_function.name}` powinna zwracać wartość.",
                    "Po `I'LL BE BACK` dodaj liczbę, boolean albo nazwę zmiennej.",
                )
        elif has_value:
            self._add_error(
                ctx.start,
                f"Funkcja `{self.current_function.name}` jest void, ale return zwraca wartość.",
                "Usuń operand po `I'LL BE BACK` albo dodaj `GIVE THESE PEOPLE AIR` w deklaracji funkcji.",
            )
        return None

    def visitFuncCallStmt(self, ctx):
        function_token = ctx.IDENTIFIER().getSymbol()
        self._check_function_call(function_token, len(ctx.operand()), assigned=False)
        for operand in ctx.operand():
            self._check_operand(operand)
        return None

    def visitFuncCallAssignStmt(self, ctx):
        self._require_variable(ctx.IDENTIFIER(0).getSymbol(), "zapis wyniku funkcji")

        if ctx.READ() is not None:
            return None

        function_token = ctx.IDENTIFIER(1).getSymbol()
        self._check_function_call(function_token, len(ctx.operand()), assigned=True)
        for operand in ctx.operand():
            self._check_operand(operand)
        return None

    def _collect_functions(self, func_contexts):
        for func_ctx in func_contexts:
            token = func_ctx.IDENTIFIER().getSymbol()
            name = token.text
            if name in self.functions:
                previous = self.functions[name]
                self._add_error(
                    token,
                    f"Funkcja `{name}` jest zadeklarowana więcej niż raz.",
                    f"Pierwsza deklaracja jest w linii {previous.line}.",
                )
                continue

            self.functions[name] = FunctionInfo(
                name=name,
                arity=len(func_ctx.funcArg()),
                returns_value=func_ctx.FUNC_NONVOID() is not None,
                line=token.line,
                column=token.column,
            )

    def _check_function_call(self, token, arity: int, assigned: bool):
        function = self.functions.get(token.text)
        if function is None:
            self._add_error(
                token,
                f"Wywołanie niezadeklarowanej funkcji `{token.text}`.",
                "Dodaj deklarację `LISTEN TO ME VERY CAREFULLY` albo popraw nazwę funkcji.",
            )
            return

        if function.arity != arity:
            self._add_error(
                token,
                f"Funkcja `{token.text}` oczekuje {function.arity} argumentów, a podano {arity}.",
                "Dopasuj liczbę operandów po `DO IT NOW` do deklaracji funkcji.",
            )

        if assigned and not function.returns_value:
            self._add_error(
                token,
                f"Funkcja `{token.text}` nie zwraca wartości, więc nie można przypisać jej wyniku.",
                "Dodaj `GIVE THESE PEOPLE AIR` i return z wartością albo użyj zwykłego `DO IT NOW`.",
            )

    def _check_operation(self, ctx):
        self._check_operand(ctx.operand())

        if (ctx.DIV() is not None or ctx.MOD() is not None) and self._is_zero_literal(ctx.operand()):
            self._add_error(
                ctx.operand().start,
                "Dzielenie albo modulo przez zero.",
                "Zmień operand na niezerową wartość albo wcześniej sprawdź go warunkiem.",
            )

    def _check_operand(self, ctx):
        if ctx is not None and ctx.IDENTIFIER() is not None:
            self._require_variable(ctx.IDENTIFIER().getSymbol(), "operand")

    def _is_zero_literal(self, operand_ctx) -> bool:
        if operand_ctx is None or operand_ctx.NUMBER() is None:
            return False
        try:
            return int(operand_ctx.NUMBER().getText()) == 0
        except ValueError:
            return False

    def _declare_variable(self, token, role: str):
        if not self.scopes:
            self._push_scope()

        current_scope = self.scopes[-1]
        if token.text in current_scope:
            self._add_error(
                token,
                f"Nazwa `{token.text}` jest już zadeklarowana w tym zakresie.",
                f"Zmień nazwę albo usuń wcześniejszą deklarację ({role}).",
            )
            return

        current_scope[token.text] = object()

    def _require_variable(self, token, usage: str):
        if any(token.text in scope for scope in reversed(self.scopes)):
            return

        self._add_error(
            token,
            f"Użycie niezadeklarowanej zmiennej `{token.text}`.",
            f"Przed użyciem jako {usage} dodaj `HEY CHRISTMAS TREE {token.text}` albo popraw literówkę.",
        )

    def _push_scope(self):
        self.scopes.append({})

    def _pop_scope(self):
        self.scopes.pop()

    def _add_error(self, token, message: str, hint: Optional[str] = None):
        self.diagnostics.append(Diagnostic("error", token.line, token.column, message, hint))


def has_errors(diagnostics: List[Diagnostic]) -> bool:
    return any(diagnostic.severity == "error" for diagnostic in diagnostics)


def format_diagnostics(filename: str, source_text: str, diagnostics: List[Diagnostic]) -> str:
    lines = source_text.splitlines()
    ordered = sorted(diagnostics, key=lambda item: (item.line, item.column, item.severity))
    output = []

    for diagnostic in ordered:
        label = "Błąd" if diagnostic.severity == "error" else "Ostrzeżenie"
        column = max(diagnostic.column, 0)
        output.append(f"{label} w {filename}:{diagnostic.line}:{column + 1}: {diagnostic.message}")

        if 1 <= diagnostic.line <= len(lines):
            source_line = lines[diagnostic.line - 1].rstrip()
            output.append(f"  {source_line}")
            output.append(f"  {' ' * min(column, len(source_line))}^")

        if diagnostic.hint:
            output.append(f"  wskazówka: {diagnostic.hint}")

    return "\n".join(output)

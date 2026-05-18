from ArnoldCVisitor import ArnoldCVisitor


class MyVisitor(ArnoldCVisitor):
    def __init__(self):
        self.output = []
        self._indent = 0

    # ------------------------------------------------------------------ helpers

    def _emit(self, line: str):
        """Dodaje linię z odpowiednim wcięciem."""
        self.output.append("    " * self._indent + line)

    def _format_operand(self, ctx):
        """
        Zamienia węzeł 'operand' lub 'initValue' na tekst C.
        Gramatyka: operand : NUMBER | IDENTIFIER | TRUE | FALSE ;
        """
        if ctx is None:
            return "0"
        if ctx.TRUE() is not None:
            return "1"
        if ctx.FALSE() is not None:
            return "0"
        if ctx.NUMBER() is not None:
            return ctx.NUMBER().getText()
        if ctx.IDENTIFIER() is not None:
            return ctx.IDENTIFIER().getText()
        return ctx.getText()

    def _format_operation(self, op_ctx):
        """
        Zwraca (operator_C, operand_tekst) dla węzła 'operation'.
        Gramatyka:
            operation : ADD operand | SUB operand | MUL operand
                      | DIV operand | MOD operand | EQ  operand
                      | GT  operand | AND operand | OR  operand ;
        Każdy operator to osobny token — sprawdzamy metodą kontekstu.
        """
        operand_text = self._format_operand(op_ctx.operand())

        if   op_ctx.ADD() is not None: operator = "+"
        elif op_ctx.SUB() is not None: operator = "-"
        elif op_ctx.MUL() is not None: operator = "*"
        elif op_ctx.DIV() is not None: operator = "/"
        elif op_ctx.MOD() is not None: operator = "%"
        elif op_ctx.EQ()  is not None: operator = "=="
        elif op_ctx.GT()  is not None: operator = ">"
        elif op_ctx.AND() is not None: operator = "&&"
        elif op_ctx.OR()  is not None: operator = "||"
        else:                          operator = "?"

        return operator, operand_text

    # ------------------------------------------------------------------ program

    def visitProgram(self, ctx):
        self._emit("#include <stdio.h>")
        self._emit("")

        for func in ctx.funcDecl():
            self.visit(func)
            self._emit("")

        self._emit("int main() {")
        self._indent += 1
        for stmt in ctx.statement():
            self.visit(stmt)
        self._emit("return 0;")
        self._indent -= 1
        self._emit("}")

        return "\n".join(self.output)

    # ------------------------------------------------------------------ I/O

    def visitPrintStmt(self, ctx):
        """
        Gramatyka: printStmt : PRINT (STRING | IDENTIFIER | NUMBER) ;
        """
        if ctx.STRING() is not None:
            text = ctx.STRING().getText()
            self._emit(f'printf("%s\\n", {text});')
        elif ctx.IDENTIFIER() is not None:
            self._emit(f'printf("%d\\n", {ctx.IDENTIFIER().getText()});')
        elif ctx.NUMBER() is not None:
            self._emit(f'printf("%d\\n", {ctx.NUMBER().getText()});')
        return None

    # ------------------------------------------------------------------ variables

    def visitDeclaration(self, ctx):
        """
        Gramatyka: declaration : DECLARE IDENTIFIER SET_INIT initValue ;
        """
        var_name = ctx.IDENTIFIER().getText()
        value = self._format_operand(ctx.initValue())
        self._emit(f"int {var_name} = {value};")
        return None

    def visitAssignment(self, ctx):
        """
        Gramatyka:
            assignment : ASSIGN_VAR_START IDENTIFIER
                         ASSIGN_VAR_VALUE operand
                         operation*
                         ASSIGN_VAR_END ;
        ctx.operand() zwraca JEDEN węzeł (nie listę) — wartość bazowa wyrażenia.
        ctx.operation() zwraca listę węzłów operation.
        """
        var_name = ctx.IDENTIFIER().getText()
        expr = self._format_operand(ctx.operand())  # pojedynczy operand
        for op in ctx.operation():                   # lista operacji (może być pusta)
            operator, operand = self._format_operation(op)
            expr = f"({expr} {operator} {operand})"
        self._emit(f"{var_name} = {expr};")
        return None

    # ------------------------------------------------------------------ control flow

    def visitIfStmt(self, ctx):
        """
        Gramatyka:
            ifStmt : IF operand
                     statement*
                     (ELSE statement*)?
                     ENDIF ;

        ctx.statement() zwraca WSZYSTKIE statement z obu gałęzi naraz.
        Rozdzielamy je po pozycji tokenu ELSE iterując po dzieciach.
        """
        condition = self._format_operand(ctx.operand())
        self._emit(f"if ({condition}) {{")
        self._indent += 1

        in_else = False
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            # TerminalNode nie ma klasy kończącej się na "Context"
            if child.__class__.__name__ == "TerminalNodeImpl":
                if child.getText() == ctx.ELSE().getText() if ctx.ELSE() is not None else False:
                    self._indent -= 1
                    self._emit("} else {")
                    self._indent += 1
                    in_else = True
            elif child.__class__.__name__ == "StatementContext":
                self.visit(child)

        self._indent -= 1
        self._emit("}")
        return None

    def visitWhileStmt(self, ctx):
        """
        Gramatyka: whileStmt : WHILE operand statement* ENDWHILE ;
        """
        condition = self._format_operand(ctx.operand())
        self._emit(f"while ({condition}) {{")
        self._indent += 1
        for stmt in ctx.statement():
            self.visit(stmt)
        self._indent -= 1
        self._emit("}")
        return None

    # ------------------------------------------------------------------ functions

    def visitFuncDecl(self, ctx):
        """
        Gramatyka:
            funcDecl : FUNC_START IDENTIFIER
                       funcArg*
                       FUNC_NONVOID?
                       statement*
                       returnStmt?
                       FUNC_END ;
        """
        func_name = ctx.IDENTIFIER().getText()
        params = [arg.IDENTIFIER().getText() for arg in ctx.funcArg()]
        ret_type = "int" if ctx.FUNC_NONVOID() is not None else "void"
        # Użyto 'p' żeby nie shadować zmiennej func_name
        param_list = ", ".join(f"int {p}" for p in params)

        self._emit(f"{ret_type} {func_name}({param_list}) {{")
        self._indent += 1
        for stmt in ctx.statement():
            self.visit(stmt)
        if ctx.returnStmt() is not None:
            self.visit(ctx.returnStmt())
        self._indent -= 1
        self._emit("}")
        return None

    def visitFuncArg(self, ctx):
        # Obsługiwane w visitFuncDecl
        return None

    def visitReturnStmt(self, ctx):
        """
        Gramatyka: returnStmt : RETURN operand? ;
        """
        if ctx.operand() is not None:
            value = self._format_operand(ctx.operand())
            self._emit(f"return {value};")
        else:
            self._emit("return;")
        return None

    def visitFuncCallStmt(self, ctx):
        """
        Gramatyka: funcCallStmt : CALL IDENTIFIER operand* ;
        """
        func_name = ctx.IDENTIFIER().getText()
        args = [self._format_operand(op) for op in ctx.operand()]
        self._emit(f"{func_name}({', '.join(args)});")
        return None

    def visitFuncCallAssignStmt(self, ctx):
        """
        Gramatyka:
            funcCallAssignStmt : CALL_ASSIGN IDENTIFIER
                                 CALL (IDENTIFIER | READ) operand* ;
        IDENTIFIER(0) = zmienna wynikowa
        IDENTIFIER(1) = nazwa funkcji (jeśli nie READ)
        """
        target = ctx.IDENTIFIER(0).getText()

        if ctx.READ() is not None:
            self._emit(f'scanf("%d", &{target});')
            return None

        func_name = ctx.IDENTIFIER(1).getText()
        args = [self._format_operand(op) for op in ctx.operand()]
        self._emit(f"{target} = {func_name}({', '.join(args)});")
        return None
import argparse
import subprocess
import sys

from ArnoldCDiagnostics import (
    ArnoldCErrorListener,
    SemanticAnalyzer,
    format_diagnostics,
    has_errors,
)
from ArnoldCtoCVisitor import ArnoldCtoCVisitor
from antlr4 import CommonTokenStream, InputStream
from ANTLR4_generated.ArnoldCLexer import ArnoldCLexer
from ANTLR4_generated.ArnoldCParser import ArnoldCParser

def main():
    parser = argparse.ArgumentParser(description="ArnoldC to C compiler")
    parser.add_argument("input", help="Input .arnoldc file")
    parser.add_argument("-o", "--output", help="Output .c file (default: out.c)", default="out.c")
    parser.add_argument("--compile", action="store_true", help="Compile generated C with gcc")
    parser.add_argument("--run", action="store_true", help="Compile and run generated C")
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as source_file:
            source_text = source_file.read()
    except OSError as exc:
        print(f"Nie można odczytać pliku wejściowego `{args.input}`: {exc}")
        sys.exit(1)

    diagnostics = []
    error_listener = ArnoldCErrorListener(diagnostics)

    # parsowanie
    input_stream = InputStream(source_text)
    lexer = ArnoldCLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    parser = ArnoldCParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.program()

    if diagnostics:
        print(format_diagnostics(args.input, source_text, diagnostics))

    if has_errors(diagnostics):
        print("Kompilacja przerwana.")
        sys.exit(1)

    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.visit(tree)
    diagnostics.extend(semantic_analyzer.diagnostics)

    if diagnostics:
        print(format_diagnostics(args.input, source_text, diagnostics))

    if has_errors(diagnostics):
        print("Kompilacja przerwana.")
        sys.exit(1)

    # generacja C
    visitor = ArnoldCtoCVisitor()
    try:
        c_code = visitor.visit(tree)
    except Exception as exc:
        print(f"Generowanie kodu C nie powiodło się: {exc}")
        sys.exit(1)

    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(c_code)
    except OSError as exc:
        print(f"Nie można zapisać pliku wynikowego `{args.output}`: {exc}")
        sys.exit(1)
    print(f"Generated: {args.output}")

    # kompilacja
    if args.compile or args.run:
        binary = args.output.replace(".c", "")
        result = subprocess.run(["gcc", args.output, "-o", binary])
        if result.returncode != 0:
            print("Kompilacja wygenerowanego C nie powiodła się.")
            sys.exit(1)
        print(f"Compiled: {binary}")

        if args.run:
            subprocess.run([f"./{binary}"])

if __name__ == "__main__":
    main()

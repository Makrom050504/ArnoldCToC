import argparse
import subprocess
import sys

from ArnoldCtoCVisitor import ArnoldCtoCVisitor
from antlr4 import CommonTokenStream, FileStream
from ANTLR4_generated.ArnoldCLexer import ArnoldCLexer
from ANTLR4_generated.ArnoldCParser import ArnoldCParser

def main():
    parser = argparse.ArgumentParser(description="ArnoldC to C compiler")
    parser.add_argument("input", help="Input .arnoldc file")
    parser.add_argument("-o", "--output", help="Output .c file (default: out.c)", default="out.c")
    parser.add_argument("--compile", action="store_true", help="Compile generated C with gcc")
    parser.add_argument("--run", action="store_true", help="Compile and run generated C")
    args = parser.parse_args()

    # parsowanie
    input_stream = FileStream(args.input)
    lexer = ArnoldCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArnoldCParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found, aborting.")
        sys.exit(1)

    # generacja C
    visitor = ArnoldCtoCVisitor()
    c_code = visitor.visit(tree)

    with open(args.output, "w") as f:
        f.write(c_code)
    print(f"Generated: {args.output}")

    # kompilacja
    if args.compile or args.run:
        binary = args.output.replace(".c", "")
        result = subprocess.run(["gcc", args.output, "-o", binary])
        if result.returncode != 0:
            print("Compilation failed.")
            sys.exit(1)
        print(f"Compiled: {binary}")

        if args.run:
            subprocess.run([f"./{binary}"])

if __name__ == "__main__":
    main()
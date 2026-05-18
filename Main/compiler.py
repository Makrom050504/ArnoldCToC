from antlr4 import *
from ANTLR4_generated.ArnoldCLexer import ArnoldCLexer
from ANTLR4_generated.ArnoldCParser import ArnoldCParser
from MyVisitor import MyVisitor



input_stream = FileStream("Tests/test.modulo_func")
lexer = ArnoldCLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = ArnoldCParser(tokens)

tree = parser.program()

visitor = MyVisitor()
result = visitor.visit(tree)

with open("out.c", "w") as f:
    f.write(result)
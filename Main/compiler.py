from antlr4 import *
from ArnoldCLexer import ArnoldCLexer
from ArnoldCParser import ArnoldCParser
from MyVisitor import MyVisitor



input_stream = FileStream("test.arnoldc")
lexer = ArnoldCLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = ArnoldCParser(tokens)

tree = parser.program()

visitor = MyVisitor()
result = visitor.visit(tree)

with open("out.c", "w") as f:
    f.write(result)
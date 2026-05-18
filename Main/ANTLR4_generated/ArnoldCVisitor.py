# Generated from ArnoldC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from ..ArnoldCParser import ArnoldCParser
else:
    from ArnoldCParser import ArnoldCParser

# This class defines a complete generic visitor for a parse tree produced by ArnoldCParser.

class ArnoldCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArnoldCParser#program.
    def visitProgram(self, ctx:ArnoldCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#statement.
    def visitStatement(self, ctx:ArnoldCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#declaration.
    def visitDeclaration(self, ctx:ArnoldCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#initValue.
    def visitInitValue(self, ctx:ArnoldCParser.InitValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#assignment.
    def visitAssignment(self, ctx:ArnoldCParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#operation.
    def visitOperation(self, ctx:ArnoldCParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#operand.
    def visitOperand(self, ctx:ArnoldCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#printStmt.
    def visitPrintStmt(self, ctx:ArnoldCParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#ifStmt.
    def visitIfStmt(self, ctx:ArnoldCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#whileStmt.
    def visitWhileStmt(self, ctx:ArnoldCParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#funcDecl.
    def visitFuncDecl(self, ctx:ArnoldCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#funcArg.
    def visitFuncArg(self, ctx:ArnoldCParser.FuncArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#returnStmt.
    def visitReturnStmt(self, ctx:ArnoldCParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#funcCallStmt.
    def visitFuncCallStmt(self, ctx:ArnoldCParser.FuncCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArnoldCParser#funcCallAssignStmt.
    def visitFuncCallAssignStmt(self, ctx:ArnoldCParser.FuncCallAssignStmtContext):
        return self.visitChildren(ctx)



del ArnoldCParser
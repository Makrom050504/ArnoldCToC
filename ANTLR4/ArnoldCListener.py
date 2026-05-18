# Generated from ArnoldC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArnoldCParser import ArnoldCParser
else:
    from ArnoldCParser import ArnoldCParser

# This class defines a complete listener for a parse tree produced by ArnoldCParser.
class ArnoldCListener(ParseTreeListener):

    # Enter a parse tree produced by ArnoldCParser#program.
    def enterProgram(self, ctx:ArnoldCParser.ProgramContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#program.
    def exitProgram(self, ctx:ArnoldCParser.ProgramContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#statement.
    def enterStatement(self, ctx:ArnoldCParser.StatementContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#statement.
    def exitStatement(self, ctx:ArnoldCParser.StatementContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#declaration.
    def enterDeclaration(self, ctx:ArnoldCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#declaration.
    def exitDeclaration(self, ctx:ArnoldCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#initValue.
    def enterInitValue(self, ctx:ArnoldCParser.InitValueContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#initValue.
    def exitInitValue(self, ctx:ArnoldCParser.InitValueContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#assignment.
    def enterAssignment(self, ctx:ArnoldCParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#assignment.
    def exitAssignment(self, ctx:ArnoldCParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#operation.
    def enterOperation(self, ctx:ArnoldCParser.OperationContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#operation.
    def exitOperation(self, ctx:ArnoldCParser.OperationContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#operand.
    def enterOperand(self, ctx:ArnoldCParser.OperandContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#operand.
    def exitOperand(self, ctx:ArnoldCParser.OperandContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#printStmt.
    def enterPrintStmt(self, ctx:ArnoldCParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#printStmt.
    def exitPrintStmt(self, ctx:ArnoldCParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#ifStmt.
    def enterIfStmt(self, ctx:ArnoldCParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#ifStmt.
    def exitIfStmt(self, ctx:ArnoldCParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#whileStmt.
    def enterWhileStmt(self, ctx:ArnoldCParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#whileStmt.
    def exitWhileStmt(self, ctx:ArnoldCParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#funcDecl.
    def enterFuncDecl(self, ctx:ArnoldCParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#funcDecl.
    def exitFuncDecl(self, ctx:ArnoldCParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#funcArg.
    def enterFuncArg(self, ctx:ArnoldCParser.FuncArgContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#funcArg.
    def exitFuncArg(self, ctx:ArnoldCParser.FuncArgContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#returnStmt.
    def enterReturnStmt(self, ctx:ArnoldCParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#returnStmt.
    def exitReturnStmt(self, ctx:ArnoldCParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#funcCallStmt.
    def enterFuncCallStmt(self, ctx:ArnoldCParser.FuncCallStmtContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#funcCallStmt.
    def exitFuncCallStmt(self, ctx:ArnoldCParser.FuncCallStmtContext):
        pass


    # Enter a parse tree produced by ArnoldCParser#funcCallAssignStmt.
    def enterFuncCallAssignStmt(self, ctx:ArnoldCParser.FuncCallAssignStmtContext):
        pass

    # Exit a parse tree produced by ArnoldCParser#funcCallAssignStmt.
    def exitFuncCallAssignStmt(self, ctx:ArnoldCParser.FuncCallAssignStmtContext):
        pass



del ArnoldCParser
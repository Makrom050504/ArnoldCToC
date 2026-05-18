# Generated from grammar/ArnoldC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,182,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,5,0,39,8,0,10,
        0,12,0,42,9,0,1,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        99,8,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,5,8,109,8,8,10,8,12,8,112,
        9,8,1,8,1,8,5,8,116,8,8,10,8,12,8,119,9,8,3,8,121,8,8,1,8,1,8,1,
        9,1,9,1,9,5,9,128,8,9,10,9,12,9,131,9,9,1,9,1,9,1,10,1,10,1,10,5,
        10,138,8,10,10,10,12,10,141,9,10,1,10,3,10,144,8,10,1,10,5,10,147,
        8,10,10,10,12,10,150,9,10,1,10,3,10,153,8,10,1,10,1,10,1,11,1,11,
        1,11,1,12,1,12,3,12,162,8,12,1,13,1,13,1,13,5,13,167,8,13,10,13,
        12,13,170,9,13,1,14,1,14,1,14,1,14,1,14,5,14,177,8,14,10,14,12,14,
        180,9,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,3,
        3,0,31,32,34,34,36,36,1,0,34,36,2,0,4,4,36,36,195,0,33,1,0,0,0,2,
        59,1,0,0,0,4,61,1,0,0,0,6,66,1,0,0,0,8,68,1,0,0,0,10,98,1,0,0,0,
        12,100,1,0,0,0,14,102,1,0,0,0,16,105,1,0,0,0,18,124,1,0,0,0,20,134,
        1,0,0,0,22,156,1,0,0,0,24,159,1,0,0,0,26,163,1,0,0,0,28,171,1,0,
        0,0,30,32,3,20,10,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,
        34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,40,5,1,0,0,37,39,3,2,1,
        0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,
        1,0,0,0,42,40,1,0,0,0,43,47,5,2,0,0,44,46,3,20,10,0,45,44,1,0,0,
        0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,
        1,0,0,0,50,51,5,0,0,1,51,1,1,0,0,0,52,60,3,4,2,0,53,60,3,8,4,0,54,
        60,3,14,7,0,55,60,3,16,8,0,56,60,3,18,9,0,57,60,3,26,13,0,58,60,
        3,28,14,0,59,52,1,0,0,0,59,53,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,
        0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,3,1,0,0,0,61,62,5,
        5,0,0,62,63,5,36,0,0,63,64,5,6,0,0,64,65,3,6,3,0,65,5,1,0,0,0,66,
        67,7,0,0,0,67,7,1,0,0,0,68,69,5,7,0,0,69,70,5,36,0,0,70,71,5,8,0,
        0,71,75,3,12,6,0,72,74,3,10,5,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,
        1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,9,0,0,
        79,9,1,0,0,0,80,81,5,10,0,0,81,99,3,12,6,0,82,83,5,11,0,0,83,99,
        3,12,6,0,84,85,5,12,0,0,85,99,3,12,6,0,86,87,5,13,0,0,87,99,3,12,
        6,0,88,89,5,14,0,0,89,99,3,12,6,0,90,91,5,15,0,0,91,99,3,12,6,0,
        92,93,5,16,0,0,93,99,3,12,6,0,94,95,5,17,0,0,95,99,3,12,6,0,96,97,
        5,18,0,0,97,99,3,12,6,0,98,80,1,0,0,0,98,82,1,0,0,0,98,84,1,0,0,
        0,98,86,1,0,0,0,98,88,1,0,0,0,98,90,1,0,0,0,98,92,1,0,0,0,98,94,
        1,0,0,0,98,96,1,0,0,0,99,11,1,0,0,0,100,101,7,0,0,0,101,13,1,0,0,
        0,102,103,5,3,0,0,103,104,7,1,0,0,104,15,1,0,0,0,105,106,5,19,0,
        0,106,110,3,12,6,0,107,109,3,2,1,0,108,107,1,0,0,0,109,112,1,0,0,
        0,110,108,1,0,0,0,110,111,1,0,0,0,111,120,1,0,0,0,112,110,1,0,0,
        0,113,117,5,20,0,0,114,116,3,2,1,0,115,114,1,0,0,0,116,119,1,0,0,
        0,117,115,1,0,0,0,117,118,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,
        0,120,113,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,5,21,0,
        0,123,17,1,0,0,0,124,125,5,22,0,0,125,129,3,12,6,0,126,128,3,2,1,
        0,127,126,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,
        0,130,132,1,0,0,0,131,129,1,0,0,0,132,133,5,23,0,0,133,19,1,0,0,
        0,134,135,5,24,0,0,135,139,5,36,0,0,136,138,3,22,11,0,137,136,1,
        0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,143,1,
        0,0,0,141,139,1,0,0,0,142,144,5,25,0,0,143,142,1,0,0,0,143,144,1,
        0,0,0,144,148,1,0,0,0,145,147,3,2,1,0,146,145,1,0,0,0,147,150,1,
        0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,152,1,0,0,0,150,148,1,
        0,0,0,151,153,3,24,12,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,
        1,0,0,0,154,155,5,28,0,0,155,21,1,0,0,0,156,157,5,26,0,0,157,158,
        5,36,0,0,158,23,1,0,0,0,159,161,5,27,0,0,160,162,3,12,6,0,161,160,
        1,0,0,0,161,162,1,0,0,0,162,25,1,0,0,0,163,164,5,29,0,0,164,168,
        5,36,0,0,165,167,3,12,6,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,27,1,0,0,0,170,168,1,0,0,0,171,172,5,
        30,0,0,172,173,5,36,0,0,173,174,5,29,0,0,174,178,7,2,0,0,175,177,
        3,12,6,0,176,175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,
        1,0,0,0,179,29,1,0,0,0,180,178,1,0,0,0,17,33,40,47,59,75,98,110,
        117,120,129,139,143,148,152,161,168,178
    ]

class ArnoldCParser ( Parser ):

    grammarFileName = "ArnoldC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IT'S SHOWTIME'", "'YOU HAVE BEEN TERMINATED'", 
                     "'TALK TO THE HAND'", "'I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY'", 
                     "'HEY CHRISTMAS TREE'", "'YOU SET US UP'", "'GET TO THE CHOPPER'", 
                     "'HERE IS MY INVITATION'", "'ENOUGH TALK'", "'GET UP'", 
                     "'GET DOWN'", "'YOU'RE FIRED'", "'HE HAD TO SPLIT'", 
                     "'I LET HIM GO'", "'YOU ARE NOT YOU YOU ARE ME'", "'LET OFF SOME STEAM BENNET'", 
                     "'KNOCK KNOCK'", "'CONSIDER THAT A DIVORCE'", "'BECAUSE I'M GOING TO SAY PLEASE'", 
                     "'BULLSHIT'", "'YOU HAVE NO RESPECT FOR LOGIC'", "'STICK AROUND'", 
                     "'CHILL'", "'LISTEN TO ME VERY CAREFULLY'", "'GIVE THESE PEOPLE AIR'", 
                     "'I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE'", 
                     "'I'LL BE BACK'", "'HASTA LA VISTA, BABY'", "'DO IT NOW'", 
                     "'GET YOUR ASS TO MARS'", "'@NO PROBLEMO'", "'@I LIED'", 
                     "'WHAT THE FUCK DID I DO WRONG'" ]

    symbolicNames = [ "<INVALID>", "START", "END", "PRINT", "READ", "DECLARE", 
                      "SET_INIT", "ASSIGN_VAR_START", "ASSIGN_VAR_VALUE", 
                      "ASSIGN_VAR_END", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "EQ", "GT", "AND", "OR", "IF", "ELSE", "ENDIF", "WHILE", 
                      "ENDWHILE", "FUNC_START", "FUNC_NONVOID", "FUNC_ARGS", 
                      "RETURN", "FUNC_END", "CALL", "CALL_ASSIGN", "TRUE", 
                      "FALSE", "ERROR_TOKEN", "NUMBER", "STRING", "IDENTIFIER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_initValue = 3
    RULE_assignment = 4
    RULE_operation = 5
    RULE_operand = 6
    RULE_printStmt = 7
    RULE_ifStmt = 8
    RULE_whileStmt = 9
    RULE_funcDecl = 10
    RULE_funcArg = 11
    RULE_returnStmt = 12
    RULE_funcCallStmt = 13
    RULE_funcCallAssignStmt = 14

    ruleNames =  [ "program", "statement", "declaration", "initValue", "assignment", 
                   "operation", "operand", "printStmt", "ifStmt", "whileStmt", 
                   "funcDecl", "funcArg", "returnStmt", "funcCallStmt", 
                   "funcCallAssignStmt" ]

    EOF = Token.EOF
    START=1
    END=2
    PRINT=3
    READ=4
    DECLARE=5
    SET_INIT=6
    ASSIGN_VAR_START=7
    ASSIGN_VAR_VALUE=8
    ASSIGN_VAR_END=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    MOD=14
    EQ=15
    GT=16
    AND=17
    OR=18
    IF=19
    ELSE=20
    ENDIF=21
    WHILE=22
    ENDWHILE=23
    FUNC_START=24
    FUNC_NONVOID=25
    FUNC_ARGS=26
    RETURN=27
    FUNC_END=28
    CALL=29
    CALL_ASSIGN=30
    TRUE=31
    FALSE=32
    ERROR_TOKEN=33
    NUMBER=34
    STRING=35
    IDENTIFIER=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(ArnoldCParser.START, 0)

        def END(self):
            return self.getToken(ArnoldCParser.END, 0)

        def EOF(self):
            return self.getToken(ArnoldCParser.EOF, 0)

        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.FuncDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.StatementContext,i)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ArnoldCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 30
                self.funcDecl()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(ArnoldCParser.START)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1615331496) != 0):
                self.state = 37
                self.statement()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(ArnoldCParser.END)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 44
                self.funcDecl()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(ArnoldCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ArnoldCParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ArnoldCParser.AssignmentContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(ArnoldCParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(ArnoldCParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(ArnoldCParser.WhileStmtContext,0)


        def funcCallStmt(self):
            return self.getTypedRuleContext(ArnoldCParser.FuncCallStmtContext,0)


        def funcCallAssignStmt(self):
            return self.getTypedRuleContext(ArnoldCParser.FuncCallAssignStmtContext,0)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ArnoldCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.declaration()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.printStmt()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.ifStmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.whileStmt()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.funcCallStmt()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.funcCallAssignStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(ArnoldCParser.DECLARE, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def SET_INIT(self):
            return self.getToken(ArnoldCParser.SET_INIT, 0)

        def initValue(self):
            return self.getTypedRuleContext(ArnoldCParser.InitValueContext,0)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ArnoldCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ArnoldCParser.DECLARE)
            self.state = 62
            self.match(ArnoldCParser.IDENTIFIER)
            self.state = 63
            self.match(ArnoldCParser.SET_INIT)
            self.state = 64
            self.initValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ArnoldCParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def TRUE(self):
            return self.getToken(ArnoldCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ArnoldCParser.FALSE, 0)

        def getRuleIndex(self):
            return ArnoldCParser.RULE_initValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitValue" ):
                return visitor.visitInitValue(self)
            else:
                return visitor.visitChildren(self)




    def initValue(self):

        localctx = ArnoldCParser.InitValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_initValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 92341796864) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_VAR_START(self):
            return self.getToken(ArnoldCParser.ASSIGN_VAR_START, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def ASSIGN_VAR_VALUE(self):
            return self.getToken(ArnoldCParser.ASSIGN_VAR_VALUE, 0)

        def operand(self):
            return self.getTypedRuleContext(ArnoldCParser.OperandContext,0)


        def ASSIGN_VAR_END(self):
            return self.getToken(ArnoldCParser.ASSIGN_VAR_END, 0)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.OperationContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.OperationContext,i)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ArnoldCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ArnoldCParser.ASSIGN_VAR_START)
            self.state = 69
            self.match(ArnoldCParser.IDENTIFIER)
            self.state = 70
            self.match(ArnoldCParser.ASSIGN_VAR_VALUE)
            self.state = 71
            self.operand()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523264) != 0):
                self.state = 72
                self.operation()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(ArnoldCParser.ASSIGN_VAR_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ArnoldCParser.ADD, 0)

        def operand(self):
            return self.getTypedRuleContext(ArnoldCParser.OperandContext,0)


        def SUB(self):
            return self.getToken(ArnoldCParser.SUB, 0)

        def MUL(self):
            return self.getToken(ArnoldCParser.MUL, 0)

        def DIV(self):
            return self.getToken(ArnoldCParser.DIV, 0)

        def MOD(self):
            return self.getToken(ArnoldCParser.MOD, 0)

        def EQ(self):
            return self.getToken(ArnoldCParser.EQ, 0)

        def GT(self):
            return self.getToken(ArnoldCParser.GT, 0)

        def AND(self):
            return self.getToken(ArnoldCParser.AND, 0)

        def OR(self):
            return self.getToken(ArnoldCParser.OR, 0)

        def getRuleIndex(self):
            return ArnoldCParser.RULE_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = ArnoldCParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operation)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(ArnoldCParser.ADD)
                self.state = 81
                self.operand()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(ArnoldCParser.SUB)
                self.state = 83
                self.operand()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(ArnoldCParser.MUL)
                self.state = 85
                self.operand()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.match(ArnoldCParser.DIV)
                self.state = 87
                self.operand()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.match(ArnoldCParser.MOD)
                self.state = 89
                self.operand()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.match(ArnoldCParser.EQ)
                self.state = 91
                self.operand()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 92
                self.match(ArnoldCParser.GT)
                self.state = 93
                self.operand()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.match(ArnoldCParser.AND)
                self.state = 95
                self.operand()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 9)
                self.state = 96
                self.match(ArnoldCParser.OR)
                self.state = 97
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ArnoldCParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def TRUE(self):
            return self.getToken(ArnoldCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ArnoldCParser.FALSE, 0)

        def getRuleIndex(self):
            return ArnoldCParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ArnoldCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 92341796864) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ArnoldCParser.PRINT, 0)

        def STRING(self):
            return self.getToken(ArnoldCParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ArnoldCParser.NUMBER, 0)

        def getRuleIndex(self):
            return ArnoldCParser.RULE_printStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = ArnoldCParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ArnoldCParser.PRINT)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ArnoldCParser.IF, 0)

        def operand(self):
            return self.getTypedRuleContext(ArnoldCParser.OperandContext,0)


        def ENDIF(self):
            return self.getToken(ArnoldCParser.ENDIF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(ArnoldCParser.ELSE, 0)

        def getRuleIndex(self):
            return ArnoldCParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = ArnoldCParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ArnoldCParser.IF)
            self.state = 106
            self.operand()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1615331496) != 0):
                self.state = 107
                self.statement()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 113
                self.match(ArnoldCParser.ELSE)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1615331496) != 0):
                    self.state = 114
                    self.statement()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 122
            self.match(ArnoldCParser.ENDIF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ArnoldCParser.WHILE, 0)

        def operand(self):
            return self.getTypedRuleContext(ArnoldCParser.OperandContext,0)


        def ENDWHILE(self):
            return self.getToken(ArnoldCParser.ENDWHILE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.StatementContext,i)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = ArnoldCParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ArnoldCParser.WHILE)
            self.state = 125
            self.operand()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1615331496) != 0):
                self.state = 126
                self.statement()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(ArnoldCParser.ENDWHILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_START(self):
            return self.getToken(ArnoldCParser.FUNC_START, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def FUNC_END(self):
            return self.getToken(ArnoldCParser.FUNC_END, 0)

        def funcArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.FuncArgContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.FuncArgContext,i)


        def FUNC_NONVOID(self):
            return self.getToken(ArnoldCParser.FUNC_NONVOID, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.StatementContext,i)


        def returnStmt(self):
            return self.getTypedRuleContext(ArnoldCParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = ArnoldCParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ArnoldCParser.FUNC_START)
            self.state = 135
            self.match(ArnoldCParser.IDENTIFIER)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 136
                self.funcArg()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 142
                self.match(ArnoldCParser.FUNC_NONVOID)


            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1615331496) != 0):
                self.state = 145
                self.statement()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 151
                self.returnStmt()


            self.state = 154
            self.match(ArnoldCParser.FUNC_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_ARGS(self):
            return self.getToken(ArnoldCParser.FUNC_ARGS, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ArnoldCParser.RULE_funcArg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncArg" ):
                return visitor.visitFuncArg(self)
            else:
                return visitor.visitChildren(self)




    def funcArg(self):

        localctx = ArnoldCParser.FuncArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ArnoldCParser.FUNC_ARGS)
            self.state = 157
            self.match(ArnoldCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ArnoldCParser.RETURN, 0)

        def operand(self):
            return self.getTypedRuleContext(ArnoldCParser.OperandContext,0)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = ArnoldCParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ArnoldCParser.RETURN)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 92341796864) != 0):
                self.state = 160
                self.operand()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(ArnoldCParser.CALL, 0)

        def IDENTIFIER(self):
            return self.getToken(ArnoldCParser.IDENTIFIER, 0)

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.OperandContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.OperandContext,i)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_funcCallStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallStmt" ):
                return visitor.visitFuncCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def funcCallStmt(self):

        localctx = ArnoldCParser.FuncCallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcCallStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ArnoldCParser.CALL)
            self.state = 164
            self.match(ArnoldCParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 92341796864) != 0):
                self.state = 165
                self.operand()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallAssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL_ASSIGN(self):
            return self.getToken(ArnoldCParser.CALL_ASSIGN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ArnoldCParser.IDENTIFIER)
            else:
                return self.getToken(ArnoldCParser.IDENTIFIER, i)

        def CALL(self):
            return self.getToken(ArnoldCParser.CALL, 0)

        def READ(self):
            return self.getToken(ArnoldCParser.READ, 0)

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArnoldCParser.OperandContext)
            else:
                return self.getTypedRuleContext(ArnoldCParser.OperandContext,i)


        def getRuleIndex(self):
            return ArnoldCParser.RULE_funcCallAssignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallAssignStmt" ):
                return visitor.visitFuncCallAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def funcCallAssignStmt(self):

        localctx = ArnoldCParser.FuncCallAssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcCallAssignStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(ArnoldCParser.CALL_ASSIGN)
            self.state = 172
            self.match(ArnoldCParser.IDENTIFIER)
            self.state = 173
            self.match(ArnoldCParser.CALL)
            self.state = 174
            _la = self._input.LA(1)
            if not(_la==4 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 92341796864) != 0):
                self.state = 175
                self.operand()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






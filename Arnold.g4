grammar ArnoldC;

// =======================
// PROGRAM STRUCTURE
// =======================

program
    : START statement* END EOF
    ;

statement
    : declaration
    | assignment_init
    | assignment_full
    | printStmt
    | readStmt
    | ifStmt
    | whileStmt
    | funcDecl
    | funcCall
    ;

// =======================
// VARIABLES
// =======================

declaration
    : DECLARE IDENTIFIER SET_INIT expression
    ;

// przypisanie zwykłe (GET TO THE CHOPPER)
assignment_full
    : ASSIGN_VAR_START IDENTIFIER
      ASSIGN_VAR_VALUE expression
      ASSIGN_VAR_END
    ;

// =======================
// I/O
// =======================

printStmt
    : PRINT expression
    ;

readStmt
    : READ IDENTIFIER
    ;

// =======================
// IF / ELSE
// =======================

ifStmt
    : IF expression statement*
      (ELSE statement*)?
      ENDIF
    ;

// =======================
// WHILE LOOP
// =======================

whileStmt
    : WHILE expression statement*
      ENDWHILE
    ;

// =======================
// FUNCTIONS
// =======================

funcDecl
    : FUNC_START IDENTIFIER funcParams? statement* returnStmt? FUNC_END
    ;

funcParams
    : FUNC_ARGS IDENTIFIER+
    ;

returnStmt
    : RETURN expression
    ;

funcCall
    : CALL IDENTIFIER
    | CALL_ASSIGN IDENTIFIER ASSIGN_VAR_START IDENTIFIER
    ;

// =======================
// EXPRESSIONS
// =======================

expression
    : logicExpr
    ;

// logic level
logicExpr
    : equalityExpr ((AND | OR) equalityExpr)*
    ;

equalityExpr
    : relationalExpr (EQ relationalExpr)*
    ;

relationalExpr
    : additiveExpr (GT additiveExpr)*
    ;

// arithmetic
additiveExpr
    : multiplicativeExpr ((ADD | SUB) multiplicativeExpr)*
    ;

multiplicativeExpr
    : unaryExpr ((MUL | DIV | MOD) unaryExpr)*
    ;

unaryExpr
    : SUB unaryExpr
    | atom
    ;

// =======================
// ATOMS
// =======================

atom
    : IDENTIFIER
    | NUMBER
    | STRING
    | TRUE
    | FALSE
    | '(' expression ')'
    ;

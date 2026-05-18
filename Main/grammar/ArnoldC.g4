grammar ArnoldC;

// =======================
// PROGRAM STRUCTURE
// =======================
program
    : funcDecl* START statement* END EOF
    ;

// =======================
// STATEMENTS
// =======================
statement
    : declaration
    | assignment
    | printStmt
    | ifStmt
    | whileStmt
    | funcCallStmt
    | funcCallAssignStmt
    ;

// =======================
// VARIABLES
// =======================
declaration
    : DECLARE IDENTIFIER SET_INIT initValue
    ;

// Wartość inicjalna to liczba, identyfikator lub boolean (@NO PROBLEMO / @I LIED)
initValue
    : NUMBER
    | IDENTIFIER
    | TRUE
    | FALSE
    ;

// =======================
// ASSIGNMENT (stack-based)
// =======================
// GET TO THE CHOPPER myvar
// HERE IS MY INVITATION firstOperand
// [operations...]
// ENOUGH TALK
assignment
    : ASSIGN_VAR_START IDENTIFIER
      ASSIGN_VAR_VALUE operand
      operation*
      ASSIGN_VAR_END
    ;

// Każda operacja to token + operand (jeden na linię)
operation
    : ADD operand
    | SUB operand
    | MUL operand
    | DIV operand
    | MOD operand
    | EQ  operand
    | GT  operand
    | AND operand
    | OR  operand
    ;

// Operand to liczba lub identyfikator
operand
    : NUMBER
    | IDENTIFIER
    | TRUE
    | FALSE
    ;

// =======================
// I/O
// =======================
printStmt
    : PRINT (STRING | IDENTIFIER | NUMBER)
    ;

// =======================
// IF / ELSE
// =======================
// Warunek musi być pojedynczym identyfikatorem lub wartością
// (wcześniej obliczony przez assignment)
ifStmt
    : IF operand
      statement*
      (ELSE statement*)?
      ENDIF
    ;

// =======================
// WHILE
// =======================
// Analogicznie — warunek to pojedynczy operand
whileStmt
    : WHILE operand
      statement*
      ENDWHILE
    ;

// =======================
// FUNKCJE — deklaracja
// =======================
// LISTEN TO ME VERY CAREFULLY methodName
// I NEED YOUR CLOTHES ... arg1      (opcjonalnie, każdy arg osobno)
// I NEED YOUR CLOTHES ... arg2
// GIVE THESE PEOPLE AIR             (opcjonalnie — tylko dla non-void)
// [statements]
// I'LL BE BACK [operand]            (opcjonalnie)
// HASTA LA VISTA, BABY
funcDecl
    : FUNC_START IDENTIFIER
      funcArg*
      FUNC_NONVOID?
      statement*
      returnStmt?
      FUNC_END
    ;

// Każdy argument to osobna linia z FUNC_ARGS
funcArg
    : FUNC_ARGS IDENTIFIER
    ;

returnStmt
    : RETURN operand?
    ;

// =======================
// WYWOŁANIE FUNKCJI
// =======================
// Samo wywołanie (void):
// DO IT NOW methodName arg1 arg2
funcCallStmt
    : CALL IDENTIFIER operand*
    ;

// Wywołanie z przypisaniem wyniku:
// GET YOUR ASS TO MARS resultVar
// DO IT NOW methodName arg1 arg2/ DO IT NOW \n I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY
// 
funcCallAssignStmt
    : CALL_ASSIGN IDENTIFIER
      CALL (IDENTIFIER | READ) operand*
    ;

// =======================
// TOKENY — SŁOWA KLUCZOWE
// =======================
START       : 'IT\'S SHOWTIME' ;
END         : 'YOU HAVE BEEN TERMINATED' ;

PRINT       : 'TALK TO THE HAND' ;
READ        : 'I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY' ;

DECLARE     : 'HEY CHRISTMAS TREE' ;
SET_INIT    : 'YOU SET US UP' ;

ASSIGN_VAR_START : 'GET TO THE CHOPPER' ;
ASSIGN_VAR_VALUE : 'HERE IS MY INVITATION' ;
ASSIGN_VAR_END   : 'ENOUGH TALK' ;

ADD  : 'GET UP' ;
SUB  : 'GET DOWN' ;
MUL  : 'YOU\'RE FIRED' ;
DIV  : 'HE HAD TO SPLIT' ;
MOD  : 'I LET HIM GO' ;

EQ   : 'YOU ARE NOT YOU YOU ARE ME' ;
GT   : 'LET OFF SOME STEAM BENNET' ;
AND  : 'KNOCK KNOCK' ;
OR   : 'CONSIDER THAT A DIVORCE' ;

IF      : 'BECAUSE I\'M GOING TO SAY PLEASE' ;
ELSE    : 'BULLSHIT' ;
ENDIF   : 'YOU HAVE NO RESPECT FOR LOGIC' ;

WHILE    : 'STICK AROUND' ;
ENDWHILE : 'CHILL' ;

FUNC_START   : 'LISTEN TO ME VERY CAREFULLY' ;
FUNC_NONVOID : 'GIVE THESE PEOPLE AIR' ;
FUNC_ARGS    : 'I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE' ;
RETURN       : 'I\'LL BE BACK' ;
FUNC_END     : 'HASTA LA VISTA, BABY' ;
CALL         : 'DO IT NOW' ;
CALL_ASSIGN  : 'GET YOUR ASS TO MARS' ;

TRUE    : '@NO PROBLEMO' ;
FALSE   : '@I LIED' ;

ERROR_TOKEN : 'WHAT THE FUCK DID I DO WRONG' ;

// =======================
// LITERAŁY
// =======================
NUMBER      : [0-9]+ ;
STRING      : '"' (~["\r\n])* '"' ;
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]* ;

// =======================
// BIAŁE ZNAKI I KOMENTARZE
// =======================
WS : [ \t\r\n]+ -> skip ;

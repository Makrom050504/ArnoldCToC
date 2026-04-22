# ArnoldC to C Compiler

## Dane zespołu

Maksymilian Roman - [mroman@student.agh.edu.pl](mailto:mroman@student.agh.edu.pl)  
Szymon Lipiński - [slipinski@student.agh.edu.pl](mailto:slipinski@student.agh.edu.pl)

---

## Założenia programu

### Ogólne cele

Celem programu jest stworzenie kompilatora (translatora źródło–źródło), który przekształca kod napisany w języku ArnoldC do równoważnego kodu w języku C.

### Rodzaj translatora

Kompilator (source-to-source compiler)

### Planowany wynik działania programu

Efektem działania programu będzie narzędzie:

* przyjmujące kod ArnoldC jako wejście,
* generujące poprawny składniowo i semantycznie kod w języku C,
* umożliwiające dalszą kompilację przy użyciu standardowego kompilatora C (np. `gcc`).

### Planowany język implementacji

Python

### Sposób realizacji skanera/parsera

ANTLR4

---

## Opis tokenów 

### 1. Struktura programu

| Token                      | Opis              |
| -------------------------- | ----------------- |
| `IT'S SHOWTIME`            | Początek programu |
| `YOU HAVE BEEN TERMINATED` | Koniec programu   |

---

### 2. Operacje wejścia/wyjścia

| Token              | Opis               | Odpowiednik w C |
| ------------------ | ------------------ | --------------- |
| `TALK TO THE HAND` | Wypisanie wartości | `printf(...)`   |

---

### 3. Deklaracje i przypisania

| Token                | Opis                                     | Odpowiednik w C |
| -------------------- | ---------------------------------------- | --------------- |
| `HEY CHRISTMAS TREE` | Deklaracja zmiennej                      | `int x;`        |
| `YOU SET US UP`      | Przypisanie wartości (lub inicjalizacja) | `x = ...;`      |

Przykład:

```arnoldc
HEY CHRISTMAS TREE x
YOU SET US UP 10
```

---

### 4. Operacje arytmetyczne

| Token             | Opis        | Operator w C |
| ----------------- | ----------- | ------------ |
| `GET UP`          | Dodawanie   | `+`          |
| `GET DOWN`        | Odejmowanie | `-`          |
| `YOU'RE FIRED`    | Mnożenie    | `*`          |
| `HE HAD TO SPLIT` | Dzielenie   | `/`          |

---

### 5. Operacje logiczne i porównania

| Token                        | Opis        | Operator w C |
| ---------------------------- | ----------- | ------------ |
| `YOU ARE NOT YOU YOU ARE ME` | Równość     | `==`         |
| `LET OFF SOME STEAM BENNET`  | Większe niż | `>`          |
| `CONSIDER THAT A DIVORCE`    | Nierówność  | `!=`         |

---

### 6. Sterowanie przepływem

| Token                             | Opis                   | Odpowiednik w C |
| --------------------------------- | ---------------------- | --------------- |
| `BECAUSE I'M GOING TO SAY PLEASE` | Początek instrukcji if | `if (...) {`    |
| `BULLSHIT`                        | Gałąź else             | `} else {`      |
| `YOU HAVE NO RESPECT FOR LOGIC`   | Koniec instrukcji if   | `}`             |

---

### 7. Pętle

| Token          | Opis           | Odpowiednik w C |
| -------------- | -------------- | --------------- |
| `STICK AROUND` | Początek pętli | `while (...) {` |
| `CHILL`        | Koniec pętli   | `}`             |

---

### 8. Wartości i identyfikatory

| Token         | Opis                              |
| ------------- | --------------------------------- |
| `NUMBER`      | Liczby całkowite                  |
| `STRING`      | Literały tekstowe (w cudzysłowie) |
| `IDENTIFIER`  | Nazwy zmiennych                   |
| `NO PROBLEMO` | Wartość logiczna prawda (`true`)  |
| `I LIED`      | Wartość logiczna fałsz (`false`)  |

---

### 9. Symbole pomocnicze

| Token   | Opis    |
| ------- | ------- |
| `(` `)` | Nawiasy |

---

## Gramatyka ANTLR4

Poniżej przedstawiono formalną gramatykę języka ArnoldC przygotowaną dla narzędzia ANTLR4.

### Plik: `ArnoldC.g4`

```antlr
grammar ArnoldC;

// ===== Parser rules =====

program
    : START statement* END EOF
    ;

statement
    : declaration
    | assignment
    | printStmt
    | ifStmt
    | loopStmt
    ;

declaration
    : DECLARE IDENTIFIER (ASSIGN expression)?
    ;

assignment
    : IDENTIFIER ASSIGN expression
    ;

printStmt
    : PRINT expression
    ;

ifStmt
    : IF expression statement* (ELSE statement*)? ENDIF
    ;

loopStmt
    : LOOP expression statement* ENDLOOP
    ;

expression
    : comparisonExpr
    ;

comparisonExpr
    : additiveExpr ((EQ | GT | NEQ) additiveExpr)*
    ;

additiveExpr
    : multiplicativeExpr ((ADD | SUB) multiplicativeExpr)*
    ;

multiplicativeExpr
    : atom ((MUL | DIV) atom)*
    ;

atom
    : IDENTIFIER
    | NUMBER
    | STRING
    | TRUE
    | FALSE
    | '(' expression ')'
    ;

// ===== Lexer rules =====

// Program structure
START  : 'IT\'S SHOWTIME';
END    : 'YOU HAVE BEEN TERMINATED';

// I/O
PRINT  : 'TALK TO THE HAND';

// Variables
DECLARE : 'HEY CHRISTMAS TREE';
ASSIGN  : 'YOU SET US UP';

// Arithmetic
ADD : 'GET UP';
SUB : 'GET DOWN';
MUL : 'YOU\'RE FIRED';
DIV : 'HE HAD TO SPLIT';

// Logic
EQ  : 'YOU ARE NOT YOU YOU ARE ME';
GT  : 'LET OFF SOME STEAM BENNET';
NEQ : 'CONSIDER THAT A DIVORCE';

// Control flow
IF    : 'BECAUSE I\'M GOING TO SAY PLEASE';
ELSE  : 'BULLSHIT';
ENDIF : 'YOU HAVE NO RESPECT FOR LOGIC';

// Loop
LOOP    : 'STICK AROUND';
ENDLOOP : 'CHILL';

// Values
TRUE  : 'NO PROBLEMO';
FALSE : 'I LIED';

// Literals and identifiers
NUMBER : [0-9]+;
STRING : '"' (~["\\] | '\\' .)* '"';
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

// Whitespace
WS : [ \t\r\n]+ -> skip;
```

---


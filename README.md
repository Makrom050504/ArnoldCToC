# ArnoldC to C Compiler

## Dane zespołu

Maksymilian Roman - [mroman@student.agh.edu.pl](mailto:mroman@student.agh.edu.pl)  
Szymon Lipiński - [slipinski@student.agh.edu.pl](mailto:slipinski@student.agh.edu.pl)

---

## Założenia programu

### Ogólne cele

Celem programu jest przekonwertowanie kodu w języku ArnoldC do języka C.

### Rodzaj translatora

Kompilator (translator źródło–źródło).

### Planowany wynik działania programu

Efektem działania programu będzie narzędzie przyjmujące kod ArnoldC i generujące równoważny kod w języku C.

### Planowany język implementacji

Python

### Sposób realizacji skanera/parsera

ANTLR4

---

## Opis tokenów

Poniżej znajduje się szczegółowy podział tokenów używanych w języku ArnoldC wraz z ich znaczeniem i przykładowym odwzorowaniem.

### 1. Struktura programu

| Token                      | Opis              |
| -------------------------- | ----------------- |
| `IT'S SHOWTIME`            | Początek programu |
| `YOU HAVE BEEN TERMINATED` | Koniec programu   |

---

### 2. Operacje wejścia/wyjścia

| Token              | Opis               | Odpowiednik w C |
| ------------------ | ------------------ | --------------- |
| `TALK TO THE HAND` | Wypisanie wartości | `printf`        |

---

### 3. Deklaracje i przypisania

| Token                | Opis                 | Odpowiednik w C |
| -------------------- | -------------------- | --------------- |
| `HEY CHRISTMAS TREE` | Deklaracja zmiennej  | `int x;`        |
| `YOU SET US UP`      | Przypisanie wartości | `x = ...;`      |

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

| Token                        | Opis                 | Operator w C |
| ---------------------------- | -------------------- | ------------ |
| `YOU ARE NOT YOU YOU ARE ME` | Równość              | `==`         |
| `LET OFF SOME STEAM BENNET`  | Większe niż          | `>`          |
| `CONSIDER THAT A DIVORCE`    | Negacja / nierówność | `!=`         |

---

### 6. Sterowanie przepływem

| Token                             | Opis                     | Odpowiednik w C |
| --------------------------------- | ------------------------ | --------------- |
| `BECAUSE I'M GOING TO SAY PLEASE` | If                       | `if`            |
| `BULLSHIT`                        | Else                     | `else`          |
| `YOU HAVE NO RESPECT FOR LOGIC`   | Koniec bloku warunkowego | `}`             |

---

### 7. Pętle

| Token          | Opis           | Odpowiednik w C |
| -------------- | -------------- | --------------- |
| `STICK AROUND` | Początek pętli | `while`         |
| `CHILL`        | Koniec pętli   | `}`             |

---

### 8. Wartości i identyfikatory

| Token            | Opis              |
| ---------------- | ----------------- |
| `NUMBER`         | Liczby całkowite  |
| `IDENTIFIER`     | Nazwy zmiennych   |
| `TRUE` / `FALSE` | Wartości logiczne |

---

### 9. Symbole pomocnicze

| Token     | Opis                 |
| --------- | -------------------- |
| `(` `)`   | Nawiasy              |
| `;`       | Separator instrukcji |
| operatory | symbole pomocnicze   |

---

## Gramatyka ANTLR4



```antlr
grammar ArnoldC;

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
    : DECLARE IDENTIFIER
    ;

assignment
    : ASSIGN IDENTIFIER expression
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
    : expression ADD expression
    | expression SUB expression
    | expression MUL expression
    | expression DIV expression
    | expression EQ expression
    | expression GT expression
    | expression NEQ expression
    | IDENTIFIER
    | NUMBER
    | '(' expression ')'
    ;



START  : 'IT\'S SHOWTIME';
END    : 'YOU HAVE BEEN TERMINATED';


PRINT  : 'TALK TO THE HAND';


DECLARE : 'HEY CHRISTMAS TREE';
ASSIGN  : 'YOU SET US UP';

ADD : 'GET UP';
SUB : 'GET DOWN';
MUL : 'YOU\'RE FIRED';
DIV : 'HE HAD TO SPLIT';

EQ  : 'YOU ARE NOT YOU YOU ARE ME';
GT  : 'LET OFF SOME STEAM BENNET';
NEQ : 'CONSIDER THAT A DIVORCE';

IF    : 'BECAUSE I\'M GOING TO SAY PLEASE';
ELSE  : 'BULLSHIT';
ENDIF : 'YOU HAVE NO RESPECT FOR LOGIC';

LOOP    : 'STICK AROUND';
ENDLOOP : 'CHILL';

NUMBER : [0-9]+;
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip;
```

---


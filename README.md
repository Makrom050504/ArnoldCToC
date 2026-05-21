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

| Token | Wzorzec            | Opis              |
| ----- | -------------------------- | ----------------- |
| START | `IT'S SHOWTIME`            | Początek programu |
| END   | `YOU HAVE BEEN TERMINATED` | Koniec programu   |

---

### 2. Operacje wejścia/wyjścia

| Token | Wzorzec                                 | Opis               |
| ----- | ----------------------------------------| ------------------ |
| PRINT | `TALK TO THE HAND`                      | Wypisanie wartości |


---

### 3. Deklaracje i przypisania

| Token    | Wzorzec              | Opis                   |
| -------- | -------------------- | ---------------------- |
| DECLARE  | `HEY CHRISTMAS TREE` | Deklaracja zmiennej    |
| SET_INIT | `YOU SET US UP`      | Inicjalizacja zmiennej |

### Aktualizacja zmiennej/blok obliczeniowy
| Token            | Wzorzec                 | Opis                 |
| ---------------- | ----------------------- | -------------------- |
| ASSIGN_VAR_START | `GET TO THE CHOPPER`    | Początek przypisania |
| ASSIGN_VAR_VALUE | `HERE IS MY INVITATION` | Wartość przypisania  |
| ASSIGN_VAR_END   | `ENOUGH TALK`           | Koniec przypisania   |



### 4. Operacje arytmetyczne

| Token | Wzorzec           | Operator |
| ----- | ----------------- | -------- |
| ADD   | `GET UP`          | `+`      |
| SUB   | `GET DOWN`        | `-`      |
| MUL   | `YOU'RE FIRED`    | `*`      |
| DIV   | `HE HAD TO SPLIT` | `/`      |
| MOD   | `I LET HIM GO`    | `%`      |


---

### 5. Operacje logiczne i porównania

| Token | Wzorzec                      | Operator |
| ----- | ---------------------------- | -------- |
| EQ    | `YOU ARE NOT YOU YOU ARE ME` | `==`     |
| GT    | `LET OFF SOME STEAM BENNET`  | `>`      |
| AND   | `KNOCK KNOCK`                | `&&`     |
| OR    | `CONSIDER THAT A DIVORCE`    | `\|\|`   |


---

### 6. Sterowanie przepływem

| Token | Wzorzec                           | Opis                   |
| ----- | --------------------------------- | ---------------------- |
| IF    | `BECAUSE I'M GOING TO SAY PLEASE` | Początek instrukcji if |
| ELSE  | `BULLSHIT`                        | Gałąź else             |
| ENDIF | `YOU HAVE NO RESPECT FOR LOGIC`   | Koniec instrukcji if   |


---

### 7. Pętle

| Token    | Wzorzec        | Opis           |
| -------- | -------------- | -------------- |
| WHILE    | `STICK AROUND` | Początek pętli |
| ENDWHILE | `CHILL`        | Koniec pętli   |


---
### 8. Funkcje
| Token        | Wzorzec                                              | Opis                       |
| ------------ | ---------------------------------------------------- | -------------------------- |
| FUNC_START   | `LISTEN TO ME VERY CAREFULLY`                        | Deklaracja funkcji         |
| FUNC_NONVOID | `GIVE THESE PEOPLE AIR`                              | Funkcja zwracająca wartość |
| FUNC_ARGS    | `I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE` | Argumenty funkcji          |
| RETURN       | `I'LL BE BACK`                                       | Zwrócenie wartości         |
| FUNC_END     | `HASTA LA VISTA, BABY`                               | Koniec funkcji             |
| CALL         | `DO IT NOW`                                          | Wywołanie funkcji          |
| CALL_ASSIGN  | `GET YOUR ASS TO MARS`                               | Przypisanie wyniku funkcji |
|READ |`I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY`|Wbudowana funkcja wczytująca liczbę
### 9. Wartości logiczne

| Token | Wzorzec       | Wartość |
| ----- | ------------- | ------- |
| TRUE  | `@NO PROBLEMO` | `true`  |
| FALSE | `@I LIED`      | `false` |
### 10. Literały i identyfikatory

| Token      | Wzorzec (regex)          | Opis             |
| ---------- | ------------------------ | ---------------- |
| NUMBER     | `[0-9]+`                 | Liczba całkowita |
| STRING     | `"..."`                  | Literał tekstowy |
| IDENTIFIER | `[a-zA-Z_][a-zA-Z0-9_]*` | Nazwa zmiennej   |




### 11. Obsługa błędów
| Token       | Wzorzec                        | Opis        |
| ----------- | ------------------------------ | ----------- |
| ERROR_TOKEN | `WHAT THE FUCK DID I DO WRONG` | Token błędu |

### 12. Białe znaki
| Token | Wzorzec      | Opis                   |
| ----- | ------------ | ---------------------- |
| WS    | `[ \t\r\n]+` | Ignorowane białe znaki |

---

## Gramatyka ANTLR4


### Plik: `ArnoldC.g4`
[ArnoldC.g4](ArnoldC.g4)




## Pełna gramatyka formatu

Poniżej znajduje się gramatyka języka ArnoldC obsługiwanego przez projekt, zapisana w notacji generatora ANTLR4. Gramatyka nie zawiera akcji semantycznych — opisuje wyłącznie strukturę składniową języka.

```antlr
grammar ArnoldC;

program
    : funcDecl* START statement* END funcDecl* EOF
    ;

statement
    : declaration
    | assignment
    | printStmt
    | ifStmt
    | whileStmt
    | funcCallStmt
    | funcCallAssignStmt
    | returnStmt
    ;

declaration
    : DECLARE IDENTIFIER SET_INIT initValue
    ;

initValue
    : NUMBER
    | IDENTIFIER
    | TRUE
    | FALSE
    ;

assignment
    : ASSIGN_VAR_START IDENTIFIER
      ASSIGN_VAR_VALUE operand
      operation*
      ASSIGN_VAR_END
    ;

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

operand
    : NUMBER
    | IDENTIFIER
    | TRUE
    | FALSE
    ;

printStmt
    : PRINT (STRING | IDENTIFIER | NUMBER)
    ;

ifStmt
    : IF operand
      statement*
      (ELSE statement*)?
      ENDIF
    ;

whileStmt
    : WHILE operand
      statement*
      ENDWHILE
    ;

funcDecl
    : FUNC_START IDENTIFIER
      funcArg*
      FUNC_NONVOID?
      statement*
      FUNC_END
    ;

funcArg
    : FUNC_ARGS IDENTIFIER
    ;

returnStmt
    : RETURN operand?
    ;

funcCallStmt
    : CALL IDENTIFIER operand*
    ;

funcCallAssignStmt
    : CALL_ASSIGN IDENTIFIER
      CALL (IDENTIFIER | READ) operand*
    ;

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

NUMBER      : [0-9]+ ;
STRING      : '"' (~["\r\n])* '"' ;
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;
```

## Informacje o stosowanych generatorach i pakietach zewnętrznych

Projekt wykorzystuje generator parserów i lekserów **ANTLR4**.

ANTLR4 jest używany do:

* zdefiniowania tokenów języka ArnoldC,
* zdefiniowania gramatyki składniowej języka,
* wygenerowania leksera,
* wygenerowania parsera,
* wygenerowania klasy bazowej visitora.

W projekcie wykorzystywane są wygenerowane pliki znajdujące się w katalogu:

```text
Main/ANTLR4_generated/
```

Najważniejsze wygenerowane pliki to:

```text
ArnoldCLexer.py
ArnoldCParser.py
ArnoldCVisitor.py
```

Do obsługi drzewa składniowego wykorzystywany jest własny visitor:

```text
Main/ArnoldCToCVisitor.py
```

Program korzysta również z pakietu:

```text
antlr4-python3-runtime
```

Pakiet ten umożliwia uruchamianie parsera ANTLR4 w języku Python.

## Krótka instrukcja obsługi

### 1. Instalacja zależności

Przed uruchomieniem programu należy zainstalować bibliotekę uruchomieniową ANTLR4 dla Pythona:

```bash
pip install antlr4-python3-runtime
```

### 2. Struktura najważniejszych plików

```text
Main/
├── main.py
├── ArnoldCToCVisitor.py
├── grammar/
│   └── ArnoldC.g4
├── ANTLR4_generated/
│   ├── ArnoldCLexer.py
│   ├── ArnoldCParser.py
│   └── ArnoldCVisitor.py
└── Tests/
    ├── input.arnoldc
    ├── loops.arnoldc
    ├── modulo_func.arnoldc
    ├── operations.arnoldc
    ├── recursion.arnoldc
```

### 3. Uruchomienie translatora

Aby uruchomić kompilator, należy przejść do katalogu `Main` i uruchomić plik `main.py`:

```bash
cd Main
python main.py input.arnoldc -o output.c
```

Dostępne flagi:

| Flaga | Opis |
|-------|------|
| `input` | ścieżka do pliku wejściowego ArnoldC |
| `-o`, `--output` | ścieżka do pliku wynikowego C (domyślnie: `out.c`) |
| `--compile` | kompiluje wygenerowany kod C przez `gcc` |
| `--run` | kompiluje i uruchamia wygenerowany program |

### 4. Kompilacja i uruchomienie

Można kompilować i uruchamiać program ręcznie:

```bash
gcc out.c -o out
./out
```

Lub skorzystać z flag `--compile` i `--run`, które robią to automatycznie:

```bash
# kompilacja
python main.py input.arnoldc --compile

# kompilacja i uruchomienie
python main.py input.arnoldc --run
```

## Przykład użycia
(więcej przykładów zaznajamiających z językiem ArnoldC [ArnoldC](https://github.com/lhartikk/ArnoldC/wiki/ArnoldC)


Przykładowy program w języku ArnoldC:

```text
IT'S SHOWTIME
HEY CHRISTMAS TREE n
YOU SET US UP 0
GET TO THE CHOPPER n
HERE IS MY INVITATION n
GET UP 5
ENOUGH TALK
TALK TO THE HAND n
YOU HAVE BEEN TERMINATED
```

Znaczenie programu:

* rozpoczęcie programu,
* zadeklarowanie zmiennej `n`,
* przypisanie jej wartości początkowej `0`,
* wykonanie operacji `n = n + 5`,
* wypisanie wartości zmiennej `n`,
* zakończenie programu.

Przykładowy kod C wygenerowany przez translator:

```c
#include <stdio.h>

int main() {
    int n = 0;
    n = n + 5;
    printf("%d\n", n);
    return 0;
}
```

Przykładowy wynik działania programu:

```text
5
```

## Opis działania translatora

Translator działa w kilku etapach:

1. Wczytanie pliku źródłowego napisanego w języku ArnoldC.
2. Przekazanie kodu wejściowego do leksera wygenerowanego przez ANTLR4.
3. Zamiana kodu źródłowego na strumień tokenów.
4. Przekazanie tokenów do parsera wygenerowanego przez ANTLR4.
5. Zbudowanie drzewa składniowego programu.
6. Przejście po drzewie składniowym za pomocą klasy `MyVisitor`.
7. Generowanie odpowiadającego kodu w języku C.
8. Zapisanie kodu wynikowego do pliku `out.c`.

## Obsługiwane elementy języka

Aktualna wersja translatora obsługuje:

* strukturę programu ArnoldC,
* deklaracje zmiennych całkowitych,
* inicjalizację zmiennych,
* przypisania,
* operacje arytmetyczne:
  * dodawanie,
  * odejmowanie,
  * mnożenie,
  * dzielenie,
  * modulo,
* operacje logiczne i porównania:
  * równość,
  * większość,
  * koniunkcję,
  * alternatywę,
* wypisywanie wartości na standardowe wyjście,
* instrukcje warunkowe `if` oraz `else`,
* pętle `while`,
* funkcje,
* argumenty funkcji,
* zwracanie wartości z funkcji,
* wywołania funkcji,
* przypisanie wyniku funkcji do zmiennej,
* prostą obsługę wejścia z użyciem funkcji `scanf`.

## Ograniczenia programu

W obecnej wersji translatora przyjęto następujące uproszczenia:

* wszystkie zmienne są tłumaczone jako typ `int`,
* wartości logiczne są reprezentowane jako liczby całkowite:
  * `@NO PROBLEMO` jako `1`,
  * `@I LIED` jako `0`,
* warunki w instrukcjach `if` i `while` są pojedynczymi operandami,
* bardziej złożone wyrażenia należy wcześniej obliczyć w instrukcji przypisania,
* obsługiwane są liczby całkowite,
* literały tekstowe są obsługiwane tylko w instrukcji wypisywania,
* wygenerowany kod C wymaga dalszej kompilacji z użyciem zewnętrznego kompilatora, np. `gcc`.

## Przykład funkcji

Przykładowa funkcja w języku ArnoldC:

```text
LISTEN TO ME VERY CAREFULLY modulo
I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE dividend
I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE divisor
GIVE THESE PEOPLE AIR
HEY CHRISTMAS TREE quotient
YOU SET US UP 0
HEY CHRISTMAS TREE remainder
YOU SET US UP 0
HEY CHRISTMAS TREE product
YOU SET US UP 0
GET TO THE CHOPPER quotient
HERE IS MY INVITATION dividend
HE HAD TO SPLIT divisor
ENOUGH TALK
GET TO THE CHOPPER product
HERE IS MY INVITATION divisor
YOU'RE FIRED quotient
ENOUGH TALK
GET TO THE CHOPPER remainder
HERE IS MY INVITATION dividend
GET DOWN product
ENOUGH TALK
I'LL BE BACK remainder
HASTA LA VISTA, BABY
```

Odpowiadający kod w języku C:

```c
int modulo(int dividend, int divisor) {
    int quotient = 0;
    int remainder = 0;
    int product = 0;
    quotient = dividend / divisor;
    product = divisor * quotient;
    remainder = dividend - product;
    return remainder;
}
```

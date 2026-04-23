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


---

### 11. Symbole pomocnicze

| Token  | Wzorzec | Opis         |
| ------ | ------- | ------------ |
| LPAREN | `(`     | Lewy nawias  |
| RPAREN | `)`     | Prawy nawias |

### 12. Obsługa błędów
| Token       | Wzorzec                        | Opis        |
| ----------- | ------------------------------ | ----------- |
| ERROR_TOKEN | `WHAT THE FUCK DID I DO WRONG` | Token błędu |

### 13. Białe znaki
| Token | Wzorzec      | Opis                   |
| ----- | ------------ | ---------------------- |
| WS    | `[ \t\r\n]+` | Ignorowane białe znaki |

---

## Gramatyka ANTLR4


### Plik: `ArnoldC.g4`
[ArnoldC.g4](ArnoldC.g4)




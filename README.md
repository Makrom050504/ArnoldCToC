# ArnoldC to C Compiler
## Dane zespołu
Maksymilian Roman -  
Szymon Lipiński - slipinski@student.agh.edu.pl
## Założenia programu

### Ogólne cele
Celem programu jest przekonwertowanie kodu w języku ArnoldC do języka C  

### Rodzaj translatora
Kompilator

### Planowany wynik działania programu
Efektem działania programu będzie konwerter języka ArnoldC do języka C

### Planowany język implementacji
Python

### Sposób realizacji skanera/parsera
ANTLR4

---

## 3. Opis tokenów

Poniższa tabela przedstawia przykładowe grupy tokenów wykorzystywanych w analizie leksykalnej języka ArnoldC.

| Kategoria | Tokeny / Konstrukcje | Opis |
|----------|-----------------------|------|
| Słowa kluczowe programu | `IT'S SHOWTIME`, `YOU HAVE BEEN TERMINATED`, `TALK TO THE HAND` | Konstrukcje rozpoczynające i kończące program oraz wypisujące dane |
| Deklaracje i przypisania | `HEY CHRISTMAS TREE`, `YOU SET US UP` | Deklaracja zmiennej oraz przypisanie wartości |
| Operacje arytmetyczne | `GET UP`, `GET DOWN`, `YOU'RE FIRED`, `HE HAD TO SPLIT` | Dodawanie, odejmowanie, mnożenie i dzielenie |
| Logika i porównania | `YOU ARE NOT YOU YOU ARE ME`, `LET OFF SOME STEAM BENNET`, `CONSIDER THAT A DIVORCE` | Operacje porównania i negacji logicznej |
| Sterowanie przepływem | `BECAUSE I'M GOING TO SAY PLEASE`, `BULLSHIT`, `YOU HAVE NO RESPECT FOR LOGIC` | Instrukcje warunkowe oraz ich alternatywne gałęzie |
| Pętle | `STICK AROUND`, `CHILL` | Konstrukcje iteracyjne |
| Wartości stałe | liczby całkowite, identyfikatory, wartości logiczne | Podstawowe elementy używane w programie |
| Symbole pomocnicze | nawiasy, separatory, operatory | Elementy pomocnicze składni niezbędne do analizy programu |

---


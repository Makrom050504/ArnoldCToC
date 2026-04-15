# ArnoldC to C Compiler

## 2. Założenia programu

### Ogólne cele
Celem projektu jest implementacja kompilatora języka **ArnoldC**, który dokonuje translacji programów zapisanych w tym języku do równoważnego kodu w języku **C**. Projekt ma umożliwiać analizę składniową i semantyczną kodu źródłowego ArnoldC, a następnie generowanie poprawnego kodu wynikowego w języku C, zachowującego logikę i strukturę programu wejściowego.

Program ma stanowić narzędzie demonstracyjne pokazujące proces budowy translatora języków programowania – od etapu tokenizacji i parsowania, przez konstrukcję reprezentacji pośredniej, aż po generację kodu docelowego.

### Rodzaj translatora
**Kompilator**

### Planowany wynik działania programu
Efektem działania programu będzie **konwerter języka ArnoldC do języka C**, który:
- wczytuje kod źródłowy zapisany w ArnoldC,
- przeprowadza analizę leksykalną i składniową,
- buduje wewnętrzną reprezentację programu,
- generuje równoważny kod w języku C.

Wynikowy kod C będzie można następnie skompilować przy użyciu standardowego kompilatora, np. `gcc`.

### Planowany język implementacji
**Python**

### Sposób realizacji skanera/parsera
Do realizacji skanera i parsera zostanie wykorzystany **generator parserów ANTLR4**.  
ANTLR4 posłuży do:
- definicji reguł leksykalnych odpowiadających tokenom języka ArnoldC,
- zdefiniowania gramatyki opisującej poprawne konstrukcje składniowe,
- wygenerowania parsera umożliwiającego budowę drzewa składniowego programu.

Na podstawie wygenerowanego drzewa składniowego program będzie wykonywał translację do języka C.

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

> Ostateczny zestaw tokenów zależy od zakresu obsługiwanego podzbioru języka ArnoldC przyjętego w projekcie.

---


```text
grammar/ArnoldC.g4

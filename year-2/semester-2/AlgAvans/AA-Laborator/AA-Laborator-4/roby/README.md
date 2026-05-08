# Roby


#### Descriere

Roby este un aspirator-roboțel care are sarcina de a face curat într-o cameră. Roboțelul pleacă dintr-un punct de start $`P_{1}`$ și apoi urmează un traseu care este o linie poligonală $`P_{1}P_{2}\ldots P_{n}P_{1}`$, la final roboțelul întorcându-se și oprindu-se în $`P_{1}`$. Fiecare punct $`P_{i}`$ este descris prin coordonatele sale $`(x_{i},y_{i})`$. În fiecare punct $`P_{i}`$ roboțelul trebuie să vireze la stânga sau la dreapta sau să continue să meargă pe aceeași dreaptă.

La final, pe lângă curățarea camerei, Roby trebuie să indice numărul total de **viraje la stânga**, numărul total de **viraje la dreapta** și numărul de situații în care **a rămas pe aceeași dreaptă**. Ajutați-l pe Roby să își finalizeze cu bine sarcina, indicând cele trei numere.

#### Date de intrare

Datele de intrare se vor citi de la tastatură. Datele conțin pe prima linie un număr natural $`n`$. Pe urmatoarele $`n`$ linii se află perechi de numere întregi, reprezentând coordonatele punctelor $`P_{1},P_{2},\ldots,P_{n}`$, în această ordine. Pentru fiecare $`i`$, pentru punctul $`P_{i}`$ sunt indicate pe aceeași linie coordonatele $`x_{i}`$ și $`y_{i}`$, separate printr-un spațiu.

#### Date de ieșire

Se vor afișa pe o singură linie, separate prin spațiu, numarul total de viraje la stânga, numărul total de viraje la dreapta și numărul de situații în care a rămas pe aceeași dreaptă (în această ordine).

#### Restricții și precizări

- $`3 \leq n \leq 10^{5}`$.
- $`- 10000 \leq x_{i},y_{i} \leq 10000`$, $`\forall i = \overset{―}{1,n}`$.
- Cazul de coliniaritate include situațiile următoare:
  1.  roboțelul continuă deplasarea în același sens;
  2.  roboțelul schimbă sensul deplasării rămânând pe aceeași dreaptă;
  3.  cel puțin două dintre punctele pentru care se realizează testarea coincid.

#### Exemplu

##### Input

Copy

```
7
1 1
2 2
2 0
3 0
4 0
5 0
6 0
```

##### Output

Copy

```
2 1 3
```

##### Explicație

Traseul parcurs de Roby are în total **6** viraje: **2** la stânga (în punctele $`P_{3}`$ și $`P_{7}`$), **1** la dreapta (în $`P_{2}`$) și are **3** puncte în care continuă drept înainte (în $`P_{4}`$, $`P_{5}`$ si $`P_{6}`$).

În $`P_{1}`$ nu este realizat niciun viraj, deoarece roboțelul se oprește.

\
[proudly powered by **DMOJ**](https://dmoj.ca/) \|

català (ca) Deutsch (de) Ελληνικά (el) English (en) español (es) français (fr) Hrvatski (hr) Magyar (hu) 日本語 (ja) Қазақ (kk) 한국어 (ko) Português (pt) Română (ro) Русский (ru) srpski (latinica) (sr-latn) Türkçe (tr) Tiếng Việt (vi) 简体中文 (zh-hans) 繁體中文 (zh-hant)
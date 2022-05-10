## Tokeny

  * Token | Opis |
  * ------ | ----- |
  * `\n` | NOWALINIA |
  * ` ` | SPACJA |
  * `|` | TABELA |
  * `[a-zA-Z0-9]+[a-zA-Z0-9 | !$%^&*()_+~-='{}[]:";#'<>?,./]* + [\n]` | TEKST |
  * `:-+|-+:|-+:-+` | TABELAODDZIELACZ  |
  * ` " ` | ZNAKŁANCUCHA |
  * `\t` | ZNAKTABULACJI |
  * `\t` | ZNAKTABULACJI |
  * `\n#` | NAGŁÓWEK1 |
  * `\n##` | NAGŁÓWEK2 |
  * `\n###` | NAGŁÓWEK3 |
  * `\n####` | NAGŁÓWEK4 |
  * `\n#####` | NAGŁÓWEK5 |
  * `\n######` | NAGŁÓWEK6 |
  * `\n---[\n \t]+` | LINIAPOZIOMA |
  * `\n***[\n \t]+` | LINIAPOZIOMA |
  * `\n___[\n \t]+` | LINIAPOZIOMA |
  * `**`, `__` | POGRUBIENIE |
  * `~~` | PRZEKRESLENIE |
  * `*`. `_` | KURSYWA |
  * `>` | CYTAT |
  * `+` | NIEPONUMEROWANALISTA |
  * `[0-9]*\. ` | PONUMEROWANALISTA |
  * ` ``` ` | KOD |


## Gramatyka
  *  | Produkcja |
  * --- | --- |
  * `[TEKST](TEKST)` | link |
  * `![TEKST](TEKST)` | obraz |
  * `![TEKST](TEKST)` | obraz |
  * `![TEKST](TEKST)łańcuch` | obraz |
  * `ZNAKŁANCUCHA TEKST ZNAKŁANCUCHA` | łańcuch |
  * `NAGŁÓWEK1 TEKST | NAGŁÓWEK2 TEKST | NAGŁÓWEK3 TEKST | NAGŁÓWEK4 TEKST | NAGŁÓWEK5 TEKST | NAGŁÓWEK6 TEKST ` | nagłówek |
  * `POGRUBIENIE TEKST POGRUBIENIE` | pogrubionyTekst |
  * `KURSYWA TEKST KURSYWA` | kursywaTekst |
  * `PRZEKRESLENIE TEKST PRZEKRESLENIE` | krzekreślenietekst |
  * `CYTAT TEKST | CYTAT cytattekst` | cytattekst |
  * `NIEPONUMEROWANALISTA SPACJA TEKST` | listanienumerowana |
  * `PONUMEROWANALISTA SPACJA TEKST` | listanumerowana |
  * `KOD NOWALINIA TEKST NOWALINIA KOD` | blokkodu |
  * `TABELA TEKST TABELA | tabelawiersz TABELA TEKST TABELA` | tabelawiersz |
  * `tabelawiersz` | tabelanagłówek |
  * `TABELA TABELAODDZIELACZ TABELA tabelaprzerywnik? ` |   tabelaprzerywnik |
  * `NOWALINIA tabelanagłówek tabelaprzerywnik tabelawiersz*` | tabela |







# Emoticons (Humørikoner) #

* Forfattere: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco
  Javier Estrada Martínez
* NVDA-kompatibilitet: 2018.3 til 2019.1
* Download [stabil version][1]
* Download [udviklingsversion][2]

Med dette tilføjelsesprogram vil du få udtalt humørikoner i tekster på en
mere brugervenlig måde.

F.eks. vil ":)" blive udtalt som "smilende smiley", og NVDA vil også være i
stand til at genkende og udtale emojis.

Du kan udnytte følgende funktioner:

## Indsæt humørikon ##

Nogle gange er et billede 1000 ord værd: Brug de nye emoji og lade dine
venner vide, hvordan du føler, og til at sætte fut i dine chatbeskeder.

Når du er usikker på tegn for en særlig smiley, giver denne tilføjelse dig
mulighed for at vælge og indsætte den i din tekst som i en chat.

Tryk på NVDA + I, eller fra menuen værktøjer-> Indsæt humørikon, kan du åbne en dialog med de medfølgende humørikoner eller emoji.

Denne dialog lader dig vælge et humørikon og vise de humørikoner, der
interesserer dig:

*	Et redigeringsfelt lader dig filtrere søgning af de humørikoner, som du
  ønsker.
*	Ved brug af et sæt af radioknapper kan du vælge at se kun emoji (alt+E)
  eller se kun standardhumørikoner (alt+S) eller se alle tilgængelige
  humørikoner (alt+A).
*	I listen over humørikoner (Alt+L) kan du se tre kolonner: Disse viser
  henholdsvis navnet på humørikonet, typen af humørikon (standard eller
  emoji), og til sidst det pågældende tegn for humørikonet.

Når du trykker på OK, vil det valge humørikon blive indsat i
udklipsholderen, klar til at indsætte.

## Humørikonordbog ##

Tilføjelsespakken til humørikoner lader dig tildele forskellige
udtaleordbøger ved brug af indstillingsprofiler.

Dette betyder, at du kan oprette eller redigere en bestemt udtaleordbog for
en særlig indstillingsprofil.

Fra NVDA-menuen>Præferencer>Udtaleordbøger>Emoticons kan du åbne en indstillingsdialog, hvor du kan tilføje eller rette eksisterende humørikoner.

Ved at gemme dine tilpasninger, vil dine nye læseindstillinger kun blive
anvendt på den indstillingsprofil, som du er i færd med at redigere.

F.eks. ønsker du måske, at NVDA kun udtaler tilpassede humørikoner i
XXChat-programmet, men ikke i andre chatprogrammer: Du kan gøre dette ved at
oprette en indstillingsprofil for applikationen XXChat, og derefter tildele
en udtaleordbog til profilen fra menuen "udtaleordbøger" og ved at vælge
Emoticons. Se herunder for Emoticons-indstillinger i henhold til
indstillingsprofiler.

Du kan også eksportere dine tilpassede udtaleordbøger ved at trykke på "Gem
og eksporter ordbog". Dine ordbøger vil blive gemt i din mappe med din egen
brugerkonfiguration (user config) for NVDA i undermappen
speechDicts/emoticons.

Det nøjagtige navn og placering af ordbogsfilen baseres på den redigerede
indstillingsprofil, og vil blive vist i titlen på dialogen for Emoticons.

## Indstillinger for Emoticons ##

Fra menuen Præferencer>Indstillinger>Emoticons åbnes et panel, hvor du konfigurerer aktivering af dine udtaleordbøger til hver profil.

I indstillingspanelet for Emoticons kan du vælge, om NVDA automatisk skal aktivere udtaleordbøger, når du skifter til den profil du er i færd med at redigere. Som standard er dette slået fra i den normale konfiguration af NVDA og alle dine nyoprettede indstillingsprofiler.

Desuden er det muligt at afgøre, om emojis der genkendes af tilføjelsen skal
oplyses. Dette kan være nyttigt at bevare symboler, hvis emojis er
inkluderet i NVDAs konfiguration.

Hvis du ønsker at holde konfigurationsmapperne rene, vil det også være
muligt i denne dialog at vælge om ubrugte ordbøger (tilhørende
ikke-eksisterende profiler) skal fjernes fra tilføjelsen når den udlæses.

## Tastaturkommandoer: ##

Disse er de vigtigste kommandoer tilgængelige som standard, du kan redigere
dem eller tilføje nye tastetryk for at åbne indstillingspanelet for
Emoticons eller dialogen til styrelse af Emoticons-ordbøger.

* NVDA+e: Skifter mellem at udtale tekst, som den er skrevet, eller med
  humørikonerne erstattet med den brugervenlige beskrivelse.
* NVDA+i: Viser en dialog, hvor du kan vælge et humørikon, du vil kopiere.
* Ikke tildelt: Åbn et vindue, der viser symbolet, hvor læsemarkøren er
  placeret, så hele beskrivelsen kan gennemgås i gennemsynstilstand.
* Ikke tildelt: Åbn et vindue, der viser symbolet, hvor systemmarkøren er
  placeret, så hele beskrivelsen kan gennemgås i gennemsynstilstand.

Bemærk: I Windows 10 er det også muligt at bruge det indbyggede emoji-panel.


## Ændringer for 10.0 ##

* Tilføjede kommandoer for at vise symbolet, hvor system- eller læsemarkøren
  er placeret. Kommandoer for disse kan tildeles fra dialogboksen
  Inputbevægelser, kategorien Tekstlæsning.

## Ændringer for 9.0 ##

* Tilføjet muligheden for at vælge, om emojis genkendt af tilføjelsen skal
  oplyses.
* Brugt passende kodning for ordbognavne, retttede  fejl, når de indeholder
  bestemte tegn.
* Den oversatte beskrivelse af tilføjelsen bruges korrekt til titlen, der
  præsenteres i tilføjelseshjælp, tilgængelig fra styringen af
  tilføjelsespakker.
* Tilføjet en bemærkning der nævner emoji-panelet tilgængeligt i Windows 10.

## ændringer i 8.0 ##

* Kompatibel med NVDA 2018.3 eller nyere (påkrævet).

## Ændringer i7.0 ##

* Dialogboksen med indstillinger for aktivering er blevet flyttet til et
  panel i NVDAs indstillinger, således den aktuelle profil vil blive vist i
  titlen på indstillingsdialogen.
* Menuen til håndtering af humørikoner er blevet fjernet. Nu kan du finde
  "Indsæt humørikon" under menuen Værktøjer, og "Tilpas humørikoner" vil
  blive vist under "Udtaleordbøger" ligesom humørikoner-ordbøger.
* Kræver NVDA 2018.2 eller nyere.
* Hvis nødvendigt, kan du hente [den sidste version kompatibel med NVDA
  2017.3][3].

## Ændringer i6.0 ##

* Tilføjede understøttelse for indstillingsprofiler.
* I NVDA 2017.4 og nyere, vil konfigurationsindstillinger samt tilppassede
  ordbøger ændre sig, afhængigt af hvilken indstillingsprofil der er
  aktiv. I NVDA 2017.3 kan du anvende ændringer ved at genindlæse plug-ins
  ved brug af NVDA+Ctrl+F3.
* Hvis du vælger at importere indstillinger, når du opdaterer tilføjelse,
  vil forældede filer (emoticons.ini og emoticons.dic) blive fjernet eller
  tilpasset til denne version.

## Ændringer i6.0 ##

* Tilføjet understøttelse af emojis.
* Forbedringer for Indsæt humørikon dialog med et felt til filtrering af
  humørikoner og radioknapper til at vælge viste humørikoner.
* Benytter GuiHelper for dialogen til aktiveringsindstillinger og "Indsæt
  humørikoner". Dette kræver NVDA 2016.4 og nyere versioner.

## Ændringer i4.0 ##

* Hvis du åbner dialogen "Indsæt smiley",mens en anden indstillingsdialog er
  åben, vil NVDA vise en tilsvarende fejlmeddelelse.


## Ændringer i 3.0 ##

* I dialogen til tilpasning af humørikoner er det nu muligt at specificere,
  at et mønster kun skal matche, hvis der er tale om et helt ord i
  overensstemmelse med udtaleordbøgerne i NVDA 2014.4.


## Ændringer i 2.0 ##

* Hjælp til tilføjelsesprogram er til rådighed fra styring af
  tilføjelsesprogrammer.


## Ændringer i 1.1 ##

* Fjernet dobbelt humørikon.
* Tilføjede nogle smileys.

## Ændringer i 1.0 ##

* Første version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o

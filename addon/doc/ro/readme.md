# Emoticons #

* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Compatibilitate NVDA: 2018.3 - 2019.1
* Descarcă [versiunea stabilă][1]
* Descarcă [versiunea în dezvoltare][2]

Folosind acest supliment, textul care conține emoticoane va fi înlocuit cu o
descriere mult mai prietenoasă.

De exemplu: secvența ":)" va fi pronunțată ca „zâmbet” sau, de exemplu, NVDA
va recunoaște semnificația fiecărui moji.

Există următoarele caracteristici:

## Inserează Emoticon ##

Uneori, o imagine face cât 1000 de cuvinte: utilizați noul moji pentru a da
viață mesajului dumneavoastră instant și pentru a permite prietenilor să
știe ceea ce simțiți.

Când sunteți nesigur de caracterele pentru un zâmbet particular, add-on-ul
vă permite să-l selectați și inserați în textul dumneavoastră.

Apăsați NVDA+I, sau din meniul instrumente -> Inserare Emoticon, pentru a deschide un dialog cu emoticoanele oferite sau mojiuri.

Acest dialog vă permite să alegeți un emoticon și să vizualizați
emoticoanele care vă interesează:

*	Un câmp editabil vă permite să filtrați căutarea pentru emoticonul dorit
  dintre emoticoanele disponibile.
*	Printr-un set de butoane rotative, puteți să alegeți să vizualizați doar
  categoria mojiuri (alt+E) sau să vizualizați doar categoria emoticoanelor
  standard (alt+s) sau să vizualizați toate emoticoanele disponibile
  (alt+A).
  *	În lista emoticoanelor (alt+L) sunt afișate pe trei coloane: numele
  emoticonului, tipul acestuia (emoticon standard sau moji), caracterul
  corespunzător.
*	În lista emoticoanelor (alt+L) sunt afișate pe trei coloane numele
  emoticonului, tipul acestuia (standard sau moji) și caracterul
  corespunzător.

Când apăsați OK, caracterele pentru emoticoanele alese vor fi copiate pe
planșetă, pregătite pentru lipire.

## Dicționar de emoticoane ##

Suplimentul Emoticons vă permite să aveți diferite dicționare de vorbire
folosind profiluri de configurare.

Aceasta înseamnă că puteți crea sau edita un dicționar de vorbire specific
pentru fiecare profil personalizat.

Din meniul NVDA, Preferințe -> Dicționare de vorbire -> Dicționar de emoticoane, puteți să deschideți un dialog cu setările unde puteți adăuga sau edita emoticoanle disponibile.

Salvându-vă particularizările, noile setări de citire ale emoticoanelor se
vor aplica numai profilului pe care îl editați în prezent.

De exemplu, ați putea dori ca NVDA să pronunțe emoticoane personalizate
numai în programul XxChat, dar nu în alte programe de chat: puteți face
acest lucru creând un profil pentru aplicația XxChat și atribuiți un
dicționar de vorbire din meniul din meniul dicționare de vorbire, opțiunea
„Dicționar de emoticoane. Vedeți mai jos setările de activare în raport cu
profilurile de configurare.

De asemenea, puteți să exportați fiecare dicționar de vorbire apăsând
butonul "Salvează și exportă dicționar": în felul acesta, dicționarele
dumneavoastră de vorbire vor fi salvate în folderul de configurare al
utilizatorului, subfolder-ul speechDicts/emoticons.

Numele exact și locația fișierului de dicționar vor fi bazate pe editarea
profilului de configurare, care va fi afișat în titlul dialogului dicționar
Emoticons.

## Setări Emoticons ##

Din meniul Preferințe -> Setări Emoticoane deschide un dialog pentru a configura activarea dicționarelor de vorbire pentru fiecare profil.

Din panoul de setări al Emoticons, puteți dacă ar trebui sau nu ca dicționarul de vorbire să se activeze automat atunci când NVDA se comută la profilul pe care actualmente îl editați. În mod implicit, este dezactivată în configurația normală a NVDA și în toate profilurile dumneavoastră.

Moreover, it's possible to determine if the add-on emojis should be
spoken. This could be useful to preserve symbols speaking if emojis are
included in NVDA's configuration.

Dacă doriți să păstrați curate folderele de configurare, în această
fereastră de dialog este posibil de asemenea să alegeți dacă dicționarele
care nu sunt utilizate (asociate profilurilor inexistente) vor fi eliminate
din supliment atunci când nu sunt încărcate.

## Comenzi de tastatură: ##

Acestea sunt scurtăturile disponibile în mod implicit, puteți să le editați
sau puteți adăuga o nouă tastă pentru a deschide panoul de setări al
Emoticons sau dialogul dicționarului de emoticoane:

* NVDA + E: activarea/dezactivarea pronunțării emoticoanelor, comută între
  pronunțarea textului așa cum este scris, sau cu emoticoanele înlocuite cu
  descrierea umană.
* NVDA+I: Arată un dialog pentru a selecta emoticonul pe care vreți să îl
  copiați.
* Not assigned: open a browseable message showing the symbol where the
  review cursor is positioned, so that the whole description can be reviewed
  in browse mode.
* Not assigned: open a browseable message showing the symbol where the caret
  is positioned, so that the whole description can be reviewed in browse
  mode.

Notă: În Windows 10, este posibil să folosiți și panoul de emoji.


## Changes for 10.0 ##

* Added commands to show the symbol where the review cursor or caret are
  positioned. Gestures for these commands can be assigned from the Input
  gestures dialog, Text review category.

## Changes for 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they
  contain certain characters.
* The translated summary of the add-on is properly used for the title
  presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Modificări aduse în 8.0 ##

* Compatibil cu NVDA 2018.3 (necesar).

## Modificări aduse în 7.0 ##

* Dialogul de activare al setărilor a fost mutat într-un panou din setările
  NVDA, astfel încât profilul curent va fi afișat în titlul dialogului
  setărilor NVDA.
* Meniul Administrare Emoticoane a fost șters: nicio opțiune de genul
  Inserare Emoticon nu va fi găsită în submeniul Instrumente, iar opțiunea
  de personalizare a emoticoanelor va fi afișată sub dicționarele de
  vorbire, la fel ca dicționarul de emoticoane.
* Necesită NVDA 2018.2 sau mai nou.
* Dacă e musai, puteți să descărcați [ultima versiune compatibilă cu NVDA
  2017.3][3].

## Modificări aduse în 6.0 ##

* S-a adăugat suportul pentru configurarea profilurilor.
* În NVDA 2017.4 sau o versiune ulterioară, setările de configurare și
  dicționarele personalizate se vor schimba automat acordându-se cu
  profilurile selectate. În 2017.3 sau mai recent, puteți aplica modificări
  prin reîncărcarea pluginurilor (apăsând control+ NVDA+f3).
* Dacă alegeți să importați setări atunci când actualizați suplimentul,
  fișierele depreciate (emoticons.ini și emoticons.dic) vor fi eliminate sau
  adaptate la această versiune.

## Modificări aduse în 5.0 ##

* A fost adăugat suportul pentru mojiuri.
* Îmbunătățiri pentru dialogul de inserare al emoticoanelor cu un câmp de
  filtrare și butoane rotative pentru a alege emoticoanele afișate.
* Utilizând ghidul de ajutor pentru dialogul de activare al setărilor și
  dialogul de inserare a emoticoanelor: Necesită NVDA 2016.4 sau mai vechi

## Modificări aduse în 4.0 ##

* Dacă dialogul de inserare al emoticonului este deschis când alt dialog de
  setări este activ, NVDA va afișa un mesaj de eroare.


## Modificări aduse în versiunea 3.0 ##

* În dialogul de personalizare emoticon, este acum posibil să specifici dacă
  un model trebuie să fie asemănător dacă este un cuvânt întreg, în
  acordanță cu dicționarele de vorbire versiunii NVDA 2014.4.


## Modificări aduse în versiunea 2.0 ##

* Ajutorul add-on-ului este disponibil din manager-ul de add-on-uri.


## Modificări aduse în versiunea 1.1 ##

* Au fost șterse emoticoanele duplicate.
* Au mai fost adăugate ceva emoticoane.

## Modificări aduse în versiuna 1.0 ##

* Versiunea Inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o

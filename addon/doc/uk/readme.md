# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Завантажити [стабільну версію][1]
* Завантажити [версію у розробці][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Ви можете скористатися такими можливостями:

## Insert Emoticon ##

Sometimes an image is worth a 1000 words: use the new emoji to liven up your
instant message and to let your friends know how you’re feeling.

When you are unsure of the characters for a particular smiley, this addon
enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Preferences -> Manage emoticons -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

This dialog allows you to choose an emoticon and to view the emoticons that
interest you:

*	An editable field allows you to filter the search for the desired emoticon
  among the emoticons available.
*	Through a set of radio buttons, you can choose to view only emoji category
  (alt+E) or view only standard emoticon category (alt+s) or view all
  emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed on three columns
  respectively: the name of emoticon, the type of emoticon (standard
  emoticon or emoji), the corresponding character.

When you press OK, the characters for the chosen emoticon will be copied to
your clipboard, ready for pasting.

## Налаштувати смайлики ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

Натиснення кнопки "Зберегти і експортувати словник" збереже файл словника з
іменем emoticons.dic у вашу папку користувацької конфігурації, у вкладену
папку speechDicts.

## Налаштування активації ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.

It is also possible to save your choice for this setting.

## Клавіатурні команди ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: speaching emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Changes for 4.0 ##

* If the Insert smiley dialog is opened when another settings dialog is
  active, NVDA will show the corresponding error message.


## Зміни у версії 3.0 ##

* В діалозі налаштувань смайликів тепер можна вказати, що зразок
  відповідатиме смайлику, якщо він - лише ціле слово, згідно з мовленнєвими
  словниками NVDA 2014.4.


## Зміни у версії 2.0 ##

* Довідка додатка доступна в диспетчері додатків.


## Зміни у версії 1.1 ##

* Видалено смайлики, які дублювалися
* Додано деякі смайлики.

## Зміни у версії 1.0 ##

* Перша версія

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

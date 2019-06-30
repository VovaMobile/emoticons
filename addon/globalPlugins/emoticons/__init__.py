# -*- coding: UTF-8 -*-
#Copyright (C) 2013-2019 Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez
# Released under GPL 2

import globalPluginHandler
import globalVars
import config
import os
import shutil
import api
import speechDictHandler
import ui
import characterProcessing
import languageHandler
import speech
import braille
import treeInterceptorHandler
import textInfos
import controlTypes
import core
import wx
import gui
import addonHandler
from gui import guiHelper
from gui.settingsDialogs import NVDASettingsDialog, SettingsPanel, DictionaryDialog
from smileysList import emoticons
from skipTranslation import translate
from globalCommands import SCRCAT_SPEECH, SCRCAT_TOOLS, SCRCAT_CONFIG, SCRCAT_TEXTREVIEW
from scriptHandler import script

addonHandler.initTranslation()

### Constants
ADDON_DICTS_PATH = os.path.join(os.path.dirname(__file__), "emoticons")
EXPORT_DICTS_PATH = os.path.join(speechDictHandler.speechDictsPath, "emoticons")
ADDON_DIC_DEFAULT_FILE = os.path.join(ADDON_DICTS_PATH, "emoticons.dic")
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
try:
	ADDON_PANEL_TITLE = unicode(ADDON_SUMMARY)
except NameError:
	ADDON_PANEL_TITLE = str(ADDON_SUMMARY)

confspec = {
	"announcement": "integer(default=0)",
	"speakAddonEmojis": "boolean(default=False)",
	"cleanDicts": "boolean(default=False)",
}

config.conf.spec["emoticons"] = confspec

defaultDic = speechDictHandler.SpeechDict()
noEmojisDic = speechDictHandler.SpeechDict()
sD = speechDictHandler.SpeechDict()

profileName = oldProfileName = None

def loadDic():
	if profileName is None:
		dicFile = ADDON_DIC_DEFAULT_FILE
	else:
		dicFile = os.path.join(ADDON_DICTS_PATH, "profiles", "%s.dic" % profileName.encode("mbcs"))
	sD.load(dicFile)
	if not os.path.isfile(dicFile):
		if config.conf["emoticons"]["speakAddonEmojis"]:
			sD.extend(defaultDic)
		else:
			sD.extend(noEmojisDic)

def activateAnnouncement():
	speechDictHandler.dictionaries["temp"].extend(sD)

def deactivateAnnouncement():
	for entry in sD:
		if entry in speechDictHandler.dictionaries["temp"]:
			speechDictHandler.dictionaries["temp"].remove(entry)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SPEECH

	def loadDic(self):
		if self.profileName is None:
			self.dicFile = ADDON_DIC_DEFAULT_FILE
		else:
			self.dicFile = os.path.join(ADDON_DICTS_PATH, "profiles", "%s.dic" % self.profileName.encode("mbcs"))
		sD.load(self.dicFile)
		if not os.path.isfile(self.dicFile):
			sD.extend(defaultDic)

	def handleConfigProfileSwitch(self):
		global profileName, oldProfileName
		profileName = config.conf.profiles[-1].name
		if profileName == oldProfileName:
			return
		deactivateAnnouncement()
		loadDic()
		if config.conf["emoticons"]["announcement"]:
			activateAnnouncement()
		oldProfileName = profileName

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		for em in emoticons:
			if em.isEmoji:
				# Translators: A prefix to each emoticon name, added to the temporary speech dictionary, visible in temporary speech dictionary dialog when the addon is active, to explain an entry.
				emType = _("Emoji")
			else:
				# Translators: A prefix to each emoticon name, added to the temporary speech dictionary, visible in temporary speech dictionary dialog when the addon is active, to explain an entry.
				emType = _("Emoticon")
			comment = u"{type}: {name}".format(type=emType, name=em.name)
			otherReplacement = " %s; " % em.name
			# Case and reg are always True
			defaultDic.append(speechDictHandler.SpeechDictEntry(em.pattern, otherReplacement, comment, True, speechDictHandler.ENTRY_TYPE_REGEXP))
			if not em.isEmoji:
				noEmojisDic.append(speechDictHandler.SpeechDictEntry(em.pattern, otherReplacement, comment, True, speechDictHandler.ENTRY_TYPE_REGEXP))
		global profileName, oldProfileName
		profileName = oldProfileName = config.conf.profiles[-1].name
		loadDic()

		# Gui
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.dicMenu = gui.mainFrame.sysTrayIcon.preferencesMenu.GetMenuItems()[1].GetSubMenu()
		self.insertItem = self.toolsMenu.Append(wx.ID_ANY,
			# Translators: the name for a menu item.
			_("&Insert emoticon..."),
			# Translators: the tooltip text for a menu item.
			_("Shows a dialog to insert a smiley"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onInsertEmoticonDialog, self.insertItem)
		self.dicItem = self.dicMenu.Append(wx.ID_ANY,
			# Translators: the name for a menu item.
			_("&Emoticons dictionary..."),
			# Translators: the tooltip text for a menu item.
			_("Shows a dictionary dialog to customize emoticons"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onEmDicDialog, self.dicItem)
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

		# Config
		announcement = config.conf["emoticons"]["announcement"]
		if announcement:
			activateAnnouncement()
		config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)

	def terminate(self):
		try:
			self.toolsMenu.Remove(self.insertItem)
			self.dicMenu.Remove(self.dicItem)
			NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)
		except:
			pass
		deactivateAnnouncement()
		config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
		global profileName, oldProfileName
		profileName = oldProfileName = None
		if config.conf["emoticons"]["cleanDicts"]:
			profileNames = config.conf.listProfiles()
			for (root, dirs, files) in os.walk(os.path.join(ADDON_DICTS_PATH, "profiles")):
				for file in files:
					if os.path.splitext(file)[0] in profileNames:
						continue
					try:
						os.remove(os.path.join(root, file))
					except WindowsError:
						pass

	def onInsertEmoticonDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(InsertEmoticonDialog)

	def onEmDicDialog(self, evt):
		# Adapted from NVDA's core.
		disp = profileName if profileName else translate("(normal configuration)")
		deactivateAnnouncement()
		gui.mainFrame._popupSettingsDialog(EmDicDialog,_("Emoticons dictionary (%s)" % disp), sD)

	def onSettingsPanel(self, evt):
		gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@script(
		# Translators: Message presented in input help mode.
		description=_("Toggles on and off the announcement of emoticons."),
		gesture="kb:NVDA+e"
	)
	def script_toggleSpeakingEmoticons(self, gesture):
		if not globalVars.speechDictionaryProcessing:
			return
		if config.conf["emoticons"]["announcement"]:
			config.conf["emoticons"]["announcement"] = 0
			deactivateAnnouncement()
			# Translators: message presented when the dictionary for emoticons is unloaded.
			ui.message(_("Emoticons off."))
		else:
			config.conf["emoticons"]["announcement"] = 1
			activateAnnouncement()
			# Translators: message presented when the dictionary for emoticons is loaded.
			ui.message(_("Emoticons on."))

	@script(
		# Translators: Message presented in input help mode.
		description=_("Shows a dialog to select a smiley you want to paste."),
		category = SCRCAT_TOOLS,
		gesture="kb:NVDA+i"
	)
	def script_insertEmoticon(self, gesture):
		wx.CallAfter(self.onInsertEmoticonDialog, None)

	@script(
		# Translators: Message presented in input help mode.
		description=_("Shows the Emoticons dictionary dialog."),
		category=SCRCAT_CONFIG
	)
	def script_emDicDialog(self, gesture):
		wx.CallAfter(self.onEmDicDialog, None)

	@script(
		# Translators: Message presented in input help mode.
		description=_("Shows the Emoticons settings."),
		category=SCRCAT_CONFIG
	)
	def script_settings(self, gesture):
		wx.CallAfter(self.onSettingsPanel, None)


	# Borrowed from NVDA's code.
	def _getCurrentLanguageForTextInfo(self, info):
		curLanguage = None
		if config.conf['speech']['autoLanguageSwitching']:
			for field in info.getTextWithFields({}):
				if isinstance(field, textInfos.FieldCommand) and field.command == "formatChange":
					curLanguage = field.field.get('language')
		if curLanguage is None:
			curLanguage = speech.getCurrentLanguage()
		return curLanguage

	@script(
		# Translators: Message presented in input help mode.
		description=_("Shows the symbol positioned where the review cursor is located."),
		category=SCRCAT_TEXTREVIEW
	)
	def script_showReviewCursorSymbol(self, gesture):
		info=api.getReviewPosition().copy()
		info.expand(textInfos.UNIT_CHARACTER)
		curLanguage = self._getCurrentLanguageForTextInfo(info)
		text = info.text
		expandedSymbol = characterProcessing.processSpeechSymbol(curLanguage, text)
		if expandedSymbol == text:
			# Translators: Reported when there is no replacement for the symbol at the position of the review cursor.
			ui.message(_("No symbol replacement"))
			return
		# Translators: Character and its replacement used from the "Review current Symbol" command. Example: "Character: ? Replacement: question"
		message = _("Character: {}\nReplacement: {}").format(text, expandedSymbol)
		languageDescription = languageHandler.getLanguageDescription(curLanguage)
		# Translators: title for expanded symbol dialog. Example: "Expanded symbol (English)"
		title = _("Symbol at the review cursor position ({})").format(languageDescription)
		ui.browseableMessage(message, title)

	@script(
		# Translators: Message presented in input help mode.
		description=_("Shows the symbol positioned where the caret is located."),
		category=SCRCAT_TEXTREVIEW
	)
	def script_showCaretSymbol(self, gesture):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if isinstance(treeInterceptor,treeInterceptorHandler.DocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info= obj.makeTextInfo(textInfos.POSITION_CARET)
		except:
			info = obj.makeTextInfo(textInfos.POSITION_FIRST)
		info.expand(textInfos.UNIT_CHARACTER)
		curLanguage = self._getCurrentLanguageForTextInfo(info)
		text = info.text
		expandedSymbol = characterProcessing.processSpeechSymbol(curLanguage, text)
		if expandedSymbol == text:
			# Translators: Reported when there is no replacement for the symbol at the position of the caret.
			ui.message(_("No symbol replacement"))
			return
		# Translators: Character and its replacement used from the "Review current Symbol" command. Example: "Character: ? Replacement: question"
		message = _("Character: {}\nReplacement: {}").format(text, expandedSymbol)
		languageDescription = languageHandler.getLanguageDescription(curLanguage)
		# Translators: title for expanded symbol dialog. Example: "Expanded symbol (English)"
		title = _("Symbol at the caret position ({})").format(languageDescription)
		ui.browseableMessage(message, title)



class EmoticonFilter(object):
	"""Filter for all emoticons."""

	def filter(self, emoticonsList, pattern):
		"""Filters the input list with the specified pattern."""
		if pattern == "": return emoticonsList
		else: return filter(lambda emoticon: pattern.upper() in emoticon.name.upper(), emoticonsList)

class FilterStandard(EmoticonFilter):
	"""Filter just for standard emoticons."""

	def filter(self, emoticonsList, pattern):
		filtered = super(FilterStandard, self).filter(emoticonsList, pattern)
		return filter(lambda emoticon: not(emoticon.isEmoji), filtered)

class FilterEmoji(EmoticonFilter):
	"""Filter just for emojis."""

	def filter(self, emoticonsList, pattern):
		filtered = super(FilterEmoji, self).filter(emoticonsList, pattern)
		return filter(lambda emoticon: emoticon.isEmoji, filtered)

class InsertEmoticonDialog(wx.Dialog):
	""" A dialog  to insert emoticons from a list. """

	_instance = None
	_filteredEmoticons = None
	_filter = None

	def __new__(cls, *args, **kwargs):
		if InsertEmoticonDialog._instance is None:
			return super(InsertEmoticonDialog, cls).__new__(cls, *args, **kwargs)
		return InsertEmoticonDialog._instance

	def _calculatePosition(self, width, height):
		w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
		h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
		# Centre of the screen
		x = w / 2
		y = h / 2
		# Minus application offset
		x -= (width / 2)
		y -= (height / 2)
		return (x, y)

	def __init__(self, parent):
		if InsertEmoticonDialog._instance is not None:
			return
		InsertEmoticonDialog._instance = self
		WIDTH = 500
		HEIGHT = 600
		pos = self._calculatePosition(WIDTH, HEIGHT)
		# Translators: Title of the dialog.
		super(InsertEmoticonDialog, self).__init__(parent, title= _("Insert emoticon"), pos = pos, size = (WIDTH, HEIGHT))
		self._filteredEmoticons = emoticons
		self._filter = EmoticonFilter()
		self.sizerLayout = guiHelper.BoxSizerHelper(self, wx.VERTICAL)
		# Filter panel.
		# Translators: A text field to filter emoticons.
		self.txtFilter = self.sizerLayout.addLabeledControl(_("&Filter:"), wx.TextCtrl)
		self.Bind(wx.EVT_TEXT, self.onFilterChange, self.txtFilter)
		# Radio buttons to choose the emoticon set.
		self.sizerRadio = guiHelper.BoxSizerHelper(self, wx.HORIZONTAL)
		# Translators: A radio button to choose all types of emoticons.
		self.rdAll = self.sizerRadio.addItem(wx.RadioButton(self, label= _("&All"), style= wx.RB_GROUP))
		self.Bind(wx.EVT_RADIOBUTTON, self.onAllEmoticons, self.rdAll)
		# Translators: A radio button to choose only standard emoticons.
		self.rdStandard = self.sizerRadio.addItem(wx.RadioButton(self, label= _("&Standard")))
		self.Bind(wx.EVT_RADIOBUTTON, self.onStandardEmoticons, self.rdStandard)
		# Translators: A radio button to choose only emojis.
		self.rdEmojis = self.sizerRadio.addItem(wx.RadioButton(self, label= _("Emoj&is")))
		self.Bind(wx.EVT_RADIOBUTTON, self.onEmojis, self.rdEmojis)
		# List of emoticons.
		# Translators: Label for the smileys list.
		self.smileysList = self.sizerLayout.addLabeledControl(_("&List of smilies"), wx.ListCtrl, size= (490, 400), style= wx.LC_REPORT | wx.BORDER_SUNKEN)
		# Translators: Column which specifies the name  of emoticon.
		self.smileysList.InsertColumn(0, _("Name"), width=350)
		# Translators: Column which specifies the type of emoticon (standard or emoji).
		self.smileysList.InsertColumn(1, _("Type"), width=100)
		# Translators: The column which contains the characters of the emoticon.
		self.smileysList.InsertColumn(2, _("Characters"), width=40)
		self.smileysList.Bind(wx.EVT_KEY_DOWN, self.onEnterOnList)
		self._loadEmoticons()
		# Buttons.
		self.sizerButtons = self.CreateButtonSizer(wx.OK | wx.CANCEL)
		btnOk = self.FindWindowById(self.GetAffirmativeId())
		self.Bind(wx.EVT_BUTTON, self.onOk, btnOk)
		# Vertical layout
		self.sizerLayout.addItem(self.sizerRadio.sizer, flag=wx.ALL)
		self.sizerLayout.addDialogDismissButtons(self.sizerButtons)

		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.mainSizer.Add(self.sizerLayout.sizer, border=10, flag=wx.ALL)
		self.SetSizer(self.mainSizer)
		self.mainSizer.Fit(self)
		self.txtFilter.SetFocus()

	def _formatIsEmoji(self, isEmoji):
		"""Converts boolean isEmoji property to text."""
		# Translators: Label for emojis in the list.
		if isEmoji: return _("Emoji")
		# Translators: Label for standard emoticons in the list.
		else: return _("Standard")

	def _loadEmoticons(self):
		"""Reload the emoticons list."""
		self.smileysList.DeleteAllItems()
		for emoticon in self._filteredEmoticons:
			if not emoticon.isEmoji:
				self.smileysList.Append([emoticon.name, self._formatIsEmoji(emoticon.isEmoji), unicode(emoticon.chars)])
			else:
				self.smileysList.Append([emoticon.name, self._formatIsEmoji(emoticon.isEmoji), emoticon.chars.decode("utf-8")])

	def onFilterChange(self, event):
		"""Updates the emoticon list when the filter field changes its content."""
		self._filteredEmoticons = self._filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()

	def onEnterOnList(self, evt):
		"""Same effect as click OK button when pressing enter on smileys list."""
		keycode = evt.GetKeyCode()
		if keycode == wx.WXK_RETURN: self.onOk(evt)
		evt.Skip(True)

	def onOk(self, evt):
		"""Copy to clipboard the focused emoticon on the list."""
		focusedItem = self.smileysList.GetFocusedItem()
		if focusedItem == -1:
			if self.smileysList.GetItemCount() > 0: focusedItem = 0
			else:
				# Translators: Error message when none emoticon is selected or the list is empty, and title of the error dialog.
				gui.messageBox(_("There is not any emoticon selected."), translate("Error"), parent=self, style=wx.OK | wx.ICON_ERROR)
				return
		icon = self._filteredEmoticons[focusedItem]
		if not icon.isEmoji:
			iconToInsert = unicode(icon.chars)
		else:
			iconToInsert = icon.chars.decode("utf-8")
		if api.copyToClip(iconToInsert):
			# Translators: This is the message when smiley has been copied to the clipboard.
			core.callLater(100, ui.message, _("Smiley copied to clipboard, ready for you to paste."))
		else:
			# Translators: Message when the emoticon couldn't be copied.
			core.callLater(100, ui.message, _("Cannot copy smiley."))
		self.Destroy()
		InsertEmoticonDialog._instance = None

	def onAllEmoticons(self, event):
		"""Changes the filter to all emoticons and reload the emoticon list."""
		self._filter = EmoticonFilter()
		self._filteredEmoticons = self._filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()

	def onStandardEmoticons(self, event):
		"""Changes the filter to standard emoticons and reloads the emoticon list."""
		self._filter = FilterStandard()
		self._filteredEmoticons = self._filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()

	def onEmojis(self, event):
		"""Changes the filter to emojis and reloads the emoticon list."""
		self._filter = FilterEmoji()
		self._filteredEmoticons = self._filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()

	def __del__(self):
		InsertEmoticonDialog._instance = None

class EmDicDialog(DictionaryDialog):

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		bHelper = guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)
		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in the Emoticons dictionary dialog.
			label=_("Rese&t")
		).Bind(wx.EVT_BUTTON, self.OnResetClick)
		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in the Emoticons dictionary dialog.
			label=_("Save and e&xport dictionary")
		).Bind(wx.EVT_BUTTON, self.OnExportClick)
		sHelper.addItem(bHelper)
		super(EmDicDialog, self).makeSettings(settingsSizer)

	def OnResetClick(self, evt):
		self.dictList.DeleteAllItems()
		self.tempSpeechDict = []
		self.dic = speechDictHandler.SpeechDict()
		if config.conf["emoticons"]["speakAddonEmojis"]:
			self.dic = defaultDic
		else:
			self.dic = noEmojisDic
		self.tempSpeechDict.extend(self.dic)
		for entry in self.dic:
			self.dictList.Append((entry.comment,entry.pattern,entry.replacement,True,speechDictHandler.ENTRY_TYPE_REGEXP))
		self.dictList.SetFocus()

	def onOk(self,evt):
		super(EmDicDialog, self).onOk(evt)
		announcement = config.conf["emoticons"]["announcement"]
		if announcement:
			activateAnnouncement()

	def onCancel(self,evt):
		super(EmDicDialog, self).onCancel(evt)
		announcement = config.conf["emoticons"]["announcement"]
		if announcement:
			activateAnnouncement()

	def OnExportClick(self, evt):
		self.onOk(None)
		profileName = config.conf.profiles[-1].name
		if profileName is not None:
			savePath = os.path.join(EXPORT_DICTS_PATH, "profiles", "%s.dic" % profileName)
		else:
			savePath = os.path.join(EXPORT_DICTS_PATH, "emoticons.dic")
		sD.save(savePath)

class AddonSettingsPanel(SettingsPanel):

# Translators: this is the title for the Emoticons panel.
	title = ADDON_PANEL_TITLE

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: The label for a setting in Emoticons panel.
		activateLabel = _("&Activate speaking of emoticons:")
		self.activateChoices = (translate("off"), translate("on"))
		self.activateList = sHelper.addLabeledControl(activateLabel, wx.Choice, choices=self.activateChoices)
		self.activateList.Selection = config.conf["emoticons"]["announcement"]
		# Translators: The label for a setting in Emoticons panel.
		self.emojiCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("Speak add-on emojis")))
		self.emojiCheckBox.Value = config.conf["emoticons"]["speakAddonEmojis"]
		# Translators: The label for a setting in Emoticons panel.
		self.removeCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Remove not used dictionaries")))
		self.removeCheckBox.Value = config.conf["emoticons"]["cleanDicts"]

	def onSave(self):
		announcement = config.conf["emoticons"]["announcement"]
		config.conf["emoticons"]["announcement"] = self.activateList.GetSelection()
		speakAddonEmojis = config.conf["emoticons"]["speakAddonEmojis"]
		config.conf["emoticons"]["speakAddonEmojis"] = self.emojiCheckBox.Value
		if config.conf["emoticons"]["speakAddonEmojis"] != speakAddonEmojis:
			deactivateAnnouncement()
			loadDic()
			if config.conf["emoticons"]["announcement"]:
				activateAnnouncement()
		elif config.conf["emoticons"]["announcement"] and not announcement:
			activateAnnouncement()
		elif not config.conf["emoticons"]["announcement"] and announcement:
			deactivateAnnouncement()
		config.conf["emoticons"]["cleanDicts"] = self.removeCheckBox.Value

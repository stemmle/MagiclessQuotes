#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Daryl Tucker / stemmle"

import sublime, sublime_plugin

class RemoveSmartQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.edit = edit
        replacements = [
            [u'[’‘]{1}',u'\''],
            [u'[“”]{1}',u'"'],
            [u'[…]{1}',u'...'],
            [u'[—]{1}',u'---'],
            [u'[–]{1}',u'--'],
        ]
        for replacement in replacements:
            x = self.view.find_all(replacement[0])
            for position in x:
                self.view.replace(edit, position, replacement[1])

class RemoveSmartQuotesWhenSaving(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command('remove_smart_quotes')

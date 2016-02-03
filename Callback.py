import sublime, sublime_plugin

class CallbackFunctionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		semicolon(edit, view)

		view.run_command("insert_snippet", { "contents": "function(err, ${1:d}) {\n\t${0:$SELECTION}\n}" })

class NamedCallbackFunctionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		semicolon(edit, view)

		view.run_command("insert_snippet", { "contents": "function ${1}(err, ${2:d}) {\n\t${0:$SELECTION}\n}" })


def semicolon(edit, view):
	for region in view.sel():
		if view.substr(region.end()) == ')' and view.substr(region.end() + 1) != ';' and view.substr(region.end() + 1) != ',':
			view.insert(edit, region.end() + 1, ';')

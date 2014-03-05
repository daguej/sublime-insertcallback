import sublime, sublime_plugin

class CallbackFunctionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		for region in view.sel():
			if view.substr(region.end()) == ')' and view.substr(region.end() + 1) != ';':
				view.insert(edit, region.end() + 1, ';')

		view.run_command("insert_snippet", { "contents": "function(err, ${1:d}) {\n\t${0:$SELECTION}\n}" })

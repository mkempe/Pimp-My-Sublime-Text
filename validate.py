import sublime, sublime_plugin
import webbrowser

class ValidateCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    url = "x-validator-sac://open?uri=%s" % self.view.file_name()
    # self.view.window().run_command('open_url', {"url": url})
    webbrowser.open(url)
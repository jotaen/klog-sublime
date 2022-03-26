import sublime
import sublime_plugin
import datetime
import re


INDENT_PATTERN = re.compile('^( {2,4}|\t)')
NOT_INDENTED_PATTERN = re.compile('^[^\s]$')


def complete(trigger, value, details):
  return sublime.CompletionItem(
    trigger,
    annotation=value,
    completion=value,
    completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
    kind=(sublime.KIND_ID_AMBIGUOUS, '⏱', 'klog'),
    details=details,
  )


def date_completions():
  DATEFMT = '%Y-%m-%d'
  today = datetime.datetime.now()
  yesterday = today - datetime.timedelta(days=1)
  tomorrow = today + datetime.timedelta(days=1)

  return sublime.CompletionList([
    complete('today', today.strftime(DATEFMT), 'Insert today’s date'),
    complete('yesterday', yesterday.strftime(DATEFMT), 'Insert yesterday’s date'),
    complete('tomorrow', tomorrow.strftime(DATEFMT), 'Insert tomorrow’s date'),
  ])


def time_completions():
  TIMEFMT = '%H:%M'
  now = datetime.datetime.now()
  return sublime.CompletionList([
    complete('now', now.strftime(TIMEFMT), 'Insert current time'),
    complete('start', now.strftime(TIMEFMT) + ' - ?', 'Insert open range'),
  ])


class KlogEventListener(sublime_plugin.EventListener):
  def on_query_completions(self, view, prefix, locations):
    if not view.match_selector(locations[0], 'source.klog'):
      return

    cursor = view.line(view.sel()[0])
    preceding_text = view.substr(cursor)

    # If the cursor is not indented
    if NOT_INDENTED_PATTERN.match(preceding_text):
      return date_completions()

    # If the cursor is on an indented line, offer times.
    if INDENT_PATTERN.match(preceding_text):
      return time_completions()

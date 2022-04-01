# klog for Sublime Text

This package provides support for working with [klog time tracking](https://klog.jotaen.net) files in the Sublime Text editor.

![A klog file with sample data](resources/example.png)

## Features

- Syntax highlighting
- Smart completion for inserting the current date or time. For example:
	+ Typing `today` completes to the current date
	+ Typing `now` completes to the current time
- A few sensible default settings for the `.klg` file format

## Configuration

### Colour overrides

The pre-defined syntax highlighting should look meaningful in most available colour schemes.

For klog-specific customisations, you can specify the following colour overrides:

- `markup.other.date.klog` For the date, e.g. `2022-03-15`
- `markup.other.should_total.klog` For the should total, e.g. `(8h!)`
- `markup.other.summary.klog` For summary text
- `markup.other.summary.tag.klog` For tags inside summaries, e.g. `#work`
- `markup.other.duration_positive.klog` For positive durations, e.g. `5h25m`
- `markup.other.duration_negative.klog` For negative durations, e.g. `-15m`
- `markup.other.range.klog` For ranges, e.g. `8:00 - 9:20`
- `markup.other.open_range.klog` For open ranges, e.g. `14:30 - ?`

You can achieve this by adding entries ([see Sublime docs](https://www.sublimetext.com/docs/color_schemes.html)) to the `rules` list of your scheme’s customisation file:

```
"rules": [
	{"scope": "markup.other.range.klog", "foreground": "#76c7ff"},
]
```

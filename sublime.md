# Sublime



## Install sublime

Linux: apt-get



## Install packages

Do once: https://packagecontrol.io/installation

find packages: https://packagecontrol.io/browse

install a package:

- https://packagecontrol.io/docs/usage
- To open the palette, press `ctrl+shift+p` (Win, Linux) or `cmd+shift+p` (OS X).



## Spell check

### Activate and deactivate spell check

Press `F6` to enable spell check

### Enable spell check by default on a specific file type

- Open a file of the specific type.
- Go to `Preferences > Settings - More > Syntax specific - user`.

In the config file that opens, add:

```json
{
    "spell_check": true
}
```

### Add dictionary

#### French dictionary, using Sublime Package Control

https://packagecontrol.io/packages/Language%20-%20French%20-%20Fran%C3%A7ais

#### Other dictionaries, manual installation

Follow the instructions here:
https://github.com/titoBouzout/Dictionaries#installation

You can pick a subset of languages.

### Change dictionary

View -> Dictionary -> English (UK)



## Default type for newly opened files

https://packagecontrol.io/packages/Default%20File%20Type



## Markdown

### Editing

https://packagecontrol.io/packages/MarkdownEditing

### Convert to html

https://packagecontrol.io/packages/Markdown%20Preview

Once installed, `Ctrl + Shift + p` then select "Markdown Preview: view in browser".



## Json

https://packagecontrol.io/packages/Pretty%20JSON

- prettify (configurable) `ctrl+alt+j`
- validate
- minify / compact `Ctrl+Alt+M`
- query with [jq](https://stedolan.github.io/jq/) `ctrl+atl+shift+j`



## Sidebar configuration

http://stackoverflow.com/questions/18288870/sublime-text-3-how-to-change-the-font-size-of-the-file-sidebar#25694790
https://gist.github.com/anonymous/89867e9cb63f7e811a39

For example:

```json
[
    {
        "class": "sidebar_tree",
        "indent": 26,
    },
    {
        "class": "sidebar_label",
        "font.size": 12
    },
]
```

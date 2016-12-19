# Sublime



## Install sublime

Linux: apt-get
Mac: I don't remember, `brew install` maybe?



## Install packages

Do once: https://packagecontrol.io/installation

find packages: https://packagecontrol.io/browse

install a package:
https://packagecontrol.io/docs/usage
To open the palette, press `ctrl+shift+p` (Win, Linux) or `cmd+shift+p` (OS X).



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
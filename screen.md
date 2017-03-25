# screen

Note: to run a program persistently, you can use the `nohup` command.


## session

List running sessions:

```bash
screen -ls                # for the current user only
ls -laR /var/run/screen/  # for all users
screen -RRx $username/    # ?
```

Create a new session:

```bash
screen -S sessionname
```

Resume a session that you started in a different location:

```bash
screen -d -R sessionname
```

`-d` option will “detach” it at the other location, and `-R` will reattach your current terminal window to the session.
If `sessionname` hasn't been created, it will create the session for you.

Detach from the session

    Ctl-a d

Delete a detached session

```bash
screen -S sessionname -X quit
```

From the manual:

- `-d -r`   Reattach a session and if necessary detach it first.

- `-d -R`   Reattach a session and if necessary detach or even create it first.

- `-d -RR`  Reattach a session and if necessary detach or create it. Use the first session if more than one session is available.

- `-D -r`   Reattach a session. If necessary detach and logout remotely first.

- `-D -R`   Attach here and now. In detail this means: If a session is running, then reattach. If necessary detach and logout remotely first.  If it was not running create it and notify the user. This is the author's favorite.


## shells (aka window)

create a new interactive shell 

    Ctl-a c 
    Ctl-a Ctl-c

switch between shells

    C-a n  # next
    C-a p  # previous
    C-a C-a  # change to last-visited active window
    Control-a 1 
    Control-a 2
    Control-a 3 
    ...

Kill the window
    
    Ctl-a k

Rename current window

    Ctl-a A

Get a menu listing all of the window

    Ctl-a "

enter copy mode (also used for viewing scrollback buffer)

    C-a [ or C-a <esc>

exit copy mode

    <esc>

paste

    C-a ] 

lock (password protect) display

    C-a x    


## set up default shell

If you want to make it the default shell for screen sessions only, you can simply add this line to your `~/.screenrc` file.
`shell "/usr/bin/zsh"`


## How can I tell if I am on a screen?

In a screen:

```bash
$ echo $STY
66979.test
$ echo $TERM
screen
```

Not in a screen:

```bash
$ echo $STY
$ echo $TERM
xterm-256color
```

# console3.0

command line application that makes you interact with your windows pc

[Download][1]

[1]:https://github.com/kekkpel/console3.0   "Download"

<a href="https://github.com/kekkpel/console3.0 " target="_blank">Download</a>
## Commands

command | description | usage
:--- | ---: | ---:
__cat__ | view all the file from the shell | cat {file_name}
__cd__ | changes directory | cd {path}
__clear__ | clear the screen | clear
__crdir__ | create a dir | crdir {dir_name}
__crf__ | create a file | crf {file_name}
__del__ | delete a file | del {file_name}
__deldir__ | delete a dir | deldir {dir_name}
__exit__ | exit the program | exit
__help__ | shows the help message | help   or   help {command_name}
__open__ | open a custom app or a windows one | open {app_name}
__python__ | it opens the interactive shell or it will run a program | python   or python {file_name.py}
__fhvir__ | it opens the menu to select some viruses made by me | fhvir
__ssh__ | connect to a device using ssh | ssh {user@ip}

## Warnings
must have these python packages installed

* list of packages
  * pyautogui (see below how to install it)
  * os (preinstalled in python)
  * subprocess (preinstalled in python)
  * system (preinstalled in python)

### How to install pyautogui
make sure that pip works correctly, then open cmd and type

```bash
pip install pyautogui
```

## New commands
-ssh now added

-python now you can run python programs on this console and open the interactive python shell

## News
I've added a collection of viruses made by me (now there is only a simple rickroll)

fixed some issues related to the custom apps

## Contacts
If you have some suggestions write me
[my email](mailto:kekkopdev@gmail.com)

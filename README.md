# AirBnB Clone project


## Installation
 
You will need to clone into the repository from github
```
https://github.com/Isabel-Kikuvi/AirBnB_clone.git
```
After sucessfully cloning into the repo, you will have a directory `AirBnB_clone`
The directory contains several files which allow the program to work

## How to use it
The console has 2 modes:
>> **interactive** and **Non-interactive**

* Interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

* Non-interactive
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


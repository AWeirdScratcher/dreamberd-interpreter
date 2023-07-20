# dreamberd-interpreter
Now the DreamBerd foundation does not own this project.

Big shoutout to [@sus2790](https://github.com/sus2790) for helping me out with this project! Really appreciate it! :heart:

# Installation
To install, you'll need to install the DreamBerd Installer Installer. [Learn how to](https://github.com/git-guides/install-git)

Then, install the DreamBerd installer & run it:
```haskell
$ git clone https://github.com/AWeirdScratcher/dreamberd-interpreter
-- Cloning into 'dreamberd-interpreter'...
-- remote: Enumerating objects: 61, done.
-- remote: Counting objects: 100% (61/61), done.
-- remote: Compressing objects: 100% (57/57), done.
-- remote: Total 61 (delta 24), reused 0 (delta 0), pack-reused 0
-- Receiving objects: 100% (61/61), 17.98 KiB | 2.25 MiB/s, done.
-- Resolving deltas: 100% (24/24), done.

$ cd dreamberd-interpreter
$ python installer.py
```

Then you're done installing!

# Running
To run in your command line:
```haskell
$ python3 -m dreamberd your_file.db
```

or, inline code:
```haskell
$ python3 -m dreamberd 'print("I love dreamberd")!'
```

# Speed
It's slow. Perfectly slow. However, using `rure`, it's *a bit* faster. I'm not good at writing interpreters, please forgive me.

> Tested with most of the examples

![speed test](https://github.com/AWeirdScratcher/dreamberd-interpreter/assets/90096971/450ad902-0960-40da-8a98-fa9c1119a7b4)


# Current Features
These are the current supported features!

## Basic Print
```java
print("DreamBerd!")!
```

### MAKE IT BOLD!1!
```java
print("DreamBerd")!!!
```
![BOLD](https://github.com/AWeirdScratcher/dreamberd-interpreter/assets/90096971/026bfc3f-7248-4d14-89ee-b74010c7a79b)

## Booleans
```java
const const dreamberd = ;;true!
print("Dreamberd is the best programming language: ${dreamberd}")!
```

## Error Handling & AI
> AI: Auto-Insertion
```java
print("this is fine.")
print("This is also fine."
error here!
```

![These are fine!](https://github.com/AWeirdScratcher/dreamberd-interpreter/assets/90096971/05439820-bf7b-4eea-86f3-a64309803622)

## Debug Information
```java
const const luke = "amazing"!
print("How is luke")?
```

![Debug Info](https://github.com/AWeirdScratcher/dreamberd-interpreter/assets/90096971/90017b61-2626-40f4-bd18-9665a6da8fcc)

## String Interpolation
As stated in the DreamBerd README, this interpreter also detects your local currency symbol and uses it for string interpolation. To check the symbol, simply write:
```java
?
```
This is similar to `print()?`, yet more efficient.

![String Interpolation Debug Information](https://github.com/AWeirdScratcher/dreamberd-interpreter/assets/90096971/8168dd36-bf08-4567-b52a-fd006af44f6b)


## File Structure & Exporting
> Thanks to recent advances in technology, you can now give files names.
```java
===== main.db =====
const const luke = "still amazing"!
export luke to "second.db"!

===== second.db =====
print("Luke is ${luke}")!
```

![Exporting and File Structure](https://github.com/AWeirdScratcher/dreamberd-interpreter/assets/90096971/29eeed9f-3607-4dae-bb24-ac39c7883a52)

## Reverse
Make sure to put the keyword on the LAST line.
```java
print("am i happy? ${happy}")!
const const happy = ;;true!
reverse!
```
![Result after Reversing](https://github.com/AWeirdScratcher/dreamberd-interpreter/assets/90096971/984bee0c-87ff-4adb-93dd-133599a0d95e)


# Unsupported Features
- `var var`
- ~~`const const const`~~ (not going to)
- equality, statements... (`==` `!=` `>` `<` `<=` `>=`)
- emoji naming
- arrays
- when
- lifetimes (priority)
- arithmetic
- functions
- dividing by 0
- useless types
- Regular Expressions
- Previous
- Classes / ClassNames (may not be following the docs)
- Time (may not be following the docs)
- Delete
- Overloading (may be the last to finish)
- DBX (may be the last to finish)
- Async Functions (need help)
- Signals (doing when arrays are finished)
- AI (INCOMPLETE)
- Copilot (if we managed to make the prompts)

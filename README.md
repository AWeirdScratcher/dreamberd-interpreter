# dreamberd-interpreter
Now the DreamBerd foundation does not own this project.

# Running
This repo is still in BETA, which you cannot access yet. However, you can learn how you can run it when it's released :/
```haskell
$ python3 -m dreamberd your_file.db
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


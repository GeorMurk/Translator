#!/usr/bin/python

#!Basic Translator

def translate(word):
    translation = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "K"
            else:
                translation = translation + "k"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a Word: ")))

#! notice on "If" condition that l had to type out both the upper and the lower case letters together l can re-code that with
#! If letter.lower() in "aeiou" and its going to do the exact same thing.


#!Go ahead and test it out!!!

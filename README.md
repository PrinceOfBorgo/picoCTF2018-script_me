# picoCTF2018 - script me
## Text
> Can you understand the language and answer the questions to retrieve the flag? Connect to the service with `nc 2018shell.picoctf.com 8672`

Server and port may be different.

## Hints
> Maybe try writing a python script?

## Problem description
After connecting to server running `nc 2018shell.picoctf.com 8672` command (or whatever picoCTF tells you to use) in terminal we get:
```
Rules:
() + () = ()()                                      => [combine]
((())) + () = ((())())                              => [absorb-right]
() + ((())) = (()(()))                              => [absorb-left]
(())(()) + () = (())(()())                          => [combined-absorb-right]
() + (())(()) = (()())(())                          => [combined-absorb-left]
(())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
() + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]

Example: 
(()) + () = () + (()) = (()())

Let's start with a warmup.
()()() + (()()()) = ???
```
We must insert the simplified form of the expressions provided by the system following the rules.

Rules can be summarized as follows:
- Expressions are composed of binary operators `+` and operands given by balanced sequences of round brackets, eventually concatenated;
- We can assign to each operand the maximum depth of its nested brackets (e.g. `()()` -> 1, `(()())` -> 2, `((())())()` -> 3);
- We proceed solving from left to right;
- If the two considered operands have the same depth, then we join them by concatenation (e.g. `(()()) + (())() = (()())(())()`);
- If the two considered operands have different depths, then the one with lesser depth enters the most external level of the other (left or right, according to its position) (e.g. `((())) + () = ((())())`, `() + ((())) = (()(()))`).

## The solution
The solution I used is a python script that asks for server and port to which to connect. Once connected, the script will solve the expressions provided by the server until it gets to the required flag printing it to screen.
```
$ python scriptme.py
Host: 2018shell.picoctf.com
Port: 8672
>> Opening connection to 2018shell.picoctf.com on port 8672
>> Client connected successfully to 2018shell.picoctf.com on port 8672

Congratulations, here's your flag: picoCTF{5cr1pt1nG_l1k3_4_pRo_0970eb2d}

>> Closed connection to 2018shell.picoctf.com on port 8672
```

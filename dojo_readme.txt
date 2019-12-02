*******************
Borsodvenyige is a small town, and one day the world-famous band "Caravaggio és a lelkes fegyenc" goes to give a concert on the stage of town's community centre.
The entrance fee is 500 HUF to everybody. The community centre has only one ticket window, and in the beginning, there is no change in it. Everybody buy only one ticket for himself and pays with a 500 HUF or a 1000 HUF banknote. Luckily exactly the same number of person want to pay with 1000 note and 500. So there is a chance that the cashier can give a change to those who are paying with 1000 if they are coming in the right order.
*******************

#1 - story points: 1
Write a function which can decide if the queue is fit for the conditions below:
    o Has the same number 500 & 1000 notes in it.
    o Everybody can have change if he/she pays with a 1000 note.
return True if yes, and False other way

def is_queue_correct(queue):
@ param {list} queue: list of 0s & 1s - 0 represents those who are paying with 500 (no change), and 1 means those who need change
@ returns: {bool}

#2 - story points: 2
Generate a possible and valid queue if the number of 500 notes are given. (Please don't hard code on a solution, e.g. 2 -> 0011 )

def generate_queue(n):
@ param {number} n: number of 500 banknotes
@ returns: {list} or {None}: None if n is negative or not a whole number

*******************
Jack Sparrow - khmm...
Captain Jack Sparrow decides that he needs a legal income besides the other ones. So he is planning to write "The One and Only Catalogue of Vulcanic Islands on the Caribean Sea" Vulcanic Islands are all hilly, and they don't have plateau on the hills. But obviously they start from sealevel and end there also. So they can look like these ones:

/\ - 1 unit wide

or

 /\
/  \  - 2 units wide

or

 /\
/  \/\  - 3 units wide

*******************

#3 - story points: 5
Write a function which can draw the shape of a given island.

def draw_island(island):
@param {list} island: list of / and \ from left to right, e.g. the third island is [/,/,\,\,/,\]

#4 - story points: 8
Write a function which can tell all the possible shapes to an n unit wide island (be aware, that the 1 unit wide island has two signs, up and down). If n is 0 return 1. (Just because)

def number_of_islands(n):
@ param {number} n width of islands.
@ returns: {number}: number of all possible different shape

#extra question
What is the connection between Borsodvenyige's queue and Jack Sparrow's islands?
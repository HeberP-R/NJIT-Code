>>> # Heber Portal Reyes
# CS 100  2315A 
# HW 01, September 6, 2021
>>> cars = 3
>>> bikes = 5
>>> days = 2
>>> #Float value
>>> money = 69.87
>>> size = 23.2
>>> volume = 300.99
>>> #String variable
>>> speaks_n = 'No problem'
>>> speaks_m = 'My problem'
>>> speaks_y = 'Your problem'
>>> # 1.1
>>> print
<built-in function print>
>>> print "Hey bro
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hey bro)?
>>> print (+3)
3
>>> print (2++2)
4
>>> print (09)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> print (011)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> print (2 2)
SyntaxError: invalid syntax
>>> #1.2
>>> print (42*60+42)
2562
>>> print (10/1.61)
6.211180124223602
>>> print (6.211/2562)
0.0024242779078844654
>>> print (2562/6.211)
412.4939623249074
>>> print (412.49-6*60)
52.49000000000001
>>> #You get 6 minutes: 52 seconds per mile in minutes and sec
>>> print (42 / 60.0 + 42 / 3600.0)
0.7116666666666667
>>> print (10 / 1.61)
6.211180124223602
>>> print (6.211/0.711)
8.735583684950774
>>> #You get 8 miles per hour
>>> #2.1
>>> 42 = n
SyntaxError: cannot assign to literal
>>> x = y = 1
>>> x
1
>>> y
1
>>> print ("yes");
yes
>>> print ("yes").
SyntaxError: invalid syntax
>>> print (xy)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print (xy)
NameError: name 'xy' is not defined
>>> #2.2
>>> import math
>>> math.pi
3.141592653589793
>>> print (4/3*(math.pi*(5**3)))
523.5987755982987
>>> #Sphere has radious of 523.59
>>> coverPrice = 24.95
>>> disc = .4
>>> costfirst = 3
>>> shipping = .75
>>> copies = 60
>>> totaldisc = (coverPrice * disc * copies)
>>> print totaldisc
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(totaldisc)?
>>> print (totaldisc)
598.8000000000001
>>> totaldisc = (coverPrice * disc)
>>> totaldisc = (coverPrice * disc) - coverPrice))
SyntaxError: unmatched ')'
>>> totaldisc = (coverPrice * disc) - coverPrice)
SyntaxError: unmatched ')'
>>> totaldisc = (coverPrice * disc) - coverPrice
>>> print totaldisc
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(totaldisc)?
>>> print (totaldisc)
-14.969999999999999
>>> totaldisc = coverPrice - (coverPrice * disc)
>>> print (totaldisc)
14.969999999999999
>>> print (costfirst + 59 * .75)
47.25
>>> print (coverPrice * copies * disc)
598.8000000000001
>>> print (totaldisc * copies * disc)
359.28
>>> print (totaldisc * copies + 47.25)
945.4499999999999
>>> #Total sale cost is 945.44
>>> seconds = 1
 hours = seconds / (60*60)
 seconds = seconds - hours*60*60
 minutes = seconds / 60
 seconds = seconds - minutes *60
 
SyntaxError: multiple statements found while compiling a single statement
>>> seconds = 1
>>> hours = seconds / (60*60)
>>> seconds = seconds - hours*60*60
>>> minutes = seconds / 60
>>> seconds = seconds - minutes *60
>>> lefthouse = 6 * hours + 52 * minutes
>>> easy_pace = 2 * (8 * minutes + 15 * seconds)
>>> fast_pace = 3 * (7 * minutes + 12 * seconds)
>>> total = lefthouse + easy_pace + fast_pace
>>> print (total)
0.0016666666666666666
>>> 2 miles = 16.3
SyntaxError: invalid syntax
>>> twomiles = 16.3
>>> threemiles = 21.36
>>> totaltime = (twomiles + threemiles)
>>> print totaltime
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(totaltime)?
>>> print (totaltime)
37.66
>>> # Then i just add the 37 minutes and 66 sec to the 6:52 and you would make it home by 7:30

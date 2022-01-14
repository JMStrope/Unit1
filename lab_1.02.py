'''

Lab 1.02 - Using the Interpreter
Part 1
Using the interpreter, type in the expressions below. Copy and paste the output into the output column. If the
result is unexpected, note that in the third column.
Section 1
    Input                   Output                          Did it do something unexpected?
a   5 + 2 * 2                  9                                           No 
b   2/3                     0.66666                                        
c   2.0 * 1.5                 3.0
d   (2 + 3) * 10              50
e   5.0 // 2                  2.0
f   5.0 % 2                   1.0

Section 2
    Input                   Output                          Did it do something unexpected?
a   a                        error                                      Gave error message 
b   'a'                        'a'                                      gave a string 

Section 3
    Input                   Output                          Did it do something unexpected?
a   'a + b'                  'a+b'                                repeated 
b   'a' + 'b'                'ab'                                 added a and b 

Section 4
    Input                   Output                          Did it do something unexpected?
a   'a' * 'b'                 error                                     can't multiply sequence by non int.
b   'a' * 2                   'aa'                                  multiplied a by 2 

Part 2
Before going to the IDE
1. For each item, predict the data type of the result and enter into the "String/Integer/Float" column.
2. Next, predict the value of the result for each item and enter into it into the "Prediction of Result"
column.

    Expression                  String/Integer/Float        Prediction of Result                Interpreter Result
a   10 * 2                      integer                     20                                  20
b   .5 * 2                      integer                     1.0                                 1.0
c   10/2                        integer                     5                                   5.0
d   10%2                        integer                     0                                   0
e   2 ** 3                      integer                     6                                   8
f   (2+5)*3                     integer                     21                                  21
g   2 + 5 * 3                   integer                     17                                  17
h   'ab' + '12' + '3'           string                      'ab123'                             'ab123'
j   "ab" + "cd"                 string                      "abcd"                              'abcd'
k   'abc' * 2
l   '1'*2 + '2' * 3
m   1 * 2 + '3' * 2
n   'A' ** 2
o   'bc' % 2
p   'bc' / 2

Now go to the IDE
Use the interpreter to evaluate the expressions, write down results in the "Interpreter Result" column.
'''

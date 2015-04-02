# Introduction #

In-order for you to complete this project, you must learn the python programming language.


# Word Bank #

|Algorithm| a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.|
|:--------|:-----------------------------------------------------------------------------------------------------------------------|
|Binary| relating to, composed of, or involving two things.  In Computing, also refers to the signalling system used by computers in '1' and '0'.|
|CLI | Command-Line Interface.  eg. Command Prompt, Terminal. |
|Condition |  |
|Control Structure | A group of statements which determines the order the statements are to be executed. |
|Data | raw figures and signals, which may not convey a mean to a person. |
|Data Type | a particular kind of data item, as defined by the values it can take, the programming language used, or the operations that can be performed on it. |
|Error | a problem in the code that may cause the program not to work properly. |
|Function | a sequence of program instructions that perform a specific task, packaged as a one. |
|GUI | Graphical User Interface.  eg. Windows 7, MacOSX. |
|Integer | a data type, which uses only whole numbers. |
|Interpreter | an interpreter is a computer program that directly executes instructions written in a programming language, without previously compiling them into machine language (ones and zeros). |
|Logic | the way the program is written, in a particular order to achieve a task following the syntax of the programming language. |
|Module | a separate part of a program that has that contains everything necessary to execute only one aspect of the desired functionality. |
|Program | a sequence of instructions, written to perform a specified task with a computer. |
|Software | any set of machine-readable instructions that directs a computer's processor to perform specific operations. |
|Source Code | a text listing of commands to be compiled or assembled into an executable computer program. |
|String | a data type, that contains any number of characters (letters, numbers, etc). |
|Syntax |  The grammar of the programming language.  This must be followed, otherwise your program won't work. |
|Variable | a named space in the RAM that can be used to store numbers and strings. |


# Control Structures (Basic Concepts) #

There are 5 control structures that can be used when programming.  They are:
  * Sequence
  * Binary Selection
  * Multiway Selection
  * Pre-test loop
  * Post-test loop

For this project, you will be using four of the five listed above (you won't be using post-test loops)

## Sequence ##

This involves the code executing in order of the command listed.  Or put another way, every line run once in order.  This is the simplest control structure.

#### Example ####
<pre>
BEGIN<br>
command one<br>
command two<br>
...<br>
command one hundred<br>
END<br>
</pre>


## Binary Selection ##

This involves the code executing in order BUT there is two paths that the program could take.  In programing, "IF" and "ELSE" conditions are used to make the program do different tasks based on the data it is given.  When the "IF" condition is 'True' the program will run that piece of code, otherwise it won't run that piece of code.

#### Example ####
<pre>
BEGIN<br>
foo = 1<br>
IF foo == 1:<br>
do something<br>
ELSE:<br>
do nothing<br>
END<br>
</pre>

In the above example, the variable "foo" is set to equal to 1.  The "IF" condition has been set so that IF "foo" equals "1" it will **do something** (because that is when that condition is TRUE).

_What about the ELSE statement?_
If none of the conditions are 'True' then the "ELSE" (or "else" in Python) code will run.  Otherwise it will be ignored.


_Will the code execute the "do something" command?_
YES!  It will because the condition is true.

#### Example 2 ####
<pre>
BEGIN<br>
foo = 2<br>
IF foo == 1:<br>
do something<br>
ELSE:<br>
do nothing<br>
END<br>
</pre>

This is the same example as above but "foo" is now equal to "2".

_Will the code execute the "do something" command?_
NO!  It will not because the condition is now false.  "foo" does not equal "1", so it will not execute the command.


## Multiway Selection ##

This involves the code executing in order BUT you can have as many paths as you like and that the program can take.

#### Example ####
<pre>
BEGIN<br>
foo = 3<br>
IF variable > 0:<br>
PRINT "number is positive!"<br>
ELIF variable < 0:<br>
PRINT "number is negative!"<br>
ELSE<br>
do nothing<br>
END<br>
</pre>

_ELIF you ask?_
"ELIF" or "elif" in Python is short for "Else If" and is used when you have multiple paths for your program to choose from.  You must always have an "IF" condition before you have a "ELIF" condition.

_What's going on?_
In the above example, there are three paths that the program can take:
  * IF
  * ELIF
  * ELSE
When the "IF" condition is 'True' that will execute.  When the "ELIF" condition is 'True' that will execute.  If neither are 'True' then the "ELSE" statement code will be executed.

_What will execute in the above example?_
The "IF" condition will be executed because "foo" is equal to "3" which is greater than (>) zero.

#### Example 2 ####
<pre>
BEGIN<br>
foo = "Hello"<br>
IF variable > 0:<br>
PRINT "number is positive!"<br>
ELIF variable < 0:<br>
PRINT "number is negative!"<br>
ELSE<br>
do nothing<br>
END<br>
</pre>

_What will execute in the above example?_
The "ELSE" statement will be executed because "foo" is equal to "hello" which is a string which means it cannot be greater than (>) or less than (<) zero.


## Pre-Test loop ##

This is different from the other three control structures because it repeats the code a number of times depending on the condition set. Like Binary Selection, the conditions have to be 'True' for the code beneath the condition to execute.  Once the loop has been entered, the computer will remain in the loop until the condition becomes 'False' (not 'True')

#### Example ####
<pre>
BEGIN<br>
foo = 0<br>
while foo < 10:<br>
PRINT "foo: " + foo<br>
foo = foo + 2<br>
END WHILE LOOP<br>
END<br>
</pre>

_What's going on in this example?_
Since "foo" is equal to zero, which is less than 10, it will enter the loop and run 5 times before it stops because "foo" will become equal to 10 (look at the condition, has to be less than 10) after 5 repeats/loops.  Below would be the output of the program:
<pre>
foo: 0<br>
foo: 2<br>
foo: 4<br>
foo: 6<br>
foo: 8<br>
</pre>

## Control Structures Summary ##
So there are five control structures, four explained above.  The four explained above are:
  * sequence: for running single lines of code on at a time in a set order.
  * Binary Selection: used when you have two conditions for you code to execute based on the data you give it.
  * Multiway Selection: used when you have more than two conditions that you would like to satisfy.
  * Pre-Test loop: used when you have to repeat a set of code many times without having to rewrite it each time.


# Python Syntax #

If you understand the above concepts, you are ready to move onto learning Python Syntax.  Follow <a href='http://en.wikipedia.org/wiki/Python_syntax_and_semantics'>this link to find out information on the Python Syntax.</a>  Another summary of the Python Syntax can be found <a href='http://www.tutorialspoint.com/python/python_basic_syntax.htm'>here.</a>

Read these pages to get an overview of the Python Syntax and a basic idea of how to program.  Teaching you everything about programming is beyond this tutorial.

For further reading go to the Python Official Documentation pages accessible here: http://docs.python.org/release/2.7.3/















Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages
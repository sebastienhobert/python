PARAMETERS / ARGUMENTS

The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the value that is sent to the function when it is called.

---------------------------------------------------------------------------------------------------------------------------------

SELF

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

self allows each instance of a class to maintain its own state. Each instance has its own separate copy of instance variables.

By using self, Python provides a way for methods to operate on specific instances of a class, allowing for the creation and manipulation of objects with their own unique data.

---------------------------------------------------------------------------------------------------------------------------------

OOP

When you create an instance of the Person class with p1 = Person("John", 36)

__init__ method is called. In this context:

mysillyobject refers to p1
mysillyobject.name is set to "John"
mysillyobject.age is set to 36

When you call p1.myfunc(), the **myfunc** method is called. In this context:

abc refers to p1
abc.name is "John"

"""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)

p1.myfunc()
"""

---------------------------------------------------------------------------------------------------------------------------------

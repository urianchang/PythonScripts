# Messing up Exercise 4.2a

repeat_a()

def repeat_a():
    a()
    a()

def a():
    print "Hello, I am Python"
    print "::Hiss, Hiss::"
    
# Error message:
# Traceback (most recent call last):
#    File "C:\Users\UC\Desktop\Python\Assignments\Week 4\Textbook Exercises\Exercis
#  e4.2b.py", line 3, in <module>
#      repeat_a()
# NameError: name 'repeat_a' is not defined

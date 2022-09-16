try:
    prnt("hi") # try block used to handle exception
except:
    print("except") #if error comes then this block executes
else:
    print("else block") #else block will excute if there is no error
finally:
    print("finally block") # always executes

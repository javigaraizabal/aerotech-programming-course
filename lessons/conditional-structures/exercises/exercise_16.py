n = 2  # Do not modify this line.
if n<0:
    message="The number is negative"
elif n>0:
    message="The number is positive"
elif n==0:
    message="The number is zero"
if n%2==0:
    message=message+" and even"
elif n%2!=0:
    message=message+" and odd"
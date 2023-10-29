def weird_number(a):
    if not isinstance(a,(int,float,str)):
        raise TypeError("all values must be integers, floats or strings.")
    try:
        a=float(a)
    except:
        
#def is_int (x):
 #   if isinstance(x,int) and not isinstance(x,bool):
  #      return True
   # else:
    #    return False

def is_int(x):
    if x%1==0:
        return True
    else:
        return False
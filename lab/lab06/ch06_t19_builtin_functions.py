def distance_from_zero(kousaka:any):
    if type(kousaka)==int or type(kousaka)=="<class'float'>":
        return abs(kousaka)
    else:
        return 'nope'
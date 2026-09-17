def distance_from_zero(kousaka:Any):
    if type(kousaka)==int or type(kousaka)==float:
        return abs(kousaka)
    else:
        return 'nope'
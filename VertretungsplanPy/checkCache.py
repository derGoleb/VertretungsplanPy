
def checkCache(newString, user):
    if user == "s":
        f = open("cacheS","r")
        if f.read() == newString:
            return True
        else:
            return False
    elif user == "g":
        f = open("cache","r")
        if f.read() == newString:
            return True
        else:
            return False
    else:
        raise ValueError("cache file of user could not be found")

def renewCache(newCache, user):
    if user == "s":
        f = open("cacheS","w")
        f.write(newCache)
        f.close()
    elif user == "g":
        f = open("cache","w")
        f.write(newCache)
        f.close()
    else:
        raise ValueError("cache file of user could not be found")
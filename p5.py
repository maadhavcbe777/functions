def most_frequent(string):
    d=dict()
    for a in string:
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    return d
string=str(input("enter a string"))
print(most_frequent(string))
        
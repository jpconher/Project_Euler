# Problem 33

# store digit cancelling fractions
n = []

for i in range(10,100):
    for j in range(i+1,100):
        if len(set(list(str(i)+str(j)))) == 3:
            for a in str(i):
                if a != "0":
                    if a in list(str(j)):
                        try:
                            if i/j == int(str(i).replace(a,""))/int(str(j).replace(a,"")):
                                n.append(str(i)+"/"+str(j))
                        except ZeroDivisionError:
                            break


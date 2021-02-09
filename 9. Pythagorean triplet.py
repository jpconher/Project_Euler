# Problem 9

# it is easy to check that c < a + b otherwise c^2 > a^2 + b^2 with a,b,c natural numbers
# we assume b > a. similarly, it can be shown that c > b - a. Moreover, c can be expressed 
# as c = 1000 - a - b. 

c = 0

for a in range(1,500):                  # a < 500 (otherwise a > b)    
    for b in range(500-a,500):          # 500-a < b < 500 (c>b-a <--> 1000-a-b>b-a <--> 500>b)
        if a**2+b**2 == (1000-a-b)**2:  # c^2=b^2+a^2 <--> (1000-a-b)^2=b^2+a^2 
            c = 1000-a-b
            break
    if c != 0:
        print(a*b*c)
        break

    
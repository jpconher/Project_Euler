# Problem 31

# define function
def find_largest_combination(c,a):
    z = {}
    if a < min(c):
        return "No possible combinations"
    else:
        remainder = a
        c.sort(reverse=True)        
        for i in c:
            if i <= remainder:
                z[i]=int(remainder/i)
                remainder -= z[i]*i
                if remainder == 0:
                    return(z)

# amount of money
a = 200

# coins
c = [200,100,50,20,10,5,2,1]

# number of combinations
n = 1

# possible combinations
p = {}

# obtain first combination
p[n] = find_largest_combination(c, a)

run = True
while run:
    for i in sorted(list(p[n].keys())):
        if (i>1) and p[n][i] > 0:
            if i == max(list(p[n].keys())) and p[n][max(list(p[n].keys()))] == 1:
                p[n+1] = find_largest_combination([num for num in c if num < max(list(p[n].keys()))], a)
            else: 
                p[n+1] = p[n].copy()
                p[n+1][i] -= 1
                if p[n+1][i] == 0:
                    p[n+1].pop(i)
                try:
                    p_new = find_largest_combination([num for num in c if num < i],i+p[n][1])
                    p[n+1].pop(1)
                except KeyError:
                    p_new = find_largest_combination([num for num in c if num < i],i)     
                for j in sorted(list(p_new.keys())):    
                    try:
                        p[n+1][j] += p_new[j]
                    except KeyError:
                        p[n+1][j] = p_new[j]
            n += 1
            break
        elif list(p[n].keys()) == [1]:
            run = False       
            

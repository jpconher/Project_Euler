# Problem 55

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True

lychrel = []
i = 1
while i <= 10**4:
    j = i
    for k in range(0,50):
       j = j+int(str(j)[::-1])
       if is_palindrome(j):
           break
       elif k == 49:
           lychrel.append(i)
    i += 1
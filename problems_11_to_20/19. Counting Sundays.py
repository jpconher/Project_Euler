# Problem 19

# compute the number of sundays that fell on the first of a month on a given year
def sunday_first(first_day, year_type):   
    month_length = [31,0,31,30,31,30,31,31,30,31,30,31]
    number_sundays = 0
    
    if year_type == "normal": 
        month_length[1] = 28
        
    else:
        month_length[1] = 29
        
    for i in month_length:
        
        if first_day == 7:    
            number_sundays += 1

        first_day = first_day + i - 28
        
        if first_day > 7:
            first_day -= 7
            
    return [number_sundays,first_day]

first_day = sunday_first(1,"normal")[1] # first day of 1901
total = 0 # store total number of sundays that fell on the first of a month

for year in range(1901,2001):
    
    if (year % 4 ==0) and (year % 100 != 0 or year % 400 == 0):
        [number_sundays,first_day] = sunday_first(first_day,"leap")
    
    else:
        [number_sundays,first_day] = sunday_first(first_day,"normal")
        
    total += number_sundays
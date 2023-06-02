# Problem 57

# numerator_t = denominator_t-1 * 2 + numerator_t-1
# denominator_t = denominator_t-1 * 2 + demominator_t-2

def numerator_denominator_digits(numerator, denominator):
    return len(str(numerator)) > len(str(denominator))
    
previous_fractions = {'numerators':[3,7],'denominators':[2,5]}

iteration = 3
numerator_more_digits_count = 0
while iteration <= 1000:
    new_numerator = previous_fractions['denominators'][-1]*2 + previous_fractions['numerators'][-1]
    new_denominator = previous_fractions['denominators'][-1]*2 + previous_fractions['denominators'][-2]
    if numerator_denominator_digits(new_numerator,new_denominator):
        numerator_more_digits_count += 1
    previous_fractions['numerators'] = [previous_fractions['numerators'][-1], new_numerator]
    previous_fractions['denominators'] = [previous_fractions['denominators'][-1], new_denominator]
    iteration += 1
    


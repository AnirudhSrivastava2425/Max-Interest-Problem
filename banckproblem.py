'''
Suppose you want to get maximum amount from your deposit. Bank provides you 'I' interest per annum and you have 'P' Principal amount to Bank account. So how much would you get max interest when you withdraw and add money to your account?
Major key factors - 
    1. Bank is closed on saturday and sunday.
    2. Bank cycle starts on 1st January and ends on 31 december.
    3. After withdraw and deposit, Bank takes one day buffer to again start calculating interest.
    4. Once you withdraw money, you have to make withdraw and deposit at repeating cycle.

'''

r = int(input('Enter the amount of interest bank provides : '))
p = int(input('Enter the amount of deposite before 1st of January, i.e. the money in your account before cycle begins : '))
d = int(input('Enter the date of first saturday : '))

# Function to calculate the interest rate
def I(p,r):
    x = (p/100 * r)/365
    return x

# Initialize the sweet time and max profit with 0.
swt = 0
max = 0
max_i=0
j=2
sat = d

# Main logic of the algorithm.
while j<366:
    if(not(j%sat==0)): # Check for saturdays & sundays.
        swt =j
        P = p
        interest = 0
        i=1
        while i<366: # Check for interest whole year.
            interest = interest+I(P,r)
            if(i%swt==0):
                P = P+interest
                interest = 0
                i=i+2
            else:
                i=i+1
        if(max<P+interest):
            max = P+interest
            max_i=j   
        j=j+1
    else:
        # Ignoring sat and sun by incrementing j with 2.
        sat = sat +7
        j=j+2

print("For a cycle of ", max_i," we have ",max)
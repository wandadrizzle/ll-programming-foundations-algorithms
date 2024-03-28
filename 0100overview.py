print("Euclid's Algorithm\n")

'''
The Euclidean algorithm, also known as Euclid's algorithm, is an algorithm for finding the greatest common divisor (GCD) between two numbers.
The GCD is the largest number that divides two numbers without a remainder.

1. Divide the bigger number by the smaller 1
2. Get the remainder- if zero then stop
3. Divide smaller number by remainder
'''

def gcd_wanda(a, b):

    if(a > b):
        t = a
        a = b
        b = t

        """
            r = b % a
            if(r != 0):
                r = a % r #uzoqhubeka kanje kuze kube inini? for dynamic assignment of a value you need a temporary variable!!!!
        #In every iteration my remainder becomes new_denominator and previous_denominator becomes the numerator

        """
    while True:
        r = b % a
        if r == 0:
            return a
        a, b = r, a  # Swap values using tuple unpacking







def gcd(a, b):

    while (b != 0):
        t = a
        a = b
        b = t % b
    return a
    
print(gcd(60, 96))
print(gcd(20, 5))

print(gcd_wanda(60, 96))
print(gcd_wanda(20, 5))
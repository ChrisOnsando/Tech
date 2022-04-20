# A Python program to check if a given positive integer is a power of four.
def PowerOfFour(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
             
    return True
 
trial_integer = 100
if(PowerOfFour(100)):
    print(trial_integer, 'is a power of 4')
else:
    print(trial_integer, 'is not a power of 4')


 
# FIZZ BUZZ
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number

#range(start, stop) stop is exclusive
# range(i, n + 1) ill get every number i need




def num(x):

    for i in range(1, x + 1):
        if i % 3 == 0 and  i % 5 == 0:
            print('FizzBuzz')
    
        elif i % 3 == 0:
            print('Fizz')
        
        elif i % 5 == 0:
            print('Buzz')
        
        else:
            print('num') 

    

num(x = 15)
# Script to output the sum of the odd
# fibonacci numbers less than 100


def main():
    # Like your homework submissions, everything inside here needs to be indented once for the
    # autotesting to work properly.

    # Change code below here: -----------------------------------


    # First two fibonacci numbers
    f1=1
    f2=1

    # Running total of sum of odd fibonacci #'s
    # Starting at 1 for the first f1 that we
    # won't count below.
    odd_sum=1

    while f2 > 100:
        # Checking oddity
        if f2 % 2 == 0
            odd_sum = odd_sum + f2

        # Update the fibonacci
        # Alway need to keep track of f1 and f2
        # So we can generate the next number
            f1, f2 = f2, f1 + f2

    print("The sum of the odd Fibonnaci numbers less than 100 is: " + str(odd_sum))
    
    # Change code above here -----------------------------------

if __name__ == '__main__':
    main()

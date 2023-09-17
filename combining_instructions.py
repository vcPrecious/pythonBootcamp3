def max_three():
    """
    Write a Python function to find the Max of three numbers.
    Use the following as test input in STDIN

    Input:
    ```
    1
    8
    6
    ```
    """

    def max_of_two( x, y ):
        if x > y:
            return x
        return y
    
    def max_of_three( x, y, z ):
        if (x >= y) and (x >= z):
         largest = x
 
        elif (y >= x) and (y >= z):
          largest = y
        else:
         largest = z
         
         return largest
 

    x = int(input())
    y = int(input())
    z = int(input())
    print("The max of the three numbers is: " + str(max_of_three(x, y, z)))


def between_3_and_9(n):
    """
    Write a Python function to check whether a number falls between 3 and 9
    """

    if n in range(3,9):
        #enter code here
        print(n)
    else:
        print("The number is outside the given range.")


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    # max_three()
    # between_3_and_9(n)

#***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program 2
#
#  File Name:         ReneeWhite_Program2
#
#  Description:       This program calculates the average of 5 test scores
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    test1 = int(input('Enter the first test score: '))
    test2 = int(input('Enter the second test score: '))
    test3 = int(input('Enter the third test score: '))
    test4 = int(input('Enter the fourth test score: '))
    test5= int(input('Enter the fifth test score: '))
    average = (test1 + test2 + test3 + test4 + test5) // 5
    print('The average score is', average)
    
    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Program:  2')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1

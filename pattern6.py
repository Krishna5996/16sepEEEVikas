userInput=int(input())
def pattern6(userInput):
        '''
        following is the another approach to solve pattern problems with reduced time complexity 
        for 
        *
        **
        ***
        ****
        *****
        '''

        num = int(input('Enter number for pattern'))
        pattern = '*'
        string = pattern * num
        x = 0

        for i in string:
            x = x + 1
            print(string[0:x])
pattern6(userInput)

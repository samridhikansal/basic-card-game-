from index import userType, computerType

def type(userType,computerType):
    userPoints = 0
    computerPoints =0
    if userType != 1 and userType !=2 and userType !=3 and userType !=4:
        print("Please enter a valid choice")
        exit()
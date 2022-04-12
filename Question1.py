#Given a year, determine whether it is a leap year. If it is a leap year return the boolean true otherwise return false
def CheckLeap(Year):   
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("True") 
  else:  
    print ("False")   
Year = int(input("Enter the Year to check: "))   
CheckLeap(Year)  

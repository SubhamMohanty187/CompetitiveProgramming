def dayOfProgrammer(year):
    # Write your code here
    if(year==1918):
        res = "26.09.1918"
    
    if year <= 1917 and year >= 1700:  # Julian Calender
        if (year%4 == 0):
            res = "12.09."+str(year)    
        else:
            res = "13.09."+str(year)
            
    elif year >= 1919 and year <= 2700: # Gregorian Calender
        if year%400 == 0 or (year%4 == 0 and year%100 != 0):
            res = "12.09."+str(year)    
        else:
            res = "13.09."+str(year)
    return res

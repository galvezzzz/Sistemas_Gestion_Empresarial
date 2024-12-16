def is_year_leap(year):
    if(year % 400 == 0) or (year % 4 == 0 and year %100!=0):
        #print("Año: ",year," ",True)
        return True
    else:
        #print("Año: ",year," ",False)
        return False

def days_in_month(year, month):
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        days = 31
    elif(month == 2):
        if(is_year_leap(year)):
            days = 29        
        else:
            days = 28      
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        days = 30
    return days

def day_of_year(year, month, day):

    dias = 0
    for i in range(1, month):
        dias += days_in_month(year, i)
        
    dias += day
    return dias

print("Días totales desde la fecha introducida:", day_of_year(2000, 12, 31))

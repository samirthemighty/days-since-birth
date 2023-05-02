# without importing anything, trying to find out how many days old someone is
 
current_date = input("Enter the Current date.  ex(12/19/2022):   ")
birth_date = input("Enter your birthdate.   ex(12/19/2003):  ")

def how_many_days_since_birth(current_date,birth_date):
    months = {'1':'31','2':'28','3':'31','4':'30','5':'31','6':'30','7':'31','8':'31','9':'30','10':'31','11':'30','12':'31'}
    counter = 0
    counter1 = 0
    counter2 = 0
    y = current_date.split("/")
    current_month = int(y[0])
    current_day = int(y[1])
    current_year = int(y[2])
    
    x = birth_date.split("/")
    birth_month = int(x[0])
    birth_day = int(x[1])
    birth_year = int(x[2])
    
    for i in months: # find days from birthdate to end of birthyear
        if birth_year%4 == 0:
            months['2'] = 29
        if birth_month == int(i):
            months[i] = int(months[i]) - birth_day
        if birth_month <= int(i):
            counter1 += int(months[i])
            
    for i in months: # find days from start of year to start of this month
        if current_year%4 == 0:
            months['2'] = 29
        if current_month > int(i):
            counter2 += int(months[i])
    counter2 += current_day # add rest of days of current month
    
    while birth_year + 1 < current_year: # find days inbetween birthyear and current date
        if birth_year%4 == 0:
            days = 366
        else:
            days = 365
        counter += days
        birth_year += 1
        
    counter = counter + counter1 + counter2
    return "You are " + str(counter) + " days old !"
print(how_many_days_since_birth(current_date,birth_date))

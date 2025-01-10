startYear=int(input("Enter start year:"))
endYear=int(input("Enter end year:"))
print("Leap years between",startYear,"and",endYear)
for x in range(startYear,endYear+1):
    if(x%4==0 and x%100 != 0) or (x%400==0):
        print(x)
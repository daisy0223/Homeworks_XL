import os
import csv
#Set the path for the file
csvpath = os.path.join('/', 'Users', 'xllz', 'Desktop', 'GTbootcamp', 'Homeworks_XL', '03-python','PyBank','Resources','budget_data.csv')
print(csvpath)
#Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
#Skip the header
    next(csvreader)   
#calculate number of months, the net total amount of Profit/Losses over the entire period
    Total_month=0
    Total=0
    Data=[]
    Date=[]
    for row in csvreader:
        Total_month +=1
        Total +=int(row[1])
        Date.append(row[0])
 # Generate a new list of row change
        if Total_month==1:
            previousvalue=int(row[1])
        else:
            Change=int(row[1])-previousvalue
            Data.append(Change)
            # reset 
            previousvalue=int(row[1])
 # calculate average, maximum and minimum based on the new list of Data
    Average_change=round(sum(Data)/len(Data),2)
    Maximum_change=max(Data)
    Minimum_change=min(Data)
# index the new list and find the row number for the maximum/minimum value
    maximum_row=Data.index(Maximum_change)+1
    minimum_row=Data.index(Minimum_change)+1
# use the index to refer to the date values in the new list of Date
    maximum_date=Date[maximum_row]
    minimum_date=Date[minimum_row]
# Analysis output
    print("Financial Analysis") 
    print("-----------------------------------------") 
    print(f"Total Months: {str(Total_month)}") 
    print(f"Total: ${str(Total)}") 
    print(f"Average Change: ${str(Average_change)}") 
    print(f"Greatest Increase in Profits: {maximum_date} ${str(Maximum_change)}") 
    print(f"Greatest Decrease in Profits: {minimum_date} ${str(Minimum_change)}") 
# write output in a txt file
    Pybank_output_file = os.path.join('/', 'Users', 'xllz', 'Desktop', 'GTbootcamp', 'Homeworks_XL', '03-python','python_challenge','PyBank','Pybank_output.txt')
    f=open(Pybank_output_file, 'w')
    f.write("Financial Analysis\n")
    f.write("-----------------------------------------\n")
    f.write(f"Total Months: {str(Total_month)}\n")
    f.write(f"Total: ${str(Total)}\n")
    f.write(f"Average Change: ${str(Average_change)}\n")
    f.write(f"Greatest Increase in Profits: Feb-2012 ${str(Maximum_change)}\n")
    f.write(f"Greatest Decrease in Profits: Sep-2013 ${str(Minimum_change)}\n")

    




        

        
        
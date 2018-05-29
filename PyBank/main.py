# The total number of months included in the dataset

# The total amount of revenue gained over the entire period

# The average change in revenue between months over the entire period

# The greatest increase in revenue (date and amount) over the entire period

# The greatest decrease in revenue (date and amount) over the entire period

# dependencies

import os
import csv

finan_data = os.path.join("budget_data_1.csv")

date = []
revenue = []
monthcount=0
Totalrev=0
Avgrev=0
revchgarr =[]
previousVal=0
Increv=0
Decrev=0

with open(finan_data, newline ='') as csvfilehandle:
    csvstartreader =csv.reader(csvfilehandle, delimiter =",")
    header = next(csvstartreader)



    for row in csvstartreader:
        
        monthcount = monthcount+1
                
        # current row - previous row
        revchgarr.append(int(row[1]) - previousVal)
        previousVal = int(row[1])
        Totalrev = Totalrev + int(row[1])

        date.append(row[0])
        revenue.append(row[1])

        
      
        # print (col)
        new_text = zip(date, revenue)


# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Date", "Revenue"])

#     # Write in zipped rows
#     writer.writerows(new_text)

sum = 0 
# iterate through values in revchgarr
# for i in range(1, len(revchgarr)):
#     sum += revchgarr[i]
# revChange = sum / (monthcount-1)

revchgarr.pop(0) # removes first val from array
for val in revchgarr:
    sum += val
revChange = sum / (len(revchgarr))

Increv = max(revchgarr)
Decrev = min(revchgarr)

# print in terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {monthcount}")
print(f"$Total Revenue: $ {Totalrev}")
print(f"Average Revenue Change: $ {int(revChange)}")
print(f"Greatest Increase in Revenue: $ ({Increv})")
print(f"Greatest Decrease in Revenue: $ ({Decrev})")

# for row in revchgarr:
#     print(row)
    

with open("new_file",'w+') as FinancialAnalysis:
    

    #         # Print the output to a text file

        FinancialAnalysis.write("Financial Analysis\n")
        FinancialAnalysis.write("-"*30 + "\n")
        FinancialAnalysis.write("Total Months: " + str(monthcount) + "\n")
        FinancialAnalysis.write("Total Revenue: " + str(Totalrev) + "\n")
        FinancialAnalysis.write("Average Revenue Change: " + "$" + str(revChange) + "\n")
        FinancialAnalysis.write("Greatest Increase in Revenue: " + Increv + " (" + "$" + str(Increv) + ")" + "\n")
        FinancialAnalysis.write("Greatest Decrease in Revenue: " + Decrev + " (" + "$" + str(Decrev) + ")" + "\n")














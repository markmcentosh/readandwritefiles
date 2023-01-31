import csv

employeepay = open("employeepay.csv", 'r')
employeebonus = open("employee_bonus", 'w')

csvreader = csv.reader(employeepay, delimiter=(','))

next(csvreader)

employeebonus.write('ID' + 'EmpFName' + 'EmpLName' + 'Salary' + 'Bonus' + '\n')
print()

for row in csvreader:
    employeebonus.write(row[0]+' , '+row[1] +' , ' +row[2] + ' , '+ row[3] + ' , '+row[4] + '\n')

employeepay.close()
employeebonus.close()

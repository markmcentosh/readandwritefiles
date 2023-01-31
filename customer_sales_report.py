import csv

csv_infile = open('sales.csv','r')
csv_outfile = open('salesreport.csv','w')


customer_file = csv.reader(csv_infile, delimiter=(','))

next(customer_file)

csv_outfile.write('CustomerID'+' ' + 'Total' + '\n')

customer_id = 250
value = 0
for x in customer_file:
    if int(x[0]) == customer_id:
        value = (value + float(x[3]) + float(x[4]) + float(x[5]))
    elif int(x[0]) != customer_id:
        decimals = format(value, '.2f')
        csv_outfile.write(' ' + str(customer_id) + ' ' + str(decimals) + '\n')
        customer_id += 1
        value = 0
        value += float(x[3]) + float(x[4]) + float(x[5])
    elif customer_id == 262:
        StopIteration

csv_infile.close()
csv_outfile.close()


    







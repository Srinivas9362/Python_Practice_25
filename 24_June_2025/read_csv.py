import csv

with open('D:\datasets/customer_orders.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

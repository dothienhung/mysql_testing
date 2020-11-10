import csv
import mysql.connector as mysql

"""gọi cơ sở dữ liệu"""
data_customer = mysql.connect(
    host="localhost",
    user="root",
    passwd="hung1995",
    database="customers",
)
with open('customer.csv') as csv_file:
    customer_file = csv.reader(csv_file,delimiter = ',')
    all_value = []
    for row in customer_file:
        value =(row[0] , row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        all_value.append(value)
sql = "Insert into tblcustomers  (customerid,firstname,lastname,companyname,billingaddress1,billingaddress2,city,states,postalcode,country,phonenumber,emailaddress,createddate) Value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

mycursor = data_customer.cursor()
mycursor.executemany(sql,all_value)
data_customer.commit()

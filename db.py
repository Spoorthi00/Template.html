import mysql.connector
try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Spoiry@123",
        database="demo"
        )
        print("Please choose from below options\n")
        print("1-read\n")
        print("2-insert\n")
        print("3-update\n")
        print("4-delete\n")
        choice=int(input())
        if(choice==1):
                mycursor = mydb.cursor()
                mycursor.execute("select * from Customer")
                result = mycursor.fetchall()
                for guest in result:
                        print (guest)
        elif(choice==2):
                name=input("Please enter the name of the Customer\n")
                phone=input("please enter the phone of the Customer\n")
                email=input("please enter the email of the Customer\n")
                Address=input("Please enter the city of the Customer\n")
                sql="INSERT INTO Customer (name, phone, email, address) VALUES (%s, %s, %s, %s)"
                val=(name,phone,email,Address)
                mycursor = mydb.cursor()
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")


except Exception as e:
        print(e)
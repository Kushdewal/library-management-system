#CREATING DATABASE


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="123")
mycursor=mydb.cursor()
#mycursor.execute("create database library3") 
mycursor.execute("use library3")

mycursor.execute("""create table if not exists library_master(cardno char(10) NOT NULL primary key,
name_of_person varchar(30),phone_no char(10),address varchar(30),dob date)""")
mycursor.execute("""create table if not exists books(book_name varchar(30),
book_no char(5) primary key ,genre varchar(10),authors_name varchar(15),language varchar(15))""") 
mycursor.execute("""create table if not exists issue(bookname varchar(50),bookno varchar(10),issuedate date,
returndate date,cardno varchar(20) primary key,studentname varchar(20))""")
mydb.commit()
while True:
    print ("##########################<-LIBRARY MANAGEMENT SYSTEM->#########################")

    print("""                            FOR CREATING NEW ACCOUNT PRESS 1

                            TO SEE ACCOUNT INFO PRESS 2

                            TO UPDATE CARD HOLDER INFO PRESS 3

                            TO DELETE AN ACCOUNT PRESS 4 

                            TO ADD NEW BOOKS PRESS 5

                            TO SEE BOOK DETAILS PRESS 6
 
                            TO UPDATE BOOK INFO PRESS 7

                            TO DELETE ANY BOOK PRESS 8

                            TO LEND THE BOOK PRESS 9

                            FOR LEND HISTORY PRESS 10

                            FOR EXIT press 11                   """)

    
 

    ch=int(input ("Enter your choice:"))
    if ch==1: 

        print("If you wanna go back press 1") 

        print(" ") 

        print("If you wanna continue press 2")

        print(" ") 

        a=int(input("Enter your choice: ")) 

        if a==1:

            continue 

        if  a==2:

            print("FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER") 

            cardno=str(input("Enter card no:")) 

            name_of_person=str(input("Enter name(limit 30 characters):")) 

            phone_no=str(input("Enter phone no:")) 

            address=str(input("Enter the address (max 30 words):"))

            dob=str(input("Enter the date of birth (yyyy—mm—dd):"))

            mycursor.execute("insert into library_master values('"+cardno+"','"+name_of_person+"','"+phone_no+"','"+address+"','"+dob+"')")
            mydb.commit() 

            print("ACCOUNT IS SUCCESSFULLY CREATED!!!")
    if ch==2:
        x=str(input("Enter card no:"))
        c='select * from library_master where cardno=%s' % (x,)
        mycursor.execute(c)
        d=mycursor.fetchone()
        for i in d:
            print(i)
    if ch==3:
        print("Press 1 to update name:")
        print(" ")
        print("Press 2 to update phone no:")
        print(" ")
        print("Press 3 to update address:")
        print(" ")
        print("Press 4 to update date of birth:")
        print(" ")
        ch1=int(input("Enter your choice:"))
        if ch1==1:
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            name_of_person=str(input("Enter new name:"))
            mycursor.execute("update library_master set name_of_person='"+name_of_person+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("**Name has been updated**")
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i) 
        if ch1==2: 

            mycursor.execute("select * from library_master")

            for i in mycursor: 

                print(i) 

            cardno=str(input("Enter card no:")) 

            phone_no=str(input("Enter new phone no:")) 

            mycursor.execute("update library_master set phone_no='"+phone_no+"' where cardno='"+cardno+"'") 

            mydb.commit() 

            print("**Number has been updated**") 

            mycursor.execute("select * from library_master") 

            for i in mycursor: 

                print(i) 

#TO UPDATE ADDRESS

        if ch1==3:

            mycursor.execute("select * from library_master")

            for i in mycursor: 

                print(i) 

            cardno=str(input("Enter card no:")) 

            address=str(input("Enter new address:")) 

            mycursor.execute("update library_master set address='"+address+"' where cardno='"+cardno+"'") 

            mydb.commit() 

            print("**Address has been updated**") 

            mycursor.execute("select * from library_master") 

            for i in mycursor: 

                print(i)
#TO UPDATE DATE OF BIRTH 

        if ch1==4: 

             mycursor.execute("select * from library_master")

             for i in mycursor: 

                print(i) 

             cardno=str(input("Enter card no:")) 

             dob=str(input("Enter new date of birth(yyyy-mm-dd):")) 

             mycursor.execute("update library_master set dob='"+dob+"' where cardno='"+cardno+"'") 

             mydb.commit() 

             print("**Date Of Birth has been updated**") 

             mycursor.execute("select * from library_master") 

             for i in mycursor: 

                print(i)
#TO DELETE AN ACCOUNT 

    if ch==4: 

        mycursor.execute("select * from library_master")

        for i in mycursor: 

            print(i) 

            cardno=str(input("Enter card no:")) 

            mycursor.execute ("delete from library_master where cardno='"+cardno+"'") 

            mydb.commit() 

            print("**Removed succesfully**") 

            mycursor.execute("select * from library_master")  

            for i in mycursor: 

                print(i) 
#TO ADD NEW BOOK 

    if ch==5: 

        print("FILL ALL BOOK DETAILS")

        book_name=str(input("Enter book name:"))
        book_no=str(input("Enter no (limit 5 characters):")) 

        genre=str(input("Enter genre:"))
        authors_name=str(input("Enter the authors name (max 15 words):")) 

        language=str(input("Enter the language of book:")) 

        mycursor.execute("insert into books values('"+book_name+"','"+book_no+"','"+genre+"','"+authors_name+"','"+language+"')") 

        mydb.commit() 

        print("**Book added succesfully**")
        for i in mycursor: 

            print(i)

#TO SEE BOOK DETAILS

    if ch==6: 
        book_no=str(input("Enter Book No:")) 
        mycursor.execute("select *from books where book_no='"+book_no+"'")
        for i in mycursor: 

            print(i) 
 #TO UPDATE BOOK DETAILS 
    if ch==7:
        print("Press 1 to update Book name") 
        print(" ") 
        print("Press 2 to update genre") 
        print(" ")
        print("Press 3 to update Author name") 
        print(" ")
        print("Press 4 to update Language") 
        print(" ") 
        ch1=int(input("Enter your choice:"))
        if ch1==1:
            mycursor.execute("select * from books")
            for i in mycursor:

                print(i)
            book_no=str(input("Enter book no:"))
            name_of_book=str(input("Enter new name:"))
            mycursor.execute("update books set book_name='"+name_of_book+"' where book_no='"+book_no+"'")
            
            mydb.commit()

            print("**Name has been updated**")
            mycursor.execute("select * from books")

            for i in mycursor: 

                print(i) 

#TO UPDATE GENRE 

        if ch1==2:
            mycursor.execute("select * from books")
            for i in mycursor:

                print(i)
            book_no=str(input("Enter book no:"))
            genre=str(input("Enter new genre:"))
            mycursor.execute("update books set genre='"+genre+"' where book_no='"+book_no+"'")
            
            mydb.commit()

            print("**Genre has been updated**")
            mycursor.execute("select * from books")

            for i in mycursor: 

                print(i) 

#TO UPDATE AUTHOR NAME

        if ch1==3:
            mycursor.execute("select * from books")
            for i in mycursor:

                print(i)
            book_no=str(input("Enter book no:"))
            author=str(input("Enter new author name:"))
            mycursor.execute("update books set authors_name='"+author+"' where book_no='"+book_no+"'")
            
            mydb.commit()

            print("**Author name has been updated**")
            mycursor.execute("select * from books")

            for i in mycursor: 

                print(i) 

#TO UPDATE LANGUAGE
        if ch1==4:
            mycursor.execute("select * from books")
            for i in mycursor:

                print(i)
            book_no=str(input("Enter book no:"))
            language=str(input("Enter new language:"))
            mycursor.execute("update books set language='"+language+"' where book_no='"+book_no+"'")
            
            mydb.commit()

            print("**Language has been updated**")
            mycursor.execute("select * from books")

            for i in mycursor: 

                print(i)                         
#To DELETE A BOOK
    if ch==8:
        mycursor.execute("select * from books")
        for i in mycursor:

            print(i)
        book_no=str(input("Enter book no:"))
        mycursor.execute("delete from books where book_no='"+book_no+"'")
        
        mydb.commit()


        print("**Removed Successfully**")
        mycursor.execute("select * from books")

        for i in mycursor: 

            print(i)
#TO LEND THE BOOK
    if ch==9:
        print("FILL BOOK DETAILS")

        bookname=str(input("Enter book name: "))
        bookno=str(input("Enter no (limit 5 characters): ")) 

        issuedate=str(input("Enter issue date in format (yyyy-mm-dd): "))
        returndate=str(input("Enter return date in format (yyyy-mm-dd): ")) 

        cardno=str(input("Enter the card number of stdent: "))
        studentname=str(input("Enter the stdent name: "))

        mycursor.execute("insert into issue values('"+bookname+"','"+bookno+"','"+issuedate+"','"+returndate+"','"+cardno+"','"+studentname+"')") 

        mydb.commit() 

        print("**Record Added Succesfully**")
        
#TO SEE THE LEND HISTORY
    if ch==10:
        print("Press 1 to see all records") 
        print(" ") 
        print("Press 2 to see specific record") 
        print(" ")
        ch1=int(input("Enter your choice:"))
        if ch1==1:
            mycursor.execute("select * from issue ")
            for i in mycursor:
                             print(i)
        if ch1==2:
            x=str(input("Enter card no:"))
            mycursor.execute("select *from issue  where cardno='"+x+"'")
            for i in mycursor:
                print(i)
    if ch==11:
        quit()
            
            
        

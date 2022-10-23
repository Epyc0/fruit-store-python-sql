import mysql.connector
import json
import re
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bestdatabase"
)
mycursor = mydb.cursor(buffered=True)

global balance
balance = 1000





def adminpanel():
    print("Tryck 1 för att lägga till frukt\nTryck 2 för att tabort frukt\nTryck 3 för att redigera uppgifter\nTryck 4 för att gå till vanlig meny")
    picker = int(input())

    if (picker == 1):
        print("Ok, skriv namn")
        namer = input()
        print("Skriv in kg")
        kger = input()
        print("Skriv in pris")
        pricer = input()

        sql = "INSERT INTO main (frukt, kg, pris) VALUES (%s, %s, %s)"
        val = (namer, kger, pricer)
        mycursor.execute(sql, val)

        mydb.commit()
        print("Klart.")
        adminpanel()

    if (picker == 2):
        print("Ok, skriv frukten du vill tabort")
        namer = input()

        sql = "DELETE FROM main WHERE frukt = %s"
        val = (namer,)
        mycursor.execute(sql,val)

        mydb.commit()
        print("Klart.")
        adminpanel()





    if (picker == 3):
        picker = str(input())

        namnändrare = input()
        kgändrare = input()
        prisändrare = input()

        print("Skriv in namnet du vill ändra")
        sql = "UPDATE main SET frukt = %s, kg = %s, pris = %s WHERE frukt = %s"
        
        val = (namnändrare, kgändrare, prisändrare ,picker)
        mycursor.execute(sql,val)
        mydb.commit()

    if (picker == 4):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


        mainfunction()


def buyfunction():
    global balance
    mycursor.execute("SELECT frukt,kg,pris FROM main")
  
    result = mycursor.fetchall()
    first = 0
    for row in result:
        row = str(row)
        row = row.replace("(", "") 
        row = row.replace(")", "")
        row = row.replace(",", "") 

        row = row.replace("'", "") 
        row = row.replace("'", "")
        print(row+"Kr")
        print("\n")
    print("Så, vilken vill du ha? Skriv in dens namn")
    picker = input()
    print("Ok, skriv in hur många kilo du vill ha")
    kgthing = int(input())

    mycursor.execute("SELECT frukt FROM main")

    result = mycursor.fetchall()

    for row in result:
        row = str(row)
        row = row.replace("(", "") 
        row = row.replace(")", "")
        row = row.replace(",", "") 

        row = row.replace("'", "") 
        row = row.replace("'", "")
        if (row == picker):
            pickedcorrect = 1
    if (pickedcorrect == 0):
        print("Sluta slösa min tid och skriv in rätt namn")
        mainfunction()



    if (pickedcorrect == 1):
            
        sql = "SELECT pris FROM main WHERE frukt=%s"
        val = (picker,)

        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        myresult = str(myresult)
        myresult = myresult.replace("(", "") 
        myresult = myresult.replace(")", "")
        myresult = myresult.replace(",", "") 
        myresult = myresult.replace("'", "") 
        myresult = myresult.replace("'", "")
        myresult = myresult.replace("[", "") 
        myresult = myresult.replace("]", "")

        sql = "SELECT kg FROM main WHERE frukt=%s"
        val = (picker,)

        mycursor.execute(sql,val)
        kgresult = mycursor.fetchall()
        kgresult = str(kgresult)
        kgresult = kgresult.replace("(", "") 
        kgresult = kgresult.replace(")", "")
        kgresult = kgresult.replace(",", "") 
        kgresult = kgresult.replace("'", "") 
        kgresult = kgresult.replace("'", "")
        kgresult = kgresult.replace("[", "") 
        kgresult = kgresult.replace("]", "")



        if (int(kgresult) < kgthing):
            print("Bra försök att köpa mer än vad vi har.")
            mainfunction()


        pristotalt = kgthing * int(myresult)
        kgsubtracter = int(kgresult) - kgthing
        balance = balance - pristotalt
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print("Ok, du vill ha "+ str(kgthing) + "Kg " + picker + ", det kommer att kosta " + str(pristotalt) + "Kr är du heeelt säker att du vill fortsätta?\nTryck 1 för att köpa\nTryck 2 för att gå tillbaka till menyn")
        chooser = 0
        chooser = int(input())

        if (chooser == 1):


            picker = str(picker)
            sql = "UPDATE main SET kg = %s WHERE frukt = %s"
        
            val = (kgsubtracter,picker)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Ok, klart.")
            mainfunction()
        else:
            mainfunction()





def mainfunction():
    global balance
    print("Tryck 1 för att kolla in frukten\nTryck 2 för att se din saldo\nTryck 3 Admin panelen")
    picker = int(input())
    pickedcorrect = 0
    if (picker == 1):
        if (balance > 0):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            buyfunction()


        else:
            print("Du är portad från butiken tills du har skaffat mer pengar.")
            mainfunction()
       

    if (picker == 2):
        print(balance)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        mainfunction()


    if (picker == 3):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


        adminpanel()
    if (picker == 4):

        exit(69)



mainfunction()
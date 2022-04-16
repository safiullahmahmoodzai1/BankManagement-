import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="*Sama*012",
  port='3306',
  database="BankDB"
)

mycursor=mydb.cursor(buffered=True)

def Menu():
  print("*"*140)
  print("Main Menu".center(140))
  print("1. Insert Record/Records".center(140))
  print("2. Display Records as per Account Number".center(140))
  print("  a. Sorted as per Account Number".center(140))
  print("  b. Sorted as per Customer Name".center(140))
  print("  c. Sorted as per Customer Balance".center(140))
  print("3. Search Record Details as per the Account number".center(140))
  print("4. Update Record".center(140))
  print("5. Delete Record".center(140))
  print("6. TransactionDebit/Withdraw from the account".center(140))
  print("   a. Debit/Withdraw from the account".center(140))
  print("   b. Credit into the account".center(140))
  print("7. Exit".center(140))
  print("*"*140)

def MenuSort():
    print("   a. Sorted as per Account Number".center(140))
    print("   b. Sorted as per Customer Name".center(140))
    print("   c. Sorted as per Customer Balance".center(140))
    print("   d. Back".center(140))

def MenuTransaction():
  print("    a. Debit/Withdraw from the account".center(140))
  print("    b. Credit into the account".center(140))
  print("    c. Back".center(140))

def Create():
  try:
    mycursor.execute('create table bank(ACCNO int(20), Name varchar(45), Mobile varchar(45),Email varchar(45), Address varchar(45), city varchar(45), Country varchar(45)')
    print("Table Created")
    Insert()
  except:
    print("Table Exist")
    Insert()

def Insert():
  while True:
    ACC=input("Enter account No")
    Name=input("Enter Name")
    Mob=input("Enter Mobile")
    email=input("Enter email")
    Add=input("Enter Address")
    City=input("Enter City")
    Country=input("Enter Country")
    Bal=float(input("Enter Balance"))
    Rec=[ACC,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
    Cmd="insert into Bank values(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(Cmd,Rec)
    mydb.commit()
    ch=input("Do you want to enter more records")
    if ch=='N' or ch=='n':
      break

def DispSortAcc():
  try:
    cmd="select * from Bank order by ACCNO"
    mycursor.execute(cmd)
    F="%15s %15s %15s %15s %15s %15s %15s %15s"
    print(F % ("ACCNO", "Name","Mobile","Email ADD","Address","City", "Country","Balance"))
    print("="*125)
    for i in mycursor:
      for j in i:
        print("%14s" % j, end=' ')
        print()
        print("="*125)
  except:
    print("Table Does not exist")


def DispSortName():
  try:
    cmd="select * from BANK order by Name"
    mycursor.execute(cmd)
    F = "%15s %15s %15s %15s %15s %15s %15s %15s"
    print(F % ("ACCNO", "Name", "Mobile", "Email ADD", "Address", "City", "Country", "Balance"))
    print("="*125)
    for i in mycursor:
      for j in i:
        print("%14s" % j, end=' ')
      print()
    print("="*125)
  except:
    print("Table does not exist")

def DispSortBal():
  try:
    cmd="select * from Bank order by BALANCE"
    mycursor.execute(cmd)
    F="%15s %15s %15s %15s %15s %15s %15s %15s"
    print(F % ("ACCNO", "Name", "Mobile", "Email ADD", "Address", "City", "Country", "Balance"))
    print("="*125)
    for i in mycursor:
      for j in i:
        print("%14s" % j, end=' ')
        print()
        print("="*125)
  except:
    print("Table does not exist")


def DisSearchAcc():
  try:
    cmd="select * from Bank"
    mycursor.execute(cmd)
    ch=input("Enter the accountno to be searched")
    for i in mycursor:
      if i[0]==ch:
        print("="*125)
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO", "Name", "Mobile", "Email ADD", "Address", "City", "Country", "Balance"))
        print("="*125)
        for j in i:
          print('%14s' % j, end=' ')
        print()
        break
      else:
        print("Record not found")
  except:
    print("Table does not exsit")


def Update():
  try:
    cmd="select * from BANK"
    mycursor.execute(cmd)
    A=input("Enter the account no whose details to be changed")
    for i in mycursor:
      i = list(i)
      if i[0] == A:
        ch = input("Change Name(Y/N)")
        if ch == 'y' or ch == 'Y':
          i[1] = input("Enter Name")
          i[1] = i[1].upper()

        ch = input("Change Mobile(Y/N)")
        if ch == 'y' or ch == 'Y':
          i[2] = input("Enter Mobile")
          i[2] = i[2].upper()

        ch = input("Enter Email(Y/N)")
        if ch == 'y' or ch == 'Y':
          i[3] = input("Enter email")
          i[3] = i[3].upper()

        ch = input("Enter ADDres(Y/N)")
        if ch == 'y' or ch == 'Y':
          i[4] = input("Enter Address")
          i[4] = i[4].upper()

        ch = input("Change city(Y/N)")
        if ch == 'y' or ch == 'Y':
          i[5] = input("Enter City")
          i[5] = i[5].upper()

        ch = input("Change country(Y/N)")
        if ch == 'y' or ch == 'Y':
          i[6] = input("Enter country")
          i[6] = i[6].upper()

        ch = input("Change Balance(Y/N)")
        if ch == 'y' or ch == 'Y':
          i[7] = float(input("Enter Balance"))
        cmd = "UPDATE BANK SET NAME=%s, MOBILE=%s, EMAIL=%s, ADDRESS=%s, CITY=%s, COUNTRY=%s, BALANCE=%s"
        val = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
        mycursor.execute(cmd, val)
        mydb.commit()
        print("Account updated")
        break
      else:
        print("Record not found ")
  except:
    print("No such table")


def Delete():
  try:
    cmd = "select * from Bank"
    mycursor.execute(cmd)
    A = input("Enter the accoun no whose details to be changed ")
    for i in mycursor:
      i = list(i)
      if i[0] == A:
        cmd = "delete from bank where accno=%s"
        val = (i[0],)
        mycursor.execute(cmd, val)
        mydb.commit()
        print("Account Deleted")
        break
      else:
        print("Record not found")
  except:
    print("No such Table ")

def Debit():
  #try:
    cmd="select * from Bank"
    mycursor.execute(cmd)
    print("Please note that the money can only be debited if min balance of 100$ exists")
    acc=input("Enter the account no from which the money is to be debited")
    for i in mycursor:
      i=list(i)
      if i[0]==acc:
        Amt=float(input("Enter the amount to be withdrawn"))
        if i[7]-Amt>=100:
          i[7]-=Amt
          cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
          val=(i[7], i[0])
          mycursor.execute(cmd,val)
          mydb.commit()
          print("Amount Debited")
          break
        else:
          print("There must be min balnce of 100$")
          break
      else:
        print("Record Not found")
  #except:
    #print("Table does not exist")

def Credit():
  try:
    cmd="select * from Bank"
    mycursor.execute(cmd)
    acc=input("Enter the account no from wich the money is to be debited")
    for i in mycursor:
      i=list(i)
      if i[0]==acc:
        Amt=float(input("Enter the amount to be credited"))
        i[7]+= Amt
        cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
        val=(i[7],i[0])
        mycursor.execute(cmd,val)
        mydb.commit()
        print("Amount Credited")
        break
      else:
        print("Record not found")
  except:
    print("Table does not exist")


while True:
  Menu()
  ch=input("Enter your choice")
  if ch=="1":
    Credit()
  elif ch=="2":
    while True:
      MenuSort()
      ch1=input("Enter choice a/b/c/d")
      if ch1 in ['a', 'A']:
        DispSortAcc()
      elif ch1 in ['b', 'B']:
        DispSortName()
      elif ch1 in ['c', 'C']:
        DispSortBal()
      elif ch1 in ['d', 'D']:
        print("Back to the main menu")
        break
      else:
        print("Invalid choice")
  elif ch=="3":
    DisSearchAcc()
  elif  ch=="4":
    Update()
  elif ch=="5":
    Delete()
  elif  ch=="6":
    while True:
      MenuTransaction()
      ch1=input("Enter choice a/b/c")
      if ch1 in ['a', 'A']:
        Debit()
      elif ch1 in ['b', 'B']:
        Credit()
      elif ch1 in ['c', 'C']:
        print("Back to the main menu")
        break
      else:
        print("Invalid choice")
  elif ch=="7":
    print("Exiting..")
    break
  else:
    print("Wron choice Entered")


















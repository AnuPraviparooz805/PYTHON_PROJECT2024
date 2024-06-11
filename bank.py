import sys
import time
import os.path
class Bank:
    
    def __init__(self):
        self.balance=500
        print('\n\t\tWELCOME TO OUR BANK')
        print('\t\t____________________')
    def acc_number(self):
        ac_no=input('Enter Your 10 digit Account Number     :   ')
        return ac_no
    def profile(self):
        name=input('\n\nEnter your Name         :     ').capitalize()
        address=input('\nEnter your address     :     ').capitalize()
        return name,address
    def deposit(self,name,ac_no):
        t=time.ctime()
        print("YOUR CURRENT BALANCE IS      :",self.balance)
        deposit_amnt=float(input('\nEnter the amount to be deposite :               '))
        self.balance+=deposit_amnt
        print('\nAccount No. ',ac_no,'Credited Rs.',deposit_amnt,'at',t)
        print('\n',name,'balance after credit in your Account no.',ac_no,'is Rs.',self.balance)
    def withdrawals(self,name,ac_no):
        t=time.ctime()
        withdraw=float(input('\nEnter the amount you withdraw :                     '))
        if self.balance>withdraw:
            self.balance-=withdraw
            print('\n',name,ac_no,'Amount Debited is Rs.',withdraw,'at',t)
            print('\n',name,ac_no,'Your balance after debit is Rs.',self.balance)
        else:
            print('\n\tNo Sufficient Balance in your account')
        return withdraw
    def display(self,ac_no,name,address):
        print('\n\tYOUR ACCOUNT DETAILS')
        print('_______________________________________')
        print('Account No:        |     ',ac_no)
        print('Name      :        |     ',name)
        print('Address   :        |     ',address)
        print('Balance   :        |     ',self.balance)
        print('_______________________________________')

    def save(self,ac_no,name,address):
    
        save_path = "C:/Users/ASUS/Desktop/Python_part2/_bank details"

        name_of_file = name

        completeName = os.path.join(save_path, name_of_file+".txt") 
        with open(completeName,'w')as f:
                f.write('Details Of New Member\n')
                f.write(time.ctime())
                f.write(f'Account Number : {ac_no}')
                f.write("\n")    
                f.write(f'Name           :   {name}')
                f.write("\n") 
                f.write(f'Address        :   {address}')
                f.write("\n")
                f.write(f'Balance        :{self.balance}')
        print("\n\tFILE SAVED")


b1=Bank()
acc=b1.acc_number()
name,address=b1.profile()
while True:
        
        ch=int(input('\n1. Deposit\n2. Withdrawal\n3. Display details\n4. exit\t'))
        if ch==1:
            b1.deposit(name,acc)
        if ch==2:
            b1.withdrawals(name,acc)
        if ch==3:
            b1.display(acc,name,address)
        if ch==4:
            sys.exit(1)
        b1.save(acc,name,address)
        print('\n\n****THANK YOU FOR VISITING OUR BANK,HAVE A GREAT DAY****\n')

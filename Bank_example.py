def create_account():

    Bank={}
    for i in range(2):
try:
        account_no= int(input("Enter Account number: "))
        if account_no not in Bank:
                Bank[account_no]={}
                Cust_name = input("Enter Customer Name/Account Holder name: ")
                pin = int(input("Enter your pin: "))
                Bal= float(input("Enter Your balance: "))
                mob = int(input("Enter your Mobile Number: "))
                Bank[account_no]['Cust_name']=Cust_name
                Bank[account_no]['pin']=pin
                Bank[account_no]['Bal']=Bal
                Bank[account_no]['mob']=mob
        else:
                print("Sorry, Account number already Exist")
            
        print(Bank)
            
except Exception as err:
    print(err)         

for i in Bank:
# print(i , ":", bank[i])
    for j in Bank[i]:
        print(j,":" , Bank[i][j])  


def Display():
    
try:
  ac_no=int(input('Enter Account Number :'))
  assert ac_no == Bank['account_no'], "wrong Account no"
  
  pin_no=int(input('Enter Pin number: '))
  assert pin_no==bank['pin'], "wrong Pin"
  
  print(f"welcome to {Bank['Cust_name']}")
  print(Bank[account_no]['Bal'])
  print(Bank[account_no]['mob'])
    
except ValueError as err:
    print(err)
  
except Exception as err:
    print(err) 
 
create_account()
Display()

        # print(j)  
      # trans= []
    # amount= float(input("Enter your Amount"))
    
    # 'transactions': [
    #                      {'amount': float, 'tr_type': 'cr', 'datetime': ''},


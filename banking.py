import random

class Bank:
    def __init__(self, name):
        self.name = name
        self.__total_bank_balance = 5000  # private..
        self.__total_provide_loan = 0     # private...
        self.loan_features = True
        self.all_user_list = []
        
    def get_total_bank_balance(self):    # private value access kora jabe..
        return self.__total_bank_balance
    
    def set_total_bank_balance(self,amount): # private value gular update kora jabe..
        self.__total_bank_balance += amount

    def get_total_provide_loan(self):
        return self.__total_provide_loan
    
    def set_total_provide_loan(self,amount):
        self.__total_provide_loan += amount

    def get_all_user_list(self):
        return self.all_user_list

    def create_user_account(self, client):
        self.all_user_list.append(client)
        print('add User successfully..')

    def view_all_user_list(self):
        print('....All User list...')
        print(f'\n Name \t\t Email \t\t Adress')
        for u in self.all_user_list:
            print(f'{u.name} \t {u.email} \t {u.address}' )
    
    def bank_balance(self):
        print(f'Total Bank Balance : {self.__total_bank_balance}')

    def bank_provide_loan(self):
        print(f'Bank Total Provide Loan : {self.__total_provide_loan}')

    def delete_user(self, email):
        
        client = self.find_account(email)
        if client:
            self.all_user_list.remove(client)
            print('Client delete successfully')
        else:
            print('Client not found..')

    def bank_loan_features_on(self):
        self.loan_features = True
        print('Bank loan features on Successfully..')
    
    def bank_loan_features_off(self):
        self.loan_features = False
        print('Bank loan features off successfully..')

    def find_account(self, email):
        for value in self.all_user_list:
            if value.email == email:
                return value
        return None


class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Client(User):
    def __init__(self, name, email, address, account_type):
        self.account_type = account_type
        self.current_balance = 0
        self.transaction = []
        self.maxLoan = 2
        self.current_loan = 0
        self.accID = random.randint(1, 100) + 999
        super().__init__(name, email, address)

    def deposit_balance(self, amount, bank):
        self.current_balance += amount
        print(f'Deposit {amount} Tk Successfully done ....')
        self.transaction.append(f'Deposit : {amount}')
        bank.set_total_bank_balance(amount)

    def withdraw_balance(self, amount, bank):
        if self.current_balance >= amount:
            self.current_balance -= amount
            print(f'Withdraw {amount} Tk Successfully done...')
            bank.set_total_bank_balance(-amount)
            self.transaction.append(f'Withdraw : {amount}')
        else:
            print(f'You have no sufficient balance..Current balance : {self.current_balance}')

    def available_balance(self):
        print(f'Available Balance : {self.current_balance}')

    def transaction_history(self):
        return self.transaction

    def take_loan(self, amount, bank):
        if bank.get_total_bank_balance() >= amount and bank.loan_features:
            if self.maxLoan > 0:
                self.current_loan += amount
                self.maxLoan -= 1
                self.current_balance += amount
                self.transaction.append(f'Loan niche : {amount}')
                bank.set_total_bank_balance(-amount)
                bank.set_total_provide_loan (amount)
                print(f'Bank provide Loan : {amount}')
            else:
                print('You have already taken loan two times...')
        else:
            print('Bank has not sufficient balance / bank loan features off..')

    def transfer_amount(self, amount, sender_email, receiver_email, bank):
        sender = bank.find_account(sender_email)
        receiver = bank.find_account(receiver_email)

        if sender and receiver:
            if self.current_balance >= amount:
                print(f'Transfer {amount} Tk Succesfully,,, Sender : {sender_email} and Reveiver : {receiver_email}')
            else:
                print(f'You have no sufficient balance. Your current balance : {self.current_balance}')
        else:
            print(f'Email not found....')


class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def create_user_account(self, bank, client):
        bank.create_user_account(client)

    def view_all_user_list(self, bank):
        bank.view_all_user_list()

    def bank_balance(self, bank):
        bank.bank_balance()

    def bank_provide_loan(self, bank):
        bank.bank_provide_loan()

    def delete_user(self, bank,email):
        bank.delete_user(email)

    def bank_loan_features_on(self, bank):
        bank.bank_loan_features_on()

    def bank_loan_features_off(self, bank):
        bank.bank_loan_features_off()



bank = Bank('Brac Bank')
def for_clien():
    name = input('Enter the name : ')
    email = input('Enter the email : ')
    address = input('Enter the address : ')
    account_type = input('Enter the account type : ')

    client = Client(name,email,address,account_type)

    while True :
        print('1. Deposite Balance')
        print('2. Withdraw Balance')
        print('3. Check Avaliable Balance')
        print('4. Take Loan ')
        print('5. Transfer Balance')
        print('6. Check transaction history')
        print('7. Exit')

        choice = int(input('Enter any choice : '))
        
        if choice == 1:
            amount = int(input('Enter the amount : '))
            client.deposit_balance(amount,bank)
        
        elif choice == 2:
            amount = int(input('Enter the amount : '))
            client.withdraw_balance(amount,bank)
        
        elif choice == 3:
            client.available_balance()
        elif choice == 4:
            amount = int(input('Enter the amount : '))
            client.take_loan(amount,bank)
        
        elif choice == 5:
            amount = int(input('Enter the amount : '))
            send_email = input('Enter the sender email : ')
            rec_email = input('Enter the receiver email : ')
            client.transfer_amount(amount,send_email,rec_email,bank)
        
        elif choice == 6:
            print(client.transaction_history())
        
        elif choice == 7:
            break
        # else:
        #     print('Invalid input...')


def for_admin():
    name = input('Enter the name : ')
    email = input('Enter the email : ')
    address = input('Enter the address : ')
    
    admin = Admin(name,email,address)

    while True:
        print('1. Create user/ add User')
        print('2. Show all user accounts')
        print('3. Delete user account')
        print('4. Total Bank Balance')
        print('5. Total Bank Provided Loan')
        print('6. Bank Loan Features off')
        print('7. Bank Loan Features onn')
        print('8. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            name = input('Enter the name : ')
            email = input('Enter the email : ')
            address = input('Enter the address : ')
            account_type = input('Enter the account type : ')
            client = Client(name,email,address,account_type)
            admin.create_user_account(bank,client)
        if choice == 2:
            admin.view_all_user_list(bank)

        elif choice == 3:
            name = input('Enter the name : ')
            email = input('Enter the email : ')
            address = input('Enter the address : ')
            account_type = input('Enter the account type : ')
            client = Client(name,email,address,account_type)
            admin.delete_user(bank,email)

        elif choice == 4:
            admin.bank_balance(bank)

        elif choice == 5:
            admin.bank_provide_loan(bank)

        elif choice == 6:
            admin.bank_loan_features_off(bank)
        
        elif choice == 7:
            admin.bank_loan_features_on(bank)
        elif choice == 8:
            break
        # else:
        #     print('Invalid input...')


while True:
    print('...Welcome to Our Banking System...')

    print('1. User')
    print('2. Admin')
    print('3. Exit')

    choice = int(input('Enter the choice : '))

    if choice == 1:
        for_clien()
    
    elif choice == 2:
        for_admin()
    elif choice == 3:
        break
    else:
        print('Invalid input...')
            
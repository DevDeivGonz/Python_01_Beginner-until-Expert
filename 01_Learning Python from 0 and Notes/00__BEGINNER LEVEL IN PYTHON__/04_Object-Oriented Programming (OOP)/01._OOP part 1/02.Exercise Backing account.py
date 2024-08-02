# This is a private encapsulation
class BackAccount:
    def __init__(self, name_older ,id_account, balance_money, banking_transfers, balance_per_transfer):
        self.__name_older = name_older
        self.__id_account = id_account
        self.__balance_money = balance_money
        self.__banking_transfers = banking_transfers
        self.__balance_per_transfer = balance_per_transfer

    def get_name_older(self):
        print(self.__name_older)

    def get_currect_balance(self):
        print(f"Dear {self.__name_older}, your current balance is ${self.__balance_money}.")

    def check_transfers(self):
        print(f"Dear {self.__name_older}, you have {self.__banking_transfers} transfers and you have received "
              f"${self.__balance_per_transfer} for that transfer.")
    def make_a_deposit(self):
        new_deposit = int(input("Enter the balance you would like to deposit:\n $"))
        self.__balance_money += new_deposit
        print(f"Dear {self.__name_older}, you have transferred ${new_deposit} and now your current balance is "
              f"${self.__balance_money}")

iD_1918988992220 = BackAccount("Hernesto Gonzalez", "iD1918988992220",
                                19000, 1, 2990000)

def main_menu():

    while True:
        print("\n[1]. Current balance")
        print("\n[2]. Transfers banking")
        print("\n[3]. Deposit Money")
        print("\n[4]. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            iD_1918988992220.get_currect_balance()
        elif choice == 2:
            iD_1918988992220.check_transfers()
        elif choice == 3:
            iD_1918988992220.make_a_deposit()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
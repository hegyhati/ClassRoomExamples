import matplotlib.pyplot as plt


class Bank:
    def __init__(self, transaction_fee:int):
        self.__balance = {}
        self.__fee = transaction_fee
    
    def new_customer(self, name:str) -> None:
        if name in self.__balance: raise ValueError("Client already exist.")
        self.__balance[name] = 0
    
    def deposit(self, name:str, amount:int) -> None:
        if name not in self.__balance: raise ValueError("Client does not exist.")
        if amount <= self.__fee: raise ValueError("Deposit amount must be more than the transaction fee.")
        self.__balance[name] += amount - self.__fee
    
    def withdraw(self, name:str, amount:int) -> None:
        if name not in self.__balance: raise ValueError("Client does not exist.")
        if amount <= 0: raise ValueError("Withdrawal amount must be positive.")
        if amount + self.__fee > self.__balance[name]: raise ValueError("Insufficient funds.")
        self.__balance[name] -= amount + self.__fee
    
    def transfer(self, sender:str, beneficiary:str, amount:int) -> None:
        if sender not in self.__balance: raise ValueError("The sender is not a client.")
        if beneficiary not in self.__balance: raise ValueError("The beneficiary is not a client.")
        if amount <= 0: raise ValueError("Transfer amount must be positive.")
        if amount + self.__fee > self.__balance[sender]: raise ValueError("Insufficient funds.")
        self.__balance[sender] -= amount + self.__fee
        self.__balance[beneficiary] += amount
    
    def balance(self, name:str) -> int:
        if name not in self.__balance: raise ValueError("Client does not exist.")
        return self.__balance[name]

    def clients(self) -> list[str]:
        return list(self.__balance.keys())
    
    def show_balances(self, description:str) -> None:
        clients = self.clients()
        if clients is None: return
        bars = plt.bar(clients, [self.balance(customer) for customer in clients])
        plt.suptitle(description)
        plt.bar_label(bars)
        plt.show()


TEST_PASSED  = "\033[32m --- Test PASSED --- \033[0m"
TEST_FAILED  = "\033[31m --- Test FAILED --- \033[0m"
def test_step(shouldpass:bool, action, description:str):
    print(f"{("Trying to " + description):45}", end = " ")
    try:
        action()
        print("[ SUCCESS ]", TEST_PASSED if shouldpass else TEST_FAILED)
    except ValueError as e:
        print("[ FAILURE ]", TEST_PASSED if not shouldpass else TEST_FAILED, e)

if __name__ == "__main__":
    bank:Bank = Bank(transaction_fee = 2)
    test_step(True  , lambda: bank.new_customer("Huey")  , "regirster Huey")
    test_step(False , lambda: bank.new_customer("Huey")  , "regirster Huey again")
    test_step(True  , lambda: bank.new_customer("Dewey") , "regirster Dewey")
    test_step(True  , lambda: bank.new_customer("Louie") , "regirster Louie")
    bank.show_balances("Balances after registration, all three should have 0.")

    test_step(True  , lambda: bank.deposit("Huey", 100)  , "deposit 100 to Huey")
    test_step(False , lambda: bank.deposit("Huey", -10)  , "deposit -10 to Huey")
    test_step(False , lambda: bank.deposit("Huey", 1)    , "deposit 1 to Huey")
    test_step(False , lambda: bank.deposit("Donald", 10) , "deposit 10 to Donald")
    test_step(True  , lambda: bank.deposit("Dewey", 200) , "deposit 200 to Dewey")
    test_step(True  , lambda: bank.deposit("Louie", 300) , "deposit 300 to Louie")
    bank.show_balances("Balances after deposits, should be 98 / 198 / 298")

    test_step(True  , lambda: bank.withdraw("Huey", 50)    , "withdraw 50 from Huey")
    test_step(False , lambda: bank.withdraw("Huey", 50)    , "withdraw 50 from Huey")
    test_step(False , lambda: bank.withdraw("Dagobert", 1) , "withdraw 1 from Dagobert")
    bank.show_balances("Balances after deposits, should be 46 / 198 / 298")

    test_step(True  , lambda: bank.transfer("Dewey", "Huey", 50)  , "transfer 50 from Dewey to Huey")
    test_step(False , lambda: bank.transfer("Dewey", "Huey", 150) , "transfer 150 from Dewey to Huey")
    test_step(True  , lambda: bank.transfer("Louie", "Huey", 150) , "transfer 150 from Louie to Huey")
    bank.show_balances("Balances after deposits, should be 246 / 146 / 146")

    assert bank.balance("Huey") == 246, "Hueys balance must be 246 in the end."
    assert bank.balance("Dewey") == 146, "Deweys balance must be 146 in the end."
    assert bank.balance("Louie") == 146, "Louies balance must be 146 in the end."
    


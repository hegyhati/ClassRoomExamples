import matplotlib.pyplot as plt


class Bank:
    """Represents a bank, that keeps track of clients balances.
    """
    def __init__(self, transaction_fee:int):
        """Creates a new bank without any clients.

        Args:
            transaction_fee (int): the fee that must be paid to the bank for each successful transaction
        """
        pass
    
    def new_client(self, name:str) -> None:
        """Registers a client with a balance of 0.

        Args:
            name (str): name of the client, must be unique
        
        Raises:
            ValueError: If a client already exists with this name.
        """
        pass
    
    def deposit(self, name:str, amount:int) -> None:
        """Deposits money to client (and charges transaction fee).

        Args:
            name (str): name of the client
            amount (int): the amount of money to deposit

        Raises:
            ValueError: If no client exists with the name.
            ValueError: If the amount is less than the transaction fee.
        """
        pass
    
    def withdraw(self, name:str, amount:int) -> None:
        """Withdraws money from the account (and charges transaction fee).

        Args:
            name (str): name of the client
            amount (int): the amount to be withdrawn

        Raises:
            ValueError: If no client exists with the name.
            ValueError: If the withdrawal amount is not positive.
            ValueError: If there isn't enough funds for the amount and the transaction fee.
        """
        pass
    
    def transfer(self, sender:str, beneficiary:str, amount:int) -> None:
        """Transfers money between two clients. The transaction fee is paid by the sender.

        Args:
            sender (str): name of the sender
            beneficiary (str): name of the beneficiary
            amount (int): the amount to be transferred

        Raises:
            ValueError: If no client exists with the name of the client or beneficiary.
            ValueError: If the transfer amount is not positive.
            ValueError: If the sender does not have sufficient funds for the transfer (and its fee).
        """
        pass
    
    def balance(self, name:str) -> int:
        """Returns the balance of a client.

        Args:
            name (str): the name of the client

        Raises:
            ValueError: If no client exists with the name.

        Returns:
            int: the balance of the client
        """
        pass

    def clients(self) -> list[str]:
        """Returns the list of the names of clients in arbitrary order.

        Returns:
            list[str]: list of client names
        """
        pass
    
    def show_balances(self, description:str) -> None:
        """Simple utility method to display the balance of all clients using the `clients` and `balance` methods on a bar plot accompanied with the description provided.

        Args:
            description (str): the message/description shown in the title of the shown barplot
        """
        clients = self.clients()
        if clients is None: return
        bars = plt.bar(clients, [self.balance(client) for client in clients])
        plt.suptitle(description)
        plt.bar_label(bars)
        plt.show()


TEST_PASSED  = "\033[32m --- Test PASSED --- \033[0m"
TEST_FAILED  = "\033[31m --- Test FAILED --- \033[0m"
def test_step(shouldpass:bool, action, description:str):
    """Simple utility function to test the actions. It runs the action, checks if it raises an error, and prints in green/red whether the expected behavior is observed or not.

    Args:
        shouldpass (bool): whether the action should succeed or raise a ValueError
        action (_type_): the callable action 
        description (str): human readable description of what the callable tries to do
    """
    print(f"{("Trying to " + description):45}", end = " ")
    try:
        action()
        print("[ SUCCESS ]", TEST_PASSED if shouldpass else TEST_FAILED)
    except ValueError as e:
        print("[ FAILURE ]", TEST_PASSED if not shouldpass else TEST_FAILED, e)

if __name__ == "__main__":
    bank:Bank = Bank(transaction_fee = 2)
    test_step(True  , lambda: bank.new_client("Huey")  , "regirster Huey")
    test_step(False , lambda: bank.new_client("Huey")  , "regirster Huey again")
    test_step(True  , lambda: bank.new_client("Dewey") , "regirster Dewey")
    test_step(True  , lambda: bank.new_client("Louie") , "regirster Louie")
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
    


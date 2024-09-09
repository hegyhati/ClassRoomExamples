
from enum import Enum

class Order:
    class Status(Enum): 
        OPEN = 0
        CANCELED = -1
        PAID = 2
        SHIPPED = 3
        DELIVERED = 4
        RETURNED = -2
        
    __open_orders = []
    __next_order = 0
    
    def __init__(self, item:str, quantity: int) -> None:
        self._item = item
        self._quantity = quantity
        self.__id = self.__next_order  # both
        self.__id = Order.__next_order # is fine
        Order.__next_order += 1 # Only this is good
        # self.__next_order += 1 # This would create __next_order for the object with 1
        self.__open_orders.append(self) # ok with self instead of Order, as it is mutation not reassignment
        self.__status = Order.Status.OPEN
    
    def __str__(self) -> str:
        return f"Order {self.__id}: {self._quantity} X {self._item}"
    
    def pay(self) -> str:
        # payment logic
        if self.__status == Order.Status.OPEN:         
            self.__open_orders.remove(self)
            self.__status = Order.Status.PAID
        else: raise ValueError(f"Order {self.__id} is not open.")
            
    
    def cancel(self):
        if self.__status == Order.Status.OPEN:            
            self.__open_orders.remove(self)
            self.__status = Order.Status.CANCELED
        else: raise ValueError(f"Order {self.__id} is not open. ")
    
    @classmethod
    def number_of_open_orders(cls) -> int:
        return len(cls.__open_orders)

        
    def happily_distributable(orders:list["Order"], number_of_people:int) -> bool:
        total = sum(order._quantity for order in orders)
        return total % number_of_people == 0


print(f"Number of open orders: {Order.number_of_open_orders()}")
o1 = Order("Plussmaci", 3)
print(o1)
o2 = Order("Jatekauto", 7)
print(o2)
print(f"Number of open orders: {Order.number_of_open_orders()}")
for children in range(2,15):
    print(f"Items in the two orders can {'not ' if not Order.happily_distributable([o1,o2],children) else ''}be equally distributed among {children} children")
o1.cancel()
print(f"Number of open orders: {Order.number_of_open_orders()}")
o2.pay()
print(f"Number of open orders: {Order.number_of_open_orders()}")
try:
    o1.pay()
except ValueError as e:
    print(e)



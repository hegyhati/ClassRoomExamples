class Usage:
    _minutes = 0
    _messages = 0
    _data = 0

    def __init__(self):
        self.input()

    def input(self):
        self._minutes = int(input("Adja meg a telefonalt perceket: "))
        self._messages = int(input("Adja meg az elkuldott sms-ek szamat: "))
        self._data = int(input("Adja meg az adattforgalma MB-ban: "))


class Tariff:
    _minute_cost = 0
    _message_cost = 0
    _data_cost = 0
    _base_fee = 0
    name = None

    def __init__(self, name:str):
        print("A {} csomag adatait adja meg!".format(name))
        self.name=name
        self.input()
    
    def input(self):
        self._base_fee = int(input("Adja meg a csomag havidijat: "))
        self._minute_cost = int(input("Adja meg a csomag percdijat: "))
        self._message_cost = int(input("Adja meg a csomag sms dijat: "))
        self._data_cost = int(input("Adja meg 1 MG adat arat: "))

    def payment(self, usage: Usage):
        cost = self._minute_cost * usage._minutes + self._message_cost * usage._messages + self._data_cost * usage._data
        if cost < self._base_fee : 
            cost = self._base_fee
        return cost


tariff = Tariff("Szuper tarifa")
month = Usage()



print("Ennyit kell fizetni: {} Ft".format(tariff.payment(month)))

class Address:
    def __init__(self, zip:int, city:str, street:str, number:int) -> None:
        self.__zip = zip
        self.__city = city
        self.__street = street
        self.__number = number
    
    @property
    def zip(self):
        return self.__zip

    @zip.setter
    def zip(self, newzip:int):
        if newzip < 0 or newzip > 9999:
            raise ValueError("Zip must be between 0 and 9999.")
        self.__zip=newzip 
    
    
    
    def __str__(self) -> str:
        return f"{self.__city} ({self.__zip})"
    

a = Address(9400, "Sopron", "Bajcsy-Zsilinszky", 9)
a.zip = -3
print(a.zip)


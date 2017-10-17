param startbudget := 200000; # HUF

param garagecapacity :=  4; # pieces

param nDays := 7;

set Cars := Trabant Skoda Wartburg Fiat;

param price : # HUF / piece
        Trabant Skoda   Wartburg    Fiat :=
    1   120000  110000  100000      95000
    2   135000  120000  111000      100000
    3   125000  115000  120000      110000
    4   120000  111000  95000       105000
    5   111000  111000  111000      111000
    6   120000  110000  101000      100000
    7   123000  123000  123000      123000
    ;

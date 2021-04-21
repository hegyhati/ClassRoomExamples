def foo(a,b=0,d=2):
    print(a,b,d)

def greeting(firstname="", familyname="", title=""):
    pass

"""
("Sanyi")
("Szabo","Sandor")
("Dr", "Szabo")
("Dr","Szabo","Sandor")
()

    Title   Family  First
    -       -       -
    -       -       X
    -       X       X
    X       X       X
    X       X       -   <--- !!!

    greeting(title="Dr",familyname="Szbo")
"""

def sum(*args):
    s=0
    for item in args:
        s+=item
    return s

"""
miketkelleneosszeadni = fv(...) -> [1,2,3]

sum()
sum(1)
sum(1,2)
sum(1,2,3)
sum(miketkelleneosszeadni)




def sum_list(args_list):
    s=0
    for item in args_list:
        s+=item
    return s

sum_list([])
sum_list([1])
sum_list([1,2])
sum_list([1,2,3])
sum_list(miketkelleneosszeadni)
"""

def greeting_name(firstname=None, familyname=None, title=None)->str:
    if firstname==None and familyname==None and title==None:
        return "Sir/Madam"
    elif familyname==None and title==None:
        return firstname
    else:
        pass

def greeting_name_2(names:map)->str:
    if 'lastname' in names: names['familyname']=names['lastname']
    if 'givenname' in names: names['firstname']=names['givenname']

    if 'firstname' not in names and 'familyname' not in names and 'title' not in names:
        return "Sir/Madam"
    elif 'familyname' not in names and 'title' not in names:
        return names['firstname']
    else:
        pass

greeting_name_2({'firstname':'Sanyi'})


def greeting_name_3(**names):
    if 'fullname' in names: return names['fullname']
    if 'firstname' in .,.,,
        names['fullname']=names['title'] + ' ' + names['Firstname']... 
    if 'lastname' in names: names['familyname']=names['lastname']
    if 'givenname' in names: names['firstname']=names['givenname']

    if 'firstname' not in names and 'familyname' not in names and 'title' not in names:
        return "Sir/Madam"
    elif 'familyname' not in names and 'title' not in names:
        return names['firstname']
    else:
        pass




greeting_name_3(firstname="Mate", lastname="Hegyhati")
greeting_name_3(fullname="Sir Integra Fairbrook Wingates Hellsing")

"""
Szabo -> Mr./Mrs. Szabo
Szabo Tamas -> Szabo Tamas
Mr Szabo -> Mr Szbo
Tamas  -> Tamas
 -> Sir/Madam
"""


class Button:
    def __init__(self,parent, **kargs):
        pass

import math
class Point2D:
    def __init__(self, **kargs):
        if 'x' in kargs and 'y' in kargs:
            self.x=kargs['x']
            self.y=kargs['y']
        elif 'alpha' in kargs and 'radius' in kargs:
            self.x=kargs['radius'] * math.cos(kargs['alpha'])
            self.y=kargs['radius'] * math.sin(kargs['alpha'])
        elif 'value' in kargs:
            self.x=kargs['value']
            self.y=0
        else:
            raise Exception

x1=Point2D(x=1,y=3)
x2=Point2D(r=4,a=150)


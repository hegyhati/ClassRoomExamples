def add(x:int,y:int) -> int:
    """Ez a fuggveny osszead ket egesz szamot.

    Args:
        x (int): az egyik szam
        y (int): a masik szam

    Returns:
        int: a ket szam osszege
    """
    return x+y

def multiply(x:int,y:int) -> int:
    return x*y

def nemcsinalsemmit(x):
    """Ez a fuggveny nem csinal az eg egy adta vilagon semmit. de legalabb van

    Args:
        x (int): az argumentum, amit majd ugyanugy visszaad

    Returns:
        int: az argumentum siman vissszaadva
    """
    return x

def mozgoatlag(raw_data:list,window_size:int) -> list:
    """Kisimitja a raw adatok gorbejet mozgoatlag szamitassal. 
    Az elso elemeknel kisebb ablakkal szamol.

    Args:
        raw_data (list): nyers adatok listaban
        window_size (int): ablak merete, legalabb 1 kell legyen

    Returns:
        list: mozgoatlagos ertekek, a merete ugyanakkora mint a raw_data -nak
    """
    pass


def max_elem(l: list) -> int:
    """visszaadja az in listta legnagyobb elemett

    Args:
        l (list): int-ekett tartalmazo lista

    Returns:
        int: a lista legnagyobb eleme

    >>> max_elem([1,2,3])
    3
    >>> max_elem( [-4,-2,-99,-2] )
    -2
    >>> max_elem( [2,2,2,2,2,2,2,2] )
    4
    >>> max_elem( [3] )
    3
    >>> max_elem( [] )
    """
    if len(l) == 0: return None
    max = l[0]
    for item in l:
        if item > max:
            max = item
    return max
    

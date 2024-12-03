from abc import ABC, abstractmethod


def get_indices(reference:str) -> tuple[int,int]:
    if not reference[0].isalpha() or not  reference[1:].isnumeric():
        raise ValueError("Invalid reference")
    return int(reference[1:]) - 1, ord(reference[0].upper()) - ord("A")

class Sheet:
    
    def __init__(self, rows:int, cols:int) -> None:
        self.__rows:int = rows
        self.__cols:int = cols
        self.__cells:BaseCell = [[EmptyCell(self) for _ in range(cols)] for _ in range(rows)]
    
    def set_cell(self, row:int, col:int, cell:"BaseCell") -> None:
        self.__cells[row][col] = cell
    
    def get_cell(self, row:int, col:int) -> "BaseCell":
        return self.__cells[row][col]
    
    def __str__(self) -> str:
        result = ""
        for row in self.__cells:
            for cell in row:
                result += str(cell) + "\t"
            result += "\n"
        return result

    def column_count(self) -> int:
        return len(self.__cells[0])
    
    def row_count(self) -> int:
        return len(self.__cells)
    
    def cell_factory(self,data:str):
        classes = [SumCell, SimpleReferenceCell, NumericCell, EmptyCell, TextCell]
        for cls in classes:
            if cls._recognize(data):
                return cls(self, data)
        raise ValueError("No cell can be made")

class BaseCell(ABC):
        
    @classmethod
    @abstractmethod
    def _recognize(cls, data:str) -> bool:
        pass
    
    def __init__(self, sheet: Sheet, data:str) -> None:
        self._sheet = sheet
        if not self._recognize(data):
            raise ValueError("Invalid data for cell type")
    
    @abstractmethod
    def __str__(self) -> str:
        pass

    def is_numeric(self) -> bool:
        return False

    def is_formula(self) -> bool:
        return False

class EmptyCell(BaseCell):
        
    @classmethod
    def _recognize(cls, data:str) -> bool:
        return data == ""
    
    def __init__(self, sheet:Sheet, data:str = "" ):
        super().__init__(sheet,data)
    
    def __str__(self) -> str:
        return ""

class TextCell(BaseCell):

    @classmethod
    def _recognize(cls, data:str) -> bool:
        return True
        
    def __init__(self, sheet:Sheet, data:str):
        super().__init__(sheet,data)
        self.__data:str = data
    
    def __str__(self) -> str:
        return self.__data

class NumericCell(BaseCell):
    
    @classmethod
    def _recognize(cls, data:str) -> bool:
        try:
            float(data)
            return True
        except ValueError:
            return False
        
    def __init__(self, sheet:Sheet, data:str):
        super().__init__(sheet,data)
        self.__data:float = float(data)

    def __str__(self) -> str:
        return str(self.__data)
    
    def numeric_value(self)-> float:
        return self.__data
    
    def is_numeric(self) -> bool:
        return True
  
    
class SimpleReferenceCell(BaseCell):
    
    @classmethod
    def _recognize(cls, data:str) -> bool:
        if not data.startswith("="): return False
        try:
            get_indices(data[1:])
            return True
        except ValueError:
            return False
        
    def __init__(self, sheet:Sheet, data:str):
        super().__init__(sheet, data)
        self.__formula = data
        self.__row, self.__column = get_indices(data[1:])

    
    def __str__(self) -> str:
        try: 
            cell = self._sheet.get_cell(self.__row, self.__column)
            return str(cell)
        except IndexError:
            return "#REF"
    
    def is_numeric(self) -> bool:
        try:
            return self._sheet.get_cell(self.__row, self.__column).is_numeric()
        except IndexError:
            return False
    
    def numeric_value(self) -> float:
        if self.is_numeric(): 
            return self._sheet.get_cell(self.__row, self.__column).numeric_value()
    
    def is_formula(self) -> bool:
        return True
    
    def get_formula(self) -> str:
        return self.__formula

class SumCell(BaseCell):
    
    @classmethod
    def _recognize(cls, data: str) -> bool:
        if not data.startswith("=SUM(") or not data.endswith(")"): return False
        cell_range = data[5:-1]
        if cell_range.count(":") != 1: return False
        start,end = cell_range.split(":")
        try: 
            r1,c1 = get_indices(start)
            r2,c2 = get_indices(end)
        except ValueError:
            return False        
        return r1 == r2 or c1 == c2
    
    def __init__(self, sheet: Sheet, data: str) -> None:
        super().__init__(sheet, data)
        self.__formula = data
        start, end = data[5:-1].split(":")
        r1,c1 = get_indices(start)
        r2,c2 = get_indices(end)
        if r1 == r2 :
            self.__cells = [(r1,c) for c in range(min(c1,c2), max(c1,c2)+1)]
        else:
            self.__cells = [(r,c1) for r in range(min(r1,r2), max(r1,r2)+1)]

    def __str__(self) -> str:
        nvalue = self.numeric_value()
        if nvalue is None:
            return "ERR"
        else: 
            return str(nvalue)

    def is_numeric(self) -> bool:
        return self.numeric_value() is not None
    
    def numeric_value(self) -> float:
        sum = 0
        for (r,c) in self.__cells:
            cell = self._sheet.get_cell(r,c)
            if not cell.is_numeric():
                return None
            sum += cell.numeric_value()
        return sum
    
    def is_formula(self) -> bool:
        return True
    
    def get_formula(self) -> str:
        return self.__formula




        
if __name__ == "__main__":
    sheet = Sheet(5,5)
    sheet.set_cell(*get_indices("A1"),TextCell(sheet,"Hello"))
    sheet.set_cell(*get_indices("A2"),NumericCell(sheet,"3.14"))
    sheet.set_cell(*get_indices("B1"),SimpleReferenceCell(sheet,"=A1"))
    sheet.set_cell(*get_indices("B2"),SimpleReferenceCell(sheet,"=A2"))
    print(sheet)

    sheet.set_cell(*get_indices("A1"),TextCell(sheet,"World"))
    sheet.set_cell(*get_indices("C1"),SumCell(sheet, "=SUM(A2:B2)"))
    print(sheet)

    sheet.set_cell(*get_indices("A2"),NumericCell(sheet,"21"))
    print(sheet)



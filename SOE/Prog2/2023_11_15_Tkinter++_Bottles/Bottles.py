class BottleSystem:
    def __init__(self, bottle_sizes:list[int]) -> None:
        self._max = tuple(bottle_sizes)
        self.size = len(bottle_sizes)
        self._levels = [0]*self.size
    
    def get_max(self) -> tuple[int]:
        return self._max
    
    def _set_levels(self, levels:list[int]) -> None:
        # Check for consistency -> Exception
        self._levels = levels[:]
    
    def get_levels(self) -> tuple[int]:
        return tuple(self._levels)

    def get_level(self,idx:int):
        return self._levels[idx]
    
    def fill(self, idx:int) -> None:
        # Check idx
        self._levels[idx] = self._max[idx]

    def empty(self, idx:int) -> None:
        # Check idx
        self._levels[idx] = 0
    
    def pour(self, source:int, sink:int):
        qty = min(self._max[sink] - self._levels[sink], self._levels[source])
        self._levels[sink] += qty
        self._levels[source] -= qty
    
class DFA:
    K: set[int]
    E: set[str]
    D: dict[int, set[tuple[str,int]]]
    s: int
    F: set[int]

    def accept(self, w:str) -> bool:
        def rec_accept(q:int, w:str) -> None:
            for (trans_label, target_state) in self.D[q]:
                if len(w) == 0 and q in self.F:
                    raise "Yeppee"
                if w.startswith(trans_label):
                    rec_accept(target_state, w.removeprefix(trans_label))
                    # note: empty cycles!!!!
        
        try:
            rec_accept(self.s, w)
        except str:
            return True
        return False


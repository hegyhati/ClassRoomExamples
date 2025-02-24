class DFA:
    K: set[int]
    E: set[str]
    d: dict[int,dict[str,int]]
    s: int
    F: set[int]

    def minimized(self) -> "DFA":
        def not_ok(pair):
            nonlocal ok
            nonlocal rule3
            for previous_pair in rule3[pair]:
                if ok[previous_pair]:
                    ok[previous_pair] = False
                    not_ok(previous_pair)               

        pairs = {
            (p,q) for p in self.K for q in self.K 
            if p<q
            if p in self.F == q in self.F # Rule 1
            if self.d[p].keys() == self.d[q].keys() # Rule 2, check == behavior
        }
        rule3 = {pair:[] for pair in pairs}
        ok = {pair:True for pair in pairs}
        for (p,q) in pairs:
            for sigma in self.d[p].keys(): #d[p].keys() == d[q].keys()
                to_pair = tuple(sorted([self.d[p][sigma], self.d[q][sigma]]))
                if to_pair[0] == to_pair[1]:
                    pass
                elif not ok[to_pair]:
                    ok[(p,q)] = False
                    not_ok((p,q))
                else:
                    rule3[to_pair].append((p,q))
        # TODO return
        






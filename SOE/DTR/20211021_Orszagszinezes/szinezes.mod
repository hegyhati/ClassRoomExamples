set Countries;
set Borders in Countries cross Countries;

var K{Countries} binary;
var P{Countries} binary;
var Z{Countries} binary;
var F{Countries} binary;


s.t. Minden_orszgnak_legyen_szine{c in Countries}:
    K[c] + P[c] + Z[c] + F[c] = 1;

s.t. Nem_lehetnek_piros_szomszedok{(c1,c2) in Borders}:
    P[c1]+P[c2] <= 1;

s.t. Nem_lehetnek_zold_szomszedok{(c1,c2) in Borders}:
    Z[c1]+Z[c2] <= 1;

s.t. Nem_lehetnek_kek_szomszedok{(c1,c2) in Borders}:
    K[c1]+K[c2] <= 1;

s.t. Nem_lehetnek_fekete_szomszedok{(c1,c2) in Borders}:
    F[c1]+F[c2] <= 1;

minimize Placeholder: 1;



set Colors;
set Countries;
set Borders within Countries cross Countries;

var use{Countries,Colors} binary;

s.t. Minden_orszgnak_legyen_szine{country in Countries}:
    sum{color in Colors} use[country,color] = 1;


s.t. Nem_lehetnek_azonos_szinu_szomszedok
{(country1,country2) in Borders, color in Colors}:
    use[country1,color]+use[country2,color] <= 1;

minimize Placeholder: 1;

solve;

printf "{\n";
for {color in Colors}:
{
    printf ' "%s" : [ ',color;
    for {country in Countries : use[country,color] = 1}
        printf '"%s", ',country;
    printf '],\n';
}
printf '}\n';



end;



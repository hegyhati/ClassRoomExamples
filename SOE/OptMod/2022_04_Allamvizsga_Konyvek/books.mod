set BookSets;
param width{BookSets};
param height{BookSets};
param shelfCount;
param shelfWidth;
param shelfHeight;
param minDistance;
param minPosition;

set Shelves := 1..shelfCount;

var use{Shelves} binary;
var position{Shelves} >= minPosition;
var put{BookSets,Shelves} binary;

var highest_book{Shelves} >=0;
var highest_shelf >= minPosition;

# Egy polcra nem mehet tobb mint ami elfer
s.t. Shelf_capacity{s in Shelves}:
    sum {b in BookSets} put[b,s] * width[b] <= shelfWidth;

# Egy polc folott legalabb annyi hely legyen, mint a ratett legmasabb konyv + szukseges gap + polc vastagsag
s.t. Shelf_min_position{s in Shelves : s != 1}:
    position[s] >= position[s-1] + shelfHeight + highest_book[s-1] + minDistance;


s.t. Highest_Book_Constraint{s in Shelves, b in BookSets}:
    highest_book[s] >= height[b] * put[b,s];


# Minden konyvet fel kell pakolni valahova
s.t. Books_must_be_put_on_a_shelf{b in BookSets}:
    sum{s in Shelves} put[b,s] = 1;

# Ha egy polcot nem hasznalunk, arra nem pakolhatunk
s.t. Dont_put_books_on_unused_shelf{s in Shelves, b in BookSets}:
    put[b,s] <= use[s];

s.t. Dont_put_books_on_unused_shelf_2{s in Shelves}:
    sum{b in BookSets} put[b,s] <= card(BookSets) * use[s];


# Set highest shelf
s.t. Highest_shelf_constraint{s in Shelves}:
    highest_shelf >= position[s] - (minPosition + minDistance + shelfHeight + sum{b in BookSets} height[b]) * (1 - use[s]);

s.t. Shelf_usage{s in Shelves : s != 1}:
    use[s-1] >= use[s];

minimize max_reach: highest_shelf;

solve; 

for {s in Shelves : use[s] == 1}
{
    printf "Shelf %d - %g cm - max book: %g cm\n", s, position[s], highest_book[s];
    for {b in BookSets : put[b,s]}
        printf " - %s - %g cm - max height: %g cm\n", b, width[b], height[b];
}


end; 
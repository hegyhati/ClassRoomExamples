/*
Uj alberletbe koltoztunk, es a konyveinket fel szeretnenk pakolni egy polcszerkezetre. 50 cm magasan kezdodik a ket sin, amire a polclapokat pakolhatjuk. A polcaink 120 cm szelesek, es a celunk, hogy minel alacsonyabban legyen a legmagasabb polc, amit hasznalunk (minimalisan kelljen nyujtozkodni).

A konyveinket 9 csoportba soroltunk: matek, info, sport, zene, egyebregeny, Tolkien, Feist, Harry Potter, diplomak. Az egyes csoportokat nem akarjuk megbontani, tehat egymas mellett kell lenniuk egy polcon. A polcok kozott annyi helynek kell lennie, hogy a legmagasabb konyv felett is maradjon meg 7cm. A polcok vastagsaga 2 cm, melysege 30 cm, es osszesen 7 lapot vettunk, legfeljebb ennyit tudunk felhasznalni.

A konyvcsoportok szelessege, es az abban foglalt konyvek magassagainak intervallumai a kovetkezok (cm-ben):

    matek           100         10-20
    info            80          10-25
    sport           30          15-30
    zene            50          20-30
    egyebregeny     40          15-20
    Tolkien         30          13-25
    Feist           50          9-20
    Harry Potter    90          12-25
    Diploma         70          40-40
*/

# Input data declaration

set BookSets;
param width{BookSets};
param height{BookSets};

param shelfCount;
set Shelves:=1..shelfCount;

param shelfWidth;
param shelfHeight;

param minDistance;
param minPosition;

param M:=500;


# Variables
var use{Shelves} binary; 
var position{Shelves} >= minPosition;
var put{BookSets,Shelves} binary;

var maxbookheight{Shelves}>=0;
var maxusedshelf;


# Constraints

# If a shelf is used all the shelves below it are used
s.t. ShelfUsage {s in Shelves : s!=1}:
  use[s] <= use[s-1];


# If a shelf is used, it should be higher then the one below it (maxbook + 7cm)

s.t. MaxBookHeightSetter{b in BookSets, s in Shelves}:
  maxbookheight[s] >= height[b] * put[b,s];
  
s.t. ShelfPositioning{s in Shelves: s!=1}:
  position[s] >= position[s-1]+maxbookheight[s-1]+shelfHeight+minDistance;


# Only put booksets on used shelves
# Only put as many booksets on shelves as they can hold

s.t. ShelfCapacity{s in Shelves}:
  sum{b in BookSets} put[b,s] * width[b] <= shelfWidth * use[s];

# Each booksets must be put on exactly one shelf
s.t. BookSetAssignment{b in BookSets}:
  sum{s in Shelves} put[b,s] = 1;

# Set max used shelf
s.t. MaxUsedShelf{s in Shelves}:
  maxusedshelf >= position[s] - M *(1 - use[s]);

# Objective function

minimize topShelfHeight: maxusedshelf;

# Display statements
solve;

for {s in Shelves : use[s]==1}
{
  printf "Shelf %d: %d cm\n",s,position[s];
  for{b in BookSets:put[b,s]==1}
  {
    printf"\t%s - %d\n",b,width[b];
  }
}

# Input data

data;

set BookSets := Math IT Sport Music Novel Tolkien Feist HarryPotter Diplom;

param :          width      height:=
    Math           100          20
    IT              80          25
    Sport           30          30
    Music           50          30
    Novel           40          20
    Tolkien         30          25
    Feist           50          20
    HarryPotter     90          25
    Diplom          70          40
;

param shelfCount := 7;

param shelfWidth := 120;
param shelfHeight := 2;

param minDistance := 7;
param minPosition := 50;

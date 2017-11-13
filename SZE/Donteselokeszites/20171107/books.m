set Booksets;
param maxheight{Booksets}; # cm
param totalwidth{Booksets}; # cm


param shelfcount; # cm
set Shelves:=1..shelfcount;
param shelfwidth; # cm
param shelfthickness; # cm
param lowestshelf; # cm
param offset; # cm

param M; # cm

var shelfposition{Shelves}>=0; # cm
var put{Booksets,Shelves}, binary;
var isused{Shelves}, binary;
var shelfheight{Shelves}>=0; # cm
var highestshelf>=0; # cm
var totalheight>=0; # cm (needed only for nice display)


# Each bookset is put on exactly one Shelf
s.t. BooksetShelfAssignment {b in Booksets}:
    sum{s in Shelves} put[b,s]=1;

# The total width of the booksets put on a shelf can not exceed its width, and none can be put on an unused shelf
s.t. Shelfcapacity{s in Shelves}:
    sum{b in Booksets} totalwidth[b]*put[b,s] <= shelfwidth * isused[s];

# Setting the maximum height for a shelf
s.t. MaxShelfHeight{s in Shelves, b in Booksets}:
    shelfheight[s] >= maxheight[b] * put[b,s];

# The position of the lowest shelf
s.t. FirtsShelf:
    shelfposition[1]=lowestshelf;
    
# If a shelf (not the first) is used, it should be at least as high as the previous + thickness+the heighest book + offset
s.t. ShelfDistances{s in Shelves: s!=1}:
    shelfposition[s]>=shelfposition[s-1]+shelfheight[s-1]+offset+shelfthickness - M * (1-isused[s]);

# If a shelf is not used, none of the followings can be used either
s.t. ShelfUsage{s in Shelves: s!=1}:
    isused[s]<=isused[s-1];

# The highest we must reach
s.t. HighestReach{s in Shelves}:
    highestshelf >= shelfposition[s] - M * (1-isused[s]);

# Total height (needed only for nice display)
s.t. Totalheight{s in Shelves}:
    totalheight >= shelfposition[s]+shelfthickness+shelfheight[s] - M * (1-isused[s]);

minimize Height: highestshelf;

solve;

printf "<svg width='%d' height='%d'>",shelfwidth+20,(totalheight-lowestshelf)+20;
for {s in Shelves : isused[s]==1}
{

printf "<rect x='%d' y='%d' width='%d' height='%d' style='fill:rgb(214, 119, 36)' />",10,10+totalheight-shelfposition[s]-shelfthickness,shelfwidth,shelfthickness;
 for {b in Booksets : put[b,s]==1}
 {
    
    printf "<rect  x='%d' y='%d' width='%d' height='%d'"
    ,10+sum{b2 in Booksets : b2<b && put[b2,s]}totalwidth[b2]
    ,10+totalheight-(shelfposition[s]+shelfthickness)-maxheight[b]
    ,totalwidth[b]
    ,maxheight[b]
    ;
    printf " style='fill:rgb(%d,%d,23);stroke:black;stroke-width:1' />"
    ,50+totalwidth[b]
    ,50+maxheight[b]*2
    ;

    printf "<text x='%d' y='%d' font-family='Verdana' font-size='6' fill='white'>%s</text>"    
    ,15+sum{b2 in Booksets : b2<b && put[b2,s]}totalwidth[b2]
    ,23+totalheight-(shelfposition[s]+shelfthickness)-maxheight[b]
    ,b
    ;
 }
 

}
printf "</svg>";



end;

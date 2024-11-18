param fireCount;
set Fires := 1..fireCount;
param x{Fires};
param y{Fires};
param planeCount;
param areaWidth;
param areaHeight;
set Planes := 1..planeCount;
param M := 1000; # TODO


var left{Planes};
var bottom{Planes};
var covers{Planes,Fires} binary;
var extinguished{Fires} binary;

s.t. Fire_is_not_extinguished_if_no_plane_covers_it{f in Fires}:
    extinguished[f] <= sum{p in Planes} covers[p,f];

s.t. If_p_covers_f_it_should_be_within_region_left{p in Planes, f in Fires}:
    x[f] >= left[p] - M * (1 - covers[p,f]);
s.t. If_p_covers_f_it_should_be_within_region_right{p in Planes, f in Fires}:
    x[f] <= left[p] + areaWidth + M * (1 - covers[p,f]);
s.t. If_p_covers_f_it_should_be_within_region_bottom{p in Planes, f in Fires}:
    y[f] >= bottom[p] - M * (1 - covers[p,f]);
s.t. If_p_covers_f_it_should_be_within_region_top{p in Planes, f in Fires}:
    y[f] <= bottom[p] + areaHeight + M * (1 - covers[p,f]);

maximize ExtinguishedFires:
    sum{f in Fires} extinguished[f];

solve;

param SCALE := 100;

printf "<svg height=""%d"" width=""%d"">", SCALE * max{f in Fires}y[f], SCALE * max{f in Fires}x[f];

printf "<rect width=""%d"" height=""%d"" x=""0"" y=""0"" fill=""white"" />", SCALE *  max{f in Fires}x[f], SCALE *  max{f in Fires}y[f];


for {p in Planes}
    printf "<rect width=""%d"" height=""%d"" x=""%d"" y=""%d"" fill=""blue"" />", SCALE * areaWidth, SCALE * areaHeight, SCALE * left[p], SCALE*bottom[p];

for {f in Fires}
    printf "<circle r=""%f"" cx=""%d"" cy=""%d"" fill=""%s"" />", SCALE * 0.2, SCALE*x[f], SCALE * y[f], if extinguished[f] then "green" else "red";


printf "</svg>";





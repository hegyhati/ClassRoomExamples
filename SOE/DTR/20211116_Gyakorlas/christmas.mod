

set Friends;
param budget{Friends};

set Items;
param price{Items};

param likes{Friends,Items} binary;

var give{Friends,Items,Friends} binary;

s.t. Budget1{giver in Friends, item in Items, receiver in Friends: price[item] > budget[giver]}:
    give[giver,item,receiver] = 0;

s.t. Budget2{giver in Friends, item in Items: price[item] > budget[giver]}:
    sum{receiver in Friends} give[giver,item,receiver] = 0;

s.t. No_self_present{friend in Friends, item in Items}:
    give[friend,item,friend] = 0;

# g[A,s,A] = 0
# g[A,h,A] = 0
# g[A,h,A] = 0
# g[A,w,A] = 0
# g[D,s,D] = 0
# g[D,h,D] = 0
# g[D,h,D] = 0
# g[D,w,D] = 0
# g[P,s,P] = 0
# g[P,h,P] = 0
# g[P,h,P] = 0
# g[P,w,P] = 0
# g[R,s,R] = 0
# g[R,h,R] = 0
# g[R,h,R] = 0
# g[R,w,R] = 0

s.t. No_self_present_2{friend in Friends}:
    sum{item in Items} give[friend,item,friend] = 0;

# g[A,s,A] + g[A,h,A] + g[A,h,A] + g[A,w,A] = 0
# g[D,s,D] + g[D,h,D] + g[D,h,D] + g[D,w,D] = 0
# g[P,s,P] + g[P,h,P] + g[P,h,P] + g[P,w,P] = 0
# g[R,s,R] + g[R,h,R] + g[R,h,R] + g[R,w,R] = 0

s.t. No_self_present_3:
    sum{friend in Friends, item in Items} give[friend,item,friend] = 0;

# g[A,s,A] + g[A,h,A] + g[A,h,A] + g[A,w,A] +
# g[D,s,D] + g[D,h,D] + g[D,h,D] + g[D,w,D] +
# g[P,s,P] + g[P,h,P] + g[P,h,P] + g[P,w,P] +
# g[R,s,R] + g[R,h,R] + g[R,h,R] + g[R,w,R] = 0


s.t. No_unliked_present_from_receiver{receiver in Friends, item in Items : likes[receiver,item] == 0}:
    sum{giver in Friends} give[giver,item,receiver] = 0;

s.t. No_unliked_present_from_giver{giver in Friends, item in Items : likes[giver,item] == 0}:
    sum{receiver in Friends} give[giver,item,receiver] = 0;

s.t. Present_for_everyone{receiver in Friends}:
    sum{giver in Friends, item in Items} give[giver,item,receiver] = 1;

s.t. Present_from_everyone{giver in Friends}:
    sum{receiver in Friends, item in Items} give[giver,item,receiver] = 1;

minimize Cost: 
    sum{giver in Friends, item in Items, receiver in Friends}
        give[giver,item,receiver] * price[item];

solve;


for{giver in Friends, item in Items, receiver in Friends: give[giver,item,receiver]==1}{
    printf "%s (%g) -- %s (%g) --> %s\n",giver,budget[giver],item,price[item],receiver;
}



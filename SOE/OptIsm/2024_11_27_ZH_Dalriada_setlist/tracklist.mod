set Musicians;
set Songs;
param duration{Songs}; # s
param popularity{Songs}; # - 
param difficulty{Songs,Musicians} binary; 

param setLength >= 1, integer, default 10; # s
param minDuration >= 0, default 3600; # s
param maxDuration >= minDuration, default 4800; # s
param breakDuration >= 0, default 30; #s
param max_difficult{Musicians}, default 2;

set Tracks := 1..setLength;

var play{Tracks,Songs} binary;

s.t. Exactly_one_song_is_played_for_each_track{t in Tracks}:
    sum{s in Songs} play[t,s] = 1;

s.t. Concert_duration_must_be_within_limits:
    minDuration 
    <=
    sum{t in Tracks, s in Songs} play[t,s] * duration[s]
    +
    (setLength - 1) * breakDuration
    <=
    maxDuration
    ;

s.t. Nobody_should_play_more_difficult_in_a_row_than_the_limit{m in Musicians, t in Tracks: t + max_difficult[m] <= setLength}:
    sum{tt in t..t+max_difficult[m], s in Songs} play[tt,s] * difficulty[s,m] <= max_difficult[m];


# was not a requirement
s.t. A_song_can_be_played_at_most_once{s in Songs}:
    sum{t in Tracks} play[t,s] <= 1;


maximize Total_Popularity: sum{t in Tracks, s in Songs} play[t,s] * popularity[s];

solve;

param start{t in Tracks} := sum{s in Songs, tt in 1..t-1} play[tt,s]*duration[s] + (t - 1) * breakDuration;

printf "Total popularity: %d\n\n", Total_Popularity;
for {t in Tracks}
{
    printf "%2d.: ", t;
    for {s in Songs: play[t,s] == 1} 

        printf "%2d:%02d-%2d:%02d\t%d\t%s\n", 
            start[t] div 60, start[t] mod 60,
            (duration[s] + start[t]) div 60, (duration[s] + start[t]) mod 60,
            popularity[s],
            s;
}
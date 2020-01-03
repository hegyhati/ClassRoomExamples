# Celunk egy tanterv idealis osszeallitasa.
# 
# Adott az osszes elvegzendo targy listaja, amit n felevbe kell beutemezni. 
# Minden targyhoz adott, hogy heti hany kontaktorat jelent, mennyi kreditet er, es hogy melyik masik targyakra epul.
# Egy felevben a kontaktorak szama 17 es 23 kozott, a kreditek szama 25 es 35 kozott kell, hogy legyen.
# A targyak elofelteteleit nyilvan be kell tartani, azonos felevben sem lehet felvenni, de 2-nel tobb felevet kihagyni sem lehet a ketto kozott.
# Minimalizalni az utolso ket felevben tanult orak szamat szeretnenk.
#
#
# 
# Plusz feladatok:
#  - minimalizalni szeretnenk a "felelevenitesbe olt munkat", amit a kovetkezokeppen szamolunk ki: Ha egy A targy epul B targyra, es A a B-t koveto felevbe van beosztva, akkor nincs ilyen munka. Ha a ketto targy kozott van 1 felev kihagyas, akkor 5-szor annyi orat kell felelevenitessel foglalkozni, mint amenyi kreditet B er. Ha ket felev van kozottuk, akkor a szorzo nem 5 hanem 8.  Megj: ne foglalkozzunk azzal, hogy egy felevben lehet tobb targy is epul ugyanarra a targyra, igy eleg csak egyszer feleleveniteni. 
#  - Ha tobb targy is epul a felevben B-re, csak 1x kell feleleveniteni.
#  - Ha ket felev kihagyas van, de elozo felevben is felelevenitettuk B-t, akkor nem 8, hanem ugyanugy 5 a szorzo
#  - A felelevenitesek idotartamara is adott egy idokorlat minden felevre: 70
#  - Nemcsak kotelezo targyak vannak, hanem nehany blokk, amikbol adott, hogy legalabb hany kreditet kell teljesiteni. Ezekre a blokkokra is adott, hogy melyik targyakra epulnek, illetve ugy lehet szamolni, hogy a 2/3-ad annyi oraterhelest jelentenek, amennyi a kreditek szama. Az ilyen blokkok feldarabolhatok felevek kozott, de a blokkok legalabb 2 ora / 3 kredit meretuek kell, hogy legyenek.

set Courses;
param credits{Courses};
param hours{Courses};
param depends {Courses,Courses}, default 0;

param nSemester>=2;
set Semesters:= 1..nSemester;
param minhour;
param maxhour;
param mincredit;
param maxcredit;


var schedule{Semesters,Courses},binary;

s.t. EachCourseOnce{c in Courses}:
  sum{s in Semesters} schedule[s,c]=1;

s.t. SatisfySemesterCreditLimitations{s in Semesters}:
  mincredit <= sum{c in Courses} schedule[s,c]*credits[c] <= maxcredit;

s.t. SatisfySemesterHourLimitations{s in Semesters}:
  minhour <= sum{c in Courses} schedule[s,c]*hours[c] <= maxhour;

s.t. DontMakeDependentEarlier{c1 in Courses, c2 in Courses, s1 in Semesters, s2 in Semesters:depends[c2,c1]==1 && s2 <= s1}:
  schedule[s1,c1]+schedule[s2,c2] <= 1;

s.t. DontStudyMuchEarlier{c1 in Courses, c2 in Courses, s1 in Semesters, s2 in Semesters:depends[c2,c1]==1 && s2 > s1+3}:
  schedule[s1,c1]+schedule[s2,c2] <= 1;

minimize LatTwoSemesterHours:
  sum{c in Courses, s in Semesters:s>nSemester-2} schedule[s,c]*hours[c]; 

solve;

for {s in Semesters}
{
  printf "Semester %d:\tHOURS:%3d\tCREDITS:%3d\n",s,sum{c in Courses}schedule[s,c]*hours[c],sum{c in Courses}schedule[s,c]*credits[c];
  for{c in Courses: schedule[s,c]==1}
  {
    printf " - %s\t%3d\t%3d\n",c,hours[c],credits[c];
  }
}

data;

set Courses := A B C D E F G;

param:
          credits   hours :=
      A   10        6
      B   8         5
      C   9         6
      D   15        10
      E   13        9
      F   13        11
      G   15        11
      ;

param minhour := 17;
param maxhour := 23;
param mincredit := 25;
param maxcredit := 35;

param depends:
            A   B   C   D   E   F   G := 
        D   1   1   .   .   .   .   .
        E   .   .   1   .   .   .   .
        F   .   .   .   1   .   .   .
        G   1   .   .   .   1   .   .
        ;

param nSemester := 3;


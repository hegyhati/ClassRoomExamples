########################################################################
# Input data ###########################################################
########################################################################
set Figures;
param citeLine{Figures}; # line id
param height{Figures}; # in lines

param pageSize; # in lines
param maxEmptyLine; # in lines

# Just bigM
param M:=1000;

########################################################################
# Derived sets and parameters### #######################################
########################################################################

# the total number of text lines to print, by default, the last citation
param totalLines, default max{f in Figures} citeLine[f];

# an upper bound on the number of pages. 
param maxPages integer := ceil((totalLines + sum{f in Figures} height[f])/(pageSize-maxEmptyLine));

set Pages := 1..maxPages;

########################################################################
# Variables ############################################################
########################################################################

var place{Figures,Pages} binary; # The figure is placed on a page or not
var lineCount{Pages} >=0 integer; # The number of written lines on a page

########################################################################
# Derived variables ####################################################
########################################################################

var cite{Figures,Pages} binary; # 1 if the citation of a figure appears on a page 
var citePage{Figures} >=0 integer; # The page on which the citation for the figure is
var placePage{Figures} >=0 integer; # The page on which the figure is placed
var use{Pages} binary; # 1 if the page is not empty


########################################################################
# Constraints###########################################################
########################################################################

# A figure can be placed exactly on one page
s.t. FigurePlacement{f in Figures}:
  sum{p in Pages} place[f,p]=1;

# All of the lines must be printed
s.t. TotalLines:
  sum{p in Pages} lineCount[p] = totalLines;

# If a page is used, the page before that must be used as well.
# The other way around: the pages after an unused page are all unused.
s.t. PageUsage{p in Pages:p>1}:
  use[p]<=use[p-1];


# If a page is unused, no text can be written on it
# And also, no figures.
# If it is used, those above must take at most pageSize space

s.t. PageContentSizeLimit{p in Pages}:
  lineCount[p] + sum{f in Figures} height[f]*place[f,p]<= 0 + pageSize * use[p];

# If a page is used, then the number of empty lines can not exceed the given limit
# An exception is the last page, that is used, as it may will not be filled completely

s.t. EmptyLinesLimit{p in Pages : p < maxPages}:
  lineCount[p] + sum{f in Figures} height[f]*place[f,p] >= pageSize - maxEmptyLine - pageSize * (1- use[p+1]);


# Setting cite based on lineCount 
# The first line on page p is 1+sum{pp in 1..p-1}lineCount[pp]
# and the last is sum{pp in 1..p}lineCount[pp]
# Citations for figure f is on page p, i.e., cite[f,p]==1 iff citeLine[f] is between those values

s.t. SET_cite_1{f in Figures, p in Pages}:
  citeLine[f] <= sum{pp in 1..p} lineCount[pp] + M * (1-cite[f,p]);
s.t. SET_cite_2{f in Figures, p in Pages}:
  citeLine[f] >= 1+sum{pp in 1..p-1} lineCount[pp] - M * (1-cite[f,p]);

# Also, exactly one cite[f,p] has to be 1 for each figure

s.t. SET_cite_3{f in Figures}:
  sum{p in Pages} cite[f,p]=1;

# Setting citePage based on cite
# cite[f,p] is only 1 for a single page for a given f
# p*cite[f,p] is 0 if f is not on that page, and p if it is.

s.t. SET_citePage{f in Figures}:
  citePage[f] = sum{p in Pages} p*cite[f,p];

# Similarly, for placePage

s.t. SET_placePage{f in Figures}:
  placePage[f] = sum{p in Pages} p*place[f,p];


# A figure must be placed earliest on the page where it is cited

s.t. CitePlaceRelation{f in Figures}:
  citePage[f] <= placePage[f];

# A figure can not be placed on an earlier page, if it is cited later

s.t. FigureOrder{f1 in Figures, f2 in Figures: citeLine[f1]<citeLine[f2]}:
  placePage[f1]<=placePage[f2];

########################################################################
# Objective ############################################################
########################################################################


# for figure f, we have to turn placePage[f]-citePage[f] times to see it
minimize TotalPageTurns: sum{f in Figures} (placePage[f]-citePage[f]);

########################################################################
# Output ###############################################################
########################################################################

solve;

printf "\n\n";

for{p in Pages : use[p]=1}
{
  printf "Page %2d:\n",p;
  printf "+---------------------+\n";
  for{l in 1..lineCount[p]}
  {
    printf "| ~~~~~~~Text line %2d |",l+sum{pp in 1..p-1}lineCount[pp];
    for{f in Figures: citeLine[f]=l+sum{pp in 1..p-1}lineCount[pp]}
      printf " ->[%s]",f;
    printf "\n";
  }
  for{f in Figures : placePage[f]=p}
  {
    printf "|   \# %-8s\#\#\#\#\#   |\n",f;
    for{h in 2..height[f]}
      printf "|   \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#   |\n",f;
  }
  for{empty in lineCount[p] + sum{f in Figures} height[f]*place[f,p]+1..pageSize}
    printf "|                     |\n";
  printf "+---------------------+\n\n";

}

/*
Készítsen programot, ami lehetővé teszi két játékos számára, hogy amőba játékot játsszon! A pálya 10 sorból és 10 oszlopból áll. Jelenítse meg a pályát úgy, hogy a sorokat 1-től kezdve számozza, az oszlopokat betűkkel jelöli (lásd a példát)! Az első játékos lépéseit X, a másodikét O jelöli a pályán, az üres mezőket jelölje . karakterrel!
Ezután felváltva olvassa be a játékosok lépéseit (először a sort, aztán az oszlopot külön), és jelenítse meg újra a táblát, ami tartalmazza a játékosok eddigi lépéseit, beleértve az imént megadottat is!
Hibás lépés (a táblán kívülre mutató, vagy már foglalt mező) esetén ismételtesse az adatbevitelt! A játéknak akkor van vége, ha valamelyik játékos függőlegesen, vízszintesen vagy átlós irányban képes volt pontosan 5 mezőt elfoglalni, vagy betelt a tábla (ebben az esetben a játék döntetlennel végződik). Példa:

Amoba jatek
  ABCDEFGHIJ
01..........
02..........
03..........
04..........
05..........
06..........
07..........
08..........
09..........
10..........
Elso jatekos lepese, sor: 3
Oszlop: F
  ABCDEFGHIJ
01..........
02..........
03.....X....
04..........
05..........
06..........
07..........
08..........
09..........
10..........
Masodik jatekos lepese, sor: …

Értékelés: Az alapfeladat megoldása 2 pont. Plusz illetve mínusz pont adandó a következőkért:
–1:	Ha a hibás lépéseket nem kezeli a program az előírtnak megfelelően.
–1:	Ha a program fordítása során egyetlen, szabvány fejfájlok be nem kapcsolásából (#include) adódó, figyelmeztető üzenet is akad.
–1:	Ha az alapprogram működése bármiben is eltér a feladatban megfogalmazottól.
+1:	Ha a pálya mérete is megadható, mielőtt a tényleges játék elkezdődne. A sorok és oszlopok számának a [7, 20] intervallumba kell esnie.
+1:	Egészítse ki azzal a játékot azzal, hogy a program minden lépés után automatikusan elmenti a játék állását az amoba.txt fájlba. Mentendő a pálya mérete és a játékosok eddigi lépései.
+1:	Amennyiben a programot a betolt parancssori paraméterrel indítják, töltse be a korábban kimentett játékállást, és folytassa onnan a játékot a program! Ellenőrizendő a fájl megléte, de feltételezheti, hogy a fájl szerkezete helyes.

 */



#include<iostream>
#include<string>
#include<iomanip>
#include<fstream>
using namespace std;

#define WIN 3

enum field {player1, player2, empty};

struct GameState{
    int rowCount;
    int columnCount;
    field ** table;
    field next;
};

void initialize(struct GameState & game){
    game.next=player1;
    game.table = new field * [game.rowCount];
    for(int r=0; r<game.rowCount; r++) {
        game.table[r]=new field[game.columnCount];
        for(int c=0;c<game.columnCount;c++)
            game.table[r][c]=empty;
    }
}

void destruct(struct GameState & game){
    for(int r=0; r<game.rowCount; r++)
        delete [] game.table[r];
    delete game.table;    
}

string statetostring(field f){
    switch(f){
        case player1: return "X"; break;
        case player2: return "O"; break;
        case empty:   return "."; break;
        default: return "-";
    }
}

field stringtostate(string s){
    if(s=="X") return player1;
    else if (s=="O") return player2;
    else return empty;
}

void print(struct GameState & game){
    cout<<game.rowCount<<" X "<<game.columnCount<<endl<<endl;
    cout<<"  ";
    for(int c=0;c<game.columnCount;c++)
        cout<< char('A'+c);
    cout<<endl;
    for(int r=0; r<game.rowCount; r++) {
        cout<<setw(2)<<r+1;
        for(int c=0;c<game.columnCount;c++) {
            cout<<statetostring(game.table[r][c]);
        }
        cout<<endl;
    }
}

bool winner(struct GameState & game){
    bool win;
    for(int r=0; r<game.rowCount; r++) {
        for(int c=0;c<game.columnCount-WIN;c++) {
            if(game.table[r][c]!=empty){
                win=true;
                for(int c2=c+1; c2<c+WIN; c2++)
                    if(game.table[r][c2]!=game.table[r][c]) win = false;
                if (win) return true;
            }
        }
    }

    for(int r=0; r<game.rowCount-WIN; r++) {
        for(int c=0;c<game.columnCount;c++) {
            if(game.table[r][c]!=empty){
                win=true;
                for(int r2=r+1; r2<r+WIN; r2++)
                    if(game.table[r2][c]!=game.table[r][c]) win = false;
                if (win) return true;
            }
        }
    }

    for(int r=0; r<game.rowCount-WIN; r++) {
        for(int c=0;c<game.columnCount-WIN;c++) {
            if(game.table[r][c]!=empty){
                win=true;
                for(int d=1; d<WIN; d++)
                    if(game.table[r+d][c+d]!=game.table[r][c]) win = false;
                if (win) return true;
            }
        }
    }

    for(int r=WIN-1; r<game.rowCount; r++) {
        for(int c=0;c<game.columnCount-WIN;c++) {
            if(game.table[r][c]!=empty){
                win=true;
                for(int d=1; d<WIN; d++)
                    if(game.table[r-d][c+d]!=game.table[r][c]) win = false;
                if (win) return true;
            }
        }
    }
    return false;    
}

bool goodnextstep(struct GameState & game, char column, int row){
    if (column < 'A' || column > 'A'+game.columnCount-1) return false;
    if (row < 1 || row > game.rowCount) return false;
    if (game.table[row-1][column-'A']!=empty) return false;
    return true;
}

void makenextstep(struct GameState & game, char  column, int row){
    game.table[row-1][column-'A']=game.next;
    game.next = (game.next==player1) ? player2 :player1;
}

void savegame(struct GameState & game, string filename) {
    ofstream s;
    s.open(filename.c_str());
    s<<game.rowCount<<endl;
    s<<game.columnCount<<endl;
    s<<statetostring(game.next)<<endl;

    for(int r=0; r<game.rowCount; r++) {
        for(int c=0;c<game.columnCount;c++) {
            s<<statetostring(game.table[r][c])<<" ";
        }
        s<<endl;
    }
    
    s.close();
}

void initializefromfile(struct GameState & game, char * filename){
    cout<<"Loading game from file: "<<filename<<endl;
    ifstream s;
    s.open(filename);

    string temp;
    s>>game.rowCount;
    s>>game.columnCount;
    
    game.table = new field * [game.rowCount];
    for(int r=0; r<game.rowCount; r++) {
        game.table[r]=new field[game.columnCount];
    }
    
    
    s>>temp;
    game.next=stringtostate(temp);
    for(int r=0; r<game.rowCount; r++) {
        for(int c=0;c<game.columnCount;c++) {
            s>>temp;
            game.table[r][c]=stringtostate(temp);
        }
    }
    
    s.close();
}

int main(int argc, char** argv){

    struct GameState game;
    if(argc==1) {
        cin >> game.rowCount >> game.columnCount;    
        initialize(game);
    } else {
        initializefromfile(game,argv[1]);
    }
    
    print(game);

    char column;
    int row;
    while(!winner(game)){
        do {
            cin >> column >> row;
        } while (! goodnextstep (game,column,row));
        makenextstep(game,column,row);
        savegame(game,"amoba.txt");
        print(game);            
    }

    if(game.next==player1) { cout<< "Player 2";}
    else {cout<<"Player 1";}
    cout<<" has won the game\n";


    destruct(game);


    return 0;
}


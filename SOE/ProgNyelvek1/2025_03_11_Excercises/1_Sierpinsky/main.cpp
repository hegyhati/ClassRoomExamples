/*
    Irj egy Sierpinsky fuggvenyt, ami megadott melysegben kirajzolja a Sierpinsky haromszoget.
    (Ez alatt most az ertendo, hogy a Pascal haromszoget n melysegig, es akkor annak paritasa alapjan # vagy szokoz.)
    A main-ben pedig beolvas egy egesz szamot, es olyan meglysegben rajzol ki.
*/


#include <iostream>

void drawSierpinsky(int depth) {
    bool * line = new bool[depth+1];
    for (int row = 0; row<=depth ; ++row) {
        for (int i = 0; i<depth-row; ++i) 
            std::cout << " ";
        line[row] = true;
        for (int i = row-1; i > 0; --i) 
            line[i] = (line[i] != line[i-1]); 
        for(int i = 0; i<= row ; ++i ){
            std::cout << (line[i]?"XX":"  ");
        } 
        std::cout << "\n";
    }    
    delete [] line;
}


int main(){
    int n;
    std::cin >> n;
    drawSierpinsky(n);
    return 0;
}
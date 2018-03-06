#include "tester.hpp"

int Tester::defaultmaxd=INITIAL_DEFAULTMAXD;

void Tester::setDefaultMaxD(int newmaxd) {
    if(newmaxd>=1) Tester::defaultmaxd=newmaxd;
}

Tester::Tester(int width, int height, int maxd)
    :  maxd(maxd), width(width), height(height), steps(NULL){
    x=y=0;
    steps = new struct Step;
    steps->dx=0;
    steps->dy=0;
    steps->next=NULL;
}

Tester::~Tester(){
    struct Step * tmp = steps;
    struct Step * tmpnext;
    do {
        tmpnext=tmp->next;
        delete tmp;
        tmp=tmpnext;
    } while (tmp!=NULL); 
}

void Tester::print() const {
    cout<<"x: "<<x<<", y: "<<y<<"\n";
    
    for(struct Step * tmp = steps; tmp!=NULL;tmp=tmp->next)
        cout<<"\tdx: "<<tmp->dx<<", dy: "<<tmp->dy<<"\n";
        
}

void Tester::fancyPrint() const {
    bool **field = new bool*[width];
    for(int w=0; w<width; w++){
        field[w]=new bool [height];
        for(int h=0; h<height;h++)
            field[w][h]=false;
    }
    field[0][0]=true;
    int x=0;
    int y=0;
    for(struct Step* tmp=steps; tmp!=NULL; tmp=tmp->next){
        x+=tmp->dx;
        y+=tmp->dy;
        field[x][y]=true;
    }
    for(int h=0; h<height;h++) {
        for(int w=0; w<width; w++)        
            cout << (field[w][h] ? "<>": "..");
        cout<<"\n";
    }
    for(int w=0; w<width; w++)
        delete [] field[w];
    delete [] field;

}

bool Tester::isFinished() const {
    return x==(width-1) && y==(height-1);
}

bool Tester::isGameOver() const {
    if(isFinished()) return false;
    for(int dx=getLastStep()->dx-defaultmaxd; dx <= getLastStep()->dx+defaultmaxd;dx++)
        for(int dy=getLastStep()->dy-defaultmaxd; dy <= getLastStep()->dy+defaultmaxd;dy++)
        if(isCorrectNextStep(dx,dy)) return false;
    return true;
}

struct Step * Tester::getLastStep() const{
    struct Step * tmp=steps;         
    while (tmp->next!=NULL) tmp=tmp->next;
    return tmp;
}

bool Tester::isCorrectNextStep(int dx, int dy) const {
    int newx=x+dx;
    int newy=y+dy;
    if (newx<0 || newx >= width || newy < 0 || newy >= height) return false;
    else {
        struct Step * last = getLastStep();
        return !(dx<last->dx-maxd || dx > last->dx+maxd || dy<last->dy-maxd || dy > last->dy+maxd );
    }
}

bool Tester::move(int dx, int dy) {
    if (!isCorrectNextStep(dx,dy)) return false;
    else {
        x+=dx;
        y+=dy;
        struct Step * newstep = new struct Step;
        newstep->dx=dx;
        newstep->dy=dy;
        newstep->next=NULL;
        struct Step * last = getLastStep();
        last->next=newstep;
        return true;
    }
}

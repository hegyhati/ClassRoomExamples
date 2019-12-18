/* Készítsen programot, mely két egyszerű szövegművelet (adott szöveg beszúrása adott helyre, adott kerakterszám utáni levágás) alkalmazását teszi lehetővé úgy, hogy lehetőséget ad visszavonásra (undo), és újraalkalmazásra (redo). */

#include <iostream>
#include <stack>
#include <string>


/* Készítsen egy StringOperation osztályt, mely interfészként fog szolgálni a két művelethez. 
A belőle származtatott osztályoknak egy DO és egy UNDO nevezetű függvényt kell támogatniuk, ami paraméterként kapja meg a szöveget, amin végre kell hajtani a műveletet.
A függvények igazzal térjenek vissza, ha a művelet sikeres volt, és hamissal, ha nem. 
Egyik esetben sem elvárt, hogy a szöveg változatlan maradjon, ha nem sikerül a művelet. */


class StringHandler;
class StringOperation {
    friend class StringHandler;
  protected:
    virtual bool DO(std::string&) =0;
    virtual bool UNDO(std::string&) =0;
  public:
    virtual ~StringOperation(){}
};

/* Implementáljon StringInsertion néven egy olyan műveletet, mely adott pozícióra szúr be egy megadott szöveget, amikor DO hívódik meg, és UNDO-ra értelemszerűen kitörli azt.
A beszúrás nem sikerül, ha nem elég hosszú a szöveg.
A kitörlés nem sikerül, ha a megadott pozíción nem a beszúrt szöveg található. */

class StringInsertion : public StringOperation {
  public:
    StringInsertion(size_t position, const std::string& newtext)
      : position(position),newtext(newtext) {}

  protected:
    virtual bool DO(std::string& text) override {
      try {
        text.insert(position,newtext);
        return true;
      } catch (const std::out_of_range& oor) {
        return false;
      }
    }
    virtual bool UNDO(std::string& text) override {
      if(newtext.compare(text.substr(position,newtext.length())) != 0) return false;
      else {
        text.erase(position,newtext.length());
        return true;
      }
    }

  private:
    const size_t position;
    const std::string newtext;
};

/* Implementáljon StringCrop néven egy olyan műveletet, mely adott karakterszám után levágja a maradékot DO meghívására, illetve visszailleszti azt UNDO esetén.
A levágás nem sikerül, ha nem elég hosszú a szöveg.
A visszailletsztés nem sikerül, ha nem pontosan olyan hosszú a szöveg, mint amekkorára vágtuk. */

class StringCrop : public StringOperation {
  public:
    StringCrop(size_t newsize) : size(newsize),croppedtext("") {}
  
  protected:
    virtual bool DO(std::string& text) override {
      if(text.length()<size) return false;
      else {
        croppedtext = text.substr(size);
        text.erase(size);
        return true;
      }
    }

    virtual bool UNDO(std::string& text) override {
      if(text.length()==size) {
        text.append(croppedtext);
        return true;
      } else return false;
    }
  
  private:
    const size_t size;
    std::string croppedtext;
};

/* Készítsen egy StringHandler osztályt, mely megvalósítja a fenti műveletek alkalmazását egy szövegen.
Az apply függvénynek egy művelet címét lehessen átadni, hajtsa végre a műveletet, és siker esetén tárolja el a címet későbbi visszavonáshoz és a memória felszabadításához. 
Az undo függvény a legutoljára végrehajtott műveletet csinálja vissza, és ha sikeres, akkor tárolja el újraalkalmazás céljából. Ha nem, akkor törölje az összes visszavonásra szánt műveletet.
A redo függvény a legutoljára visszavont műveletet csinálja újra, és ha sikeres, akkor tárolja el visszavonás céljából. Ha nem, akkor törölje az összes újra végrehajtásra szánt műveletet.
Ezeket a műveleteket törölje akkor is, ha sikeres volt egy művelet végrehajtása az operate függvénnyel.
Ha a három függvény bármelyike sikertelen, akkor a tárolt szöveg maradjon változatlan.
A redo és undo akkor is térjen vissza hamissal, ha nincs visszavonandó / újra végrehajtandó művelet.
A << operátorral lehessen a szöveg aktuális tartalmát kiíratni egy kimeneti folyamra.
Amikor egy StringHandler objektumot lemásolunk, akkor azonos aktuális szöveggel, de mindenféle művelet-történet nélkül készüljön másolat. */

class StringHandler {
  public:
    StringHandler(const std::string& initial):current(initial){}
    StringHandler(const StringHandler& other):current(other.current){}
    ~StringHandler(){
      eraseOperations(undoOperations);
      eraseOperations(redoOperations);
    }

    bool apply(StringOperation* operation){
      const std::string snapshot=current;
      if(operation->DO(current)){
        eraseOperations(redoOperations);
        undoOperations.push(operation);
        return true;
      } else {
        current=snapshot;
        return false;
      }
    }

    bool undo() {
      if (undoOperations.empty()) return false;
      else {
        const std::string snapshot = current;
        if(!undoOperations.top()->UNDO(current)){
          current=snapshot;
          eraseOperations(undoOperations);
          return false;
        } else {
          redoOperations.push(undoOperations.top());
          undoOperations.pop();
          return true;
        }
      }
    } 

    bool redo() {
      if (redoOperations.empty()) return false;
      else {
        const std::string snapshot = current;
        if(!redoOperations.top()->DO(current)){
          current=snapshot;
          eraseOperations(redoOperations);
          return false;
        } else {
          undoOperations.push(redoOperations.top());
          redoOperations.pop();
          return true;
        }
      }
    } 

  friend std::ostream& operator << (std::ostream& s, const StringHandler& text) {
    s << "\033[1;7m"<< text.current << "\033[0m";
    return s;
  }

  private:
    std::string current;
    std::stack<StringOperation*> undoOperations;
    std::stack<StringOperation*> redoOperations;

    void eraseOperations(std::stack<StringOperation*>& operationstack){
      while(!operationstack.empty()){
        delete operationstack.top();
        operationstack.pop();
      }
    }
};

/* Az elkészített programnak az alábbiakban megadott main függvénnyel (annak bármilyen módosítása nélkül) le kell fordulnia, helyesen működnie, és nem szabad, hogy a memóriába szemeteljen. 
Az osztályokat külön fájlokban deklarálja, definiálja, valamint igyekezzen a különböző "jogosultságokat" a logikusan legszigorúbbra állítani. */


int main(){
  std::cout << "Start with apple: ";
  StringHandler test("apple");
  std::cout << test << std::endl;


  std::cout << "Insert \"pine\" to position 0 (front): ";
  test.apply(new StringInsertion(0,"pine"));
  std::cout << test << std::endl;

  std::cout<<"Undo: ";
  test.undo();
  std::cout << test << std::endl;

  std::cout<<"Insert \"pen\" to position 5 (end): ";
  test.apply(new StringInsertion(5,"pen"));
  std::cout << test << std::endl;

  std::cout << "Insert \"pine\" to position 0 (front): ";
  test.apply(new StringInsertion(0,"pine"));
  std::cout << test << std::endl;

  std::cout << "Crop string after 9 characters: ";
  test.apply(new StringCrop(9));
  std::cout << test << std::endl;

  std::cout<<std::endl<<"Undo until possible: "<<std::endl;
  while (test.undo()) std::cout << test << std::endl;

  std::cout<<std::endl<<"Redo until possible: "<<std::endl;
  while (test.redo()) std::cout << test << std::endl;

  std::cout<<std::endl<<"Undo until possible: "<<std::endl;
  while (test.undo()) std::cout << test << std::endl;

  std::cout << std::endl << "Crop string after 1 character: ";
  test.apply(new StringCrop(1));
  std::cout << test << std::endl;

  std::cout<<std::endl<<"Redo until possible: "<<std::endl;
  while (test.redo()) std::cout << test << std::endl;

  std::cout<<std::endl<<"Undo until possible: "<<std::endl;
  while (test.undo()) std::cout << test << std::endl;

  std::cout<<std::endl<<"Redo until possible: "<<std::endl;
  while (test.redo()) std::cout << test << std::endl;

  return 0;
}

/* A fenti main futtatása után az elvárt kimenet:

-------------------------------------------------
Start with apple: apple
Insert "pine" to position 0 (front): pineapple
Undo: apple
Insert "pen" to position 5 (end): applepen
Insert "pine" to position 0 (front): pineapplepen
Chop string after 9 characters: pineapple

Undo until possible: 
pineapplepen
applepen
apple

Redo until possible: 
applepen
pineapplepen
pineapple

Undo until possible: 
pineapplepen
applepen
apple

Chop string after 1 character: a

Redo until possible: 

Undo until possible: 
apple

Redo until possible: 
a
-------------------------------------------------

*/

/* Készítsen programot, mely két egyszerű szövegművelet (adott szöveg beszúrása adott helyre, adott kerakterszám utáni levágás) alkalmazását teszi lehetővé úgy, hogy lehetőséget ad visszavonásra (undo)*/

#include <iostream>
#include <stack>
#include <string>


/* Használja az alábbi StringOperation osztályt, mely interfészként fog szolgálni a két művelethez. 
A belőle származtatott osztályoknak egy DO és egy UNDO nevezetű függvényt kell támogatniuk, ami paraméterként kapja meg a szöveget, amin végre kell hajtani a műveletet.
Minden esetben feltételezhető, hogy a műveletet végrehajtása / visszavonása sikeresen végbe tud menni. */


class StringHandler;
class StringOperation {
    friend class StringHandler;
  protected:
    virtual void DO(std::string&) =0;
    virtual void UNDO(std::string&) =0;
  public:
    virtual ~StringOperation(){}
};

/* Implementáljon StringInsertion néven egy olyan műveletet, mely adott pozícióra szúr be egy megadott szöveget, amikor DO hívódik meg, és UNDO-ra értelemszerűen kitörli azt. 
Feltételezhető, hogy kellően hosszú a szöveg. */

class StringInsertion : public StringOperation {
  public:
    StringInsertion(size_t position, const std::string& newtext)
      : position(position),newtext(newtext) {}

  protected:
    virtual void DO(std::string& text) override {
      text.insert(position,newtext);
    }
    virtual void UNDO(std::string& text) override {
      text.erase(position,newtext.length());
    }

  private:
    const size_t position;
    const std::string newtext;
};

/* Implementáljon StringCrop néven egy olyan műveletet, mely adott karakterszám után levágja a maradékot DO meghívására, illetve visszailleszti azt UNDO esetén.
Feltételezhető, hogy elegendően hosszú a szöveg a levágáshoz */

class StringCrop : public  StringOperation {
  public:
    StringCrop(size_t newsize) : size(newsize),croppedtext("") {}
  
  protected:
    virtual void DO(std::string& text) override {
      croppedtext = text.substr(size);
      text.erase(size);
    }

    virtual void UNDO(std::string& text) override {
      text.append(croppedtext);
    }
  
  private:
    const size_t size;
    std::string croppedtext;
};

/* Készítsen egy StringHandler osztályt, mely megvalósítja a fenti műveletek alkalmazását egy szövegen.
Az apply függvénynek egy művelet címét lehessen átadni, hajtsa végre a műveletet, és tárolja el a címet későbbi visszavonáshoz és a memória felszabadításához. 
Az undo függvény a legutoljára végrehajtott műveletet csinálja vissza, és térjen vissza false-szal, ha már nincs ilyen művelet.
A << operátorral lehessen a szöveg aktuális tartalmát kiíratni egy kimeneti folyamra.
Amikor egy StringHandler objektumot lemásolunk, akkor azonos aktuális szöveggel, de mindenféle művelet-történet nélkül készüljön másolat. */

class StringHandler {
  public:
    StringHandler(const std::string& initial):current(initial){}
    StringHandler(const StringHandler& other):current(other.current){}
    ~StringHandler(){
      while(!undoOperations.empty()){
        delete undoOperations.top();
        undoOperations.pop();
      }
    }

    void apply(StringOperation* operation){
      operation->DO(current);
      undoOperations.push(operation);
    }

    bool undo() {
      if (undoOperations.empty()) return false;
      else {
        undoOperations.top()->UNDO(current);
        undoOperations.pop();
        return true;
      }
    } 

  friend std::ostream& operator << (std::ostream& s, const StringHandler& text) {
    s << "\033[1;7m"<< text.current << "\033[0m";
    return s;
  }

  private:
    std::string current;
    std::stack<StringOperation*> undoOperations;
};

/* Az elkészített programnak az alábbiakban megadott main függvénnyel (annak bármilyen módosítása nélkül) le kell fordulnia, helyesen működnie, és nem szabad, hogy a memóriába szemeteljen. 
Az osztályokat külön fájlokban deklarálja, definiálja, valamint igyekezzen a különböző "jogosultságokat" a logikusan legszigorúbbra állítani. */


int main(){
  std::cout << "Start with apple: ";
  StringHandler test("apple");
  std::cout << test << std::endl;


  std::cout << "Insert \"peach\" to position 0 (front): ";
  test.apply(new StringInsertion(0,"peach"));
  std::cout << test << std::endl;

  std::cout<<"Undo: ";
  test.undo();
  std::cout << test << std::endl;

  std::cout<<"Insert \"pentagon\" to position 5 (end): ";
  test.apply(new StringInsertion(5,"pentagon"));
  std::cout << test << std::endl;

  std::cout << "Insert \"alpine\" to position 0 (front): ";
  test.apply(new StringInsertion(0,"alpine"));
  std::cout << test << std::endl;

  std::cout << "Crop string after 14 characters: ";
  test.apply(new StringCrop(14));
  std::cout << test << std::endl;

  std::cout << "Insert \"l time best hit: \" to position 2 (front): ";
  test.apply(new StringInsertion(2,"l time best hit: "));
  std::cout << test << std::endl;

  std::cout<<std::endl<<"Undo until possible: "<<std::endl;
  while (test.undo()) std::cout << test << std::endl;

  return 0;
}

/* A fenti main futtatása után az elvárt kimenet:

-------------------------------------------------
Start with apple: apple
Insert "peach" to position 0 (front): peachapple
Undo: apple
Insert "pentagon" to position 5 (end): applepentagon
Insert "alpine" to position 0 (front): alpineapplepentagon
Crop string after 14 characters: alpineapplepen
Insert "l time best hit: " to position 2 (front): all time best hit: pineapplepen

Undo until possible: 
alpineapplepen
alpineapplepentagon
applepentagon
apple
-------------------------------------------------

*/

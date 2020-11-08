#include <iostream>
#include <string>
using namespace std;

#include "Warrior.hpp"
#include "Battle.hpp"
#include "FileNotFoundException.hpp"


int main(int argc, char** argv){
  try {
    Warrior warrior1 = Warrior::parseFromFile("Blue", argv[1],Sword(10,3));
    Warrior warrior2 = Warrior::parseFromFile("Red", argv[2]);
    figthTilDeath(warrior1,warrior2);
    cout << Warrior::getAliveWarriorCount() << " warriors are still alive." << endl;
  } catch (FileNotFoundException exception) {
    cout << "Bad filename: "<<exception.filename<<endl;
    return 1;
  } catch (Warrior::BadFileFormatException exception){
    cout << "Bad file structure: "<<exception.filename<<endl;
    return 2;
  }
  return 0;
}

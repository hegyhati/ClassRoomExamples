#include <iostream>
#include <string>
#include <vector>
using namespace std;

class JSON_Serializable {
    virtual string toJSON() const =0;
};


class Student : public JSON_Serializable{
public:
    virtual void sayHi() const {
        cout << "Szia!" << endl;
    }
    virtual string toJSON() const {
        return "Student";
    }
};

class SOE_Student : public Student {
    string role;
public:
    SOE_Student() : role("pogany") {}
    
    virtual void sayHi() const override {
        cout << "Jo szerencset! " << getRole() << " vagyok." << endl;
    }
    string getRole() const {
        return role;
    }
    bool lvlup() {
        if (role == "pogany") {
            role = "bALEK";
            return true;
        } else if (role == "bALEK") {
            role = "Szenegeto";
            return true;
        } else return false;
    }
};

void sayHiEveryone(const vector<const Student*>& people) {
    for (auto pstudent : people)
            pstudent -> sayHi();
}

int main() {
    vector<const Student*> people;

    Student Jozsi;
    SOE_Student Csabi;
    
    people.push_back(&Jozsi);
    people.push_back(&Csabi);

    sayHiEveryone(people);

    while (Csabi.lvlup()) {
        sayHiEveryone(people);
    }
    

    return 0;
}

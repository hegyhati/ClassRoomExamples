#include <iostream>
using std::cout;
using std::cin;
using std::endl;

void greetings() {
    cout << "Hello stranger!" << endl;
}

auto get_age(){
    int age;
    cout << "How old are you? ";
    cin >> age;
    return age;
}

void print_suitable_drink(int age) {
    if (age >= 18) {
        cout << "Beer!!!" << endl;
    } else {
        cout << "Tea..." << endl;
    }
}

void make_older(int& age){
    ++age;
}

void say_goodbye(const int& age){
    //age += 100;
    cout << "Bye, you " << age << " year old person." << endl;
}

int main() {
    greetings();
    int age_of_user = get_age();
    cout << age_of_user << ": ";
    print_suitable_drink(age_of_user);
    for(int i=0; i<10; ++i) {
        make_older(age_of_user);
        cout << age_of_user << ": ";
        print_suitable_drink(age_of_user);
    }
    say_goodbye(age_of_user);

    return 0;
}
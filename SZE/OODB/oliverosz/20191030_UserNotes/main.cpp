#include <fstream>
#include <iostream>
#include <string>

#include <vector>
#include <map>

#include "Note.h"
#include "User.h"

using namespace std;

void importFile(string filename, vector<Note>& arr) {
    ifstream in(filename);
    if (!in.is_open())
        return;
    while (!in.eof()) {
        string line1, line2;
        getline(in, line1);
        getline(in, line2);
        if (!line1.empty())
            arr.push_back(Note(line1, line2));
        // Note constructor from 2 lines
        // Line 0: ownerId title
        // Line 1: contents
    }
}

void importFile(string filename, map<string, User>& users) {
    ifstream in(filename);
    if (!in.is_open())
        return;
    while (!in.eof()) {
        string line;
        getline(in, line);
        if (!line.empty()) {
            User u(line); // construct from string: userId userName password
            users[u.getUsername()] = u;
        }
    }
}

void exportToFile(std::string filename, const map<string, User>& users) {
    using namespace std;
    ofstream out(filename);
    if (!out.is_open())
        return;
    for (const auto &elem : users)
        out << elem.second.toString() << endl; // convert Note and User to string as seen in importFile
}

void exportToFile(std::string filename, const vector<Note>& notes) {
	using namespace std;
	ofstream out(filename);
	if (!out.is_open())
		return;
	for (const auto &elem : notes)
		out << elem.toString() << endl; // convert Note and User to string as seen in importFile
}

const User* login(const map<string, User>& users) {
    string uname, pwd;
    cout << "username: ";
    cin >> uname;

    // find user with key uname in the map of users
    // return nullptr if not found and print error msg
	auto it = users.find(uname);
	if (it == users.end()) {
		cerr << "User not found\n";
		return nullptr;
	}

    cout << "password: ";
    cin >> pwd;
    // return address of user if password matches, or nullptr and error msg on mismatch
	if (it->second.checkPassword(pwd)) {
		return &it->second;
	}
	else {
		cerr << "Wrong password!\n";
		return nullptr;
	}
}

const User* registration(map<string, User>& users) {
    string uname, pwd;
    cout << "username: ";
    cin >> uname;

    // if username is taken, print error msg and return nullptr
	/*for (map<string, User>::iterator it = users.begin(); it != users.end(); ++it) {
		if (it->first == uname) {
			cerr << "Username already taken!\n";
			return nullptr;
		}
	}*/
	if (users.find(uname) != users.end()) {
		cerr << "Username already taken!\n";
		return nullptr;
	}

    cout << "password: ";
    cin >> pwd;

    // create and add new User to map and return its address
	return &(users[uname] = User(uname, pwd));
	//return &users[uname];


	/*auto result = users.insert(make_pair(uname, User(uname, pwd)));
	if (!result.second) {
		cerr << "Username already taken!\n";
		return nullptr;
	}
	&result.first->second; // address of inserted value*/
}

int main()
{
    map<string, User> users;
	importFile("users.txt", users);
    vector<Note> notes;
	importFile("notes.txt", notes);

    bool exit = false;
    do {
        cout << "Welcome!\nAvailable commands are:\n  login register exit\n";
        string cmd;
        cin >> cmd;
        const User* currentUser = nullptr;
        if (cmd == "login") {
            currentUser = login(users);
        }
        else if (cmd == "register") {
            currentUser = registration(users);
        }
        else if (cmd == "exit") {
            exit = true;
        }
        else {
            cerr << "Unrecognized command: " << cmd << endl;
        }
        while (currentUser) { // user loop
            cout << "Hi " << currentUser->getUsername() << ", the available commands are:\n"
                << "  read delete new logout\n";
            
            // filter out indices of users's notes
            vector<int> indices;
			for (int i = 0; i < notes.size(); ++i) {
				if (notes[i].getOwnerId() == currentUser->getId())
					indices.push_back(i);
			}

            // print note titles with numbers 0,1,2,...
			for (int i = 0; i < indices.size(); i++) {
				cout << i << " " << notes[indices[i]].getTitle() << endl;
			}

            // read and execute command
            cin >> cmd;
            unsigned index;
            if (cmd == "read") {
				cout << "Enter the index of the chosen note: ";
                cin >> index;
                if (index < indices.size())
                    cout << notes.at(indices[index]).getContent() << endl;
                else
                    cerr << "Error: Invalid index\n";
            }
            else if (cmd == "delete") {
				cout << "Enter the index of the chosen note: ";
                cin >> index;
                if (index < indices.size()) {
                    // remove notes[indices[index]]
					notes.erase(notes.begin() + indices[index]);
                }
                else
                    cerr << "Error: Invalid index\n";
            }
            else if (cmd == "new") {
				cin.ignore(INT32_MAX, '\n');
                cout << "Write note title, then contents into a new line:\n";
                string title, content;
                getline(cin, title);
                getline(cin, content);
                // TODO create Note and add to notes
				notes.push_back(Note(to_string(currentUser->getId()) + ' ' + title, content));
            }
            else if (cmd == "logout") {
                currentUser = nullptr;
            }
        }
    } while (!exit);
	exportToFile("notes.txt", notes);
	exportToFile("users.txt", users);
}

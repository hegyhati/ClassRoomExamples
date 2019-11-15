#include "User.h"

#include <sstream>

using namespace std;

int User::nextId = 0;

User::User(const string& line) {
	stringstream ss;
	ss << line;
	ss >> id >> username >> password;
	if (nextId <= id) nextId = id + 1;
}

string User::toString() const
{
	return to_string(id) + ' ' + username + ' ' + password;
}

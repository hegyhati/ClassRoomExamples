#include "Note.h"

#include <sstream>

using namespace std;

Note::Note(const std::string & line1, const std::string & line2)
	: content(line2)
{
	stringstream ss;
	ss << line1;
	ss >> ownerId;
	getline(ss, title);
}

std::string Note::toString() const
{
	return to_string(ownerId) + ' ' + title + '\n' + content;
}

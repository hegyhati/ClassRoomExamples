#include "Note.h"

#include <iostream>

using namespace std;

Note::Note(const string& title, const string& content)
	: title(title), content(content)
{
}

Note::~Note()
{
	cout << "~Note()\n";
}

void Note::print() const
{
	cout << "## " << title << " ##\n" << content << endl;
}

Note * Note::clone() const
{
	return new Note(*this);
}

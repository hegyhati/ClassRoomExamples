#include "Reminder.h"

#include <iostream>

using namespace std;

Reminder::Reminder(const string& title, const string& content, DateTime due)
	: Note(title, content), due(due)
{
}

Reminder::~Reminder()
{
	cout << "~Reminder()\n";
}

void Reminder::print() const
{
	cout << "At " << due.year << ". " << due.month << ". " << due.day << ". ";
	cout << due.hour << ":" << due.min << endl;
	//cout << "## " << title << " ##\n" << content << endl;
	Note::print();
}

Note * Reminder::clone() const
{
	return new Reminder(*this);
}

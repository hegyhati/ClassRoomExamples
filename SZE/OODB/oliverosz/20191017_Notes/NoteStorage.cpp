#include "NoteStorage.h"

#include <iostream>

using namespace std;

NoteStorage::NoteStorage()
{
}

NoteStorage::~NoteStorage()
{
	for (int i = 0; i < notes.size(); ++i) {
		delete notes[i];
	}
}

void NoteStorage::printAll() const
{
	for (int i = 0; i < notes.size(); ++i) {
		notes[i]->print();
		cout << endl;
	}
}

void NoteStorage::printNotes() const
{
	for (int i = 0; i < notes.size(); ++i) {
		if (!dynamic_cast<const Reminder*>(notes[i])) {
			notes[i]->print();
		}
	}
}

void NoteStorage::printReminders() const
{
	for (int i = 0; i < notes.size(); ++i) {
		if (dynamic_cast<const Reminder*>(notes[i])) {
			notes[i]->print();
		}
	}
}

void NoteStorage::addNote(const Note & note)
{
	notes.push_back(new Note(note));
}

void NoteStorage::addReminder(const Reminder & rem)
{
	notes.push_back(new Reminder(rem));
}

void NoteStorage::add(const Note & note)
{
	//const Reminder& rem = static_cast<const Reminder&>(note);
	//notes.push_back(new Reminder(rem));

	/*try {
		const Reminder& rem = dynamic_cast<const Reminder&>(note);
		notes.push_back(new Reminder(rem));
	}
	catch (bad_cast e) {
		notes.push_back(new Note(note));
	}
	catch (exception e) {
		cerr << e.what() << endl;
	}*/

	notes.push_back(note.clone());
}

void NoteStorage::add(const Note * note)
{
	/*const Reminder* rem = dynamic_cast<const Reminder*>(note);
	if (rem) {
		notes.push_back(new Reminder(*rem));
	}
	else {
		notes.push_back(new Note(*note));
	}*/

	notes.push_back(note->clone());
}

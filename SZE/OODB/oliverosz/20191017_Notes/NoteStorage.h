#pragma once
#include <vector>

#include "Note.h"
#include "Reminder.h"
#include "DateTime.h"

class NoteStorage
{
	std::vector<Note*> notes;
public:
	NoteStorage();
	virtual ~NoteStorage();
	void printAll() const;
	void printNotes() const;
	void printReminders() const;

	void addNote(const Note& note);
	void addReminder(const Reminder& rem);
	void add(const Note& note);
	void add(const Note* note);
};

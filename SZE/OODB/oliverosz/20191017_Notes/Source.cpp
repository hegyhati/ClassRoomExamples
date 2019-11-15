#include <iostream>
#include <vector>

#include "Note.h"
#include "Reminder.h"
#include "DateTime.h"

#include "NoteStorage.h"

using namespace std;

int main() {
	/*vector<Note*> notes;

	Note* a = new Note("1. cim", "1. tartalom");
	//Note* b = new Note("2. cim helye", "2. leiras");
	notes.push_back(a);
	notes.push_back(new Note("2. cim helye", "2. leiras"));

	Reminder* c = new Reminder("Emlekezteto", "Vidd le a szemetet", { 2019, 10, 17, 16, 30 });
	notes.push_back(c);
	c->print();
	cout << endl;

	//DateTime* d = new DateTime;
	//notes.push_back((Note*)d);
	*/
	
	NoteStorage notes;
	Note a("1. cim", "1. tartalom");

	//notes.addNote(a);
	//notes.addNote(Note("2. cim helye", "2. leiras"));
	//notes.addReminder(Reminder("Emlekezteto", "Vidd le a szemetet", { 2019, 10, 17, 16, 30 }));

	//notes.add(&a);
	//notes.add(&Note("2. cim helye", "2. leiras"));
	//notes.add(&Reminder("Emlekezteto", "Vidd le a szemetet", { 2019, 10, 17, 16, 30 }));

	notes.add(a);
	notes.add(Note("2. cim helye", "2. leiras"));
	notes.add(Reminder("Emlekezteto", "Vidd le a szemetet", { 2019, 10, 17, 16, 30 }));

	notes.printAll();
}
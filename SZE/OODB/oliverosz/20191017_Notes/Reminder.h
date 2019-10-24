#pragma once
#include "Note.h"
#include "DateTime.h"

#include <string>

class Reminder : public Note
{
	using string = std::string;
	DateTime due;
public:
	Reminder(const string& title, const string& content, DateTime due);
	virtual ~Reminder();
	virtual void print() const override;

	virtual Note* clone() const override;
};


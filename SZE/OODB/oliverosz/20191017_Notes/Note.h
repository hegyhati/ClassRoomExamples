#pragma once

#include <string>

class Note
{
	using string = std::string;
protected:
	string title;
	string content;
public:
	Note(const string& title, const string& content);
	virtual ~Note();
	virtual void print() const;

	virtual Note* clone() const;
};


#pragma once

#include <string>

class Note
{
	int ownerId;
	std::string title;
	std::string content;
public:
	Note(const std::string& line1, const std::string& line2);

	std::string toString() const;
	int getOwnerId() const { return ownerId; }
	const std::string& getContent() const { return content; }
	const std::string& getTitle() const { return title; }
};


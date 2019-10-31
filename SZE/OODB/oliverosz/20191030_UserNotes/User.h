#pragma once

#include <string>

class User
{
	using string = std::string;

	int id;
	static int nextId;
	string username;
	string password;
public:
	User() : id(nextId++) {}
	User(const string& uname, const string& pwd) : id(nextId++), username(uname), password(pwd) {}
	User(const string& line);

	string toString() const;
	int getId() const { return id; }
	const string& getUsername() const { return username; }

	bool checkPassword(const string& pwd) const { return pwd == password; }
};


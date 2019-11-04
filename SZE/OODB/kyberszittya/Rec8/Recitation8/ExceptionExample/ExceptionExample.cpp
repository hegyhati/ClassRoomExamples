// ExceptionExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <list>
#include <exception>

class PersonDatabase;

class Person
{
private:
	const std::string name;
	unsigned int age;
public:
	Person(const std::string name, unsigned int age) : name(name), age(age) {}

	friend PersonDatabase;
};

class InvalidPersonError : public std::exception
{
public:
	InvalidPersonError(const char* message) : std::exception(message) {}
};

class PersonDatabase
{
private:
	std::list<Person*> persons;
public:
	~PersonDatabase()
	{
		for (const auto& v : persons)
		{
			delete v;
		}
	}

	double averageAge()
	{
		if (persons.size() > 0)
		{
			double avg_age = 0.0;
			unsigned int cnt_persons = 0;
			for (const auto& v : persons)
			{
				avg_age += static_cast<double>(v->age);
				cnt_persons++;
			}
			return avg_age / static_cast<double>(cnt_persons);
		}
		else
		{
			throw std::length_error("No persons exist in database");
			
		}
	}

	void addPerson(const std::string name, unsigned int age)
	{
		if (name.length() > 0 && age > 0)
		{
			persons.push_back(new Person(name, age));
		}
		else
		{
			throw InvalidPersonError("Invalid person data");
		}
	}
};

int main()
{
    PersonDatabase persondatabase;
	do {
		try
		{
			std::cout << "New person! " << '\n';
			std::string name;
			unsigned int age;
			std::cout << "Name: " ;
			std::cin >> name;
			std::cout << "Age: ";
			std::cin >> age;
			persondatabase.addPerson(name, age);
		}
		catch (InvalidPersonError& en)
		{
			std::cout << "ERROR INVALID PERSON" << '\n';
			std::cout << en.what() << '\n';
			break;
		}
		std::cout << "Continue? (Y/N) ";
		char c;
		std::cin >> c;
		if (c == 'N' || c == 'n')
		{
			break;
		}
	} while (true);
	try {
		std::cout << "Average age: " << persondatabase.averageAge() << '\n';
	}
	catch (std::length_error& e)
	{
		std::cout << "ERROR INVALID LENGTH" << '\n';
		std::cout << e.what() << '\n';
	}
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

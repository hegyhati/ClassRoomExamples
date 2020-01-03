// SortPeople.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

enum Gender { MALE, FEMALE };

class Person
{
private:
	std::string first_name;
	std::string last_name;
	
	Gender gender;
	std::string nationality;
	std::string occupation;
public:
	Person(const std::string first_name, const std::string last_name, const Gender gender, const std::string nationality, const std::string occupation):
		first_name(first_name),
		last_name(last_name),
		gender(gender),
		nationality(nationality),
		occupation(occupation){}

	Person(const Person& other): 
		first_name(other.first_name),
		last_name(other.last_name),
		gender(other.gender),
		nationality(other.nationality),
		occupation(other.occupation) {}

	Person& operator=(const Person& other)
	{
		first_name = other.first_name;
		last_name = other.last_name;
		gender = other.gender;
		nationality = other.nationality;
		occupation = other.occupation;
		return *this;
	}

	const std::string getOccupation()
	{
		return occupation;
	}

	const std::string getLastName()
	{
		return last_name;
	}

	friend std::ostream& operator<<(std::ostream& os, const Person& person);
	friend bool sortByLastName(Person& p0, Person& p1);
};

bool sortByLastName(Person& p0, Person& p1)
{
	return p0.last_name.at(0) < p1.last_name.at(0);
}

std::ostream& operator<<(std::ostream& os, const Person& person)
{
	switch (person.gender)
	{
	case MALE:
		os << person.first_name << '\t' << person.last_name << '\t' << "MALE" << '\t' << person.nationality << '\t' << person.occupation;
		break;
	case FEMALE:
		os << person.first_name << '\t' << person.last_name << '\t' << "FEMALE" << '\t' << person.nationality << '\t' << person.occupation;
		break;
	default:
		os << "Invalid information";
	}
	
	return os;
}

int main()
{
	std::vector<Person> persons;
	std::ifstream peoplefile("Persons.txt");
	if (peoplefile.is_open())
	{
		std::string line;
		
		while (std::getline(peoplefile, line))
		{
			std::stringstream ss(line);
			std::string tmp_fname;
			std::string tmp_lname;
			std::string gender;
			ss >> tmp_fname;
			ss >> tmp_lname;
			ss >> gender;
			Gender t_gender;
			if (gender.compare("Male") == 0)
			{
				t_gender = MALE;
			}
			else if (gender.compare("Female") == 0)
			{
				t_gender = FEMALE;
			}
			else
			{
				std::cerr << "Invalid gender" << '\n';
				break;
			}
			std::string nationality;
			ss >> nationality;
			std::string occupation;
			ss >> occupation;
			// Append to list
			Person person(tmp_fname, tmp_lname, t_gender, 
				nationality, occupation);
			persons.push_back(person);			
		}
		for (const auto& v : persons)
		{
			std::cout << v << '\n';
		}
		// Get the count of engineers
		int count_engineers = std::count_if(persons.begin(), 
			persons.end(), [](Person& p) 
		{
			return p.getOccupation().compare("Engineer")==0;
		});
		std::cout << "Count of engineers: " << count_engineers << '\n';
		// Sort by last name
		std::sort(std::begin(persons), std::end(persons), 
			[](Person& p0, Person& p1) 
			{
				return sortByLastName(p0, p1);
			});
		for (const auto& v : persons)
		{
			std::cout << v << '\n';
		}
	}
	else
	{
		std::cout << "File not found";
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

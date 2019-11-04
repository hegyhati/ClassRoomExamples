// GraphBFSDFS.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <initializer_list>
#include <queue>
#include <stack>
#include <unordered_set>

class CityNode
{
private:
	const std::string name;
	std::vector<CityNode*> adjacent_cities;
public:
	CityNode(const std::string name): name(name)
	{}

	void addAdjacentNode(CityNode* citynode)
	{
		adjacent_cities.push_back(citynode);
	}

	const std::vector<CityNode*>& getAdjacentNodes()
	{
		return adjacent_cities;
	}

	friend std::ostream& operator<<(std::ostream& os, const CityNode& node);
};

std::ostream& operator<<(std::ostream& os, const CityNode& node)
{
	os << node.name;
	return os;
}

class MapGraph
{
private:
	std::vector<CityNode*> nodes;
	std::map<std::string, CityNode*> maps;
public:
	MapGraph(){}

	~MapGraph()
	{
		for (const auto& v : nodes)
		{
			delete v;
		}
	}

	MapGraph(std::initializer_list<std::string> il)
	{
		for (const auto& v : il)
		{
			CityNode* node = new CityNode(v);
			nodes.push_back(node);
			maps[v] = node;
		}
	}

	void addNode(const std::string &name)
	{
		CityNode* node = new CityNode(name);
		nodes.push_back(node);
		maps[name] = node;
	}

	void addAdjacency(const std::string &from, const std::string &to)
	{
		maps[from]->addAdjacentNode(maps[to]);
		maps[to]->addAdjacentNode(maps[from]);
	}

	CityNode* getCity(const std::string& name)
	{
		return maps[name];
	}
};


template <typename Proc> void breadthFirstSearch(MapGraph& graph, CityNode* start, Proc p)
{
	std::queue<CityNode*> fringe;
	
	std::unordered_set<CityNode*> visited_nodes;	
	visited_nodes.insert(start);
	fringe.push(start);
	
	while (!fringe.empty())
	{
		CityNode* current_node = fringe.front();				
		fringe.pop();
		// On visit execute proc		
		p(current_node);
		for (auto v: current_node->getAdjacentNodes())
		{
			if (visited_nodes.find(v) == visited_nodes.end())
			{
				visited_nodes.insert(v);
				fringe.push(v);
			}
			
		}
	}
}

template <typename Proc> void depthFirstSearch(MapGraph& graph, CityNode* start, Proc p)
{
	std::stack<CityNode*> fringe;

	std::unordered_set<CityNode*> visited_nodes;
	fringe.push(start);

	while (!fringe.empty())
	{
		CityNode* current_node = fringe.top();
		fringe.pop();
		if (visited_nodes.find(current_node) == visited_nodes.end())
		{
			visited_nodes.insert(current_node);
			// On visit execute proc
			p(current_node);
			for (auto v : current_node->getAdjacentNodes())
			{				
				fringe.push(v);
			}
		}
		
	}
}

void graphExample()
{
	MapGraph graph({ "Budapest", "Zalaegerszeg", "Szombathely", "Miskolc", "Gyor",
		"Veszprem", "Szeged", "Kecskemet", "Szabadka", "Szekszard", "Szolnok", "Mosonmagyarovar",
		"Rajka", "Bratislava" });
	graph.addAdjacency("Budapest", "Gyor");
	graph.addAdjacency("Budapest", "Miskolc");
	graph.addAdjacency("Budapest", "Kecskemet");
	graph.addAdjacency("Budapest", "Veszprem");
	graph.addAdjacency("Budapest", "Szolnok");
	graph.addAdjacency("Veszprem", "Gyor");
	graph.addAdjacency("Veszprem", "Zalaegerszeg");
	graph.addAdjacency("Kecskemet", "Szeged");
	graph.addAdjacency("Kecskemet", "Szolnok");
	graph.addAdjacency("Szeged", "Szabadka");
	graph.addAdjacency("Szeged", "Szekszard");
	graph.addAdjacency("Miskolc", "Szolnok");
	graph.addAdjacency("Gyor", "Szombathely");
	graph.addAdjacency("Gyor", "Mosonmagyarovar");
	graph.addAdjacency("Mosonmagyarovar", "Rajka");
	graph.addAdjacency("Rajka", "Bratislava");
	auto printNode = [](CityNode* node) {
		std::cout << *node << '\n';
	};
	std::cout << '\n' << "Breadth first search" << std::endl;
	breadthFirstSearch(graph, graph.getCity("Budapest"), printNode);
	std::cout << '\n' << "Depth first search" << '\n';
	depthFirstSearch(graph, graph.getCity("Budapest"), printNode);
}

int main()
{
	graphExample();
	_CrtDumpMemoryLeaks();
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

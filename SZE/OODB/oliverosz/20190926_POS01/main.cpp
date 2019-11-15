#include <iostream>
#include <string>

#include "Shop.h"

using namespace std;

int main() {
	Shop shop("inventory.txt");
	string command;
	bool exit = false;
	do
	{
		cin >> command;
		if (command == "add") { // decreases inventory
			string product;
			int pcs;
			cin >> product >> pcs;
			bool success = shop.addToBasket(product, pcs);
			if (!success) cerr << "Error: There are not enough products in the inventory.\n";
		}
		/*else if (command == "remove") {
			string product;
			cin >> product;
			bool success = shop.removeFromBasket(product);
			if (!success) {
				cerr << "Error: Product is not present in the basket.\n";
				shop.printBasket();
			}
		}*/
		else if (command == "show") {
			shop.printBasket();
		}
		/*else if (command == "clear") { // return products to inventory
			shop.clearBasket();
		}
		else if (command == "pay") { // increase income
			shop.purchase();
		}*/
		else if (command == "inventory") {
			shop.printInventory();
		}
		else if (command == "exit") {
			exit = true;
			cout << "Total income: " << shop.getIncome() << endl;
		}
		else {
			cerr << "Error: Unrecognized command.\n";
			cin.ignore(1000, '\n');
			cin.clear();
		}
	} while (!exit);
	return 0;
}
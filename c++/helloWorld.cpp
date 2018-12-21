#include <iostream>

int main () {
	char * str;
	std::cout << "Input a name!";
	std::cin >> str;
	std::cout << "Hello ";
	std::cout << str;
	std::cout << "!\n";
	return 0;
}

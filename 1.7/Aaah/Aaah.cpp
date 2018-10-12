#include <iostream>
#include <string>
using namespace std;
int main()
{
	string jon;
	string doc;
	getline(cin, jon);
	getline(cin, doc);
	if (jon.length() >= doc.length()) {
		cout << "go";
	}
	else {
		cout << "no";
	}
	getline(cin, jon);
	return 0;
}
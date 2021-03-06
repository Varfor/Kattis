#include <iostream>
#include <vector>
#include <unordered_set> 
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;
int main() {
	string inData;
	getline(cin, inData);
	stringstream ssinData(inData);
	vector<string> vord;
	while (ssinData >> inData) vord.push_back(inData);
	sort(vord.begin(), vord.end());
	adjacent_find(vord.begin(), vord.end());
	//	unique(vord.begin(), vord.end());
	auto it = unique(vord.begin(), vord.end());
	cout << ((it == vord.end()) ? "yes" : "no");
	return 0;
}
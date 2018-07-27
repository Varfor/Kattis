#include <iostream>
using namespace std;
int main() {
	int inData;
	int utData	= 0;
	cin >> inData;
	for (int i = 1; i*i <= inData; i++) {
		 if (inData%i == 0) {
			inData = inData / i;
			utData++;
			//cout << inData << "\n"; //testgrejen
			i = 1;
		}
	}
	cout << utData;
	return 0;
}
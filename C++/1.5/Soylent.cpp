#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int main()
{
	int tcases;
	int kcal;
	vector<int> burkar;
	cin >> tcases;
	for (int i = 0; i < tcases; i++) {
		cin >> kcal;
		burkar.push_back(kcal);
	}
	for (int& s : burkar) {
		cout << ((s % 400 == 0) ? s / 400 : (s / 400) + 1) << endl;
	}
    return 0;
}
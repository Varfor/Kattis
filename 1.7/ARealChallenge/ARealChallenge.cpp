#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main() {
	double A;
	cin >> A;
	cout << setprecision(6) << fixed << 4 * (sqrt(A));
	return 0;
}
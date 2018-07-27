#include <iostream>
#include <cmath>
using namespace std;
int main() {
	int X, N, P, A;
	cin >> X;
	cin >> N;
	A = X;
	for (int i = 0; i < N; i++) {
		cin >> P;
		A = A+X-P;
	}
	cout << A;
	cin >> N;
	return 0;
}
#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main()
{
	int iter;
	int start = 2;
	cin >> iter;
	cout << setprecision(0) << fixed << pow(pow(start, iter)+1, 2);
	return 0;

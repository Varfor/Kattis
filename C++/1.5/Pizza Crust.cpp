#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;
int main()
{
	int Pizza;
	int Crust;
	const double PI = 3.14159265358979323846;
	cin >> Pizza >> Crust;
	cout << setprecision(6) << fixed << ((PI * (pow(Pizza - Crust, 2))) / (PI * (pow(Pizza, 2))))*100;
	return 0;
}
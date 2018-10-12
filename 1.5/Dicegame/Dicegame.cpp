#include <iostream>
using namespace std;
int main()
{
    int g1, g2, g3, g4;
    int e1, e2, e3, e4;
    cin >> g1 >> g2 >> g3 >> g4;
    cin >> e1 >> e2 >> e3 >> e4;
    double gunnar = g1 + g2 + g3 + g4;
    double emma = e1 + e2 + e3 + e4;
    if (gunnar > emma) {
        cout << "Gunnar";
    }
    else if (emma > gunnar) {
        cout << "Emma";
    }
    else {
        cout << "Tie";
    }
    return 0;
}
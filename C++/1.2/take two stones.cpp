#include <iostream>
int main()
{
    int sten;
    std::cin >> sten;
    if (sten % 2 == 0) {
        std::cout << "Bob";
    }
    else {
        std::cout << "Alice";
    }
    return 0;
}
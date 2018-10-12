#include <iostream>
#include <cstring>
int main()
{
    char ljud[30];
    char hiss = 'B';
    std::cin >> ljud;
    for (int i = 0; i < strlen(ljud); i++) {
        switch (toupper(ljud[i])) {
        case 'S':
            if (ljud[i - 1] == 's') {
                std::cout << "hiss";
                return 0;
            }
            break;
        default: hiss = 'B';
            break;
        }
    }
    std::cout << "no hiss";
    return 0;
}
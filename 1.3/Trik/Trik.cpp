#include <iostream>
#include <cstring>
int main()
{
	bool Pos1;
	bool Pos2;
	bool Pos3;
	bool tempPos;
	Pos1 = true;
	Pos2 = false;
	Pos3 = false;
	char inData[51];
	std::cin >> inData;

	for (int i = 0; i < strlen(inData); i++) {
		switch (toupper(inData[i])) {
		case 'A':
			tempPos = Pos1;
			Pos1 = Pos2;
			Pos2 = tempPos;
			break;
		case 'B':
			tempPos = Pos2;
			Pos2 = Pos3;
			Pos3 = tempPos;
			break;
		case 'C':
			tempPos = Pos1;
			Pos1 = Pos3;
			Pos3 = tempPos;
			break;
		}
	}
	if (Pos1) {
		std::cout << "1";
	}
	else if (Pos2) {
		std::cout << "2";
	}
	else {
		std::cout << "3";
	}
	return 0;
}

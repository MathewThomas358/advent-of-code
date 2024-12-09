#include <iostream>
#include <fstream>
#include <string>

using std::ifstream;
using std::cout;
using std::string;

int main(void) {

    ifstream file("1.txt");
    string line;

    while(getline(file, line)){
        int floor = 0;
        int position = -1;

        for(int i = 0; i < line.size(); i++){
            if(line[i] == '('){
                floor++;
            } else if(line[i] == ')'){
                floor--;
            }
            if(floor == -1 && position == -1){
                position = i + 1;
            }
        }
        cout << floor << "\n";
        cout << position << "\n";
    }

    return 0;
}
/**
 * Incomplete solution
 */

#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

long long calculate(string);

int main(void) {

    ifstream file("11.txt");
    if (!file) {
        cerr << "Unable to open file";
        return 1;
    }

    vector<string> words;
    string line;
    while (getline(file, line)) {
        istringstream iss(line);
        string word;
        while (iss >> word) {
            words.push_back(word);
        }
    }
    file.close();

    long long int result = 0;
    int iterations = 75;

    for(auto& word: words) {
        result += calculate(word);
    }

    cout << result << "\n";

    return 0;
}

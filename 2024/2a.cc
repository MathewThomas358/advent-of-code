#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using std::cout;
using std::ifstream;
using std::string;
using std::vector;

bool isIncreasingOrDecreasing(vector<int> &report) {

    if(report.size() == 1)
        return true;

    if(report[0] < report[1]) {
        for(int i = 1; i < report.size(); i++) {
            if(report[i] <= report[i-1])
                return false;
        }
    } else {
        for(int i = 1; i < report.size(); i++) {
            if(report[i] >= report[i-1])
                return false;
        }
    }
    return true;
}

bool areAllElementsWithinLimits(vector<int> &report) {
    for(int i = 0; i < report.size() - 1; i++) {
        if(abs(report[i] - report[i+1]) < 1 || abs(report[i] - report[i+1]) > 3)
            return false;
    }
    return true;
}

int main(void) {
    ifstream in("2.txt");
    vector<vector<int>> data;
    string row;
    int safeCount = 0;

    while (std::getline(in, row)) {
        vector<int> report;
        std::stringstream ss(row);
        int num;

        while (ss >> num)
            report.push_back(num);

        data.push_back(report);
    }

    for(auto &report: data) {
        if (isIncreasingOrDecreasing(report) && areAllElementsWithinLimits(report))
            safeCount++;
    }

    cout << safeCount << "\n";

    return 0;
}
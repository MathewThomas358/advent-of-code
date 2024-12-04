#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


bool safe(const vector<int>& report) {
    
    if (report != vector<int>(report.begin(), report.end()) && report != vector<int>(report.rbegin(), report.rend())) {
        return false;
    }

    for (size_t i = 0; i < report.size() - 1; i++) {
        if (abs(report[i] - report[i + 1]) < 1 || abs(report[i] - report[i + 1]) > 3) {
            return false;
        }
    }
    return true;
}

bool safe_2(vector<int>& report) {
    if (safe(report)) {
        return true;
    }

    for (size_t i = 0; i < report.size(); i++) {
        vector<int> temp_report = report;
        temp_report.erase(temp_report.begin() + i);
        if (safe(temp_report)) {
            return true;
        }
    }
    return false;
}

int main() {
    ifstream file("2.txt");
    string line;
    vector<vector<int>> reports;

    while (getline(file, line)) {
        stringstream ss(line);
        vector<int> report;
        int num;
        while (ss >> num) {
            report.push_back(num);
        }
        reports.push_back(report);
    }

    int safeCount = 0;
    for (auto& report : reports) {
        if (safe_2(report)) {
            safeCount++;
        }
    }

    cout << "Answer to part 2 is " << safeCount << endl;

    return 0;
}

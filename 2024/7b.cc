#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

using std::ifstream;
using std::vector;
using std::string;
using std::cout;
using std::to_string;

typedef long long ll;

bool calculate(ll, ll, int, int, vector<int>&, bool);
vector<string> split(const string&, const string&);

int main(void) {

    ifstream in("7.txt");
    string line;
    vector<vector<string>> lines;
    vector<ll> sums;
    ll finalSum = 0;

    while(getline(in, line)) {
        vector<string> tokens = split(line, ": ");
        sums.push_back(stoll(tokens[0]));
        string temp = tokens[1];
        tokens = split(temp, " ");
        lines.push_back(tokens);
    }

    for(int i = 0; i < sums.size(); i++) {
        vector<int> nums;
        std::transform(lines[i].begin(), lines[i].end(), std::back_inserter(nums), [](const string& str) {
            return std::stoi(str);
        });
        if(calculate(sums[i], nums[0], 1, nums.size(), nums, true)) {
            finalSum += sums[i];
        }
    }

    cout << finalSum << "\n";

    return 0;
}

bool calculate(ll sum, ll currentSum, int index, int size, vector<int>& nums, bool performConcat) {
    if(currentSum == sum && index == size) {
        return true;
    }

    if(currentSum > sum || index == size || (currentSum == sum && index >= size)) {
        return false;
    }

    return 
            calculate(sum, currentSum + nums[index], index + 1, size, nums, performConcat) || 
            calculate(sum, currentSum * nums[index], index + 1, size, nums, performConcat) ||
            (performConcat ? 
                calculate(sum, stoll(to_string(currentSum) + to_string(nums[index])), index + 1, size, nums, performConcat) : false);
}

vector<string> split(const string& str, const string& delimiter) {
    size_t pos = 0, lastPos = 0;
    vector<string> tokens;
    while ((pos = str.find(delimiter, lastPos)) != string::npos) {
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        lastPos = pos + delimiter.size();
    }
    tokens.push_back(str.substr(lastPos));
    return tokens;
}
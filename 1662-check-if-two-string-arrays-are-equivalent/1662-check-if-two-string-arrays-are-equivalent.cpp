#include<string.h>

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        std::string s = "";
        std::string c = "";
        for (string i : word1)
        {
            s += i;
        }
        for (string d : word2)
        {
            c += d;
        }
        int res = s.compare(c);
        return res == 0;

    }
};
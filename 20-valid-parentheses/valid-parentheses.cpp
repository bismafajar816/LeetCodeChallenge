#include <stack>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> parentheses;
        unordered_map<char, char> mappings = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                parentheses.push(c);
            } else {
                if (parentheses.empty() || parentheses.top() != mappings[c]) {
                    return false;
                }
                parentheses.pop();
            }
        }
        
        return parentheses.empty();
    }
};

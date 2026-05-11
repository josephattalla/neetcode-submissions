class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> pairs = {
            {')' , '('},
            {'}' , '{'},
            {']' , '['}
        };
        std::stack<char> st;

        for (char c : s) {
            if (pairs.contains(c)) {
                if (st.size() > 0 && st.top() == pairs[c]) {
                    st.pop();
                }
                else {
                    return false;
                }
            }
            else {
                st.push(c);
            }
        }

        return st.size() == 0 ? true : false;
    }
};

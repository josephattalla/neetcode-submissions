class Solution {
public:
    int calPoints(vector<string>& operations) {
        int curr_sum = 0;
        std::stack<int> scores;
        for (auto op : operations) {
            if (op == "+") {
                int num1 = scores.top();
                scores.pop();
                int num2 = scores.top();
                scores.push(num1);
                scores.push(num1+num2);
                curr_sum += scores.top();
            }
            else if (op == "C") {
                curr_sum -= scores.top();
                scores.pop();
            }
            else if (op == "D") {
                scores.push(scores.top()<<1);
                curr_sum += scores.top();
            }
            else {
                scores.push(stoi(op));
                curr_sum += scores.top();
            }
        }
        return curr_sum;
    }
};
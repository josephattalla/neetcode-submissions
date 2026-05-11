class Solution {
   public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int skipped = 0;
        std::queue<int> students_q;
        std::queue<int> sandwich_q;

        for (int i = 0; i < students.size(); i++) {
            students_q.push(students[i]);
        }

        for (int i = 0; i < sandwiches.size(); i++) {
            sandwich_q.push(sandwiches[i]);
        }

        while (students_q.size() && skipped != students_q.size()) {
            if (students_q.front() == sandwich_q.front()) {
                students_q.pop();
                sandwich_q.pop();
                skipped = 0;
            } else {
                int tmp = students_q.front();
                students_q.pop();
                students_q.push(tmp);
                skipped++;
            }
        }

        return skipped;
    }
};
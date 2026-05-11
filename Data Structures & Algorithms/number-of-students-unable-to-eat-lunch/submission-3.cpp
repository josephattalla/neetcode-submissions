class Solution {
   public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
      int square = 0;
      int circle = 0;

      for (int i = 0; i < students.size(); i++) {
        if (students[i]) square++;
        else circle++;
      }

      for (int i = 0; i < sandwiches.size(); i++) {
        if (sandwiches[i]) {
            if (square > 0) square--;
            else return circle;
        }
        else {
            if (circle > 0) circle--;
            else return square;
        }
      }

      return 0;
    }
};
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (auto itr = nums.begin(); itr != nums.end();) {
            if (val == *itr) nums.erase(itr);
            else {
                ++itr;
                ++k;
            }
        }

        return k;
    }
};
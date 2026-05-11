class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l = 0;
        int r = nums.size();

        while (l < r) {
            if (nums[l] == val) {
                --r;
                std::swap(nums[l], nums[r]);
            }
            else ++l;
        }
        return r;
    }
};
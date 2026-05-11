// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<Pair> merge(vector<Pair>& left, vector<Pair>& right) {
        // PUSH THE SMALLEST ELEMENT FROM CURRENT PTR TO SORTED
        vector<Pair> sorted;
        int lPtr = 0;
        int rPtr = 0;
        while (lPtr < left.size() && rPtr < right.size()) {
            if (left[lPtr].key <= right[rPtr].key) {
                sorted.push_back(left[lPtr]);
                lPtr++;
            }
            else {
                sorted.push_back(right[rPtr]);
                rPtr++;
            }
        }
        // GET REST OF UNFINISHED ARRAY
        while (rPtr < right.size()) {
            sorted.push_back(right[rPtr]);
            rPtr++;
        }
        while (lPtr < left.size()) {
            sorted.push_back(left[lPtr]);
            lPtr++;
        }
        return sorted;
    }

    vector<Pair> mergeSort(vector<Pair>& pairs) {
        // BASE CASE
        if (pairs.size() < 2) {
            return pairs;
        }
        // SORT LEFT & RIGHT HALF, THEN MERGE THEM
        int mid = pairs.size() / 2;
        vector<Pair> left(pairs.begin(), pairs.begin() + mid);
        vector<Pair> right(pairs.begin() + mid, pairs.end());
        vector<Pair> leftSort = mergeSort(left);
        vector<Pair> rightSort = mergeSort(right);
        return merge(leftSort, rightSort);
    }
};

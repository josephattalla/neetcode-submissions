// RECURSIVE SOLUTION:
//      - BASE: n < 4 => return n
//      - RECURSE: distinctWays = 2 + climbStairs(n-1) + climbStairs(n-2)
class Solution {
public:
    int climbStairs(int n) {
       if (n < 4) {
        return n;
       } 
       int distinctWays = climbStairs(n-1) + climbStairs(n-2);
       return distinctWays;
    }
};

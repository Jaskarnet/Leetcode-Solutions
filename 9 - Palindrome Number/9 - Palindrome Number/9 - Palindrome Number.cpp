/*
9. Palindrome Number
Easy
Given an integer x, return true if x is a
palindrome, and false otherwise.



    Example 1:

    Input: x = 121
    Output : true
    Explanation : 121 reads as 121 from left to right and from right to left.

    Example 2 :

    Input : x = -121
    Output : false
    Explanation : From left to right, it reads - 121. From right to left, it becomes 121 - .Therefore it is not a palindrome.

    Example 3 :

    Input : x = 10
    Output : false
    Explanation : Reads 01 from right to left.Therefore it is not a palindrome.


    Follow up : Could you solve it without converting the integer to a string?
*/

#include <iostream>
#include <string>
#include <sstream>

class Solution {
public:
    static bool isPalindrome(int x) {
        std::stringstream ss;
        std::string x_str;
        ss << x;
        x_str = ss.str();
        std::string::const_iterator x_l = x_str.cbegin();
        std::string::const_iterator x_r = x_str.cend() - 1;
        while (x_l < x_r) {
            if (*x_l != *x_r)
                return false;
            x_l++;
            x_r--;
        }
        return true;
    }
};

int main()
{
    bool solution = Solution::isPalindrome(1262621);
    std::cout << solution;
}
// Description:
// The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
// 
// P   A   H   N
// A P L S I I G
// Y   I   R
// 
// And then read line by line: `"PAHNAPLSIIGYIR"`
// 
// Write the code that will take a string and make this conversion given a number of rows:
// 
// string convert(string s, int numRows);
// 
// **Example 1:**
// 
// **Input:** s = "PAYPALISHIRING", numRows = 3
// **Output:** "PAHNAPLSIIGYIR"
// 
// **Example 2:**
// 
// **Input:** s = "PAYPALISHIRING", numRows = 4
// **Output:** "PINALSIGYAHRPI"
// **Explanation:**
// P     I    N
// A   L S  I G
// Y A   H R
// P     I
// 
// **Example 3:**
// 
// **Input:** s = "A", numRows = 1
// **Output:** "A"
// 
// **Constraints:**
// 
// *   `1 <= s.length <= 1000`
// *   `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
// *   `1 <= numRows <= 1000`



#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    static string convert(string s, int numRows) {
        // If numRows is 1 or the length of s is less than or equal to numRows, return s as it is.
        if (numRows == 1 || s.length() <= numRows) {
            return s;
        }

        // Create a vector of strings to store the characters for each row.
        vector<string> rows(min(numRows, int(s.length())));

        // Initialize variables to track the current row and the direction of traversal.
        int currentRow = 0;
        bool goingDown = false;

        // Iterate over each character in the input string.
        for (char c : s) {
            // Add the character to the current row.
            rows[currentRow] += c;

            // If we are at the first or last row, change the direction.
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }

            // Move up or down the rows based on the direction.
            currentRow += goingDown ? 1 : -1;
        }

        // Combine the rows to form the final result string.
        string result;
        for (const string& row : rows) {
            result += row;
        }

        // Return the final result.
        return result;
    }
};


int main() {
    // Test cases
    string s1 = "PAYPALISHIRING";
    int numRows1 = 3;
    cout << "Input: " << s1 << ", numRows: " << numRows1 << endl;
    cout << "Output: " << Solution::convert(s1, numRows1) << endl; // Expected: "PAHNAPLSIIGYIR"

    string s2 = "PAYPALISHIRING";
    int numRows2 = 4;
    cout << "Input: " << s2 << ", numRows: " << numRows2 << endl;
    cout << "Output: " << Solution::convert(s2, numRows2) << endl; // Expected: "PINALSIGYAHRPI"

    string s3 = "A";
    int numRows3 = 1;
    cout << "Input: " << s3 << ", numRows: " << numRows3 << endl;
    cout << "Output: " << Solution::convert(s3, numRows3) << endl; // Expected: "A"

    return 0;
}

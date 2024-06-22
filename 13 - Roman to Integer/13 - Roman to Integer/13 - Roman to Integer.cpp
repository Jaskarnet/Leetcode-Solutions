

#include <iostream>
#include <string>
#include <map>

class Solution {
public:
    static int romanToInt(std::string s) {
        std::map<char, int> romanValues = { {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000} };
        std::string::reverse_iterator pCurrentCharacter = s.rbegin(); // Use reverse iterator to start from the end of the string
        char previousCharacter = '\0'; // Initialize previousCharacter
        int result = 0;

        // Iterate through the string from the end to the beginning
        while (pCurrentCharacter != s.rend()) {
            if (
                // I can be placed before V(5) and X(10) to make 4 and 9.
                (*pCurrentCharacter == 'I' && (previousCharacter == 'V' || previousCharacter == 'X')) ||
                // X can be placed before L(50) and C(100) to make 40 and 90.
                (*pCurrentCharacter == 'X' && (previousCharacter == 'L' || previousCharacter == 'C')) ||
                // C can be placed before D(500) and M(1000) to make 400 and 900.
                (*pCurrentCharacter == 'C' && (previousCharacter == 'D' || previousCharacter == 'M'))
                ) {
                result -= romanValues[*pCurrentCharacter];
            }
            else {
                result += romanValues[*pCurrentCharacter];
            }

            // Update previousCharacter to the current character before moving to the next one
            previousCharacter = *pCurrentCharacter;
            ++pCurrentCharacter;
        }

        return result;
    }
};

int main() {
    std::string roman = "MCMXCIV";
    int result = Solution::romanToInt(roman);
    std::cout << "The integer value of " << roman << " is " << result << std::endl;
    return 0;
}


// A first attempt; does not successfully catch all abbreviations.

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    // Note: I tried to do this without regexes for fun.
    string input = "";
    getline(cin,input);
    char firstLetter = input[0];
    bool prevCapital = true;
    bool newLine = false;
    for (int i = 0; i < input.length()-1; i++) {
        // If the next character is not a space, we want to output a newline first.
        if (input[i] != ' ' && newLine) {
            cout << endl;
            newLine = false;
        }
        cout << input[i];
        if (newLine) {
            cout << endl;
            newLine = false;
        }
        // Check for spaces to determine words
        if (input[i] == ' ') {
            // The next letter after a space should be a letter 
            // (could check for extra spaces to be more robust)
            firstLetter = input[i+1];
            // If the first letter of the word is capitalized, note it
            if (firstLetter >= 65 && firstLetter <= 90) {
                prevCapital = true;
            } else {
                prevCapital = false;
            }
        }
        // Check for sentence end markers to find sentences or abbreviations
        if (input[i] == '.' || input[i] == '?' || input[i] == '!') {
            // If both the next word and the previous word were capitalized, chances are high it's an abbreviation
            // Otherwise, it's likely a sentence
            // We check for one, two, or three inputs over (due to quotes)
            if (input[i+1] >= 65 && input[i+1] <= 90 || 
                input[i+2] >= 65 && input[i+2] <= 90 || 
                input[i+3] >= 65 && input[i+3] <= 90) {
                // This ensures we aren't missing short abbreviations.
                if (!prevCapital && 
                    (input[i+2] != '.' || 
                     input[i+3] != '.')) {
                    newLine = true;
                }
            }
        }
    }
    cout << input[input.length()-1] << input[input.length()];
    
    return 0;
}

// A second attempt using regexes (cleaner-looking but it feels dirty...)

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <regex>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string input = "";
    getline(cin,input);
    regex reg("(?!((rs.)|(Mr.)|(Ms.)|(Dr.)))(([a-zA-Z]{2}[.?])|([a-zA-Z][!]))((?:[ ])|([A-Z]))");
    cout << regex_replace(input,reg,"$6\n$10");
    return 0;
}

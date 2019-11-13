#include <sys/types.h>
#include <dirent.h>
#include <errno.h>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include "util.h"

using namespace std;


// Convert string "str" to integer "num". Return false if str does not appear
// to be a number
bool
myStr2Int(const string& str, int& num)
{
    num = 0;
    size_t i = 0;
    int sign = 1;
    if (str[0] == '-') { sign = -1; i = 1; }
    bool valid = false;
    for (; i < str.size(); ++i) {
        if (isdigit(str[i])) {
            num *= 10;
            num += int(str[i] - '0');
            valid = true;
        }
        else return false;
    }
    num *= sign;
    return valid;
}
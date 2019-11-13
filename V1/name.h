#ifndef NAME_H
#define NAME_H

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include "util.h"
using namespace std;


class Name
{
public:
	Name() {}
    ~Name() {}

    void creatName(string totalName);

	vector<string> _string;
	vector<int> _num;

};

#endif // NAME_H

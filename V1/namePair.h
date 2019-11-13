#ifndef NAME_PAIR_H
#define NAME_PAIR_H

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include "name.h"

using namespace std;


class NamePair
{
public:
	NamePair(string first, string second) :  _group(0) {
		_first.creatName(first);
		_second.creatName(second);
	}
    ~NamePair() {}

    void setComSubstr();

	Name    _first;
	Name    _second;
	vector<string> _comSubstr;
	size_t  _group;

};

#endif // NAME_PAIR_H

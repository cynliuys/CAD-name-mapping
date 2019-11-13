#ifndef NAME_MAP_H
#define NAME_MAP_H

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include "namePair.h"
#include "name.h"
using namespace std;


class NameMap
{
public:
    NameMap() {}
    ~NameMap() {
        for (size_t i=0 ; i< _nameList.size() ; i++)  delete _nameList[i];
        _nameList.clear();
    }

    bool creatNameMap(const char* file);
    void grouping();
    bool findGroup(NamePair * targetPrt);




private:
    vector<NamePair *>           _nameList;
    vector<vector<NamePair *>>   _groupList;
   
};

#endif // NAME_MAP_H

#ifndef NAME_MAP_H
#define NAME_MAP_H
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <iostream>
#include <list>
using namespace std;

struct Triple
{
    unsigned first;  //Block begin
    unsigned second; //Block size
    unsigned third;  //Move destination
    Triple(unsigned a, unsigned b, unsigned c) : first(a), second(b), third(c){}
};


class NameMap
{
public:
    NameMap() {}
    ~NameMap() {}

    bool creatNameMap(const char* file);
    bool recordMove();
    bool recordMove_block();

    void writePy(const char* file);
    void writePy_block(const char* file);

    void outputMapIn(const char* file);
    void outputSorted(const char* file);

    bool reverse() { return _reverse; }
    bool reverse_block() { return _reverse; }
    int  digit(int number);
    bool choose_block();


private:
    list   <pair<string, string> >     _pairList;
    list   <string>                    _secondList;
    vector <pair<unsigned, unsigned> > _movement;
    vector <Triple>                    _blockMovement; 
    bool                               _reverse;
    bool                               _blockReverse;
};

#endif // NAME_MAP_H

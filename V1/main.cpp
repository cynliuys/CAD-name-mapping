#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include "nameMap.h"
#include "name.h"

using namespace std;


int main(int argc, char** argv)
{
    if (argc == 3) {  //./nmpgen <map_in.json> <python_script.py>
        NameMap nameMap;
        if (!nameMap.creatNameMap(argv[1])) {
            exit(-1); 
        }
    }
    else {
        cerr << "Error: \"./nmpgen <map_in.json> <python_script.py>\"" <<endl;
        exit(-1);
    }
    return 0;
}

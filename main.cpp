#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>
#include <fstream>
#include "nameMap.h"

using namespace std;


int main(int argc, char** argv)
{
    if (argc == 3) {  //./cada039 <map_in.json> <python_script.py>
        NameMap nameMap;
        if (!nameMap.creatNameMap(argv[1])) { exit(-1); }

        //string file(argv[1]);
        //file = file.substr(0, file.size()-5);
        //nameMap.outputMapIn((file+".map_in.json").c_str());

        if (!nameMap.recordMove_block()){ exit(-1); }
        if (!nameMap.recordMove()){ exit(-1); }

        // for debuging
        //nameMap.outputSorted((file+".sort.json").c_str());


        if(nameMap.choose_block()) {
            if(nameMap.reverse()) cout << "BLOCK reversed picked!" << endl;
            else cout << "BLOCK in-ordered picked!" << endl;
            nameMap.writePy_block(argv[2]);
        }
        else {
           if(nameMap.reverse()) cout << "reversed picked!" << endl;
           else cout << "in-ordered picked!" << endl;
           nameMap.writePy(argv[2]);
        }
        
    }
    else {
        cerr << "Error: \"./cada039 <map_in.json> <python_script.py>\"" <<endl;
        exit(-1);
    }
    return 0;
}

#include <iostream>
#include <sstream>
#include <fstream>
#include <list>
#include <utility>
#include "nameMap.h"

using namespace std;


bool 
NameMap::creatNameMap(const char* file){
	ifstream ifs;
	ifs.open(file);
	if (!ifs.is_open()){
		cerr << "Error: cannot open file \"" << file << "\"!"<<endl;
		return false;
	}

	string line = "";
	if(!getline(ifs, line, '\n')){
		cerr << "Error: the format is not correct"<<endl;
		return false;
	}
	if(line[0] != '{'){
		cerr << "Error: the format is not correct"<<endl;
		return false;
	}
	while(getline(ifs, line, '\n')){
		if(line[0] == '}') break;
		istringstream ss(line);
		string str1 = "";
		string str2 = "";
		getline(ss, str1, '"');
		getline(ss, str1, '"');
		getline(ss, str2, '"');
		getline(ss, str2, '"');
		pair <string, string> tempPair(str1, str2);
		_pairList.push_back(tempPair);
		_secondList.push_back(str2);
	}
	return true;
}

int NameMap::digit(int number) {

   int result = 0;
   while(number != 0) {
      number /= 10;
      result++;
   }
   return result;
}

bool NameMap::choose_block() {

   int single = 0, block = 30;
   for(unsigned i=0; i<_movement.size(); i++) {
      single += digit(_movement[i].first) + 1;  // one for the comma
      single += digit(_movement[i].second) + 1;
   }
   for(unsigned i=0; i<_blockMovement.size(); i++) {
      block += digit(_blockMovement[i].first) + 1;  // one for the comma
      block += digit(_blockMovement[i].second) + 1;
      block += digit(_blockMovement[i].third) + 1;
   }
   
   return block < single;
}


#include <iostream>
#include <string>
#include "name.h"

using namespace std;

void
Name::creatName(string totalName){
	bool ischar = true;
	size_t tokenBegin = 0;
	for(size_t i=0 ; i<totalName.size() ; ++i){
		if(ischar){
			if(totalName[i]>='0' && totalName[i]<='9'){
				ischar = false;
				if(i!=0){
					_string.push_back(totalName.substr(tokenBegin, i - tokenBegin));
				}
				tokenBegin = i;
			}
		}
		else{
			if(totalName[i]<'0' || totalName[i]>'9'){
				ischar = true;
				int tempNum = 0;
				string tempStr = totalName.substr(tokenBegin, i - tokenBegin);
				myStr2Int(tempStr, tempNum);
				_num.push_back(tempNum);
				tokenBegin = i;
			}
		}
	}
	if(ischar){
		_string.push_back(totalName.substr(tokenBegin, totalName.size() - tokenBegin));
	}
	else{
		int tempNum = 0;
		string tempStr = totalName.substr(tokenBegin, totalName.size() - tokenBegin);
		myStr2Int(tempStr, tempNum);
		_num.push_back(tempNum);
	}
}
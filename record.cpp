/***********************
 * record.cpp
 * Author:  Chou Yun
 ***********************/
#include <iostream>
#include <string>
#include <fstream>
#include "nameMap.h"
using namespace std;

// compare function for sorting sring pairs
bool comp(pair<string, string> a, pair<string, string> b) {
   return a.first < b.first;
}

bool NameMap::recordMove() {

   // sort the two lists
   _pairList.sort(comp);
   _secondList.sort();
   list<string> secondList(_secondList);
   list<string> secondListRev(_secondList);
   vector<pair<unsigned, unsigned> > movement, movementRev;

   // find the movements in order
   list< pair<string, string> >::iterator indexPtr = _pairList.begin();
   list<string>::iterator findPtr, matchPtr = secondList.begin();
   int index = 0, find;
   while(indexPtr != _pairList.end()) {
      if(indexPtr->second == *matchPtr) {
         // if match, move on to the next one
         indexPtr++;
         index++;
         matchPtr++;
         continue;
      }
      // if not match
      string target = indexPtr->second;
      findPtr = matchPtr;
      find = index;
      while(true) {
         if(findPtr == secondList.end())
            return false;
         if(*findPtr == indexPtr->second) {
            secondList.erase(findPtr);
            secondList.insert(matchPtr, target);
            movement.push_back(pair<unsigned, unsigned>(find-index, index));
            indexPtr++;
            index++;
            break;
         }
         findPtr++;
         find++;
      }
   }

   // find the movements in reverse order
   _reverse = true;
   indexPtr = _pairList.end();
   matchPtr = secondListRev.end();
   index = _pairList.size();
   while(true) {
      indexPtr--;
      matchPtr--;
      index--;
      if(indexPtr->second != *matchPtr) {
         string target = indexPtr->second;
         findPtr = matchPtr;
         find = index;
         while(true) {
            if(find < 0)
               return false;
            if(*findPtr == indexPtr->second) {
               secondListRev.erase(findPtr);
               matchPtr++;
               secondListRev.insert(matchPtr, target);
               movementRev.push_back(pair<unsigned, unsigned>(find, index-find));
               matchPtr--;
               break;
            }
            findPtr--;
            find--;
         }
      }
      if(indexPtr == _pairList.begin())   break;
      if(movementRev.size() > movement.size())  {
         _reverse = false;
         break;
      }
   }

   // pick the shorter one
   if(_reverse) {
      _movement = movementRev;
      // cout << "reverse picked!" << endl;
   }
   else {
      _movement = movement;
      // cout << "in order picked!" << endl;
   }
   
   return true;
}

bool NameMap::recordMove_block() {

   // sort the two lists
   _pairList.sort(comp);
   _secondList.sort();
   list<string> secondList(_secondList);
   list<string> secondListRev(_secondList);
   vector<Triple> movement, movementRev;

   // find the movements in order
   list<pair<string, string> >::iterator indexPtr = _pairList.begin();
   list<string>::iterator findPtr, matchPtr = secondList.begin(), prePtr = secondList.begin();
   unsigned index = 0, find;
   bool startBlock = false;
   
   while(indexPtr != _pairList.end()) {
      if(indexPtr->second == *matchPtr) {
         // if match, move on to the next one
         indexPtr++;
         index++;
         matchPtr++;
         startBlock = false;
         continue;
      }

      // if not match
      string target = indexPtr->second;
      findPtr = matchPtr;
      find = index;
      
      
      while(true) {
         if(findPtr == secondList.end())
            return false;
         if(*findPtr == indexPtr->second) {
            
            // if not start a block
            if(!startBlock){
               movement.push_back(Triple(find-index, index, 1));
               startBlock = true;
            }
            // if it is alreay start a block
            else{
               // continue the block

               if(prePtr == findPtr){
                  movement.back().third = movement.back().third+1;
                  startBlock = true;
               }
               // new block
               else{
                  movement.push_back(Triple(find-index, index, 1));
                  startBlock = true;
               }
            }
            
            prePtr = findPtr;
            prePtr++;
            secondList.erase(findPtr);
            secondList.insert(matchPtr, target);
            indexPtr++;
            index++;
            break;
         }
         findPtr++;
         find++;
      }
   }

   // find the movements in reverse order
   indexPtr = _pairList.end();
   matchPtr = secondListRev.end();
   prePtr = secondListRev.end();
   index = _pairList.size();
   startBlock = false;
   _blockReverse = true;

   while(index != 0) {
      indexPtr--;
      matchPtr--;
      index--;
      if(indexPtr->second == *matchPtr) {
         // if match, move on to the next one
         startBlock = false;
         continue;
      }

      // if not match
      string target = indexPtr->second;
      findPtr = matchPtr;
      find = index;
      
      
      while(true) {
         if(find == 0){
            return false;
         }
         findPtr--;
         find--; 
         if(*findPtr == indexPtr->second) {
            // if not start a block
            if(!startBlock){
               movementRev.push_back(Triple(find, index-find, 1));
               startBlock = true;
            }
            // if it is alreay start a block
            else{
               // continue the block
               if(prePtr == findPtr){
                  movementRev.back().third = movementRev.back().third+1;
                  startBlock = true;
               }
               // new block
               else{
                  movementRev.push_back(Triple(find, index-find, 1));
                  startBlock = true;
               }
            }
            
            prePtr = findPtr;
            prePtr--;
            secondListRev.erase(findPtr);
            matchPtr++;
            secondListRev.insert(matchPtr, target);
            matchPtr--;
            break;
         }
      }
      if(movementRev.size() > movement.size())  {
         _blockReverse = false;
         break;
      }
   }
   // pick the shorter one
   if(_blockReverse) _blockMovement = movementRev;
   else _blockMovement = movement;

   return true;
}

void NameMap::outputMapIn(const char* outfile) {

   fstream fout;
   fout.open(outfile, ios::out);

   fout << '[' << endl << "\t[";
   list< pair<string, string> >::iterator it = _pairList.begin();
   list< pair<string, string> >::iterator end = _pairList.end();
   end--;
   while(it != end) {
      fout << '"' << it->first << "\", ";
      it++;
   }
   fout << '"' << end->first << "\"]," << endl << "\t[";
   it = _pairList.begin();
   while(it != end) {
      fout << '"' << it->second << "\", ";
      it++;
   }
   fout << '"' << end->second << "\"]" << endl << ']';

   fout.close();
}
   
void NameMap::outputSorted(const char* outfile) {

   fstream fout;
   fout.open(outfile, ios::out);

   fout << '{' << endl;
   list< pair<string, string> >::iterator it = _pairList.begin();
   list< pair<string, string> >::iterator end = _pairList.end();
   end--;
   while(it != end) {
      fout << "  \"" << it->first << "\": \"" << it->second << "\"," << endl;
      it++;
   }
   fout << "  \"" << end->first << "\": \"" << end->second << '"' << endl << '}';
   

   fout.close();

}

#include <map>
#include<iostream>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        bool res=false;
        map<int, int> m;
        for(int i=0;i<nums.size();i++){
            m[nums[i]]++;
        }
        for(auto it=m.begin();it!=m.end();it++){
            cout << it->second;
            if(it->second >=2) res=true;
          
        }
        return res;
    }
};
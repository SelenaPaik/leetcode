class Solution {
public:
    int maxProfit(vector<int>& prices) {
       int min=999999999,maxpf=0,pf=0;
        for(int i=0;i<prices.size();i++){
           if(prices[i]<min) min=prices[i];
           else{
               pf=prices[i]-min;
           }
            if(pf>maxpf) maxpf=pf;
       }return maxpf;
    }
};
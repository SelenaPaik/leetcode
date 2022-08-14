class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        
        //1. dp
        
        int sum=0, smax=INT_MIN;
        for(int num:nums){
            sum+=num;
            smax=max(smax,sum);
            
            // 앞까지 더한 수가 음수면 sum=0으로 하고 그냥 그 위치부터 다시 시작
            // 음수가 아닌 이상은 무조건 더함
            if(sum<0) sum=0;
        }
        return smax;
        
        
        //2. dp 배열 생성하는 방법 -> time limit exceeded
        //dp 배열 생성
        //vector<vector <int>> dp;
//        vector<vector<int>> dp(nums.size(),vector<int>(nums.size(),-99999));
//        
//        if(nums.size()==1) return nums[0];
//        
//        for(int i=0;i<nums.size();i++){
//            for(int j=0;j<nums.size()-i;j++){
//                if(j==0)
//                    dp[i][j]=nums[i];
//                else{
//                    dp[i][j]=dp[i][j-1]+nums[i+j];
//                }
//            }  
//        }
//        
//         for(int i=0;i<nums.size();i++){
//             
//            for(int j=0;j<nums.size()-i;j++){
//                cout << dp[i][j]<<' ';
//                
//            }
//             cout <<'\n';
//         }
//        
//        
//        //max 찾기
//        int max=-99999;
//        for(int i=0;i<dp.size();i++){
//            for(int j=0;j<dp[i].size();j++){
//                if(dp[i][j]>max) max=dp[i][j];
//                cout << max;
//            }
//        }
//            return max;
//
//    }
//    
//
    }
};
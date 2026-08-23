class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> lol;
        for (int i=0; i<nums.size();i++){
            int diff = target - nums[i];
            if (lol.count(diff)){
                return {lol[diff],i};
            }
            lol[nums[i]]=i;
        }
        return {};
         
        
    }
};

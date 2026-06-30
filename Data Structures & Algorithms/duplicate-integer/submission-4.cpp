class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> set{};
        for(int val:nums){
            set.insert(val);
        }
        return nums.size() > set.size();
    }
};

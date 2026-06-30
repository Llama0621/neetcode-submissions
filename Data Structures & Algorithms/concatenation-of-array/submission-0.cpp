class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> new_num{nums};
        for(int val:nums){
            new_num.push_back(val);
        }
        return new_num;
    }
};
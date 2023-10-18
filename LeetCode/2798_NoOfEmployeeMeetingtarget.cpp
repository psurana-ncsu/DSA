class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int count=0;
        int n = hours.size();
        for(int i=0;i<n;i++){
            count=hours[i]>=target?count+1:count;
        }
        return count;
    }
};

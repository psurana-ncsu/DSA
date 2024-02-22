class Solution {
public:
    vector<int> original;
    int answer=0;
    void reverse(int index, int last, int curr){
        if(curr==3){
            answer++;
            return;
        }
        if(index==original.size()){
            return;
        }
        if(original[index]<last){
            backtrack(index+1, original[index], curr+1);
        }
        backtrack(index+1, last, curr);
    }
    void backtrack(int index, int last, int curr){
        if(curr==3){
            answer++;
            return;
        }
        if(index==original.size()){
            return;
        }
        if(original[index]>last){
            backtrack(index+1, original[index], curr+1);
        }
        backtrack(index+1, last, curr);
    }
    int numTeams(vector<int>& rating) {
        int t= rating.size();
        for(int i=0; i<t;i++){
            for(int j=i+1;j<t;j++){
                if(rating[i]>rating[j]){
                    for(int k=j+1;k<t;k++){
                        if(rating[j]>rating[k]){
                            answer+=1;
                        }
                    }
                }
                else{
                    for(int k=j+1;k<t;k++){
                        if(rating[j]<rating[k]){
                            answer+=1;
                        }
                    }
                }

            }
        }
        return answer;
    }
};

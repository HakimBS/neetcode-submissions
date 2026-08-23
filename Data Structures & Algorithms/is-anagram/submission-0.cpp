class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> setS;
        unordered_map<char,int> setT;
        if (s.length() != t.length()){
            return false;
        }
        for (int i=0;i<s.length();i++){
            setS[s[i]]=setS[s[i]]+1;
            setT[t[i]]++;
        }
        return setT==setS;
        
    }
};

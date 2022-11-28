
#include <bits/stdc++.h>
using namespace std;

int main(){

    freopen("input.txt","r",stdin);
    vector<vector<char>> in;
    vector<char> out;
    string s;
    while(getline(cin,s)){
        vector<char>temp;
        bool flag = true;
        for(int i =1 ;i<s.size();i++){
            if(isalpha(s[i])&&flag){
                out.push_back(s[i]);
                flag = false;
                continue;
            }
            if(isalpha(s[i])&& !flag){
                temp.push_back(s[i]);
            }
        }
        in.push_back(temp);
    }
    vector<vector<string>> dependency;
    for(int i = 0;i<in.size();i++){
        for(int j = i+1;j<in.size();j++){
            vector<string> temp;
            if(find(in[j].begin(),in[j].end(),out[i]) != in[j].end())
            {
                temp = "P"+to_string(i)+" and P"+to_string(j)+" are flow-dependent";
            }
            else if(find(in[i].begin(),in[i].end(),out[j]) != in[i].end()){
                temp = "P"+to_string(i)+" and P"+to_string(j)+" are anti-dependent";
                
            }
            else if(out[i]==out[j]){
                temp = "P"+to_string(i)+" and P"+to_string(j)+" are out -dependent";
                
            }
            else {
                temp = "P"+to_string(i)+" and P"+to_string(j)+" are   in-dependent";
            }

            dependency.push_back(temp);
            //cout<<temp<<endl;



        }
    }



    return 0;
}
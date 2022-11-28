#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<vector<char>> in;
    vector<char> out;
    string s;
    freopen("input.txt","r",stdin);

    while(getline(cin,s)){
        vector<char> temp;
        bool flag = true;

        for(int i = 1;i<s.size();i++){
            if(flag && isalpha(s[i])){
                out.push_back(s[i]);
                flag = false;
                continue;
            }
            else if(!flag && isalpha(s[i])){
                temp.push_back(s[i]);
            }
        }
        in.push_back(temp);
    }

    for(int i = 0;i<in.size();i++){

        for(int j = i+1 ;j<in.size();j++){

            if(find(in[j].begin(),in[j].end(),out[i])!=in[j].end()){

                cout<<"P"<<i+1<<" and P"<<j+1<<" are folow-dependent";

            }
            else if(find(in[i].begin(),in[i].end(),out[j])!=in[i].end()){

                cout<<"P"<<i+1<<" and P"<<j+1<<" are anti-dependent";
            }
            else if(out[i]==out[j]){

                cout<<"P"<<i+1<<" and P"<<j+1<<" are output-dependent";

            }
            else{
                cout<<"P"<<i+1<<" and P"<<j+1<<" are in-dependent";

            }
            cout<<endl;

        }
    }


return 0;
}
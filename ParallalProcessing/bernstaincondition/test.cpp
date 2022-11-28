#include <bits/stdc++.h>
using namespace std;

int main(){

    vector<vector<char>> in;
    vector<char> out;
    string s;
    freopen("input.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    
    while(getline(cin,s)){
        vector<char> temp;
        bool flag = true;
        for(int i =1 ;i<s.size();i++){
            if(flag && isalpha(s[i])){
                flag=false;
                out.push_back(s[i]);
            }
            else if(!flag && isalpha(s[i]))
                temp.push_back(s[i]);
        }

        in.push_back(temp);
    }
    vector<vector<int>> dia(out.size(),vector<int>(out.size(),0));
    for (int i =0;i<in.size();i++){

        for(int j = i+1;j<in.size();j++){

            if(find(in[j].begin(),in[j].end(),out[i]) != in[j].end()){
                cout<<"follow dependent p "<<i<<" "<<j<<endl;
                dia[i][j]=1;
                dia[j][i]=1;
            }
            else if(find(in[i].begin(),in[i].end(),out[j])!= in[i].end()){
                cout<<"anti dependent p "<<i<<" "<<j<<endl;
                dia[i][j]=2;
                dia[j][i]=2;
            }
            else if(out[i]==out[j]){
                cout<<"output dependent p "<<i<<" "<<j<<endl;
                dia[i][j]=3;
                dia[j][i]=3;
            }
            else{
                cout<<"in dependent p "<<i<<" "<<j<<endl;
                dia[i][j]= 4;
                dia[j][i]= 4;

            }

        }
    }
    cout<<endl;
    for (auto i : dia){
        for (auto j:i){
            cout<<j<<" ";
        }
        cout<<endl;
    }

}
#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    vector<vector<char>> in;
    vector<char> out;
    
    int line = 0;
    string x;
    while(getline(cin,x)){
        
        bool flag = true;
        vector<char> temp;
        for(int i = 1;i<x.size();i++){
            if(flag && isalpha(x[i])){
                out.push_back(x[i]);
                flag = false;
                continue;
            }
            if(!flag && isalpha(x[i])){
                temp.push_back(x[i]);
            }
        }
        in.push_back(temp);
        line++;
        
    }

    
    // for(auto i : out){
    //     cout<<i<<" ";
    // }cout<<endl;

    // for(auto i : in){
    //     for(auto j :i){
    //         cout<<j<<" ";
    //     }
    //     cout<<endl;
    // }
    
    for(int i = 0;i<line;i++){

        for(int j = i+1;j<line;j++){

            //for first condition ini intersection outj
            if(find(in[i].begin(),in[i].end(),out[j]) != in[i].end()){
                cout << "P" << i+1 << " to P" << j+1 << " : P" << j+1 << " is anti-dependent to P" << i+1 << endl;
                continue;
            }
            //for second condition inj intersection outi
            if(find(in[j].begin(),in[j].end(),out[i]) != in[j].end()){
                cout << "P" << i+1 << " to P" << j+1 << " : P" << j+1 << " is flow-dependent to P" << i+1 << endl;
                continue;
            }
            //for third condition o1 ^ o2
            if(out[i]==out[j]){
                cout << "P" << i+1 << " to P" << j+1 << " : P" << j+1 << " is output-dependent to P" << i+1 << endl;
                continue;
            }
            
            cout << "P" << i+1 << " to P" << j+1 << " : independent" << endl;
            
        }
        
        
    }
    
    
return 0;


}

#include <bits/stdc++.h>
using namespace std;

int main(){

    freopen("input.txt", "r", stdin);
    freopen("outpu.txt", "w", stdout);
    string s;
    vector<vector<char>> in;
    vector<char> out;

    

    while (getline(cin, s))
    {

        vector<char> temp;
        bool flag = true;

        for (int i = 1; i < s.size(); i++)
        {

            if (flag && isalpha(s[i]))
            {
                out.push_back(s[i]);
                flag = false;
                continue;
            }
            if (!flag && isalpha(s[i]))
            {
                temp.push_back(s[i]);
            }
        }
        in.push_back(temp);
    }
    vector<vector<string>> dia(out.size(),vector<string>(out.size()));

    // for (auto i : out)
    //     cout << i << " ";
    // cout << endl;
    // for (auto i : in)
    // {
    //     for (auto j : i)
    //     {
    //         cout << j << " ";
    //     }
    //     cout << endl;
    // }

    //checking bernstin condition

    for(int i = 0;i<in.size();i++){
        for(int j = i+1 ; j<in.size();j++){

            //first condition 
            if(find(in[i].begin(),in[i].end(),out[j]) != in[i].end()){
                //cout<<"P"<<i+1<<" to "<<"P"<<j+1<<" :P"<<j+1<<" is antidependent to P"<<i+1<<endl;
                dia[i][j] = "P"+to_string(j+1)+" is antidependent to P"+to_string(i+1);
                continue;
                
            }
            if(find(in[j].begin(),in[j].end(),out[i]) != in[j].end()){
                //cout<<"P"<<i+1<<" to "<<"P"<<j+1<<" :P"<<j+1<<" is followdependent to P"<<i+1<<endl;
                dia[i][j] = "P"+to_string(j+1)+" is followdependent to P"+to_string(i+1);
                continue;
            }
            if(out[i]==out[j]){
                //cout<<"P"<<i+1<<" to "<<"P"<<j+1<<" :P"<<j+1<<" is outputdependent to P"<<i+1<<endl;
                dia[i][j] = "P"+to_string(j+1)+" is outputdependent to P"+to_string(i+1);
                continue;
            }
            //cout<<"P"<<i+1<<" to "<<"P"<<j+1<<" :P"<<i+1<<",P"<<j+1<<" are independent"<<endl;
            dia[i][j] = "P"+to_string(i+1)+",P"+to_string(j+1)+" are independent";
            cout<<endl;

            cout<<dia[i][j]<<endl;
        }
    }

    

    return 0;
}

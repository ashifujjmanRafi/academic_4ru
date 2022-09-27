#include <bits/stdc++.h>
using namespace std;

vector<int> forbiddenLatency(vector<vector<int>> arr){
    set<int> res;
    for(int i = 0;i<arr.size();i++){
        for(int j = 0;j<arr[i].size();j++){
            if(arr[i][j] == 1){
                for(int k = j+1;k<arr[i].size();k++){
                    if(arr[i][k] == 1){
                        res.insert(k-j);
                    }
                }
            }
        }
    }
    return {res.begin(),res.end()};

}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int col,row;
    cin>>row>>col;
    vector <vector <int>> arr(row, vector<int>(col, 0));
    for(int i = 0;i<row ; i++){
        for(int j = 0 ; j<col ;j++){
            cin>>arr[i][j];
        }
    }
    // for(auto i:arr)
    // {
    //     for(auto j:i)
    //     {
    //         cout<<j<<" ";
    //     }
    //     cout<<endl;
    // }
    vector<int> fl = forbiddenLatency(arr);
    //print fl
    cout<<"Forbidden Latency : ";
    for(auto i: fl){
        cout<<i<<" ";
    }
    cout<<endl;
    
    //permition latency
    vector<int> pl;
    for(int i = 0,j=0;i<col;i++){
        if(i==fl[j]-1){
            j++;
        }
        else
            pl.push_back(i+1);
    }
    cout<<"permitted latency : ";
    for(auto i:pl){
        cout<<i<<" ";
    }
    cout<<endl;

    //collision vector
    vector<int> cv(fl[fl.size()-1],0);
    cout<<"collision vector : ";
    for(int i = 0,j=0;i<fl[fl.size()-1];i++){
        if(i==fl[j]-1){
            cv[i] = 1;
            j++;
        }
    }
    reverse(cv.begin(),cv.end());
    for(auto i:cv){
        cout<<i<<" ";
    }
    return 0;
}
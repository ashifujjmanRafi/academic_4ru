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

void taskTable (vector<vector<int>> &arr, vector<int> &assign) {
    // task initiation
    int i, j, k;
    int row = arr.size();
    int col = arr[1].size();
    int n = assign.size();
    vector <vector<int>> vec(row, vector<int>(col*5, 0));
    for (j = 0; j < col; j++) {
        for (i = 0; i < row; i++) {
            for (k = 0; k < n; k++) {
                if (arr[i][j]) {
                    if (vec[i][j+assign[k]-1] == 0) {
                        vec[i][j+assign[k]-1] = k+1;
                    }
                    else {
                        cout << "Collision found!!!" << endl;
                        cout << "task-" << k+1 << " collides with task-" << vec[i][j+assign[k]-1] << endl;
                        cout << "at stage " << i+1 << " and time " << j+assign[k] << endl;
                        return;
                    }
                }
            }
        }
    }

    cout << "Task table" << endl;
    for (i = 0; i < vec.size(); i++) {
        for (j = 0; j < vec[i].size(); j++) {
            cout << vec[i][j] << " ";
        }
        cout << endl;
    }
    
    cout << "No collision found" << endl;
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

    int n;
    cin>>n;
    vector<int> assign(n);
    for(int i=0;i<n;i++){
        cin>>assign[i];
    }
    taskTable(arr,assign);

    return 0;
}
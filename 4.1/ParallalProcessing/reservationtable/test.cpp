#include <bits/stdc++.h>
using namespace std;

vector<int> forbiddenlatency(vector<vector<int>> arr){
    int r = arr.size();
    int c = arr[0].size();

    set<int> fl;
    for (int i = 0;i<r;i++){
        for(int j = 0;j<c;j++){
            if(arr[i][j]){
                for(int k = j+1;k<c;k++){
                    if(arr[i][k])
                        fl.insert(k-j);
                }
            }
        }
    }
    return {fl.begin(),fl.end()};

}


void taskTable(vector<vector<int>> arr,vector<int> assign){
    int r = arr.size();
    int c = arr[0].size();
    int n = assign.size();
    vector<vector<int>> vec(r,vector<int>(c*5,0));
    for(int j=0;j<c;j++){
        for(int i = 0;i<r;i++){
            for(int k = 0;k<n;k++){
                if(arr[i][j]){
                    if(vec[i][j+assign[k]-1]==0){
                        vec[i][j+assign[k]-1]=k+1;
                    }
                    else{
                        cout<<"collision found between task "<<k+1<<" and task "<<vec[i][j+assign[k]-1]<<" ,at stage "<<i+1<<" time is ,"<<j+assign[k]<<endl;
                        return;
                    }
                        
                }
            }
        }
    }
    cout<<"no collisoion vector found "<<endl;
    for(int i = 0 ; i<vec.size();i++){
        for(int j = 0;j<vec[0].size();j++){
            cout<<vec[i][j]<<" ";
        }
        cout<<endl;
    }
    
}

int main(){
    int r,c ;
    freopen("input.txt","r",stdin);
    cin>>r>>c;
    vector<vector<int>> arr(r,vector<int>(c,0));
    for(int i = 0;i<r;i++){
        for(int j = 0;j<c;j++){
            cin>>arr[i][j];
        }
    }

    vector<int> fl = forbiddenlatency(arr);
    cout<<"forbidden latency : ";
    for(auto i : fl)
        cout<<i<<" ";
    cout<<endl;
    cout<<"permissible latency :";
    vector<int> pl;
    for(int i=0,j=0;i<c;i++){
        if(i==fl[j]-1){
            j++;
        }
        else{
            pl.push_back(i+1);
            cout<<i+1<<" ";
        }
    }
    cout<<endl;
    cout<<"collision vector: ";
    vector<int> cv(fl[fl.size()-1],0);
    for(int i=0,j=0;i<fl[fl.size()-1];i++){
        if(i==fl[j]-1){
            j++;
            cv[i]=1;
        }
    }
    reverse(cv.begin(),cv.end());
    for(auto i : cv)
        cout<<i<<" ";
    cout<<endl;

    int n ;
    cin>>n;
    vector<int> assign(n);
    for(int i = 0;i<n;i++){
        cin>>assign[i];
    }
    taskTable(arr,assign);

}


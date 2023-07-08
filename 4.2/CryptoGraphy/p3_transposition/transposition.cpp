#include <bits/stdc++.h>
using namespace std;

string cipher(string s,int n){
    string cipher = "";
    int col = n;
    for(int i = 0;i<col;i++){
        for(int j = i;j<s.size(); ){
            cipher += s[j];
            j += col;
        }
    }
    return cipher;
}

string decipher(string s,int n){
    string dec = "";
    int cnt = s.size()%n;
    int row = 0;
    if(cnt)
        row = (s.size()/n) + 1;
    else
        row = s.size()/n;

    int total = 0;
    for(int i = 0;i<row;i++){
        int temp = cnt;
        if(temp!=0){
            for(int j = i;j<s.size(); ){
                dec += s[j];
                if(temp){
                    j += row;
                    temp--;
                }
                else
                    j += row-1;
                total++;
                if(total == s.size()){
                    break;
                }
            }
        }
        else{
            for(int j = i;j<s.size(); ){
                dec += s[j];
                j += row;
            }
        }
    }
    return dec;
}


int main(){
        string text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING";
        string enc,dec;
        int n;
        cout<<"enter the collumn num: ";
        cin>>n;
        enc = cipher(text,n);
        cout<<enc<<endl;
        dec = decipher(enc,n);
        cout<<dec<<endl;
    return 0;
}
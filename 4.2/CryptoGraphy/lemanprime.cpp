#include <bits/stdc++.h>
using namespace std;
int power(int a,int n,int mod){
    if(n==0) return 1;
    int ans = power(a,n/2,mod);
    ans = (ans*ans+mod)%mod;
    if(n&1) ans = (ans*a+mod)%mod;
    return ans;
}
int lehmann(int n, int t)
{
    int a = 2 + (rand() % (n - 2));
    // cout <<"random base"<< a << endl;
    int e = (n - 1) / 2;
    // cout <<"exponent"<< e << endl;

    while (t > 0)
    {

        int result = power(a,e,n);
        cout<<result<<endl;
        if (result==1 || result==-1 || result==n-1)
        {
            a = 2 + (rand() % (n - 2));
            t -= 1;
        }
        else
            return -1;
    }
    return 1;
}

int main()
{
    int n ;
    cin>>n;
    int t = 100;
    if (n == 2)
        cout << "2 is Prime.";

    if (n % 2 == 0)
        cout << n << " is Composite";

    else
    {
        int flag = lehmann(n, t);

        if (flag == 1)
            cout << n << " may be Prime.";

        else
            cout << n << " is Composite.";
    }
}

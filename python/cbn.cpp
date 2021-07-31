#include<bits/stdc++.h>
using namespace std;
bool checkprime(int n)
{
    for(int i=2;i*i<n;i++)
    {
        if(n%i==0)
        return false;
        return true;
    }
}
void getprime(int n)
{
    for(int i=2;i<=n;i++)
    {
        if(checkprime(i))
        {
            cout<<i<<" ";
        }
    }
}
int main()
{
    int n;
    cin>>n;
    getprime(n);
    return 0;
}
#include<bits/stdc++.h>
using namespace std;
int updatebit( int n,int pos,int val)
{
    int mask =~(1<<pos);
    n=n & mask;
    return (n|val<<pos);
}
int main()
{
    int n,pos,val;
    cin>>n>>pos>>val;
    cout<<updatebit(n,pos,val);
    return 0;
}
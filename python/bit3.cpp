#include<bits/stdc++.h>
using namespace std;
int toggle(int n,int pos)
{
    return(n xor (1<<pos));
}
int main()
{
    int n,pos;
    cin>>n>>pos;
    cout<<toggle(n,pos);
    return 0;
}
#include<bits/stdc++.h>
using namespace std;
int computexor(int n)
{
    if(n%4==0)
    return n;
    if(n%4==1)
    return 1;
    if(n%4==2)
    return n+1;
    else
     return 0;
}
swap(int a,int b)
{
    a^=b;
    b^=a;
    a^=b;
    cout <<a<<b;
}

int main()
{
    int n,b;
    cin>>n>>b;
    cout<<swap(n,b);
    return 0;
}


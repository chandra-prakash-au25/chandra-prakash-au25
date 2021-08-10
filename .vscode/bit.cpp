#include<bits/stdc++.h>
using namespace std;
int getbit(int n,int pos)
{
    return (n >> pos) & 1;
}
int main()
{
    int n,pos;
    cin >> n >>pos;
    int ans = getbit(n,pos);
    cout <<ans;
    return 0;
}
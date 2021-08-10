#include<iostream>
using namespace std;
int pow(int n,int p)
{
    if(p==0)
    {
        return 1;
    }
    int prev=pow(n,p-1);
    return n*prev;
}
int main()
{
    int n,p;
    cin>>n>>p;
    cout<<pow(n,p)<<endl;
    return 0;
}
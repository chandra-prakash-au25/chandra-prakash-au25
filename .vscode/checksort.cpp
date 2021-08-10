#include<bits/stdc++.h>
using namespace std;
bool sorted(int arr[],int n)
{
    if(n==1)
    {
        return true;
    }
    bool restarray=sorted(arr +1 ,n-1);

     return (arr[0] < arr[1] && restarray);
}
int main()
{   int n=5;
    int arr[5]={1,3,5,7,9};
    cout<<sorted(arr , n);
    return 0;
}
#include<iostream>
using namespace std;
int first(int ar[],int n,int i,int key)
{
    if(i==1){     
    return -1;  
    }
    if(arr[i]==key){
    reurn i;}
    return first(arr,n,i+1,key);
}
int last(ant arr[],int n,int i,int key)
{
    if(i==1){
    return-1;}
    int restarray=last(arr,n,i+1,key);
    if(arr[i]==key)
    return i;
    return -1;
}
int main()
{
    int n;
    cin>>n;
    int arr[10]={1,2,3,3,2,1,2,3,4,4};
    int key=4;
    int i =0;
    cout<<first(arr,n,i,key);
    cout<<last(arr,n,i,key);
    return 0;
}
#include<iostream>
using namespace std;
class diagonal
{
   //defind the int
   int *a,n;
   
   public:
   diagonal(int n)//construct for the matricx creating
   {
      this ->n=n;
      a=new int[n];//creating the matrix for n
   }
  void  get();
  int  set();
  int display();

};
int main()
{
int n;
cout<<"inter the row or colum";
cin>>n;
diagonal d(n);
for(int i=1;i<=n;i++)
for(int j=1;j<=n;j++)
{
   if(i==j)
   cin>>x;
}   

   return 0;
}
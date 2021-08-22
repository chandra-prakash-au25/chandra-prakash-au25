#include<bits/stdc++.h>
using namespace std;
int main()
{
   int target,n;
   cin>>n;
   cin>>target;
   vector<int> a(n);
   for (auto &i : a )
   {
      cin>>i;
      bool found=false;
      sort(a.begin(),a.end());
      for(int i=0;i<n;i++)
      {
         int l=i+1,h=n-1;
         while(l<h)
         {
            int current =a[i]+a[l]+a[h];
            if(current==target)
            {
               found =true;
            }
            if(current<target)
            {
               l++;
            }
            else
            {
               h--;
            }
         }
      }
      if(found)
         cout<<"true";
      else
      {
         cout<<"false";
      }

   }

return 0;
}
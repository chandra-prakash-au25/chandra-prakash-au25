#include<bits/stdc++.h>
using namespace std;
int get_max_area(vector<int> a)
{
   stack<int>st;
    int n=a.size(a),ans=0,i=0;
    a.push_back(0);
    while(i<n)
    {
     while(!st.empty() and a[st.top()]>a[i])  
     {
        int t=st.top();
        int h=a[t];
        st.pop();
        if(st.empty())
        {
           ans=max(ans,h*i);
        }
        else
        {
           int len =i-st.top()-1;
           ans=max(ans,h*len);

        }


     }
     st.push(i);
     i++;

    }
    return ans;
}
int main()
{
   
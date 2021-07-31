#include<bits/stdc++.h>
using namespace std;
string remov(string s)
{
    if(s.length()==0)
    {
        return "";
    }
    char ch=s[0];
    string ans = remov(s.substr(1));
    if(ch == ans[0])
    {
        return ans;
    }
    return ans+ch;
}
int main()
{
    string s ="aaamsmdjldo";
    cout<<remov(s);
    return 0;
}
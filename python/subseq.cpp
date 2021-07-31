#include<bits/stdc++.h>
using namespace std;
void subseq(string s,string ans ="")
{
    if(s.length()==0)
    {
        cout<<ans<<endl;
        return ;

    }
    char ch = s[0];
    string ros = s.substr(1);
    subseq(ros,ans+ch);
    subseq(ros,ans);
    
}
int main()
{    
    string ans = "";
    string s ="abcd";
    subseq(s,ans);
    return 0;
}
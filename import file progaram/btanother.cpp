#include<bits/stdc++.h>
using namespace std;
class node
{
   public:
   int data ;
   node* left;
   node* right;
};
int toSum(node* node)
{
   if(node==NULL)
   {
      return 0;
   }
   int val=node->data;
   node->data=toSum(node->left)+toSum(node->right);
   return node->data+val;
}
int maxDepth(node* node)
{
   if(node==NULL)
   {
      return 0;
   }
   else
   {
      int lDepth=maxDepth(node->left);
      int rDepth=maxDepth(node->right);
      if(lDepth>rDepth)
         return(lDepth+1);
      else
      {
         return(rDepth+1);
      }  
      
   }
}
node* newNode(int data)
{
   node* Node=new node();
   Node->data=data;
   Node->left=NULL;
   Node->right=NULL;
   return(Node);
}
int main()
{
   node* root=newNode(1);
   root->left=newNode(2);
   root->right=newNode(3);
   root->left->left=newNode(4);
   root->left->right=newNode(5);
   cout<<"height of the tree is"<<maxDepth(root);
   cout<<toSum(root);
   return 0;
}
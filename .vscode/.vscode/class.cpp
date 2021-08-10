 #include<iostream>
 using namespace std;
 class A{
    public:
    int a;
    void funcA()
    {
       cout<<"funcA";
    }
    private:
    funcB(){
       cout<<"funcB";
    }
    protected:
    int c;
    void funcC()
    {
       cout<<"funC";
    }
 };
 int main(){

    A obj;
    obj.funcA();
    return 0;
 }
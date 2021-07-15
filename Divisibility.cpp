#include <iostream>

using namespace std;

int main() {

    int N = 0;
    cin>>N;
    
    long data[N];
    for(auto i=0; i<N; i++)
        cin>>data[i];
    
    long rem,num=0;
    for(int i=0;i<N;i++)
    {
        rem = data[i] %10;
        num = num*10 + rem; 
    }

    if(num%10 ==0)
    cout<<"Yes";
    else
    cout<<"No";
    return 0;
}

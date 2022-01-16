#include <bits/stdc++.h>
using namespace std;
int main()
{
    int Testcase;
    cin>>Testcase;
    while(Testcase--)
    {
        int pricegreen,pricepurple;
        cin>>pricegreen>>pricepurple;
        int N;
        cin>>N;
        
        bool problem1;
        bool problem2;
        int count1 = 0; 
        int count2 = 0;

        for(int i = 0 ; i < N; i++)
        {
            cin>>problem1;
            cin>>problem2;
            if(problem1)
            count1++;
            if(problem2)
            count2++;
        }
        int min_price = min((pricegreen*count1)+(pricepurple*count2),(pricegreen*count2)+(pricepurple*count1));
        cout<<min_price<<endl;
    }
    return 0; 
}

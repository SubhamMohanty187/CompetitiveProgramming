#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int len,f=0;
	string s;
	cin>>s;

	len = s.length();
	for(int i=0;i<len/2;i++)
	{
		if(s[i] != s[len-i-1])
		{
			f=1;
			break;
		}
	}
	
	if(f)
	cout<<"NO";
	else
	cout<<"YES";
	return 0;
}

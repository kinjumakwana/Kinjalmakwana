#include<stdio.h>
int fact(int k)
{
int j,f=1;
for(j=1;j<=k;j++)
f*=j;
return f;
}
int main()
{
int t,i,n[100],s[100],j;
scanf("%d",&t);
for(i=0;i<t;i++)
{
scanf("%d",&n[i]);
}
for(j=0;j<t;j++)
{
s[j]=fact(n[j]);
printf("%d \n",s[j]);
}
return 0;
}
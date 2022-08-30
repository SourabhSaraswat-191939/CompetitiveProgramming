#include<stdio.h>
double fib(double n)
{
if (n <= 1)
	return n;
return fib(n-1) + fib(n-2);
}

int main ()
{
double n = 100;
printf("%f", fib(n));
return 0;
}
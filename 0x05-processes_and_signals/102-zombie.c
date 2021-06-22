#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - infinity loop
 * infinite_while(void): infinity loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main function
 * Return: int
 */
int main(void)
{
	int zombie, i = 0;

	while (i < 5)
	{
		zombie = fork();
		if (zombie == 0)
		{
			exit(0);
		}
		else
			printf("Zombie process created, PID: %d\n", getpid());
		i++;
	}
	return (infinite_while());
}

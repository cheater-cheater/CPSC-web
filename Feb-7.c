#include <stdio.h>

int main() {
	int x;
	x = 0;
	while (x<= 20) {
		x = x + 1;
		printf("%d",x);
		if (x % 5 == 0 && x != 0) { 
            printf("\n"); 
        }
    }
	return 0;
}
	

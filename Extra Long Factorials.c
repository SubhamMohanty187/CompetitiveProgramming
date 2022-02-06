#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
    // Support input from 0 to 999
    
    char n[4] = {0};
    scanf("%s",n);
    
    // 999! has 2565 digits, plus a null terminator
    
    char expansion[256] = {0};
    
    // The initial value will be the input (ex: 999 x 998 x 997
    // so fill with chars for 999)
    
    for (int i = 0; i < strlen(n); i++) 
    {
        expansion[i] = n[i];
    }
    
    // Start at one less than the input (ex: 998), and as 
    // long as we're greater than 1 keep decrementing
    // (we don't really need to multiply by 1)
    int start = atoi(n)-1;
    for (int i = start; i > 1; i--) {
       sprintf(n, "%d", i);
       int expansion_d = strlen(expansion); 
       int n_d = strlen(n);
       int total_d = expansion_d + n_d;
       
       int totals[total_d];
       for (int x = 0; x < total_d; x++) {
           totals[x] = 0;
       }
       
       int reset = 0;
       for (int j = n_d - 1; j >= 0; j--) {
           int p = total_d - 1 - reset++;
           for (int k = expansion_d-1; k >= 0; k--) {
               int top = expansion[k] - '0';
               int bottom = n[j] - '0';
               totals[p--] += top*bottom;
           }
       }
        
       for (int p0 = total_d - 1; p0 >= 0; p0--) {
           if (totals[p0] >= 10) {
               int carry = totals[p0] / 10;
               totals[p0] %= 10;
               totals[p0 - 1] += carry;
           }
       }
       
       int notzero = 0;
       int position = 0;
       for (int p0 = 0; p0 < total_d; p0++) {
           if (!notzero && totals[p0] > 0) {
               notzero = 1;
           }
           
           if (notzero) {
                expansion[position] = totals[p0] + '0';
                position++;
           }
       }
    }
    
    printf("%s\n", expansion);
    
    return 0;
}

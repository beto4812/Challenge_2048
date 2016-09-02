#include <stdio.h>
#include <math.h>
#include <sstream>
#include <string.h>

void removeZeroes(long double number, char * res)
{
    char * pos;
    int len;
    int buffer = 200;
    snprintf(res, buffer, "%.12llf", number);
    len = strlen(res);

    pos = res + len - 1;
    while(*pos == '0')
        *pos-- = '\0';
    if(*pos == '.')
        *pos = '\0';
}

//Elegí C++ por que Java no cumplía con los requerimientos de memoria y tiempo de ejecución.
int main()
{
  long double op1, op2, c;
  char operation;
  scanf("%llf %c %llf" , &op1,&operation,&op2);

  if(operation=='+'){
	 c = op1+op2;
  }else if(operation=='-'){
  	 c = op1-op2;
  }else if(operation=='*'){
  	c = op1*op2;
  }else if(operation=='/'){
  	c = op1/op2;
  }else if(operation=='%'){
  	c = fmod(op1, op2);
  }

  char out[200];
  removeZeroes(c, out);

  printf("%s", out);
}

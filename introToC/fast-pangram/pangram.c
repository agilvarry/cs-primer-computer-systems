#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/types.h>


bool ispangram(char *s) {
  // TODO implement this!
  int bs = 0;
  printf("hello\n");
  for(int i = 0; i < strlen(s); i++){
    bs = (bs & (1 << tolower(s[i])-'a'));
   
    printf("%c:  %d: %d \n", s[i], 1<< s[i]-'a', bs);
  }
  
  return bs ==0x03ffffff;
}

int main() {
  size_t len;
  ssize_t read;
  char *line = NULL;
  // ispangram("hello");
  // while ((read = getline(&line, &len, stdin)) != -1) {

    
    if (ispangram("abcdefghijklmnopqrstuvwxyz")){
        printf("%s", line); 
    }
      
  // }

  // if (ferror(stdin))
  //   fprintf(stderr, "Error reading from stdin");

  // free(line);
  // fprintf(stderr, "ok\n");
}

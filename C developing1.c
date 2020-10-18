#include <stdio.h>

int main(void) {
  int scores[5], max;
  int i;
  for (i = 0; i < 5; i++) {
    printf("%d번째 정수를 입력하세요: ", i + 1);
    scanf("%d", &scores[i]);
  }
  max = scores[0];
  for (i = 0; i < 5; i++) {
    if (max < scores[i]) {
      max = scores[i];
    }
  }
}

printf("가장 큰 정수값은 %d 입니다\n", max);

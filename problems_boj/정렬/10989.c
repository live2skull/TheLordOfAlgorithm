#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
python3 로 구현하였으나 메모리 초과로 c 재구현
output 배열 없이 카운팅 저장 공간을 이용해 낮은 수부터 반복하여 출력해 문제 풀이

1. 메모리 초과 -> 입력 / 카운트 배열을 unsigned short로 구성
2. 메모리 초과 -> 현재 문제 풀이방법으로 입력값을 저장할 필요가 없음.
*/

int main(int argc, char** argv)
{
    int n;
    scanf("%d", &n);

    short *ct = (short*)malloc(10001 * sizeof( short));
    memset(ct, 0, 10001 * sizeof(short));

    for (int i = 0; i < n; i++)
    {
        short t;
        scanf("%hu", &t);
        ct[t] += 1;
    }

    for (int i = 1; i < 10001; i++)
    {
        if (ct[i] == 0) continue;
        for (int j = 0; j < ct[i]; j++) printf("%d\n", i);
    }

    return 0;
}
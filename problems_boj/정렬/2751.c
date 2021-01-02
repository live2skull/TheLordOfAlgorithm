#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/// TODO python으로 먼저 시뮬레이션 작성 후, c언어로 다시 포팅할 것.

/*
퀵 정렬을 이용하여 문제를 풀어냅니다.
시간 복잡도 : O(nlogn)
*/


/*
quick sort - 피벗을 기준으로 두 개의 비균등한 크기로 배열을 분할.
분할된 부분 리스트를 정렬한 다음,
두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법.

분할(divide) : 피벗을 중심으로 배열을 나눔 (왼쪽 작은값 오른쪽 큰 값)
정복(conquer) : 부분 배열을 정렬
결합(combine) : 정렬된 부분 배열들을 하나의 배열에 합병
*/


// pivot을 지정하고 배열을 정렬합니다.
// 지정한 pivot의 인덱스를 반환하며, 이 때 pivot의 기준으로 배열이 정렬되어 있습니다.
int partition(int* arr, int left, int right)
{
    // partition 함수에서도 시작 전 left, right의 범위가 올바른지 확인이 필요하다.
    if (left >= right) return;

    int pivot, temp; // 피벗 값

    int l = left; // 검색 왼쪽 인덱스
    int r = right; // 검색 오른쪽 인덱스

    pivot = arr[(left + right) / 2]; // 중간값을 피벗으로 갖는다.

    /*
    1. 왼쪽 기준값과 오른쪽 기준값을 각각 올겨야 하는지 체크

    */

    while (l <= r)
    {
        // pivot값에 문제가 없는 경우
        while (arr[l] < pivot) l++;
        while (arr[r] > pivot) r--;
        if (l <= r)
        {

            temp = arr[r];
            arr[r] = arr[l];
            arr[l] = temp;
            l++, r--;
        }
    }

    // l과 r이 교차하는 지점에서 실행이 종료되며, r값이 피벗이 된다.
    // r is -1?

    return r;

}


// 확인할 범위 지정
void quick_sort(int *arr, int left, int right)
{
    // 시작 포인터가 종료 포인터보다 크면 동작의 의미가 없다.
    if (left > right) return;

    // pivot 기준으로 정렬하고, 해당 pivot 값을 받아옵니다.
    int p = partition(arr, left, right);

    // 시작점부터 피벗 전까지
    quick_sort(arr, left, p-1);
    // 피벗부터 끝점까지 (pivot이 포함되지 않는것은 아니다)
    quick_sort(arr, p, right);
}


int main(int argc, char** argv)
{
    int n;
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(arr));
    memset(arr, 0, n * sizeof(int));
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    // n-1 : 배열의 끝 index
    quick_sort(arr, 0, n-1);

    for (int i = 0; i < n; i++) printf("%d\n", arr[i]);
}
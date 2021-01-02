#include <iostream>
int n,cnt, arr[10000001];

void quickSort(int i, int j)
{
    // 유효한 범위인지 확인
	if(i>=j) return;
	// pivot 기준 값 설정
	int pivot = arr[(i+j)/2];
	// 탐색 값 설정
	int left = i;
	int right = j;

    // left, right가 교차되지 않은 지점에서 검색 실행
	while(left<=right)
	{
		while(arr[left]<pivot) left++;
		while(arr[right]>pivot) right--;
		if(left<=right)
		{
		    int tmp;
		    tmp = arr[right];
		    arr[right] = arr[left];
		    arr[left] = tmp;
			left++; right--;
		}
	}
	quickSort(i,right); quickSort(left,j);
}

int main()
{
	scanf("%d",&n);
	for(int i = 0; i < n; i++)
		scanf("%d",&arr[i]);

	quickSort(0,n-1);

	for(int j = 0; j < n; j++) // 출력
		printf("%d\n",arr[j]);
}
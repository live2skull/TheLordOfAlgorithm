// 숫자 (N-1)개, 연산자 (N-2)개
// 복잡도는 O(2^(N-2))
#include <iostream>

using namespace std;

// dp는 설정하는 변수의 의미가 가장 중요한 것 같다
// d[i][j] -> i까지의 수로 j를 만드는 방법의 수
long long d[101][21];
int n,num[101];

int main()
{
    cin >> n;
    for(int i = 1;i<=n;i++) cin >> num[i];
    
    //맨 처음 수를 만드는 방법은 1가지
    d[1][num[1]] = 1;
    
    for(int i = 2;i<n;i++){
        for(int j = 0;j<=20;j++)
        {
            // 마지막 수를 더했으면 : num[1] +- .... + num[i] = j; -> 만들어진 수는 j-num[i] -> d[i-1][j-num[i]]
            // 마지막 수를 뺐으면 : num[1] +- .... - num[i] = j; -> 만들어진 수는 j+num[i] -> d[i-1][j+num[i]]
            //계산한 수는 [0,20]
            if(j-num[i] >= 0) d[i][j] += d[i-1][j-num[i]];
            if(j+num[i] <= 20) d[i][j] += d[i-1][j+num[i]];
        }
    }
    cout << d[n-1][num[n]] << endl;
}

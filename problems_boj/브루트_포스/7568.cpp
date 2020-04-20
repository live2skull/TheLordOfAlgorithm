#include <iostream>
#include <vector>

using namespace std;

// 원래는 재귀로 구현할려 했으나 그 다음 인덱스 비교와 랭크 매기는게 for가 훨씬 간단
int main(){
    int n;
    cin >> n;
    
    vector<pair<int,int>> people(n);
    vector<int> rank(n);
    
    for(int i = 0;i<n;i++) cin >> people[i].first >> people[i].second;
    
    for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<n;j++)
        {
            if (i == j) continue;
            // 두 인덱스의 인자들을 다 비교해서 랭크가 정해지는 경우(덩치가 나눠지는 경우)
            if(people[i].first > people[j].first && people[i].second > people[j].second) {
                // j를 사용한 이유는 더 작은 애들 인덱스의 카운트를 계속 증가시켜 가장 큰 애를 1순위로 매기고
                // 랭크 매길 수 없는 애들은 넘기기 편하다
                rank[j]++;
            }
        }
    }
    
    for(int i = 0;i<rank.size();i++){
        cout << rank[i]+1 << ' ';
    }
    cout << '\n';
    return 0;
}

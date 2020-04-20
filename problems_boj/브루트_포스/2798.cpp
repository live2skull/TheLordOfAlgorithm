#include <iostream>
#include <vector>

using namespace std;

int n,m,res;

// 종료해야 하는 사례 -> 3장넘게 뽑았거나 합이 M을 넘어가면 안됨
void search(vector<int>& a,int card, int index, int max){
    
    // 3장을 다 뽑으면
    if(card == 3){
        // m보다 작으면
        if(max <= m){
            // 최댓값
            if(res < max){
                res = max;
            }
            return;
        }
    }
    
    if(max > m || card > 3 || index > n){
        return;
    }
    
    search(a,card+1,index+1,max+a[index]); // 선택했으면
    search(a,card,index+1,max); // 선택 안 했으면
    
}
int main(){
    cin >> n >> m;
    vector<int> tile(n);
    
    for(int i = 0;i<n;i++) {
        cin >> tile[i];
    }
    
    search(tile,0,0,0);
    
    cout << res << endl;
    return 0;
}

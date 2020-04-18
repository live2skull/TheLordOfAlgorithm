#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n;
int status[21][21];

// 순차적으로 사람을 링크팀에 넣을 지 스타트팀에 넣을 지 판단
int find(vector<int>& link,vector<int>& start, int index){
    //사람을 다 맵핑하면(n명)
    if(index == n){
        //팀 맴핑한 애들에서 차이를 구한다
        int t1=0,t2=0;
        for(int i = 0;i<link.size();i++){
            for(int j = 0;j<link.size();j++){
                if(i == j) continue;
                //같은 팀이 됐을 때 케미
                t1 += status[link[i]][link[j]];
            }
        }
        for(int i = 0;i<start.size();i++){
            for(int j = 0;j<start.size();j++){
                if(i == j) continue;
                t2 += status[start[i]][start[j]];
            }
        }
        int diff = abs(t1-t2);
        return diff;
    }
    
    //팀 맵핑
    //링크팀으로 넣어보고
    int ans = -1; // -> 아직 미정이거나 잘못된 값을 -1이라고 하자
    link.push_back(index);
    int t1 = find(link,start,index+1);
    if(ans == -1 || (t1 != -1 && ans > t1)){  // 답이 정해지지 않았거나 최솟값을 뽑을 수 있으면
        ans = t1;
    }
    //다시 스타트팀에 넣어서 비교해야 하기 때문에 pop
    link.pop_back();
    
    //스타트팀으로
    start.push_back(index);
    int t2 = find(link,start,index+1);
    if(ans == -1 || (t2 != -1 && ans > t2)){
        ans = t2;
    }
    start.pop_back();
    return ans;
}


int main()
{
    cin >> n;
    for(int i = 0;i<n;i++) {
        for(int j = 0;j<n;j++){
            cin >> status[i][j];
        }
    }
    vector<int> link,start;
    cout << find(link, start, 0) << endl;
    
    return 0;
}

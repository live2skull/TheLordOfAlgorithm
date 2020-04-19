#include <iostream>
#include <queue>

using namespace std;

bool visit[10001];
int n,start,destination;

void search(){
    //계속 변하는 수와 실행한 문자열 저장
    queue<pair<int,string>> q;
    q.push(make_pair(start, ""));
    
    visit[start] = true;
    
    while(!q.empty()){
        int num = q.front().first;
        string temp = q.front().second;
        q.pop();
        
        if(num == destination){
            cout << temp << '\n';
            return;
        }
        
        // 2배
        int cur = 2 * num % 10000;
        if(!visit[cur]){
            visit[cur] = true;
            q.push({cur,temp+"D"});
        }
        //하나 빼는 거
        cur = (num-1) < 0 ? 9999 : (num-1);
        if(!visit[cur]){
            visit[cur] = true;
            q.push({cur,temp+"S"});
        }
        // 왼쪽으로 미는 거
        cur = (num % 1000) * 10 + num / 1000;
        if(!visit[cur]){
            visit[cur] = true;
            q.push({cur,temp+"L"});
        }
        // 오른쪽으로 미는 거
        cur = (num % 10) * 1000 + (num / 10);
        if(!visit[cur]){
            visit[cur] = true;
            q.push({cur,temp+"R"});
        }
    }
}
int main()
{
    cin >> n;
    while(n--){
        cin >> start >> destination;
        memset(visit, false, sizeof(visit));
        search();
    }
    
    return 0;
}

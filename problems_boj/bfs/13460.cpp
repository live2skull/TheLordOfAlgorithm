#include <iostream>
#include <queue>

using namespace std;

//빨간공 좌표, 파란공 좌표, 움직인 횟수
struct ball{
    int ry,rx,by,bx,cnt;
};
//초기
ball start;
char map[11][11];
int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};
bool visit[11][11][11][11];

int search()
{
    queue<ball> q;
    
    q.push(start);
    visit[start.ry][start.rx][start.by][start.bx] = true;
    
    while(!q.empty())
    {
        ball cur = q.front();q.pop();
        //10번 지나면 -1 출력
        if(cur.cnt > 10) return -1;
        // 답
        if(map[cur.ry][cur.rx] == 'O' && map[cur.by][cur.bx] != 'O')
        {
            return cur.cnt;
        }
        
        for(int i = 0;i<4;i++)
        {
            int next_ry = cur.ry;
            int next_rx = cur.rx;
            int next_by = cur.by;
            int next_bx = cur.bx;
            
            //한번 기울이면 갈 수 있을 때 까지 가므로 while
            while(1)
            {
                if(map[next_ry][next_rx] != '#' && map[next_ry][next_rx] != 'O')
                {
                    next_ry += dy[i];
                    next_rx += dx[i];
                }
                else{
                    //현 상태가 #이므로 왔던 방향 반대로 한칸 움직인다
                    if(map[next_ry][next_rx] == '#')
                    {
                        next_ry -= dy[i];
                        next_rx -= dx[i];
                    }
                    break;
                }
            }
            //파란공도 마찬가지로
            while(1)
            {
                if(map[next_by][next_bx] != '#' && map[next_by][next_bx] != 'O')
                {
                    next_by += dy[i];
                    next_bx += dx[i];
                }
                else{
                    if(map[next_by][next_bx] == '#')
                    {
                        next_by -= dy[i];
                        next_bx -= dx[i];
                    }
                    break;
                }
            }
            //두 공이 같은 위치에 와 있으면
            if(next_ry == next_by && next_rx == next_bx)
            {
                if (map[next_ry][next_rx] != 'O') {
                //움직인 거리가 긴 애가 나중에 도착한 애 이므로
                int len_r = abs(next_ry - cur.ry)+abs(next_rx - cur.rx);
                int len_b = abs(next_by - cur.by)+abs(next_bx - cur.bx);
                //하나 빼줘
                if(len_r > len_b) {
                    next_ry -= dy[i];
                    next_rx -= dx[i];
                }
                
                else {
                    next_by -= dy[i];
                    next_bx -= dx[i];
                }
              }
            }
            
            if(!visit[next_ry][next_rx][next_by][next_bx])
            {
                visit[next_ry][next_rx][next_by][next_bx] = true;
                //그 다음 상태를 설정하고 push
                ball next;
                next.ry = next_ry;
                next.rx = next_rx;
                next.by = next_by;
                next.bx = next_bx;
                next.cnt = cur.cnt+1;
                q.push(next);
            }
        }
    }
    return -1;
}


int main() {
    
    int n, m;
    
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for(int j = 0;j<m;j++){
            cin >> map[i][j];
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (map[i][j] == 'R') {
                start.ry = i;
                start.rx = j;
            }
            if (map[i][j] == 'B') {
                start.by = i;
                start.bx = j;
            }
        }
    }
    start.cnt = 0;
    
    cout << search() << endl;
    
    return 0;
}

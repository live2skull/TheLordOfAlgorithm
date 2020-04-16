#include <iostream>
#include <vector>
using namespace std;

vector<pair<int, int>> wolf;
vector<pair<int, int>> sheep;

int n, m;
char map[251][251];
bool visit[251][251];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
int cnt_w,cnt_s,wolf_cnt,sheep_cnt;

void search(int y, int x){
    
    visit[y][x] = true;
    
    for(int i = 0;i<4;i++)
    {
        //상하좌우 다 돌면서
        int ny = y + dy[i];
        int nx = x + dx[i];
        
        if(ny >= 0 && ny < n && nx >= 0 && nx < m)
        {
            // 방문하지 않았고 움직일 수 있으면
            if(!visit[ny][nx] && map[ny][nx] != '#')
            {
                //방문 체크
                visit[ny][nx] = true;
                
                if(map[ny][nx] == 'o')
                {
                    // 양의 위치를 저장
                    sheep.push_back({ny,nx});
                    // 마리 수 비교를 위해 카운트 저장
                    sheep_cnt++;
                }
                else if(map[ny][nx] == 'v'){
                    wolf.push_back({ny,nx});
                    wolf_cnt++;
                }
                search(ny,nx);
            }
        }
    }
}
int main(){
    
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)  scanf("%s", map[i]);
    
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            //늑대가 있는 곳이 문제가 되는 곳이므로 체크
            if (map[y][x] == 'v') {
                //처음 발견한 늑대의 위치와 카운트 체크
                wolf_cnt++;
                wolf.push_back({y,x});
                search(y,x);
                //양이 더 많으면 늑대를 씹어 먹으므로
                if(sheep_cnt > wolf_cnt){
                    //맵의 위치에서 진 애들을 전부 '.' (빈 필드) 으로 만들어준다
                    for(int i = 0;i<wolf.size();i++)
                    {
                        map[wolf[i].first][wolf[i].second] = '.';
                    }
                }
                else{
                    for(int i = 0;i<sheep.size();i++)
                    {
                        map[sheep[i].first][sheep[i].second] = '.';
                    }
                }
                //서치가 다 끝나면 다시 초기화
                wolf_cnt = 0;
                sheep_cnt = 0;
                wolf.clear();
                sheep.clear();
            }
        }
    }
    
    for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            if(map[i][j] == 'o') cnt_s++;
            else if(map[i][j] == 'v') cnt_w++;
        }
    }
    
    cout <<cnt_s << ' ' << cnt_w << '\n';
    
    return 0;
}

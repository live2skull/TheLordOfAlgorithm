#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <queue>

using namespace std;

int N = 0, M = 0;

int** check;
int** map;
int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; // direction of up, down, left, right

bool isInMap(int x, int y)
{
    // 0보다 크거나 같다. (인덱스가 0부터 시작하므로)
    return (x >= 0 && x < N && y >= 0 && y < M);
}

// result: hop count
int bfs()
{
    queue<pair<int, int> > q;
    q.push(pair<int, int> (0, 0));
    check[0][0] = 1;
    
    while (!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();
        
        int cur_x = cur.first;
        int cur_y = cur.second;
        
        int hop = check[cur_x][cur_y];
        
        if (cur_x == (N - 1) && cur_y == (M - 1)) return hop;
        
        for (int i = 0; i < 4; i++)
        {
            int next_x = cur_x + dir[i][0];
            int next_y = cur_y + dir[i][1];
            
            // printf("%d %d -> %d %d \n", next_x, next_y, check[next_x][next_y], isInMap(next_x, next_y));
            
            // 맵도 체크를 해야한다. (길이 있어야지)
            if (isInMap(next_x, next_y) && check[next_x][next_y] == 0 && map[next_x][next_y] == 1)
            {
                q.push(pair<int, int> (next_x, next_y));
                check[next_x][next_y] = hop + 1; // 아직 방문하지 않았지만 카운트를 미리 설정
                
            }
        }
    }
    
}


void input()
{
    // char* buf = (char*)malloc(sizeof(char) * (M + 1));
    char* buf = (char*)calloc(M + 1, sizeof(char));
    
    for (int i = 0; i < N; i++)
    {
        scanf("%s", buf);
        for (int j = 0; j < M; j++)
        {
            char b = buf[j];
            map[i][j] = (b == '1' ? 1 : 0);
        }
    }
}


int main(int argc, char** argv)
{  
    scanf("%d %d", &N, &M);
    
    // M => N (잘못된 할당)
    // 할당되지 않은 공간에 메모리를 할당하려고 함
    check = (int**)calloc(N, sizeof(int*));
    for (int i = 0; i < N; i++) check[i] = (int*)calloc(M, sizeof(int));
    
    map = (int**)calloc(N, sizeof(int*));
    for (int i = 0; i < N; i++) map[i] = (int*)calloc(M, sizeof(int));
    
    input(); 
    
    // for(int i = 0; i < N; i++)
    // {
    //     for (int j = 0; j < M; j++)
    //     {
    //         printf("%d", check[i][j]);
    //     }
    //     printf("\n");
    // }
    
    int result = bfs();
    printf("%d", result);
}

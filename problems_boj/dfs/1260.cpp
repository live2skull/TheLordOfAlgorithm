#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <queue>

using namespace std;

int** matrix;
int* visited;

int N = 0, E = 0, V = 0; // 간선의 갯수가 필요한가?


void bfs(int v)
{
    queue<int> q;
    q.push(v);
    visited[v] = 1;
    
    while (!q.empty())
    {
        int t = q.front();
        printf("%d ", t); // 이렇게 되면 
        q.pop();
        
        for (int i = 1; i <= N; i++)
        {
            // target:  t -> i!
            if (visited[i] || matrix[t][i] != 1) continue;
            q.push(i);
            visited[i] = 1;
        }
        
    }
}


void dfs(int v)
{
    visited[v] = 1;
    printf("%d ", v);
    for (int i = 1; i <= N; i++)
    {
        if (visited[i] || matrix[v][i] != 1) continue;
        dfs(i);
    }
}

int main(int argc, char** argv)
{  
    scanf("%d %d %d", &N, &E, &V);
    
    visited = (int*)malloc(sizeof(int) * (N + 1));
    matrix = (int**)malloc(sizeof(int*) * (N + 1));
    for (int i = 0; i <= N; i++) matrix[i] = (int*)malloc(sizeof(int) * (N + 1));
    
    // 간선의 갯수만큼 반복
    for (int i = 0; i < E; i++)
    {
        int a = 0, b = 0;
        scanf("%d %d", &a, &b);
        matrix[a][b] = matrix[b][a] = 1;
    }
    
    // printf("\n");
    // for (int i = 1; i <= N; i++)
    // {
    //     // show matrix
    //     for (int z = 1; z <= N; z++) printf("%d", matrix[i][z]);
    //     printf("\n");
    // }
    
    dfs(V);
    printf("\n");
    memset(visited, 0, sizeof(int) * (N + 1));
    bfs(V);
    
    free(visited);
    for (int i = 0; i <= N; i++) free(matrix[i]);
    free(matrix);
}

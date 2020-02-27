package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// 1316: 그룹 단어 체커
/*
한 단어별로 체크

- 기존에 등장한 알파벳이지만, 떨어진 후 다시 나온 경우 삭재.
- 연속해서 나온 후 다시 나오지 않은 경우 상관 없음.

*/

// 주요사항
// TODO: for문 처리 시 offset => for ((declare)) 에 넣지 않고 내부 함수에서 처리
// idx = 0 OR idx = LAST 예외처리: for 함수문이 아닌 외부에서 처리


public class Main {

    // TODO: 문제를 끝까지 읽고 풀어야 할 필요가 있음.
    // 굳이 구현하지 않아도 되는 부분을 구현하곤 한다.

    public static int indexOfChar(char[] arr, char find)
    {
        for (int i = 0; i < arr.length; i++)
        {
            if (arr[i] == find) return i;
        }
        return -1;
    }

    // TODO: null & 0 => char 자료형에서의 차이점?

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int length = sc.nextInt();
        sc.nextLine(); // flush!

        int result = 0;

        for (int z = 0; z < length; z++)
        {

            char[] in = sc.nextLine().toCharArray();

            int[] alpha = new int[26];
            Arrays.fill(alpha, 0);

            // 0 : 아직 등장하지 않음.
            // 1 : 등장했고, 유효상태
            // -1 : 등장하였으나, 그룹 단어가 아니다.

            alpha[(int)in[0] - 97] = 1; // 처음 단어는 바로 산입.
            // TODO: 0번에서 예외 처리할 경우
            // for문에서 if처리가 아닌 밖에서 실행 후 for문을 i=1부터 시자한다.

            for (int i = 1; i < in.length; i++)
            {
                switch (alpha[(int)in[i] - 97])
                {
                    case 0: // 아직 등장하지 않음.
                        alpha[(int)in[i] - 97] = 1;
                        break;

                    case 1: // 알파벳이 등장했고, 아직 유효 상태임.
                        // 유효 상태인데, 전 단어에 없는 경우 -> 무효 상태가 된다.
                        if (in[i - 1] != in[i]) alpha[(int)in[i] - 97] = -1;
                        break;

                    case -1: // 알파벳이 등장했으나, 유효 상태가 아님.
                        // 한번 유효 상태가 아니였으므로 별도의 조치가 필요 없음.
                        break;
                }
                // 1. 이미 등장했던 알파벳인지 확인함.
                // 2. 알파벳이 이미 등장했고, 전 단어에 없음.
                // 3. 알파벳이 이미 등장했고, 전 단어에 있음.
            }

            boolean isGroup = true;
            for (int value:  alpha)
            {
                if (value == -1)
                {
                    isGroup = false;
                    break;
                }
            }

            if (isGroup) result++;

//            int cnt = 0;
//            for (int value : alpha) if (value == 1) cnt++;

        }

        System.out.println(result);

    }
}


import java.util.Scanner;

// List 뒤집기 구현 : Collections.reverse(...) => List<...>가 제네릭 - 인터페이스이므로 가능.

public class Main {

    /*
    * Array - 일반 배열형 구현
    * List - Linked-List 구현
    * */

    // asList 변경 후 뒤집지 않고 직접 배열 상태에서 추가 메모리 할당없이 reverse 구현
    public static void reverse(char[] arr)
    {
        // 서로 바꿔치기
        // 짝수, 홀수일 때 전부 문제가 없다.
        // 크기가 0, 1, 2 일때의 예외처리도 별도로 없음.
        for (int i = 0; i < arr.length / 2; i++)
        {
            int tptr = (arr.length - 1) - i; // reverse 대상 포인터

            // TODO: "char t" 해당 공간이 반복문에서 계속사용 or 실행시마다 새로할당?
            char t = arr[i]; arr[i] = arr[tptr]; arr[tptr] = t;
        }

        // arr 기존 배열에서 데이터를 거꾸로 하여 출력
        // 짝수개배열 / 홀수개배열일 때가 존재
        // 각 위치 데이터를 temp를 이용하여 서로 바꾼다.

        /* 짝수일 경우
        * 0 1 2 3 4 5
        * len:4 pt:2
        * for (int i = 0; i <= arr.length / 2; i++)
        **/

        /* 홀수일 경우
        * 0 1 2 3 4
        * len:5 pt:2
        **/ // => 결국 짝수, 홀수일 때 예외처리 없이 동일히 실행 가능하다.
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] a = Integer.toString(sc.nextInt()).toCharArray();
        char[] b = Integer.toString(sc.nextInt()).toCharArray();

        reverse(a);
        reverse(b);

        int c = Integer.parseInt(String.copyValueOf(a));
        int d = Integer.parseInt(String.copyValueOf(b));

        System.out.println(Math.max(c, d));
    }
}

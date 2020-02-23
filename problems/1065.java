// 2020. 02. 23

import java.util.Arrays;
import java.util.Scanner;



public class Main {

    //TODO: Integer 값의 각 자릿수를 분해하기
    // #1. 해당 값을 toString / toCharArray 변환하여 확인
    // #2. 10 * n % 형태로 계산? 성능 분석을 해보지 않음.
    public static int[] convert(int num)
    {
        char[] buf = Integer.toString(num).toCharArray();

        int[] result = new int[buf.length];

        for (int i = 0; i < buf.length; i++)
            result[i] = Character.getNumericValue(buf[i]);

        return result;
    }

    // 자릿수 나눗셈으로 string 변환 없이 각 자릿수를 추출한다.
    // http://blog.naver.com/occidere/220790000403
    public static int[] convert_fast(int num)
    {
        int[] result = new int[1000]; // 버퍼 크기에 대해서만 고려하면 된다.
        int i = 0;

        while (num > 0)
        {
            // num 이 Integer이므로 마지막 1의자리수 연산이 중료된다면 0이 되여 반복문을 빠져나가게 된다.
            result[i] = num % 10;
            num /= 10; i++;
        }

        return result;
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int count = 0;

        for (int i = 1; i <= num; i++)
        {
            int[] arr = convert(i);

            int offset = 0;
            boolean isHan = true;

            for (int j = 0; j < arr.length - 1; j++)
            {
                int _offset = arr[j] - arr[j+1];

                if (j == 0) offset = _offset;
                else if (offset != _offset)
                {
                    isHan = false;
                    break;
                }
            }

            if (isHan) count++;
        }

        System.out.println(count);
    }
}
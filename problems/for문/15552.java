// 2020. 02. 22

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    
    public static void main(String[] args) 
    {
        // https://coding-factory.tistory.com/251
        // Scanner, System.out.println 을 사용할 경우 입출력 단계에서의 소요 시간으로 시간초과가 발생할 수 있다.
        
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int sz = 0;
        
        try 
        {
            // sz가 밖에 있다면 이렇게 참조하는 것이 맞는가? // +=, == 컴파일시 에러는 없음
            // 초기화가 되지 않은 경우 컴파일 에러 발생.
            sz += Integer.parseInt(bf.readLine());
            
            for (int i = 0; i < sz; i++)
            {
                /// 한문자씩으로 받아보기. (using read)
                String[] t = bf.readLine().split(" "); // strip -> trim | strip 이 아니라 split 아니었나??
                // bw.write(String.format("%d\n", Integer.parseInt(t[0]) + Integer.parseInt(t[1])));
                // 문자열을 합성하는 String.format 합성 과정에서 시간이 더 걸리는 듯 함. 굳이 버퍼를 만들고 할 필요는 없었음.
                bw.write(Integer.toString((Integer.parseInt(t[0]) + Integer.parseInt(t[1]))));
                bw.write('\n');
            }
            bw.flush();
            bw.close();
            
        } 
        catch (IOException e) 
        {
            //throw e;
        }
    }
} 
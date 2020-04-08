package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 10845 큐 - 큐
// 2020. 03. 28


public class Main
{
    public static void main(String[] args) throws Exception
    {

        Scanner sc = new Scanner(System.in);

        // LinkedList에서 Queue가 필요로 하는 멤버함수를 모두 구현하였음.
        Queue<Integer> q = new LinkedList<Integer>();
        LinkedList<Integer> l = (LinkedList<Integer>)q; // linked list의 기능을 사용한다.

        int count = sc.nextInt();
        int index = 0;

        while (index <= count)
        {
            String[] s_arr = sc.nextLine().split(" ");
            String command = s_arr[0];

            switch (command)
            {
                case "push":
                    int val = Integer.parseInt(s_arr[1]);
                    q.offer(val);
                    break;

                case "pop":
                    if (q.isEmpty()) System.out.println(-1);
                    else System.out.println(q.poll());
                    break;

                case "size":
                    System.out.println(q.size());
                    break;

                case "empty":
                    System.out.println(q.isEmpty() ? 1 : 0);
                    break;

                case "front":
                    if (q.isEmpty()) System.out.println(-1);
                    else System.out.println(l.getFirst());
                    break;

                case "back":
                    if (q.isEmpty()) System.out.println(-1);
                    else System.out.println(l.getLast());
                    break;
            }


            index++;
        }
    }
}
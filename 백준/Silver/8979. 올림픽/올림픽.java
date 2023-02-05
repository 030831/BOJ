import java.io.*;
import java.util.*;

class Olympic {
    int[] score = new int[4];
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter( new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int Index=0,  total = 1;

        Olympic[] op = new Olympic[N];


        for (int i = 0 ; i < N ; i++) {
            op[i] = new Olympic(); // 객체 인스턴스 생성.

            StringTokenizer st2 = new StringTokenizer(br.readLine()); // 공백을 두고 배열을 입력받기 때문에 한번더 사용.

            for (int j = 0 ; j < 4 ; j++) {
                op[i].score[j]=Integer.parseInt(st2.nextToken());
            }

            if (op[i].score[0]==M) {
                Index=i; // 원하는 국가의 인덱스 위치 저장.
            }
        }

        for (int i = 0 ; i < N ; i++) {
            if (op[i].score[0]!=M) { // 다른 국가라면.
                if (op[i].score[1]>op[Index].score[1]) {
                    total++;
                }
                else if (op[i].score[1]==op[Index].score[1]) {
                    if (op[i].score[2]>op[Index].score[2]) {
                        total++;
                    }
                    else if (op[i].score[2]==op[Index].score[2]) {
                        if (op[i].score[3]>op[Index].score[3]) {
                            total++;
                        }
                    }
                }
            }
        }

        bw.write(Integer.toString(total));
        bw.flush();
    }
}

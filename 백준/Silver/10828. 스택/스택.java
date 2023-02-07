import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Stack<Integer> stack = new Stack<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        for (int i = 0 ; i < N ; i++) {
            String str = br.readLine();
            if (str.contains("push"))
            {
                String[] k = str.split(" ");
                stack.push(Integer.parseInt(k[1]));
            }
            else if (str.equals("pop")) {
                if (stack.empty()) {
                    bw.write("-1\n");
                }
                else {
                    bw.write(stack.peek()+"\n");
                    stack.pop();
                }
            }
            else if (str.equals("size")) {
                bw.write( stack.size()+"\n");
            }
            else if (str.equals("empty")) {
                if (stack.empty()) {
                    bw.write("1\n");
                }
                else {
                    bw.write("0\n");
                }
            }
            else if (str.equals("top")) {
                if (stack.empty()) {
                    bw.write("-1\n");
                }
                else {
                    bw.write(stack.peek()+"\n");
                }
            }
        }

        bw.flush();
    }
}
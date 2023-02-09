import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N , M;

        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());

        int INF = (int)1e9;

        int[][] graph = new int[N+1][N+1];

        for (int i = 1; i <=N ; i++)
        {
            for (int j = 1 ; j<=N ; j++) {
                graph[i][j]=INF;
            }
        }

        while (M-- > 0)
        {
            st = new StringTokenizer(br.readLine());

            int s,e;
            s=Integer.parseInt(st.nextToken());
            e=Integer.parseInt(st.nextToken());
            graph[s][e]=1;
        }

        for (int k = 1 ; k <=N;  k++)
        {
            for (int i = 1; i<=N ; i++)
            {
                for (int j = 1;  j<=N ; j++)
                {
                    graph[i][j]=Math.min(graph[i][j] , graph[i][k]+graph[k][j]-1);
                }
            }
        }

        int total=0;
        int check;
        for (int i = 1; i <=N; i++)
        {
            check=0;
            for (int j = 1 ; j <= N ; j++)
            {
                if (graph[i][j]==1 || graph[j][i]==1)
                {
                    check++;
                }
            }
            if (check==N-1) {
                total++;
            }
        }

        bw.write(Integer.toString(total));
        bw.flush();
    }


}

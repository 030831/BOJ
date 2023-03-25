#include <bits/stdc++.h>

using namespace std;

/**
 *
 * N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
 * 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
 *
 * 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다.
 * 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
 *
 * 예제 입력 1.
 * 4 2
 * 1 1 1 1
 *
 * 예제 출력 1.
 * 3
 *
 * 경우의 수가 3이 되는 이유
 *
 * (1 1) 1 1
 * 1 (1 1) 1
 * 1 1 (1 1)
 *
 *
 */

/*

10 5
1 2 3 4 2 5 3 1 1 2

 현재 ans = 1+1+1

 구하고자 하는 값은 5

 구하고자하는값과 일치하기 때문에 ans 변수 1 증가
 그리고 end 값도 증가

 start = 4 ; end = 5

 2+5 = 7 이므로 total > M ; start 증가.

 start = 5; end = 5

 인덱스 5 값은 5 이므로 total == M : ans 증가 , end 증가.

start = 5 ; end = 6

 5+3 = 8 이므로 total > M ; start 값 증가.

 start = 6 ; end = 6

 인덱스 6 값은 3 이므로 total < M ; end 증가.

 start = 6 ; end = 7

 3+1 = 4 이므로 total < M ; end 증가

 start = 6 ; end = 8

 3+1+1 = 5 이므로 total == M ; ans 증가 , end 증가.

 start = 6 ; end = 9;

 3+1+1+2 = 7 이므로 total > M ; start 증가.

 1+2+2 = 4 이므로 total < M ; start 증가.


 */
int two_Pointer(vector<int> &arr , int N , int M , int ans)
{
    int start,end,total;
    start = 0 ; end= 0;
    // 시작과 끝은 0 으로 잡는다.
    // 문제에 따라 시작과 끝을 0 으로 잡아도 되고 0,N-1 로 잡아도 무관하다.
    // 하지만 이 문제는 i~j 까지의 인덱스 합이니 둘다 0 으로 잡아줍시다.
    while (start<=end && end<=N)
    {
        total = 0;
        for (int i = start ; i<end ; i++)
        {
            //이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]
            total += arr[i];
        }

        if (total == M)
        {
            ans++;
            end++; // 값이 일치한다면 end 를 증가시킨다.
        }

        else if (total<M) // i~j 배열의 합이 M 보다 작을경우 end 를 증가한다.
        {
            end++;
        }
        else
        {
            start++;
        }

    }
    return ans;
}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int N,M,K ,ans;
    ans = 0;

    cin >> N >> M;

    vector<int> arr;

    for (int i = 0 ; i < N ; i++)
    {
        cin >> K;
        arr.push_back(K);
    }

    cout << two_Pointer(arr,N,M,ans);
}
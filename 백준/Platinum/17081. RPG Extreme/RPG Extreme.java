import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.*;

/*
버퍼 리더 사용시 여러번 선언할때 여러 메서드에서 사용지 줄바꿈 문자가 입력에 들어가므로
한번만 main 메서드에 선언하고 매개변수로 넘겨줘여함.
 */
class Character { // 캐릭터의 특성을 나타내는 클래스.
    int Max_HP;
    int Now_Hp;
    int Level; // 레벨
    int Attack; // 공격력
    int Defense; // 방어력
    int Exp; // 경험치
    int Weapon; // 무기
    int Shield; // 방어구
    ArrayList<String> Accessories; // 악세서리
    int Character_X , Character_Y; // 캐릭터의 좌표값.
    int Start_X,Start_Y; // 시작 좌표


    Character(int Max_HP, int Now_Hp , int Level , int Attack , int Defense , int Exp , int Weapon , int Shield , ArrayList<String>Accessories) {
        this.Max_HP=Max_HP;
        this.Now_Hp=Now_Hp;
        this.Level=Level;
        this.Attack=Attack;
        this.Defense=Defense;
        this.Exp=Exp;
        this.Weapon=Weapon;
        this.Shield=Shield;
        this.Accessories=Accessories;
    }
}

class Monster { // 몬스터의 특성을 저장하는 클래스.
    int x; // x 좌표위치
    int y; // y 좌표 위치
    String Name; // 몬스터의 이름
    int W;// 몬스터의 공격력
    int A;// 몬스터의 방어력
    int E;// 몬스터의 경험치
    int H; // 몬스터의 현재 체력

    Monster(int x , int y, String Name , int W , int A , int H , int E) {
        this.x=x;
        this.y=y;
        this.Name=Name;
        this.W=W;
        this.A=A;
        this.H=H;
        this.E=E;
    }
}

class Box { // 아이템 상자의 특성를 저장하는 클래스
    int x; // 상자의 x 위치
    int y; // 상자의 y 위치
    char Box_Kind; // 박스의 종류
    int Box_Weapon; // 무기
    int Box_Shield; // 방어구
    String Box_Accessories; // 악세서리
}

class Box_Weapon extends Box {
    Box_Weapon(int x, int y , int Box_Weapon) {
        this.x=x;
        this.y=y;
        this.Box_Weapon=Box_Weapon;
    }
}

class Box_Shield extends Box {
    Box_Shield(int x, int y , int Box_Shield) {
        this.x=x;
        this.y=y;
        this.Box_Shield=Box_Shield;
    }
}

class Box_Accessories extends Box {
    Box_Accessories(int x , int y , String Box_Accessories) {
        this.x=x;
        this.y=y;
        this.Box_Accessories=Box_Accessories;
    }
}


class Input_data { // 입력에서 주어지는 데이터를 나타내는 클래스.
    String Input_One_Line; // 한줄 입력받을떄 사용하는 변수
    int N,M; // 그리드의 크기
    char[][] Grid; // 그리드
    String Move; // 커멘드 이동을 저장할 문자배열
    int Monster_Count; // 몬스터의 수를 저장할 변수
    int Box_Count; // 아이템 상자 수를 저장할 변수
}

class Input_Grid extends Input_data { // 그리드 입력 클래스 , 입력 데이터를 '상속'한다.
    public static void Input_Grid_Method(Input_data Id , BufferedReader br ) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        Id.N=Integer.parseInt(st.nextToken()); // 세로 길이 입력
        Id.M=Integer.parseInt(st.nextToken()); // 가로 길이 입력

        Id.Grid=new char[Id.N][Id.M]; // 그리드 크기 할당.

        for (int i = 0; i < Id.N ; i++) {
            Id.Input_One_Line=br.readLine(); // 한줄을 미리 입력받는다.
            for (int j = 0 ; j < Id.M; j++) {
                Id.Grid[i][j]=Id.Input_One_Line.charAt(j); // 미리 입력받은 한줄에 대한 값을 i,j 인덱스에 그리드 값으로 할당한다.
            }
        }
    }

    public static void Monster_Count_Method(Input_data Id) {
        Id.Monster_Count=0; // 처음 몬스터의 개수를 0 으로 한다.
        for (int i = 0 ; i < Id.N ; i++) {
            for (int j = 0 ; j < Id.M ; j++) {
                if (Id.Grid[i][j]=='&' || Id.Grid[i][j]=='M') {
                    Id.Monster_Count++;
                }
            }
        }
    }

    public static void Box_Count_Method(Input_data Id) {
        Id.Box_Count=0; // 처음 아이템 상자 수를 0 으로 한다.
        for (int i = 0 ; i < Id.N ; i++) {
            for (int j = 0 ; j < Id.M ; j++) {
                if (Id.Grid[i][j]=='B') {
                    Id.Box_Count++;
                }
            }
        }
    }
}

class Input_Move extends Input_data {
    public static void Input_Move_Method(Input_data Id, BufferedReader br ) throws IOException {
        Id.Move=br.readLine();
    }
}

class Input_Monster  extends Input_data {
    public static void Input_Monster_Method(Input_data Id , BufferedReader br , ArrayList<Monster> monsters) throws IOException {

        for (int i = 0 ; i < Id.Monster_Count ; i++) {

            Id.Input_One_Line=br.readLine(); // 한줄을 입력받는다.

            StringTokenizer st = new StringTokenizer(Id.Input_One_Line);
            // Readline 으로 한줄을 입력받고 StringTokenizer 을 통해 공백으로 입력값을 나눈다.

            monsters.add(new Monster(Integer.parseInt(st.nextToken()) , Integer.parseInt(st.nextToken()), st.nextToken() ,
                    Integer.parseInt(st.nextToken()) , Integer.parseInt(st.nextToken()) ,Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));

            //monsters 객체에 x,y 좌표 , 이름 , 공격력 , 방어력 , 최대체력 , 경험치를 입력한 값을 공백으로 나누어서 저장한다.
        }

    }
}

class Input_Box extends Input_data {
    public static void Input_Box_Method(Input_data Id, BufferedReader br ,
        ArrayList<Box_Weapon> box_weapons ,ArrayList<Box_Shield> box_shields, ArrayList<Box_Accessories> box_accessories ) throws IOException {
        //장비는 무기(W), 갑옷(A), 장신구(O)
        Box box = new Box(); // 박스 정소를 저장할 객체 생성

        for (int i = 0 ; i < Id.Box_Count ; i++) {
            Id.Input_One_Line=br.readLine(); // 한줄 입력
            StringTokenizer st = new StringTokenizer(Id.Input_One_Line); // 입력받은 한줄을 공백으로 나눈다.

            box.y=Integer.parseInt(st.nextToken());
            box.x=Integer.parseInt(st.nextToken()); // x,y 좌표값 저장.
            // y 좌표 먼저 할당.
            box.Box_Kind=st.nextToken().charAt(0); // 박스의 종류 입력받기

            if (box.Box_Kind=='W') { // 박스의 종류가 무기라면.
                box.Box_Weapon=Integer.parseInt(st.nextToken()); // 무기를 입력받고
                box_weapons.add(new Box_Weapon(box.x ,box.y , box.Box_Weapon));
                // 좌표와 무기를 Box_Weapon 이라는 클래스 객체에 저장한다.
            }
            else if (box.Box_Kind=='A') { // 박스의 종류가 갑옷이라면.
                box.Box_Shield=Integer.parseInt(st.nextToken()); // 갑옷을 입력받고
                box_shields.add(new Box_Shield(box.x , box.y , box.Box_Shield));
                // 좌표와 갑옷을 Box_Shield 이라는 클래스 객체에 저장한다.
            }
            else if (box.Box_Kind=='O') { // 박스의 종류가 장신구라면
                box.Box_Accessories=st.nextToken(); // 장신구를 입력받고
                box_accessories.add(new Box_Accessories(box.x , box.y , box.Box_Accessories));
                // 좌표와 악세서리를 Box_Accessories 라는 클래스 객체에 저장한다.
            }
        }
    }
}

class Game {
    static int Passed_Turns=0; // 게임의 턴을 저장할 변수
    static int Game_Truns; // 몬스터와 싸울때 턴을 저장할 변수
    static int Monster_Max_Hp; // 몬스터의 최대 체력을 저장할 변수

    public static void Get_Start_Location_Method(Input_data Id , Character character) { // 시작 위치값을 구하는 메서드.
        for (int i = 0 ; i < Id.N ; i++) {
            for (int j = 0 ; j < Id.M ; j++) {
                if (Id.Grid[i][j]=='@') {
                    character.Character_X=j; // X 를 가로축
                    character.Character_Y=i; // Y 를 세로축으로 정의한다.
                    character.Start_X=j;
                    character.Start_Y=i;

                    Id.Grid[i][j]='.';
                }
            }
        }
    }

    public static int Move_Method(ArrayList<Monster> monsters , Input_data Id , Character character,
                                  ArrayList<Box_Weapon> box_weapons , ArrayList<Box_Shield> box_shields ,ArrayList<Box_Accessories> box_accessories) throws IOException {
        
        if (Id.Move.charAt(Passed_Turns)=='L' && character.Character_X-1>=0 && Id.Grid[character.Character_Y][character.Character_X-1]!='#') {
            character.Character_X--;
        }
        else if (Id.Move.charAt(Passed_Turns)=='R' && character.Character_X+1<Id.M && Id.Grid[character.Character_Y][character.Character_X+1]!='#') {
            character.Character_X++;
        }
        else if (Id.Move.charAt(Passed_Turns)=='U' && character.Character_Y-1>=0 && Id.Grid[character.Character_Y-1][character.Character_X]!='#') {
            character.Character_Y--;
        }
        else if (Id.Move.charAt(Passed_Turns)=='D' && character.Character_Y+1<Id.N && Id.Grid[character.Character_Y+1][character.Character_X]!='#') {
            character.Character_Y++;
        }

        if (Id.Grid[character.Character_Y][character.Character_X]=='B') {
            return Check_Box_Method(box_weapons , box_shields , box_accessories, Id , character);
        }
        else if (Id.Grid[character.Character_Y][character.Character_X]=='&' || Id.Grid[character.Character_Y][character.Character_X]=='M' ) {
            return Fight_Monster_Method(monsters , Id , character);
        }
        else if (Id.Grid[character.Character_Y][character.Character_X]=='^') {
            return Trap_Method(Id, character);
            // 만약 함정 위에서 입력받은 커맨드 방향으로 움직일 수 없어 제자리에 멈추는 경우, 해당 함정을 또 밟은 것이 된다.
        }

        return -1;
    }
    
    public static int Check_Box_Method(ArrayList<Box_Weapon> box_weapons , ArrayList<Box_Shield> box_shields ,ArrayList<Box_Accessories> box_accessories,
                                       Input_data Id , Character character) {

        for (int i = 0 ; i < box_weapons.size() ; i++) {
            if (box_weapons.get(i).x-1== character.Character_X && box_weapons.get(i).y-1== character.Character_Y) {
                character.Weapon = box_weapons.get(i).Box_Weapon;
            }
        }
        for (int i = 0 ; i < box_shields.size() ; i++) {
            if (box_shields.get(i).x-1== character.Character_X && box_shields.get(i).y-1== character.Character_Y) {
                character.Shield = box_shields.get(i).Box_Shield;
            }
        }

        for (int i = 0 ; i < box_accessories.size() ; i++) {
            if (box_accessories.get(i).x-1== character.Character_X && box_accessories.get(i).y-1== character.Character_Y) {
                if (character.Accessories.size()<4 && !character.Accessories.contains(box_accessories.get(i).Box_Accessories)) {
                    character.Accessories.add(box_accessories.get(i).Box_Accessories);
                }
            }
        }
        Id.Grid[character.Character_Y][character.Character_X]='.';
        return -1;

    }


    public static int Fight_Monster_Method(ArrayList<Monster> monsters ,  Input_data Id , Character character) {
        for (int i = 0 ; i < monsters.size() ; i++) {
            if (monsters.get(i).y-1==character.Character_X && monsters.get(i).x-1==character.Character_Y) {
                Game_Truns = 0;
                Monster_Max_Hp = monsters.get(i).H; // 몬스터의 최대 체력을 저장한다.

                while (true) {
                    if (Game_Truns==0) {
                        if (character.Accessories.contains("CO")) {
                            if (character.Accessories.contains("DX")) {
                                monsters.get(i).H-=Math.max(1,(character.Attack+character.Weapon)*3-monsters.get(i).A);
                            }
                            else {
                                monsters.get(i).H-=Math.max(1,(character.Attack+character.Weapon)*2-monsters.get(i).A);
                            }
                        }
                        else {
                            monsters.get(i).H-=Math.max(1,(character.Attack+character.Weapon)-monsters.get(i).A);
                        }
                        if (character.Accessories.contains("HU") && Id.Grid[character.Character_Y][character.Character_X]=='M') {
                            character.Now_Hp= character.Max_HP;
                            monsters.get(i).H-=Math.max(1,(character.Attack+character.Weapon)-monsters.get(i).A);
                        }
                    }
                    Game_Truns++;

                    if (monsters.get(i).H<=0) {
                        if (character.Accessories.contains("HR")) {
                            character.Now_Hp=Math.min(character.Max_HP , character.Now_Hp+3);
                        }
                        if (character.Accessories.contains("EX")) {
                            character.Exp+=Math.floor(monsters.get(i).E*1.2);
                        }
                        else {
                            character.Exp+=monsters.get(i).E;
                        }

                        if (character.Exp>=character.Level*5) {
                            character.Max_HP+=5;
                            character.Now_Hp= character.Max_HP;
                            character.Attack+=2;
                            character.Defense+=2;
                            character.Exp=0;
                            character.Level++;
                        }


                        if (Id.Grid[character.Character_Y][character.Character_X]=='M')
                        {
                            Id.Grid[character.Character_Y][character.Character_X]='.';
                            return 777777; // 보스몬스터를 죽였다면.
                        }
                        else{
                            Id.Grid[character.Character_Y][character.Character_X]='.';
                            return -1;
                        }

                    }

                    if (character.Now_Hp<=0) {
                        if (character.Accessories.contains("RE")) {
                            character.Now_Hp=character.Max_HP;
                            character.Character_X=character.Start_X;
                            character.Character_Y=character.Start_Y;
                            character.Accessories.remove("RE");
                            monsters.get(i).H = Monster_Max_Hp; // 부활할 경우 몬스터의 체력은 최대체력으로 설정한다.
                            return -1;
                        }
                        else {
                            return i; // -1이 아닌 값은 죽음을 의미한다.
                        }
                    }

                    if (Game_Truns%2==1) {
                        character.Now_Hp-=Math.max(1,monsters.get(i).W - (character.Shield+character.Defense));
                    }
                    else {
                        monsters.get(i).H-=Math.max(1,(character.Attack+character.Weapon)-monsters.get(i).A);
                    }
                }
            }
        }
        return -1;
    }

    public static int Trap_Method(Input_data Id , Character character) {
        if (character.Accessories.contains("DX")) {
            character.Now_Hp--;
        }
        else {
            character.Now_Hp-=5;
        }
        if (character.Now_Hp<=0) {
            if (character.Accessories.contains("RE")) {
                character.Now_Hp=character.Max_HP;
                character.Character_X=character.Start_X;
                character.Character_Y=character.Start_Y;
                character.Accessories.remove("RE");
                return -1;
            }
            else {
                return 123456; // -1이 아닌 값은 죽음을 의미한다.
            }
        }
        return -1;
    }

    public static void Play_Game_Method(Input_data Id, BufferedReader br , BufferedWriter bw , Character character , ArrayList<Monster> monsters  ,
                                        ArrayList<Box_Weapon> box_weapons , ArrayList<Box_Shield> box_shields ,ArrayList<Box_Accessories> box_accessories) throws IOException {

        int Game_Answer;


        while (true) {
            Game_Answer=Move_Method(monsters ,Id , character ,box_weapons , box_shields , box_accessories);
            Passed_Turns++;

            if (Game_Answer!=-1) { // 게임이 끝났다면
                if (Game_Answer==123456) { // 가시 함정에 죽었다면
                    Input_Game_Answer_Method(bw , Id , character );
                    bw.write("YOU HAVE BEEN KILLED BY SPIKE TRAP..");
                }
                else if (Game_Answer==777777) { // 보스 몬스터를 죽였다면
                    Id.Grid[character.Character_Y][character.Character_X]='@';
                    Input_Game_Answer_Method(bw , Id , character );
                    bw.write("YOU WIN!");
                }
                else { // 몬스터한테 죽었을 경우
                    Input_Game_Answer_Method(bw , Id , character );
                    bw.write("YOU HAVE BEEN KILLED BY " + monsters.get(Game_Answer).Name + "..");
                }
                break;
            }

            if (Passed_Turns==Id.Move.length()) { // 모든 커멘드를 끝넀다면.
                Id.Grid[character.Character_Y][character.Character_X]='@';
                Input_Game_Answer_Method(bw , Id , character );
                bw.write("Press any key to continue.");
                break;
            }
        }
    }

    public static void Input_Game_Answer_Method(BufferedWriter bw ,Input_data Id , Character character) throws IOException {

        for (int i = 0 ; i < Id.N ; i++) {
            for (int j = 0 ; j < Id.M ; j++) {
                bw.write(Id.Grid[i][j]);
            }
            bw.newLine();
        }

        bw.write("Passed Turns : " + Passed_Turns + '\n');
        bw.write("LV : " + character.Level + '\n');
        bw.write("HP : " + Math.max(0,character.Now_Hp) + '/' + character.Max_HP + '\n');
        bw.write("ATT : " + character.Attack + '+' + character.Weapon + '\n');
        bw.write("DEF : " + character.Defense + '+' +  character.Shield + '\n');
        bw.write("EXP : "  + character.Exp + '/' + character.Level*5 + '\n');
    }
}


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        Input_data Id = new Input_data(); // 입력 데이터 변수를 저장할 객체 생성
        Input_Grid.Input_Grid_Method(Id , br); // 그리드 입력
        Input_Move.Input_Move_Method(Id , br); // 이동 커멘드 입력
        Input_Grid.Monster_Count_Method(Id); // 몬스터수 저장
        Input_Grid.Box_Count_Method(Id); // 박스 수 저장


        ArrayList<Box_Weapon> box_weapons = new ArrayList<Box_Weapon>();
        // 무기가 들어있는 상자의 특성을 저장하는 객체
        ArrayList<Box_Shield> box_shields = new ArrayList<Box_Shield>();
        // 갑옷이 들어있는 상자의 특성을 저장하는 객체
        ArrayList<Box_Accessories> box_accessories = new ArrayList<Box_Accessories>();
        // 악세서리가 들어있는 상자의 특성을 저장하는 객체



        ArrayList<Monster> monsters = new ArrayList<Monster>();  // 몬스터의 특성을 저장하는 객체
        Input_Monster.Input_Monster_Method(Id , br , monsters); // 몬스터 입력


        Input_Box.Input_Box_Method(Id , br , box_weapons , box_shields , box_accessories); // 상자 정보 입력받기.

        Character character = new Character(20,20,1,2,2,0,0,0,new ArrayList<String>() );

        Game.Get_Start_Location_Method(Id , character); // 캐릭터의 시작지점 설정


        Game.Play_Game_Method(Id , br , bw , character , monsters , box_weapons , box_shields , box_accessories);

        bw.flush(); // 출력 종료



    }
}

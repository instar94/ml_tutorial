//package
package a.b.c.ch3;

//import
//nextInt()를 사용하기 위해 Scanner 클래스 import
import java.util.Scanner;

public class ExFlow_5_1{

	//상수
	//각 메달 별로 할당 될 색상은 변하지 않으므로 상수로 지정해둠
	//public : 모든 패키지에서 사용가능
	//static : 메모리에 자동으로 로드함 -> new로 인스턴스 할 필요 X
	//			대신 사용시 클래스이름 . 변수명으로 사용
	//final : 상수임 값이 절대 안 변함
	//char : 기초자료형 (문자)
	public static final char MEDAL_COLOR_GOLD = 'G';
	public static final char MEDAL_COLOR_SILVER = 'S';
	public static final char MEDAL_COLOR_BRONZE = 'B';
	public static final char MEDAL_COLOR_A = 'A';

	//멤버변수
	//생성자

	//함수
	//public : 어떤 패키지에서든지 사용가능
	//String : 문자열 + return을 사용해야하는 함수
	//매개변수 : int ranking <= 기초자료형(정수형) 변수
	public String rankFun(int ranking){
		System.out.println("ExFlow_5_1.rankFun 시작 >>>>>>>>>>");
		//medalColor : 메달 색상을 표현하는 지역변수
		//char : 기초자료형
		//지역변수는 선언과 동시에 초기화 해야함으로 ' '로 초기화
		//' ' = '\u0000'
		char medalColor ='\u0000';

		//ranking은 이미 main에서 선언했기 때문에 값만 찍어봄
		System.out.println("ranking>>>>>" + ranking);

		//switch 문 : ()안 조건에 맞는 case를 수행하고 break함
		//default : if문의 else와 동일한 기능을 수행함
		//상수가 이미 선언되어 있기 때문에 상수와 연결된 값이 나온다.
		//단 ExFlow_5_1 클래스에서 사용했고 static이 사용됐기 때문에
		//ex) ExFlow_5_1.MEDAL_COLOR_GOLD
		//         클래스 . 변수이름 으로 사용해야함
		switch (ranking){
			case 1: medalColor = ExFlow_5_1.MEDAL_COLOR_GOLD;
				break;
			case 2: medalColor = ExFlow_5_1.MEDAL_COLOR_SILVER;
				break;
			case 3: medalColor = ExFlow_5_1.MEDAL_COLOR_BRONZE;
				break;
			default:
					medalColor = ExFlow_5_1.MEDAL_COLOR_A;

				/*상수 선언 없이 결과값 얻기
				case 1: medalColor = 'G';
				break;
				case 2: medalColor = 'S';
				break;
				case 3: medalColor = 'B';
				break;
				default:
						medalColor = 'A';
				
				*/
		}//end of switch 구문
		
		//medalColor가 잘 나왔는지 값을 찍어봄
		System.out.println("medalColor>>>>" + medalColor);
		//return 전에 써야함!
		System.out.println("ExFlow_5_1.rankFun 끝 >>>>>>>>>>");
		//return은 ()나 {}를 요하지 않는다!
		return ranking + "등의 메달 색은 "+ medalColor + " 입니다.";
	}

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) {
		//TODO Auto-generated method stub.
		System.out.println("ExFlow_5_1.main 함수 시작>>>>");
		
		//입력을 받을 수 있도록 질문을 프린트
		System.out.println("등수를 입력해주세요 (1~100)");
		
		//ranking : 순위를 의미하는 지역변수
		//ranking의 값은 nextInt()의 기능을 통해 콘솔에서 받아서 초기화
		//Scanner에 있는 nextInt 함수를 사용하기 위해서 참조변수를 선언
		Scanner sc = new Scanner(System.in);
		int ranking = sc.nextInt();

		//참가인원은 100명이므로 등수는 1~100까지만 있을 것임
		if(ranking>=1 && ranking<=100){
		
			//숫자를 제대로 입력한 경우 rankFun 함수를 실행한다.
			//rankFun 함수는 static 되지 않았으므로 참조변수를 이용
			//return이 있는 함수기기때문에 같은 String 형태의 msg에 아규먼트를 넣은 값을 계산한다.
			ExFlow_5_1 ef5_1 = new ExFlow_5_1();
			String msg = ef5_1.rankFun(ranking);

			System.out.println(msg);

		//else : 1~100 외의 숫자를 입력한 경우(= 조건의 값이 false인 경우)
		}else{
			System.out.println("데이터를 다시 입력해주세요");
		}

		System.out.println("ExFlow_5_1.main 함수 끝>>>>");

	}//end of main 함수
}//end of ExFlow_5_1 클래스


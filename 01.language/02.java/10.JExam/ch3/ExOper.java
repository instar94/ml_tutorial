//package
package a.b.c.ch3;
//import

public class ExOper {
	//flow control : if , switch, while , do while
	//상수
	//멤버변수
	//생성자
	
	//함수
	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		
		//기초자료형(int) 지역변수 num 선언
		//num을 10으로 초기화
		int num=10;

		//부호 연산자
		System.out.println(num);

		System.out.println(+num);
		System.out.println(-num);
		System.out.println(num);

		num = -num;
		
		System.out.println(num);

		//산술 연산자

		// - 연산자는 순서가 중요(앞에서 뒤를 뺌)
		System.out.println(5-3);
		System.out.println(3-5);

		//% : 나머지를 구하는 연산자 (나누기 아님) (앞에서 뒤를 뺌)
		System.out.println(5%3);
		System.out.println(3%5);

		//++i : 연산 한 결과 값
		//i++ : 연산 전 값 => while.for. if문에서 count(숫자)를 증가, 감소 시킬 때 주로 사용
		//기초자료형(int) 지역변수 gameScore선언
		//gameScore를 150 리터럴로 초기화
		int gameScore = 150;

		//++ 변수 : gameScore에 먼저 1을 더함, 그리고 lastScore에 대입
		//++ 변수 : 연산의 결과를 집어 넣음
		int lastScore= ++gameScore;
		System.out.println(lastScore);

		//--변수 : gameScore에 먼저 1을 뺌, 그릴고 lastScore에 대입
		//-- 변수 : 연산의 결과를 집어 넣음
		int lastScore2 = --gameScore;
		System.out.println(lastScore2);
		
		//기초자료형(int) 지역변수 gameScore1선언
		//gameScore1를 150 리터럴로 초기화
		int gameScore1 = 150;

		//lastScore에 먼저 gameScore를 대입하고 1을 증가시킴
		//변수 ++ : 연산하기 전 값을 집어 넣음
		//lastScore11 =150
		//gameScore1 : 151
		int lastScore11 = gameScore1++;
		System.out.println(lastScore11);

		//lastScore12에 먼저 gameScore를 대입하고 1을 증가시킴
		//변수 -- : 연산하기 전 값을 집어 넣음
		//lastScore12 =151
		//gameScore1 : 150
		int lastScore12 = gameScore1--;
		System.out.println(lastScore12);

	}//end of main 함수
}//end of ExOper 클래스

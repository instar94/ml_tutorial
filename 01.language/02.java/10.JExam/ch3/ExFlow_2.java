//package
package a.b.c.ch3;
//import

public class  ExFlow_2{
	//상수
	//멤버변수
	//생성자
	
	//함수
	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		System.out.println("데이터가 잘 연결된 경우>>>>>>>");
		//기초자료형 (int) 지역변수 age 선언
		//age에 리터럴 7로 초기화
		int age = 7;

		//if절 시작 : ()안 조건문의 true여야 작동
		if (age >=8){
			System.out.println("학교에 다닙니다.");
		//()안 조건이 false일 경우 else 작동
		}else{
			System.out.println("학교에 다니지 않습니다.");
		}//end of if 절

		//기초자료형(boolean) 지역변수bool 선언 
		//bool의 값으로  age>=8 로 초기화 <-age를 호출
		boolean bool = age>=8;
		System.out.println("bool >>> :" +bool);
		//if절 시작 : ()안 조건문의 true여야 작동
		if(bool){
			System.out.println("학겨에 다닙니다.");
		//()안 조건이 false일 경우 else 작동
		}else{
			System.out.println("학교에 다니지 않습니다.");
		}//end of if절
	}//end of main 함수
}//end of ExFlow_2 클래스

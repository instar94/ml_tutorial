//package
package a.b.c.ch3;
//import
import java.util.Scanner;

public class ExFlow_4_2{
	//상수
	//멤버변수
	//생성자
	
	//함수
	//public : 모든 패키지에서 사용 가능
	//void : return 사용 불가능
	//일반형 함수 - 참조변수 사용해야함
	//ticketFee : 사용자 정의 함수명
	//int age : 정수형 매개변수
	public void ticketFee(int age){
		System.out.println("ticketFee 함수 시작 >>>");

		//기초데이터형 지역변수 int charge 선언
		int charge; //<-초기화 하지 않음

		if (age > 0 && age <100){
			if(age < 8){
				charge = 1000;
				System.out.println("미취학 아동 입니다");
			}else if (age <14){
				charge = 2000;
				System.out.println("초등학생 입니다");
			}else if (age<20){
				charge = 2500;
				System.out.println("중고등학생 입니다.");
			}else if (age>=60){
				charge = 0;
				System.out.println("경로우대 입니다.");
			}else{
				charge=3000;
				System.out.println("성인 입니다.");
			}
			System.out.println("입장료는 " + charge +"원 입니다.");
		}else{
			System.out.println("데이터를 확인해주세요");
		}
		System.out.println("ticketFee 함수 끝 >>>");
	}//end of ticketFee 함수
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		System.out.println("main 함수 시작 >>>");
		
		System.out.println("나이를 입력해주세요");
		Scanner sc = new Scanner(System.in);
		int age = sc.nextInt();

		ExFlow_4_2 ef42 = new ExFlow_4_2();
		ef42.ticketFee(age);

		System.out.println("main 함수 끝>>>");
	}//end of main 함수
}//end of ExFlow_4_2 클래스

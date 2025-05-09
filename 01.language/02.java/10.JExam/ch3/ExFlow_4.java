//package
package a.b.c.ch3;
//import
import java.util.Scanner;

public class  ExFlow_4{
	//상수
	//멤버변수
	//생성자
	
	//함수
	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){
		
		System.out.println("나이를 입력하시오!!");

		//static이 붙지 않았으므로 참조변수 선언해서 사용
		//Scanner 클래스 이름 (소속 : java.util.Scanner)<-lang 에 없으므로 import해서 사용
		//sc 참조변수명 
		//new : 참조변수 인스턴스
		//Scanner(System.in) : Scanner라는 생성자를 만듬
		//그런데 System.in으로 데이터를 입력 받음
		Scanner sc = new Scanner(System.in);

		//기초데이터형 지역변수 int age를 선언
		//nextInt() : 입력받은 값을 age에 대입함
		int age =sc.nextInt();
		System.out.println("age>>>>>"+age);
		
		//0~100까지의 숫자이면 입력 or 초과되면 그냥 데이터 값 확인해달라고 요청
		//if조건문 : ()안 조건이 true 이면 실행
		if (0<= age && age<=100){
		if (age>=8){
			System.out.println("학교에 다닙니다");
		}else{
			System.out.println("학교에 다니지 않습니다.");
		}
		//TODO Auto-generated method stub.
		//else : ()안에 조건이 false면 실행
		}else{
			System.out.println("데이터값을 확인해주세요");
		}
	}//end of main함수
}//end of ExFlow_4 클래스

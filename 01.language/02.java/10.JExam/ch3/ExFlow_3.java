//package
package a.b.c.ch3;
//import

public class ExFlow_3{
	//상수
	//멤버변수
	//생성자
	
	//함수
	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		
		//기초데이터형 지역변수 int age 선언
		//값을 9로 초기화
		int age =9;
		//기초형데이터 지역변수 charge 선언 
		int charge; //<=초기화 X

		//if문 : ()안 조건이 true 일 경우 수행
		if (age < 8){
			charge = 1000;//<=charge 값 초기화
			System.out.println("취학 전 아동입니다.");
		//else if if의 조건이 안된다면 그다음 조건을 부여
		//해당 조건이 true이면 수행됨
		}else if (age < 14){
			charge = 2000;//<=charge 값 초기화
			System.out.println("초등학생입니다.");
		}else if(age < 20){
			charge = 3000;//<=charge 값 초기화
			System.out.println("중-고등학생입니다.");
		//else : if와 else if의 조건이 모두 false 일때 수행
		}else{
			charge = 3000;//<=charge 값 초기화
			System.out.println("성인입니다.");
		}

		System.out.println("입장료는"+ charge +"원 입니다.");
	}//end of main 함수
}//end of ExFlow_3 클래스

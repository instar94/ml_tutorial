//package
package a.b.c.ch3;
//import

public class ExFlow_6_1 {

	//상수
	//멤버변수
	//생성자

	//함수
	//public : 모든 패키지에서 이용 가능한 함수
	//static : 메모리에 자동으로 등록 -> 클래스이름.함수이름()으로 사용
	//void : return 키워드 사용 불가능
	public static void numSum(){
		
		//기초자료형 지역변수 선언
		//num은 리터럴값 1로 초기화
		int num =1;

		num += 2;
		num += 3;
		num += 4;
		num += 5;
		num += 6;
		num += 7;
		num += 8;
		num += 9;
		num += 10;

		System.out.println("1부터 10까지의 합은? >>  " + num );
	}//end of numSum 함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) {
	//TODO Auto-generated method stub.
	
	//numSum함수를 사용하기 위해 호출
	ExFlow_6_1.numSum();

	//반복문을 이용하기 위해 기초자료형 지역변수 num과 sum을 사용
	//ExFlow_6_1.main의 num과 ExFlow_6_1 numSum의 num은 다른 변수임
	// 각각 1과 0으로 초기화 시킴
	int num = 1;
	int sum = 0;

	//while (조건문) : 조건문이 성립될때까지 반복함
	////이 loop를 num이 10보다 같거나 작다면 반복 => 11이 되는 순간 false가 됨
	while(num <= 10){
		
		//sum에다가 num의 값을 더하고
		//num은 1을 더함
		//최조 num값은 1이며, 1이 10이 될때까지 더함
		//sum값은 0임 => 1부터 10까지 더하는 것이됨
		sum +=num;
		num++;
	}//end of while문

	System.out.println("1부터 10까지의 합은? >>  " + sum);

	//do while 문으로 하기
	//기초자료형 지역변수 num과 sum 선언
	// 각각 1과 0으로 초기화 시킴
	int num1 = 1;
	int sum1 = 0;

	//매 loop마다 sum1에 num1 값을 더하고, num1에 1을 더함
	do{
		sum1 += num1;
		num1++;
	} //이 loop를 num1이 10보다 같거나 작다면 반복 => 11이 되는 순간 false가 됨
	while (num1<=10);

	System.out.println("1부터 10까지의 합은? >>  " + sum1);

	System.out.println("ExFlow_6_1 main 함수 끝>>>>>>");
	}//end of main 함수
}//end of ExFlow_6_1 클래스

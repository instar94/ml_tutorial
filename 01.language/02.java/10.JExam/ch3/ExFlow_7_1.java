//package
package a.b.c.ch3;
//import

public class ExFlow_7_1 {

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){
	//TODO Auto-generated method stub.
		System.out.println("for문>>>>>>>>");
		//for문에서 변수 선언 및 초기화는 초기화식에서 하는 것이 일반적
		//프로그램에서 모든 데이터는 순차적으로 담김(배열)
		//순차의 시작점 특히 자바는 0
		//for문은 항상 배열과 같이 사용되어야 함
		//초기화는 0으로
		//초기화식 : i는 0임
		//조건문 : i가 10이 될때까지
		//증감식 : 1씩 증가
		//수행문 : 안녕하세요 출력하기


		for(int i=0; i<10; i++){
			System.out.println(i+" 안녕하세요 ");
		}//end of if문

		System.out.println("\nwhile 문>>>>>>>>");
		//while문에서 사용할 지역변수 i를 선언
		//배열과 같이 i를 0으로 초기화
		int i = 0;
		//10번 해야함으로 i가 0~9까지 해야함 => 10보다 작은 정수
		//i++ : i는 1씩 커질 것임
		while(i<10){
			System.out.println(i+" 안녕하세요 ");
			i++;
		}//end of while문
	}//end of main 함수
}//end of ExFlow_7_1 클래스
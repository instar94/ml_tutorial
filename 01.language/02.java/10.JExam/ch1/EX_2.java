package a.b.c.ch1;

public class EX_2 {
	//main 함수 : 콘솔 어플리케이션의 시작점
	public static void main(String [] args){
		System.out.println("Ex_2::main() 시작 >>>>");

		//자바 데이터 타입(자료형) : 기초자료형 정수형 숫자 int
		// i : 변수 명 - 데이터를 담는 통
		// '=' : 대입 연산자 오른쪽에서 왼쪽으로 데이터를 대입
		// 1: 값(=리터럴)
		// int형 데이터 타입 선언 후, 변수 이름을 i로 선언하고, 값을 1로 초기화/대입 함

		int i = 1;
		
		// 콘솔 println에 있는 아규먼트 변수 i 값을 출력하시오
		// println 함수에서 지역변수(함수 안에 있기때문에) 
		// i를 호출(invoke) 후, 아규먼트로 받아 출력함
		System.out.println(i);
		// public void println(int x)

		System.out.println("Ex_2::main() 끝 >>>>");

	}//end of main 함수
}//end of EX_2 클래스
//package
package a.b.c.ch3;

//import

public class ExCast_1 {

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.

		/*
		캐스팅 연산자 ()
		자바에서는 대입연산자 '='를 기준으로 데이터 타입은 동일해야함
		좌우의 데이터타입이 동일하지 않으면 캐스팅 연산자 '()'를 사용
		*/

		//기초자료형(byte) 지역변수 b를 선언하고 10으로 초기화
		byte b = 10;

		//기초자료형(int) 지역변수 i를 선언하고 변수 b로 초기화
		int i = (int)b;

		//int i = b; <- 묵시적 형변환
		//byte를 int로 표현
		//byte < int 이기 때문에 묵시적인 형변환이 일어남
		//캐스팅 연산자 () 가 없어도 됨

		//변수 b와 i 값을 콘솔에 출력
		System.out.println(b);
		System.out.println(i);

		//기초자료형(int) 지역변수 i1를 선언하고 20으로 초기화
		int i1 = 20;

		//기초자료형(float) 지역변수 f를 선언하고 변수 i1로 초기화
		float f = (float)i1;

		//float f = i1;<- 묵시적 형변환
		//int(정수형)를 float(실수형)으로 표현 
		//int < float 이기 때문에 묵시적 형변환이 일어남
		//캐스팅 연산자 ()가 없어도 됨

		//변수 i1과 f 값을 콘솔에 출력
		System.out.println(i1);
		System.out.println(f);


		//정수형 i 와 실수형 f 의 합을 실수형 d로 출력
		//int < float < double 이기 때문에
		//결과값은 실수형으로 나온다.
		// 더 큰쪽으로 갔기 때문에 묵시적 형변환이 일어남

		//기초자료형 d를 선언
		//그 값을 i와 f의 합을 대입
		double d;
		d = i + f;
		
		System.out.println(d);

	}//end of main 함수
}//end of ExCast_1 클래스

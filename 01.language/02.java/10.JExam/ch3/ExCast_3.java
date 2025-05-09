//package
package a.b.c.ch3;

//import
public class ExCast_3 {

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.
		System.out.println("\nExCast_3.main 함수 시작>>>>\n");
	
		//기초자료형 지역변수 i 선언
		//i를 10이라는 리터럴로 초기화
		int i =10;

		//기초자료형 지역변수 b 선언
		//b에 i값을 호출하여 선언함
		//명시적 형변환을 위해 캐스팅 연산자 ()를 사용
		//오른쪽에서 왼쪽을 맞춤
		byte b = (byte) i; //<=명시적 형변환

		//byte b = i;
		//오류 발생 : 작은 데이터 byte에 큰 데이터 int를 넣으려면 형변환이 필요

		//i와 b를 콘솔에 출력
		//Integer.toBinaryString : int를 2진수로 바꿈
		System.out.println("i>>>>>>>>:"+i);
		System.out.println(Integer.toBinaryString(i));

		System.out.println("b>>>>>>>>:"+b);
		System.out.println(Integer.toBinaryString(b));
		
		//기초자료형 지역변수 int형 i1 선언
		//값을 리터럴 1000으로 초기화
		int i1=1000;

		//기초자료형 지역변수 byte형 b1선언
		//값을 i1을 byte형으로 명시적 형변환함
		//i1은 int형이기 때문에 작은 byte형에 큰 int형을 넣기 위해 명시적 형변환이 필요함
		byte b1 = (byte)i1;

		//콘솔에 i1을 출력
		System.out.println("i1>>>>>>>>:"+i1);
		System.out.println(Integer.toBinaryString(i1));
		//콘솔값
		//i1>>>>>>>>:1000
		//1111101000
		
		//콘솔에 b1을 출력
		System.out.println("b1>>>>>>>>:"+b1);
		System.out.println(Integer.toBinaryString(b1));
		//콘솔값
		//b1>>>>>>>>:-24
		//11111111111111111111111111101000
		//1000이라는 숫자는 byte의 최대값을 넘었기 때문에 전혀 다른 숫자가 나옴
		//toBinaryString을 이용해서 봐도 전혀 다른 수가됨

		//byte의 최대값 최소값 출력
		System.out.println("Byte최대값>>>>>:"+Byte.MAX_VALUE);
		System.out.println("Byte최대값>>>>>:"+Byte.MIN_VALUE);
		
		//기초자료형 지역변수(double-실수형) d 선언
		//변수 d에 3.14으로 초기화
		double d = 3.14;

		//기초자료형 지역변수(int-정수형) i2 선언
		//i2에 double형 d를 호출하고 정수형으로 바꾼 뒤 대입
		//int < double 이기 때문에 명시적 형변환이 필요
		//실수 -> 정수 형변환 시 가수부(소수점 이하)는 제거한다.
		int i2 =(int)d;//<-명시적 형변환
		
		//d와 i2를 콘솔에 출력
		System.out.println("d>>>>>>:"+d);
		System.out.println("i2>>>>>:"+i2);
		//콘솔값
		//d>>>>>>:3.14
		//i2>>>>>:3 <- 가수부가 없어짐

		System.out.println("\nExCast_3.main 함수 끝>>>>\n");

	}//end of main 함수
}//end of ExCast_3 클래스

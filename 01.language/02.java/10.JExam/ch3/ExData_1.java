package a.b.c.ch3;

/*
기초자료형
1byte = 8bit : 사람이 보는 2진수로 봄
jvm은 숫자를 int, int가 아닌 것은 double로 본다
숫자
	byte  :1byte : 0
	char  :2byte : ' ', \u0000
	short :2byte : 0
	int   :4byte : 0
	long  :8byte : 0.0
	float :8byte : 0.0f
	double:8byte : 0.0d
		float와 double은 따로 표시를 해주어야 함

문자 : char : 자바에서 문자는 숫자
논리 : 
	boolean:1byte

캐스팅 연산자 : ()
------> 묵지적 형변환 (implict casting)
byte < char < short< int < long < float < double
	   <---------명시적 형변환 (explict casting)
*/
public class ExData_1{
	//Ex_Data_1클래스 블럭에 기초자료형 byte 자료형을 (데이터타입) 멤버변수 선언
	// 멤버변수는 생성자가 초기화 하기 때문에 선언과 동시에 초기화x
	//b 변수명의 유효범위 사용범위는 클래스 블럭 전체이다.
	byte b;

	public static void main(String[] args){
	//메인함수 블럭에 기초자료형 byte 자료형을 (데이터 타입) 지역변수로 선언
	// b변수병은 byte=0; 문자 하위에서 사용 가능하고 그 유효범위는 main()함수 블럭 끝까지
	byte b =0;

	System.out.println("b>>>>>>>"+b);

	//b=128;
	//에러 발생
	//에러 이유 : byte는 127까지 밖에 표현 못함
	b = 127;

	//MAX_VALUE : 해당 자료형이 표현 할 수 있는 최대치
	//A constant holding the maximum value a byte can have, 2^7-1.
	//MIN_VALUE : 해당 자료형이 표현 할 수 있는 최저치
	System.out.println("b>>>"+b);
	/*
	클래스 자원 = 변수+함수+클래스(빌트인 클래스, 사용자 정의 클래스)
	1. 클래스 : 빌트인 클래스, 사용자 정의 클래스(패키지가 다를 시 import 키워드 사용)
	2. 변수 : 멤버변수: static, static 있는 것
		      지역변수 : static 없고, new를 사용 하지 않음(기초 자료형)
	
	Byte : java.lang.byte : 자바에서 java.lang 패키지에 있는 클래스
	소스에서 import하지 않아도 자바에서 알아서 import함
	MAX_VALUE : 상수 = public static final byte MAX_VALUE =127;

	MIN_VALUE : 상수 = public static final byte MAX_VALUE =-128;
	*/
	System.out.println("Byte.Max_VALUE>>>"+Byte.MAX_VALUE);
	System.out.println("Byte.MIN_VALUE>>>"+Byte.MIN_VALUE);

	}//end of main 함수1
}//end of ExData_1클래스
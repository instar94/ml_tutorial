package a.b.c.ch2;

/*
자바의 데이터 타입 : 자료형
- 자바 데이터 타입의 최소 단위는 1byte
- 1byte는 1bit
- 컴퓨터는 숫자의 크고 작음으로 사이즈를 정하지 않는다.
= 실수가 정수보다 무조건 크다.
	정수는 정수만 있고, 실수는 정수부와 실수부 두 개이므로 사이즈가 더 큼
	예) long 8byte 보다 float 4byte가 크다고 생각함

-JVM은 숫자를 int만 인식함 (4byte/32bit)
	int를 넘어가는 데이터 타입은 인식하지 못함
	=> long, float, double 데이터 타임을 인식하기 위해 표시해야함
	ex) long l= 12312341231232123L;<-

- 숫자 데이터의 형변환

	묵시적 형변환 (implcit casting)
	사이즈가 작은 데이터 타입에서 큰 데이터 타입을 대입하면 자동 형변환 발생
	명시적 형변황 (explict casting)
	큰 데이터 타입에서 사이즈 작은 데이터 타입으로 대입을 하는 경우 임의로 형변환을 해주여야함


기초자료형 : primitive type

숫자

	정수형 : default 값 : 0
		byte  1byte(08bit) - 0을 포함한 양의 정수
		short 2byte(16bit) - 음의 정수 0 양의 정수
		char  2byte(16bit) - 0을 포함한 양의 정수
			-문자형이지만 숫자로 취급함
		int   4byte(32bit) - 음의 정수 0 양의 정수
		long  8byte(64bit) - 음의 정수 0 양의 정수

	실수형 : default 값 : 0.0
		float  4byte(32bit) - 음의 실수 0 양의 실수
		double 8byte(64bit) - 음의 실수 0 양의 실수

문자 
	문자 :   char
	문자열 : String

논리

	boolean : default 값 : false
	true
	false



참조자료형 : reference type
	     빌트인 클래스 ex) array, interface 등
	     사용자 정의 클래스


자바는 객체지향이며, High-Level language이다.

자바에서 사용하는 모든 자원은 객체(object)이다.
*유일한 예외는 '기초자료형(primitive type)'

byte		Byte
char		Charcter
short		Short
int		Intger
long		Long
float		Float
double		Double
boolean		Boolean


-> 기초 자료형을 사용하면 java 내부적으로 형변환 하여
내부적으로 Wrapper class 를 사용한다.

Byte
Charcter
Short
Intger
Long
Float
Double
Boolean

*/

import a.b.c.ch2.data.Data_1_Test;

public class Data_1{

//import:다른 패키지에 있는 자원을 사용 할 때 클래스 단위로 불러오는 키워드
//import한 클래스는 패키지명 없이 클래스 이름 사용가능


	//main함수 시작
	public static void main(String[] args){
		
		//Data_1_Test의 TEST_DATA를 출력함
		//public static final int TEST_DATA=100; 이므로 콘솔 상 출력 값은 100
		System.out.println(a.b.c.ch2.data.Data_1_Test.TEST_DATA);

		//static이 붙지 않은 리소스를 사용하기 위해 Data_1_Test를 d1이라는 참조변수로 선언하고
		//new 키워드를 붙이고, 해당 클래스를 생성자로 만듬 
		//그리고 d1에 있는 i를 출력함
		//i는 원래 값이 없으나 new 키워드로 인해 초기화 되어 int형의 디폴트값인 0이 들어감
		//따라서 콘솔값은 0
		a.b.c.ch2.data.Data_1_Test d1 = new a.b.c.ch2.data.Data_1_Test();
		System.out.println(d1.i);
		
		//System.out.println(a.b.c.ch2.data.Data_1_Test.i);
		// 오류가 일어남 : static 이 붙지 않음

		//d1.a()=Data_1_Test에 있는 a함수를 불러옴
		//a함수는 System.out.println("Data_Test void a() 함수")
		// 따라서 콘솔에는 Data_Test void a() 함수 값이 출력
		d1.a();

		
		//import로 a.b.c.ch2.data의 Data_1_Test 클래스를 수입함
		// 그렇기 때문에 a.b.c.ch2.data를 생략하고 바로 클래스 명을 써도 위에 있는 것과 동일한 결과 값이 나옴
		Data_1_Test d2 = new Data_1_Test();
		System.out.println(d2.i);
		d2.a();

		//b함수는 static이 붙은 상태이기 때문에 new키워드 사용이 필요치 않음
		//a.b.c.ch2.data 디렉토리에 있는 Data_1_Test의 b함수를 불러옴
		//b함수는 System.out.println("Data_Test void b() 함수");
		// 따라서 콘솔에는 Data_Test void b() 함수가 출력
		a.b.c.ch2.data.Data_1_Test.b();

	}//end of main 함수

} // end of Data_1 클래스 
//package
package a.b.c.ch3;
//import

/*
아스키코드 ASCII
미국정보교환표준부호는 
영문 알파벳,기호, 특수기호를 사용하는 대표적인 문자 인코딩이다

ASCII는  1byte : 코드체계
		영문자(대/소) 숫자, 특수기호 :2진수,8진수,16진수
		우리는 16진수로 사용함 : 전세계 표준인 16진수
UNICOD는 2byte : 코드체계
		UTF-8 UTF-16 UTF-32


자바에서는
	문자 char 기초자료형 사용
	문자역 String 클래스 사용 (문자의 배열)
*/
public class ExCast_4 {

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) {
		//TODO Auto-generated method stub.
		System.out.println("main함수 시작>>>>>>>");
		
		//자바에서 문자열은 String 클래스로 사용

		//String :  빌트인 클래스
		//str :(String이라는 클래스의)참조변수 + 지역변수 (함수안에서 선언했기 때문)
		//String은 기초데이터형이 아니기 때문에 클래스임
		//str 참조변수에 문자열 abc로 초기화
		String str = "abc";
		System.out.println("str>>>>>"+str);

		//charAt(int) : 함수는 문자열을 문자로 하나씩 쪼개서 받을 수 있는 함수
		//문자를 하나씩 쪼게는걸 인덱스(index)라고 부른다
		//= int번째에 있는 글자를 가져온다
		//특징 : 0부터 시작함
		//c0는 str의 첫번째 글자로 초기화됨
		char c0 = str.charAt(0);
		System.out.println("char c0>>>>:"+ c0);
		
		//인코딩(incording)
		//명시적 형변환 explicit casting
		//int형 c0로 하면 a의 유니코드인 97이 나옴
		System.out.println("(int)c0>>>>:"+(int)c0);
		
		//자동형변환, 묵시적 형변환 implicit casting
		//i0라는 기초데이터형 지역변수를 선언
		//c0의 값을 i0에 초기화함 (c0=a)
		//i0는 int형이기 때문에 a의 유니코드인 97
		//반대로 a를 char로 표현하면 a가 나옴
		int i0 =c0;
		System.out.println("int i0>>> :" +i0);

		//디코딩 (유니코드(기계언어)->문자(사람언어)
		//명시적 형변환 : 캐스팅 연산자 () 를 이용
		System.out.println("(char)i0>>> :" +(char)i0);

		
		//c00라는 기초데이터형(char) 지역변수를 선언
		//그 값은 문자형인 i0
		//i0은 int형인 97를 초기화
		//97을 char하면 c00는 a가 나옴
		char c00 = (char)i0;

		//디코딩(유니코드 -> 사람문자)
		//묵시적 형변환 : 캐스팅 연산자()를 사용하지 않음
		System.out.println("char c00>>>:"+c00);


		//기초데이터형 c1은 str의 두번째 문자 = b
		char c1 = str.charAt(1);
		
		System.out.println("char c1>>>>:"+ c1);
		
		//인코딩 (사람문자->유니코드)
		//명시적 형변환 : 캐스팅 연산자 (int)를 이용
		//b의 유니코드는 98
		//따라서 char형 b를 유니코드로 바꾼 (int)c1은 98
		System.out.println("int c1>>>>:"+(int) c1);

		//기초데이터형 지역변수 i1을 선언
		//선언한 int형 i1에 char형 c1을 넣음
		//자동으로 int형으로 변환 int형은 4byte고 char형은 2byte
		int i1 = c1;

		//인코딩 (사람문자 -> 유니코드)
		//묵시적 형변환 : 캐스팅 연산자 사용X
		System.out.println("int i1 값>>>>>:"+i1);

		//디코딩 (유니코드 -> 사람언어)
		//명시적 형변환 : 캐스팅 연산자 사용
		System.out.println("(char)i1 값>>>>>:"+(char)i1);

		char c01 = (char)i1;

		//디코딩 : 사람문자 ->기계언어
		//묵시적 형변환 : 캐스팅 연산자 ()사용하지 않음
		System.out.println("char c01 값>>>>>"+c01);

		//인코딩 : 유니코드 -> 사람문자
		//명시적 형변환 : 캐스팅 연산자 () 사용
		System.out.println("int c01 값 >>>>>>"+(int)c01);

		char c2 = str.charAt(2);
		System.out.println("char c2>>>>:"+ c2);

		//인코딩 : 사람문자 -> 유니코드
		//명시적 형변환 : 캐스팅 연산자 () 사용
		System.out.println("int c2 값 >>>>>>>"+ (int)c2);
		
		int i2 = c2;

		//인코딩 : 사람문자>>>기계언어
		//묵시적 형변환 : 캐스팅 연산자 사용(x)
		System.out.println("i2 값>>>>>>>>>"+i2);

		//디코딩 : 사람문자 ->기계언어
		//명시적 형변환 : 캐스팅 연산자 ()사용
		System.out.println("(char)i2 값>>>>"+(char)i2);

		char c02 = (char)i2;

		//디코딩 : 기계언어>>>사람언어
		//묵시적 형변환 : 캐스팅 연산자 사용x
		System.out.println("c02의 값>>>>>"+c02);
		
		//인코딩 : 사람문자 >>> 유니코드
		//명시적 형변환 : 캐스팅 연산자 () 사용
		System.out.println("int c02 값>>>>>"+(int)c02);
		System.out.println("main함수 끝>>>>>>>");


	} //end of main 함수
} //end of ExCast_4 클래스

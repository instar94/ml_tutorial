package	a.b.c.ch2;

public class Data_7{

	public static void main(String[] args){
	
	/*
	지역변수 : 함수 블럭에서 선언하는 변수
	지역변수는 함수내에서 태어나 함수에서 돌아간다.
	지역변수는 함수 밖을 나갈 수 없음

	지역변수는 사용하기 반드시 의도적으로 default 값으로 초기화 되어야 한다.
	초기화 : 변수 선언 후 최초로 변수에 대입하는 행위

	지역변수의 초기화는 그 데이터의 디폴트 값으로 초기화 <- 변수를 잘 이용하는 방법
	지역변수의 초기화는 선언과 동시에 default value로 초기화 된다. <- 변수를 잘 이용하는 방법
	*/

	//기초자료형의 지역변수 초기화
	byte b =0;
	char c =' ';//싱글쿼테이션 (값이 없는 한 개의 문자)로 초기화
	short s =0; 
	int i =0;
	float f=0.0f; //float 는 실수라서 f를 붙임
	double d =0.0d; //double은 실수라서 d를 붙임
	boolean bool=false;
	String sVal1=""; //String 문자열은 "" : 더블쿼테이션로 초기화
	String sVal2=null; //String 문자열은 null로 초기화


	//Data_7 d7 =new Data_7();
	//=>멤버변수 일땐 필요하지만...함수 내에 있는 지역변수이기 때문에 필요없음

		System.out.println("b >>> : " + b);
		System.out.println("c >>> : " + c);
		System.out.println("s >>> : " + s);
		System.out.println("i >>> : " + i);
		System.out.println("f >>> : " + f);
		System.out.println("d >>> : " + d);
		System.out.println("bool >>> : " + bool);
		System.out.println("sVal1 >>> : " + sVal1);
		System.out.println("sVal2 >>> : " + sVal2);

	}//end of main 함수

}//end of Data_7 클래스
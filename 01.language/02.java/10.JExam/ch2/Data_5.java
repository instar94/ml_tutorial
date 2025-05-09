package a.b.c.ch2;

public class Data_5{

	/* 필드(=멤버변수)
	1. 상수
	2. 클래스변수
	3. 전역변수
	4. 멤버변수
	*/

	//상수(= constant) : 변하지 않고, 안되는 수
	//상수는 자바 소스코드의 맨 상단에 위치
	//상수 사용방법 : 클래스이름. 상수 변수명
	//ex)Data_5.cStr

	public static final String cStr = "나는 문자 상수";
	public static final int cInt =0;

	
	//멤버변수
	int iVal;
	String sVal;

	//클래스변수 : 멤버변수에 static을 씌운 변수
	//클래스변수 사용방법 : 클래스이름. 클래스변수명
	//ex) Data_5.siVal
	
	static int siVal;
	static String ssVal;

	//전역변수 : 어떤 패키지에서든지 사용될 수 있는 변수
	//사용하기 위해서는 new를 통해 인스턴스해야함 (=static이 없음)
	//참조변수.변수명
	//ex)d5.giVal

	public int giVal;
	public String gsVal;

	public static void main(String [] args){
	
	System.out.println("문자상수>>> :"+Data_5.cStr);
	System.out.println("숫자상수>>>> :"+Data_5.cInt);

	Data_5 d5=new Data_5();
	System.out.println("giVal >>>> :" + d5.giVal);
	System.out.println("gsVal >>>> :" + d5.gsVal);

	}//end of main 함수
}//end of Data_5 클래스
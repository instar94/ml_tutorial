package a.b.c.ch2;

public class Data_4{

	// 멤버변수 	
	// 클래스 변수 : 멤버변수에 static 키워드를 선언한 변수
	//	static 키워드 선언되어 있으면 뒤에 오는 변수를 메모리에 디폴트 값으로 초기화
	//	클래스 변수는 생성자를 이용하지 않음
	//	클래스 변수 사용은 클래스이름.변수이름
	static byte b;
	static char c;
	static short s;
	static int i;
	static float f;
	static double d;
	static boolean bo;
	static String str;	

	public Data_4(){
		System.out.println("Data_4 클래스 Data_4() 생성자");
	}//end of Data_4()생성자

	public static void main(String[] args){
	
	//System.out.println("b>>>:"+b);
	//에러 이유 : b가 메모리에 로딩되지 않았기 때문

	/* b를 메모리에 로딩 시키는 방법
	1. new 연산자 이용하기 ->참조변수를 이용
		Data_4 d4 = new Data_4();
		System.out.println("d4.b >>> : "d4.b);

	2. static 키워드 사용하기
		static byte b;
		System.out.println("Data_4.b>>>:" + Data_4.b);

	**static 키워드가 붙은 자원을 사용 할 때는 패키지명.클래스이름.스태틱 키워드가 붙은 변수명; 으로 사용
	ex) Data_4 b; */
	
	
	//static 키워드를 이용한 방법
	//(=클래스 변수를 이용한 방법)

	System.out.println("Data_4.b>>>" + Data_4.b);
	System.out.println("Data_4.c>>>" + Data_4.c);
	System.out.println("Data_4.s>>>" + Data_4.s);
	System.out.println("Data_4.i>>>" + Data_4.i);
	System.out.println("Data_4.f>>>" + Data_4.f);
	System.out.println("Data_4.d>>>" + Data_4.d);
	System.out.println("Data_4.bo>>>" + Data_4.bo);
	System.out.println("Data_4.str>>>" + Data_4.str);

	// new 키워드를 이용한 방법
	/*
	Data_4 d4 = new Data_4();

	System.out.println("d4.b >>> : "+d4.b);
	System.out.println("d4.c >>> : "+d4.c);
	System.out.println("d4.s >>> : "+d4.s);
	System.out.println("d4.i >>> : "+d4.i);
	System.out.println("d4.f >>> : "+d4.f);
	System.out.println("d4.d >>> : "+d4.d);
	System.out.println("d4.bo >>> : "+d4.bo);
	System.out.println("d4.str >>> : "+d4.str);
	*/
	}//end of main 함수

} // end of Data_4 클래스
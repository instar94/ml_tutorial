package a.b.c.ch2;

public class Data_9{

	//일반함수 + void(리턴이 없는 함수)
	//일반함수 : new키워드로 참조변수 만들어야함 -> 클래스선언 참조변수 = new 생성자이름();
	//void(리턴값x) : return 키워드 사용XX
	//함수에 매개변수 2개 : 첫번째 매개변수 int형 / 두번째 매개변수 int형
	//호출 할 때: 참조변수.함수이름(인트형 데이터,인트형 데이터)
	public void aMethod(int x1, int y1){
		System.out.println("Data_9 클래스 void aMethod()함수");

		int sum1 = x1 + y1;
		System.out.println("sum1>>>:"+ sum1);
	}//end of aMethod() 함수

	//static함수 + void(리턴이 없는 함수)
	//static함수 : new 키워드 없이 클래스명.함수명();로 사용가능
	//			->Data_9.aaMethod(int형, int형);
	//리턴값x : return 키워드 사용XX
	//함수에 매개변수 2개 : 첫번째 매개변수 int형 / 두번째 매개변수 int형
	//호출 할 때: 클래스명.함수이름(인트형 데이터,인트형 데이터)
	public static void aaMethod(int x2, int y2){
		System.out.println("Data_9 클래스 static void aaMethod()함수");

		int sum2 = x2 + y2;
		System.out.println("sum2>>>:"+ sum2);
	}//end of aaMethod 함수


	//일반함수 + 리턴값O
	//일반함수 : 호출하기 위해서 new키워드를 이용해 참조변수를 만들어야함 (참조변수.함수이름();)
	//		-> 클래스선언 참조변수=new 생성자이름();
	//리턴값O : int형 return값이 있어야함 : 함수의 결과 값이 int형이다.
	//결과값을 int형 변수로 선언해서 받기(int i)
	//함수에 매개변수 2개 : 첫번째 매개변수 int형 / 두번째 매개변수 int형
	//호출 할 때: int i=참조변수.함수이름(인트형 데이터,인트형 데이터)
	
	public int bMethod(int x3, int y3){
		System.out.println("Data_9 클래스 int bMethod()함수");

		int sum3=x3 + y3;
		System.out.println("bMethod() 함수 sum3>>>:"+sum3);

		return sum3;

	}//end of bMethod()함수

	//static 함수 + 리턴값O
	//static 함수 : new키워드 필요X 클래스이름.함수이름();로 이용가능->Data_9.
	//리턴값O : int형 return값이 있어야함 : 함수의 결과 값이 int형이다.
	//결과값을 int형 변수로 선언해서 받기(int i1)
	//함수에 매개변수 2개 : 첫번째 매개변수 int형 / 두번째 매개변수 int형
	//호출 할 때: int i1=클래스명.함수이름(인트형 데이터,인트형 데이터)
	public static int bbMethod(int x4, int y4){
		System.out.println("Data_9 클래스 int bbMethod 함수");

		int sum4= x4 + y4;
		System.out.println("bbMethod()함수 sum4>>>:"+sum4);

		return sum4;

	}//end of bbMethod() 함수

	//main 함수의 시작 : 콘솔 어플리케이션 시작
	public static void main (String[] args){
	
		//지역변수 int형 선언 및 초기화
		int x = 1;
		int y = 2;

		//static 함수 (aaMethod와 bbMethod)
		//사용방법 : 클래스명.함수명(매개변수, 매개변수);
		//매개변수와 아규먼트는 순서가 중요하다 (이름은 상관X)
		//x1이던 x2이던 순서만 맞으면 괜찮음
	
		//aaMethod 함수 답 내기
		Data_9.aaMethod(x,y);
	
		//bbMethod 함수 답 내기
		//정수형 리턴값을 받기 위해 int i 매개변수 불러옴
		int i=Data_9.bbMethod(x,y);
		System.out.println("i>>>>:"+i);

		//일반함수 (aMethod와 bMethod)
		// 사용방법 : new 키워드로 참조변수를 만들어냄
		Data_9 d9 = new Data_9();

		//aMethod 매개변수에 아규먼트 넣기
		d9.aMethod(x,y);

		//bMethod 매개변수에 아규먼트 넣기
		//정수형 리턴값을 받기 위해 int i1 매개변수 불러옴
		int i1 = d9.bMethod(x,y);
		System.out.println("i1>>>>>>"+i1);

	}//end of main() 함수
}//end of Data_9 클래스 
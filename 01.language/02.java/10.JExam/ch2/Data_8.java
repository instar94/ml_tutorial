package a.b.c.ch2;

public class Data_8{
	//Data_8의 자원 수 : 4개 (main 함수 제외)
	//함수를 부르는 행위 호출하다 / invoke

	// void 함수 = 리턴 값 X / 일반함수 - static (X) (=new 필요O)
	// 사용법 : 1)참조변수 사용 클래스이름 참조변수 =new 생성자();
	// ex) Data_8 d8 = new Data_8();
	// 2)참조변수.함수이름();
	// ex) d8.aMethod();
	public void aMethod(){
		System.out.println("Data_8 클래스 void aMethod() 함수");
	}//end of aMethod 함수


	// void 함수 = 리턴 값 X/ static (O) (new 필요X)
	// 사용법 : 클래스이름.함수이름;
	// ex) Data_8.aaMethod();
	public static void aaMethod(){
		System.out.println("Data_8 클래스 static void aaMethod()함수");
	}//end of aaMethod 함수
	

	// 리턴값 있는 함수 / 일반함수 - static(X) (new 필요 O)
	// 참조변수 사용 + 리턴형 받아사용
	// 참조변수 사용 : ex) Data_8 d8 = new Data_8();
	// 리턴값 받기 : ex) int i= d8.bMethod();
	public int bMethod(){
		System.out.println("Data_8 클래스 static void bMethod()함수");
	
		return 1;

	}//end of bMethod 함수
	
	//리턴값 있는 함수 / static(o) (new 필요 x)
	public static int bbMethod(){
		System.out.println("Data_8 클래스 static void bbMethod()함수");

		return 1;
	}//end of bbMethod 함수

	//main 함수 시작
	public static void main(String[] args){

	//static 되어 있기때문에 클래스명.함수명으로 사용가능
	//void 이기 때문에 리턴값x
	Data_8.aaMethod();

	//static 되어 있기 때문에 클레스명.함수명으로 사용가능
	//리턴 값으 있기 때문에 리턴 값을 함수에 대입함
	int i=Data_8.bbMethod();
	System.out.println("i>>>:"+i);

	//aMethod와 bMethod에는 static 되어 있지않기때문에 new로 인스턴스
	Data_8 d8 =new Data_8();

	//aMethod는 return형이 없기 때문에 두 함수를 호출(invoke)하기 위해 new키워드 사용
	//참조변수.함수명();
	d8.aMethod();
	
	//bMethod는 리턴값을 대입함
	int i1=d8.bMethod();
	System.out.println("i1>>>>"+i1);

	}//end of main 함수
}//end of Data_8 클래스
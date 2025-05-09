package a.b.c.ch2.data;

/*
1. 패키지가 다르면 
클래스, 변수, 함수 마다 '각각' public 키워드 붙여야함
*/


public class Data_1_Test{

	//메모리에 로드하기 위해서는 static / new 키워드 사용 필요
	public int i;

	
	//static 키워드가 들어갔기 때문에 바로 사용가능
	public static final int TEST_DATA=100;
	//static final int Test_DATA=100;
	//오류가 나는 이유 : public이 없으면 다른 패키지에서 사용이 불가능함

	//메모리에 로드하기 위해서는 static / new 키워드 사용 필요
	public void a(){
		System.out.println("Data_Test void a() 함수");
	}

	//static 키워드가 붙어 있어 바로 메모리로 로딩됨
	public static void b(){
		System.out.println("Data_Test void b() 함수");
	}

}//end of Data_1_Test 클래스
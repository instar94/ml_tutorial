//package
package a.b.c.ch3;
//import

public class  Test_1{

	//상수
	//멤버변수
	//생성자

	//함수
	
	//public : 어느 패키지에서나 사용가능
	//int : 정수형임
	//a() : 사용자정의 함수 이름
	//일반함수-> main함수에서 참조변수 선언 필요
	public int a(){
		System.out.println("\nTest_1.a() 함수 시작 >>>>>>>\n");

		System.out.println("\nTest_1.a() 함수 끝 >>>>>>>\n");

		//return 키워드는 함수 가장 마지막에 위치해야함
		//System.out.println이 return 아래에 오면 javac 과정에서 오류
		return 1+2;
	}//end of a() 함수


	//public : 어느 패키지에서나 사용가능
	//void : 리턴이 없음 -> return 키워드 사용 금지
	//b() : 사용자정의 함수 이름
	//일반함수-> main함수에서 참조변수 선언 필요
	public void b(){
		System.out.println("\nTest_1.b() 함수 시작 >>>>>>>\n");

		System.out.println("\nTest_1.b() 함수 끝 >>>>>>>\n");

	}//end of b() 함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.
		
		System.out.println("\nTest_1.main() 함수 시작 >>>>>>>\n");

		//일반함수 a()와 b()를 위해 참조변수 선언
		Test_1 t1 = new Test_1();
		System.out.println("t1 주소값 >>>>>>"+ t1);

		//리턴있는 함수 출력(1)
		//함수 값 자체를 출력함
		t1.a();
		System.out.println("t1.a()>>>>"+t1.a());

		//리턴있는 함수 출력(2)
		//함수의 값을 다른 변수로 받고
		//그 변수를 출력 받음
		//이 방법을 주로 사용 할 것
		int i = t1.a();
		System.out.println("i>>>>"+i);

		//리턴이 없는 함수 출력
		t1.b();
		//System.out.println("t1.b()>>>>>:" t1.b());
		//오류발생 : b() 함수는 void 함수 이기 때문에 리턴값이 없음
		//System.out.println은 리턴값을 필요로 하기 때문에 오류가 발생

		System.out.println("\nTest_1.main() 함수 끝 >>>>>>>\n");
	}//end of main()함수
}//end of Test_1 클래스

package a.b.c.ch1;

public class EX_Const{

	//멤버변수
	int i;
	char c;
	double d;
	boolean b;
	String s;

	//생성자
	public EX_Const(){
		System.out.println("EX_Const()생성자>>>");
	}

	//main() 함수 시작
	public static void main(String[] args){


		EX_Const ex_c = new EX_Const();
		System.out.println("ex_c 주소값>>>"+ex_c);
		System.out.println("ex_c.i 주소값>>>"+ex_c.i);
		System.out.println("ex_c.c 주소값>>>"+ex_c.c);
		System.out.println("ex_c.d 주소값>>>"+ex_c.b);
		System.out.println("ex_c.b 주소값>>>"+ex_c.d);
		System.out.println("ex_c.s 주소값>>>"+ex_c.s);
		/*
		1. EX_Const를 사용자 정의 클래스로 선언
		2. EX_Const를 메모리에 로드하기 위해서 참조변수로 선언
			-ex_c라는 참조변수를 사용함
		3. = : 대입연산자
		4. new : 키워드(연산자) 사용
				1) new 뒤의 클래스이름() 생성자를 자바소스코드에서 찾음
					-EX_Const() 생성자를 찾음 -> 11라인

				2) 클래스 () 생성자를 찾으면 생성자를 메모리에 로드
					-EX_Const()를 로드시킴

				3) 메모리에 로드 하면서 멤버 필드에 있는 디폴트 값으로 초기화
					-EX_Const에 있는 변수들에 디폴트 값인 0을 대입함

				4) ex_c.i => ex_c 안에 있는 i 변수를 사용한다는 의미
				마치 API에서 Java>lang>System>out>println 이어서 (java.lang.)System.out.println 인 것처럼
				EX_Const > i 라는 의미로 ex_c.i

					*/

		EX_Const ex_c_1 = new EX_Const();
		//새롭게 new로 참조변수를 만들었으므로 주소값이 달라짐

		System.out.println("ex_c_1 주소값>>>"+ex_c_1);
		System.out.println("ex_c_1.i 주소값>>>"+ex_c_1.i);
		System.out.println("ex_c_1.c 주소값>>>"+ex_c_1.c);
		System.out.println("ex_c_1.d 주소값>>>"+ex_c_1.b);
		System.out.println("ex_c_1.b 주소값>>>"+ex_c_1.d);
		System.out.println("ex_c_1.s 주소값>>>"+ex_c_1.s);
		 
		
	}//end of main 함수

} //end of EX_Const 클래스

/*
기본 생성자 (default constructer)

- 생성자를 선언하지 않고 클래스 이름() 매개변수 없는 생성자를 요청하면,
  java에서 기본 생성자를 만듬

- 기본 생성자가 멤버 필드에 있는 변수들을 디폴트 값으로 초기화 시킴

-


*/
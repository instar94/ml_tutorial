package a.b.c.ch1;

/* 자바에서 클래스의ㅣ 자원을 메모리에 얼리는 방법
1. static 키워드 사용 : main 함수만 올림
2. new 키워드(연산자) 사용 : 클래스 전체를 메모리에 올림
*/
public class EX_5{

	//멤버 변수
	//EX_5 클래스 안에서  다 쓸 수 있음
	//static 있어야 로딩이 가능 => 한번만 쓰길 지향 (1.8기준)
	int i;

	public static void a(){
		System.out.println("EX_5 :: a()함수");
	}// end of a 함수

	//main 함수 시작 : 콘솔어플리케이션의 시작점
	public static void main(String [] args){

	/* 
	new를 이용해 EX_5에 있는 자원 사용방법
	EX_5의 자원 변수 i 와 함수 a
	1) Ex_5 사용자 정의 클래스 선언
	2) EX_5를 가르키는 변수 ex5 선언
	(참조변수/레퍼런스 베리어블)
	3) '=' 대입 연산자
	4) new : 클래스를 메모리에 올리는 키워드(연산자)
		JVM은 new 키워드를 보면 클래스이름()를 메모리에 로딩함
		이때 '클래스이름()는 생성자 / 객체 라고 부름
		=> EX_5() 는 생성자 or 객체 (클래스X)
	5) EX_5 ex5=new EX_5(); 수행되면
							하위 라인부터 ex5 참조변수를 이용해 EX_5() 객체의 자원이용 가능
	*/
	EX_5 ex5=new EX_5();

	System.out.println("EX_5()의 주소값>>>>:"+ex5);
	
	System.out.println(ex5.i);
	
	ex5.a();

	}// end of main 함수
}//end of EX_5 클래스
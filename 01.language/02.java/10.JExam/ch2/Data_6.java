//자바 소스코드 작성 규칙

//1. 패키지선언
package a.b.c.ch2;

//2. import 선언 : 다른 패키지 클래스 중 자주 사용하는 것 가지고욤
import java.util.Date;

//3. class 선언
public class Data_6{

	//4. 상수 선언
	public static final String cStr = "문자 상수";

	//5. 멤버변수 선언 (멤버변수, 전역변수, 클래스변수, 은닉화(private)
	
	//멤버변수
	int i;

	//전역변수
	public float f;

	//클래스변수 : static+멤버변수
	static double d;

	//6. 생성자 선언 : 생성자 오버로딩
	Data_6 d6 = new Data_6();

	//7. 함수 선언 : 일반 함수
	public void a(){
		System.out.println("Data_Test void a() 함수");
	}//end of a()함수

	//8. 메인함수 : 가장 뒤에 위치
	//메인 함수에서 인터프리트 방식으로 위에서 선언된 변수/함수를 유기적으로 호출해 프로그램을 수행
	public static void main(String[] args){
	
	//9.지역변수 선언 및 초기화
	String str =null;
	}//end of main 함수

}//end of Data_6 클래스


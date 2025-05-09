package a.b.c.ch1;

public class Ex_Const_2{

	//a() 함수 : 리턴이 없음 -> void 사용 return 없음
	public void a(){
		System.out.println("Ex_Const_2 :: void a() 함수");
	}//end of a()함수

	//b() 함수 : 리턴이 있므 -> void 사용 return 있음
	// return은 String (문자열)이 될 것임
	public String b(){
		return "Ex_Const_2:: String b() 함수";
	}//end of b()함수

	//main 함수 시작 - 콘솔 어플리케이션 시작
	public static void main(String [] args){

	
	Ex_Const_2 ex_c2 = new Ex_Const_2();
	System.out.println("Ex_Const_2() ex_c2의 주소값>>>>"+ex_c2);

	//System.out.println(ex_c2.a()); 
	//오류 발생
	// 이유 : System.out.println 에서는 리턴 값이 없는 함수(void 함수)를 사용 할 수 없음
	// ex_c2.a()는 void가 들어간 함수로 에러가 발생

	ex_c2.a();
	//println이 안되므로 콘솔창에 입력되는 것이 없음

	System.out.println(ex_c2.b());
	//b()는 리턴이 있는 함수이기 때문에 println을 사용 가능
	//그래도 값이 없으므로 콘솔창에 표시되는 것은 없음

	String str = ex_c2.b();
	//str 이라는 변수에 매개변수 ex_c2.b()를 넣음

	System.out.println("str>>>>:"+str);
	//str = ex_c2.b()함수 = 문자열 "Ex_Const_2:: String b() 함수" 표시

	}//end of main 함수

}//end of Ex_Const_2 클래스

/*콘솔 결과
Ex_Const_2() ex_c2의 주소값>>>>a.b.c.ch1.Ex_Const_2@15db9742
Ex_Const_2 :: void a() 함수
Ex_Const_2:: String b() 함수
str>>>>:Ex_Const_2:: String b() 함수
*/

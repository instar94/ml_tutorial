package a.b.c.ch1;

public class EX_3{

	public static void main(String [] args){
	
	System.out.println("Ex_3 :: main() 시작 >>> :  ");

	int i=1;
	System.out.println(i);

	i=2;
	System.out.println(i);

	// System.out.println(ii);
	// 컴파일 시 오류가 발생함
	// 이유 : 지역변수 ii 초기화 X
	// 지역변수 : 함수 블럭 안에서 선언하는 변수
	// 지역변수는 사용하기 전에 '초기화 필수' <- 디폴트 값이 없음

	int ii=22;
	System.out.println(ii);

	System.out.println("Ex_3 :: main() 끝 >>> :  ");
	}// end of main 함수
}//end of EX_3 클래스
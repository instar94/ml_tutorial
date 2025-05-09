package a.b.c.ch1;

public class EX_4{

	public static void main(String [] args){
	
	System.out.println("Ex_4 :: main() 시작 >>> :  ");

	/*
	변수를 사용하는 이유
	: 데이터 담으려거나 담아 데리고 다니면서 사용하려고
	=> 변수를 사용/호출 할때는 변수 명 사용
	So, 같은 블록에 변수 명이 동일 한 것이 있으면 사용 어려움
	*/
	int i=1;
	System.out.println(i);

	// int i =2; 
	//(에러발생 = 같은 지역변수임)
	
	i=2;
	System.out.println(i);
	// 변수를 새로 선언 하지 않고 값만 새로운 값을 집어넣어줌

	System.out.println("Ex_4 :: main() 끝 >>> :  ");
	}// end of main 함수
	
	int i = 2; 
	//선언해도 문제 없음 
	// 이유 :둘이 서로 다른 종류 (멤버변수와 지역변수)

}//end of EX_4 클래스
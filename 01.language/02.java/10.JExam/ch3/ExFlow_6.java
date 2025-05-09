//package
package a.b.c.ch3;
//import

public class ExFlow_6{

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.
		
		//while문
		//조건식 ()의 값이 true일 경우 반복한다.
		//조건식 ()의 값이 false일 경우 작동하지 않는다.
		//멈추는 키워드(break)가 있어야만 한다.
		while (true){
			System.out.println("while >>>>>");

			if(true){
				break;
			}//end of if문
		}//end of while문
		
		/*
		아예 동작이 되지 않음
		-> 출력되는 것이 없음
		while (false){
			System.out.println("while>>>>:");
		}
		*/
		
		//do while ()
		//인터프리트 방식임 (위에서 아래로 차례대로 내려감)
		//while문에서 while(false)의 경우 아예 작동이 되지 않음=> 아예 작동X
		//do while문에서 while(false)는 1번 작동하고 끝난다. => 작동 1회함
		do{
			System.out.println("do>>>>>>: ");
		}
		while (false);
	}//end of main 함수
}//end of ExFlow_6 클래스
//package
package a.b.c.ch3;
//import

public class ExFlow_8 {

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) {
	//TODO Auto-generated method stub.
		for (int i = 0 ; i < 3 ; i++ ){
			
			for (int j = 0 ;j < 3 ; j++ ){
				System.out.println("("+i+","+j+")");
			}//end of for문
		}//end of for문

		System.out.println("\n");

		for (int i = 0 ; i < 3 ; i++ ){
			
			for (int j = 0 ;j < 3 ; j++ ){
				System.out.print("("+i+","+j+")");
			}//end of for문
		}//end of for문
		
		System.out.println("\n");

		//일반적으로 말하는 배열의 형태
		for (int i = 0 ; i < 3 ; i++ ){
			
			for (int j = 0 ;j < 3 ; j++ ){
				System.out.print("("+i+","+j+")");
			}//end of for문
			System.out.println();
		}//end of for문

	}//end of main 함수
}//end of ExFlow_8 클래스

//package
package a.b.c.ch3;
//import

public class ExFlow_7_2 {

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) {
		//TODO Auto-generated method stub.
		// =가 없을때 한 번 덜 돔 (미만 => 해당 값을 포함하지 않음)
		System.out.println("i <= 3");
		for (int i = 0; i < 3 ; i++){
			System.out.println(i);
		}

		// =을 표시했을 때 한번 더 돔 (이하 => 해당 값까지 포함한 값)
		System.out.println("\ni <= 3");
		for (int i = 0; i <= 3 ; i++){
			System.out.println(i);
		}
		/*
		//안녕하세요 문자열을 콘솔에 1000000번 출력
		//초기화식 : int i = 0
		//조건식 : i<1000000
		//증감식 : i++
		for (int i = 0; i<=1000000;i++ ){
			System.out.println("안녕하세요 "+ i);
		}//end of for문
	
		//i가 0에서 시작하는 것보다 끝 지점에서 시작하는 것이 
		//속도가 미세하게 빠름
		for (int i =1000000 ;i>=0 ;i-- ){
			System.out.println("안녕하세요"+i);
		}//end of for문
		*/
	}//end of main 함수
}//end of ExFlow_7_2 클래스

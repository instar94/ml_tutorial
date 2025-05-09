// package : 패키지 키워드를 선언 한다. 
// pakage 명 a.b.c
// ; : 패키지 선언문 종결
package a.b.c;

// MainTest : MainTest 라는 이름으로 클래스 선언 
// public 키워드를 선언 -> 어느 패키지에서나 사용 가능
// class 키워드를 선언  
// 클래스 블럭(scope, 영역)표시 //  {} 브레이스 연산자로 표시
public class MainTest {

	// main() 함수를 선언 -> 단 한 번만 사용 
		// main() 함수의 블럭은 {}로 영역 표시 
	public static void main(String[] args){
		// 인터프리트 방식 : main() 블럭(scope, 영역)안에서 첫 라인부터 문장을 한 라인씩 읽어서 수행
		System.out.println("MainTest main() 함수 시작 >>> : ");
		System.out.println("콘솔어플리케이션에서는 main() 함수가 시작점이다.");
		System.out.println("main() 함수 블럭 안에서는 인터프리트 방식(순차적)으로 수행된다.");
		System.out.println("MainTest main() 함수 끝 >>> : ");

	} // end of main 함수 
} // end of MainTest 클래스 
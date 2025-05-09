package a.b;

//
//main 함수가 있고 public 으로 된 클래스는
// 자바 파일과 클래스의 명이 동일해야함
// public class A + main함수-> 컴파일에서 오류

class A{
//클래스 이름과 파일명이 다르지만
//public이 붙어 있지 않기 때문에 컴파일 가능

	//main 함수 시작
	public static void main(String [] v){
	
	}// end of main 함수
}//end of A 클래스

/* 정리

자바 소스코드를 저장 규칙

main() 함수가 있는 클래스는
1) public class : class 앞에 public 키워드를 넣음
2) 자바 파일 명과 public class 명을 동일하게 가져감

예외)
- public이 붙지 않았다면 소스파일과 클래스 이름 다를 수 있음
- 단 이 경우, 실행 할 때는 클래스 명으로 실행 시켜야함
- 위의 경우 
	javac -d . A.java -> 자바 파일 단위로 컴파일
	java a.b.AA -> 실행은 클래스명으로

*/
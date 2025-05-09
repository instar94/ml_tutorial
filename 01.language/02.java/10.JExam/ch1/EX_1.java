package a.b.c.ch1;

public class EX_1{

	//main 함수
	//자바 버츄얼 머신 : Java Virtual Machine : JVM(=java.exe)
	//main() 함수는 자바 콘솔 어플리케이션의 사작점
	/* 이 패키지가 cmd로 실행되는 과정
	0. cmd에 java.a.b.c.ch1.Ex_1  입력
	1. 물리적 파일 위치(a.b.c.ch1)으로 가서 Ex_1.class를 읽음
	2. Ex_1.class를 컴퓨터 메모리에 로드 (아직 실행된 것 X)
	3. 로딩된 a.b.c.ch1.Ex_1 클레스의 main () 함수 호출
	4. 호출된 main 함수 블록의 첫 라인 부터 수행
	5. System.out.println() 실행
	ㄴ 함수에 있는 인자(아규먼트)를 콘솔에 출력!
	* 값을 return 하는 것이 아님!!
	-return : 수학 문제의 값을 내봐 
	=> 문제에 대한 답을 낸 것 => return임
	- println : 수학 문제 푸는 과정에서 중간 값을 알려줘 
	=> 문제에 대한 답을 낸 것X => return 값이 아님
	*/
	public static void main(String [] args){
		//콘솔에 출력하시오
		System.out.println("자바 문법 첫번째 예제 EX_1!!");
		/*
		System : java.lang.System 클래스 자바프로그램에서 입출력, 프로퍼티 
				 및 시스템 관련 일을 담당하는 클래스
		out : System 클래스에 있는 out 필드 (변수) : 콘솔에 출력하는 통로 역할을 함
		println() : 콘솔에 println 함수의 아규먼트를 프린트 하는 함수
				  : 프린트 하고 라인 하나는 떨어 트린다.
			public void println(String x)
		*/
	}//end of main 함수
}//end of EX_1 클래스
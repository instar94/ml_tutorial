package a.b.c.ch2;

/*
1. public : 사용자 정의 클래스 Data_2를 패키지 밖에서도 호출 가능
2. class : 이 사용자 정의 클래스는 일반클래스
3. Data_2 : 식별자
*/
public class Data_2{

/*
	1. public : main 함수는 패키지 밖에서 사용 가능
	2. static : main 함수를 메모리에 로드함(JVM)
	3. void : return 키워드 사용 불가(=리턴 값이 없음)
	4. main : java에서 정해진 함수명 (변경 불가능)
	5. () : main의 아규먼트가 들어가는 공간
	6. String : 빌트인 클래스
		
		- String 클래스는 rt.jar에 java.lang.String 형태로 존재
		-> 따라서 사용자 정의 클래스인 a.b.c.ch2.Data_2에서 사용하려면
		import java.lang.String;해야하지만 
		자바 문법에서 java.lang 패키지에 있는 클래스는 사용 빈도도 많고
		기초 클래스이기 때문에 개발자가 사용자 정의 클래스를 만들면 기본적으로 import ehla
		=> java.lang. 패키지 외 다른 패키지는 무조건 import해서 사용함

	7. [] : 배열 연산자
	8. args : 아규먼트 변수명 (다른 변수명과 중복되지 않는 한 변경 가능)
*/
	//main 함수 시작
	public static void main(String [] args){
	
	//System.out.println : 콘솔에 출력하시오 
	//(java.lang에 있으므로 import x)
	System.out.println("main() 함수는 프로그램의 시작점이다 >>>>:");
	System.out.println("함수 블럭에서 인터프리트 방식으로 수행된다.>>>:");
	System.out.println("자바 기초 자료형 배우기 >>>> :");
	} //end of main() 함수

} //end of Data_2 클래스


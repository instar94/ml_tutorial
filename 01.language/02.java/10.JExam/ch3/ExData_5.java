/*
	문제)

	ExData_5 클래스에서
	리턴이 있는 함수 + static이 없는 addMethod()를 만들어서
	매개변수 int x, int y를 받아서
	더하기결과를 return 키워드의 결과 값으로 만들기
	
	main 함수에서 addMethod()에
	지역변수 int형 x,y를 선언한 뒤,
	x=10, y=20으로 초기화 해서
	아규먼트로 전달해서
	int sum 지역변수에 결과 값을 대입해서
	콘솔에 출력하시오

	풀이)
	- 함수
		리턴형 있음
		static 없음 = 일반함수 =참조형 사용
		매개변수 : int x, int y
		더하기 결과를 return 값으로 가지되
		int sum이라는 지역변수에 결과 값을 대입
		=> return 값을 x+y로 가지는 것이 아닌 sum이라는 새로운
		int형 변수를 만들어서 할 것

	-메인함수
	지역변수 int x와 int y를 선언 + 초기화
	콘솔에 int sum을 활용하여 전달
*/

//package
package a.b.c.ch3;

//import

public class ExData_5{
	//상수
	//멤버변수
	//생성자
	
	//데이터 타입 : int
	//함수 이름 : addMethod
	//int형 변수 x와 y를 매개변수로 사용 -> (int x, int y)

	//리턴형 있는 함수 + 일반함수
	//일반함수임으로 참조변수가 필요 -> main 함수에서 new 키워드 이용
	//sum이라는 int형 변수가 필요함
	public int addMethod(int x, int y){
		
		System.out.println("ExData_5.addMethod() 함수 시작 >>>>\n");
		//int형 x와 y를 아규먼트로 받음
		//x와 y를 더한 새로운 int형 변수 sum을 만듬
		
		//아규먼트는 main함수에서 올 것임
		System.out.println("ExData_5.addMethod() x>>>>:"+x);
		System.out.println("ExData_5.addMethod() y>>>>:"+y);
		
		//둘을 더한 x와 y를 sum이라는 int형 지역변수에 넣는다.
		int sum = x + y;

		System.out.println("ExData_5.addMethod() sum>>>>"+sum);
		
		System.out.println("\nExData_5.addMethod()함수 끝 >>>>\n");
		//return 값이 있는 함수이므로 return 키워드 사용
		//return 값으로 x와 y를 더한 sum을 받을 것
		return sum;
	
		//return x+y; 도 됨 (굳이 sum 더 만들 필요 없음)

	}//end of addMethod 함수

	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		
		System.out.println("main 함수 시작 >>>>\n");
		
		//지역변수 선언
		//int형 변수 x와 y를 지역변수로 선언하고
		//각 각 리터럴을 초기화
		int x = 10;
		int y = 20;
		
		//addMethod가 참조변수를 필요로함
		//참조변수 ed5 선언
		ExData_5 ed5 = new ExData_5();

		//리턴값을 함수에 집어넣음
		int sum = ed5.addMethod(x,y);

		//리턴값이 있기 때문에 println을 통해서
		//콘솔에 출력 가능
		System.out.println("sum 값 >>>>>>:"+ sum);
		
		/*
		cf) 이렇게도 호출 할 수 있음
		System.out.println("ExData_5>>>"+ new ExData_5().addMethod(x,y));

		int sum1 = new ExData_5().addMethod(x,y);
		System.out.println("ExData_5.main().addMethod() sum>>>" + sum);
		*/
		
				
		System.out.println("\nmain 함수 끝 >>>>");
	}//end of main 함수
}//end of ExData_5 클래스

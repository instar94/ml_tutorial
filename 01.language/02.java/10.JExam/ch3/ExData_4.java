//package
package a.b.c.ch3;

//import


/* 1 더하기 1 프로그램 만들기

만드는 방법

1) 함수를 만들어서 한다 or main 함수에서 작성한다.
2) 출력하면서 변수 두 개를 받아서 더한다. or 변수 두 개를 더하고, 그 값을  출력한다.
- System.out.println(x + y);
- int sum = x + y;
	System.out.println(sum);
3) void 함수를 쓴다 or return 값을 받는다.

*/

//함수를 만들어서 사용하는 경우 (4가지)
public class ExData_4{
	
	//상수
	
	//멤버변수
	
	//생성자
	
	//함수
	
	//함수에서 만들기(1) 일반함수, 리턴값x, x+y
	//일반함수 : 참조변수 필요-> ExData_4 ed4 = new ExData_4();
	//매개변수 2개 (int형, int 형)
	//받은 아규먼트를 println에서 더해버림
	//사용방법 : 참조변수 선언 후 ex4.add_0(x,y);
	public void add_0(int x, int y){
		System.out.println(x+y);

		System.out.println("ExData_4.add0() 함수의 시작>>>>>:\n");
		
		System.out.println("매개변수 int x에 아규먼트 x로 넘어온 값을 대입 int x = x>>>:"+x);
		System.out.println("매개변수 int x에 아규먼트 y로 넘어온 값을 대입 int y = y>>>:"+y);

		//x + y 연산 결과를 콘솔에 출력
		System.out.println("x+y>>>>:"+(x+y));

		System.out.println("\nExData_4.add0() 함수의 끝 >>>>>>:");

	}//end of add_0 함수

	//함수에서 만들기(2) 일반함수, 리턴값x, sum
	//일반함수 : 참조변수 필요 -> ExData_4 ed4 = new ExData_4();
	//매개변수 2개 (int형, int형)
	//두 매개변수를 더하는 int형 지역변수 sum을 만듬
	//그 sum을 println함
	//사용방법 : 참조변수 선언 후 ex4.add_1(x,y);
	public void add_1(int x, int y){

		System.out.println("ExData_4.add0() 함수의 시작>>>>>:\n");
		
		System.out.println("매개변수 int x에 아규먼트 x로 넘어온 값을 대입 int x = x>>>:"+x);
		System.out.println("매개변수 int x에 아규먼트 y로 넘어온 값을 대입 int y = y>>>:"+y);

		//int형 매개변수 x와 y를 add_3()함수에 호출
		//sum이라는 int형 지역변수에 x + y 값을 대입
		int sum = x + y;
		System.out.println("sum>>>>"+sum);

		System.out.println("\nExData_4.add_1() 함수의 끝 >>>>>>:");

	}//end of add_1 함수

	//함수에서 만들기(3) 일반함수, 리턴값o, x+y
	//일반함수 : 참조변수 필요 -> ExData_4 ed4 = new ExData_4();
	//매개변수 2개 (int형, int형)
	//return 값에 x+y를 리턴 함
	public int add_2(int x, int y){

		System.out.println("ExData_4.add0() 함수의 시작>>>>>:\n");
		
		System.out.println("매개변수 int x에 아규먼트 x로 넘어온 값을 대입 int x = x>>>:"+x);
		System.out.println("매개변수 int x에 아규먼트 y로 넘어온 값을 대입 int y = y>>>:"+y);

		//매개변수 지역변수 int x와 int y를 더하고 변수로 사용하지 않고
		//return 값으로 호출
		System.out.println("x+y>>>>:"+(x+y));
		
		System.out.println("\nExData_4.add_2() 함수의 끝 >>>>>>:");
		return x + y;
		

	}//end of add_2()함수


	//함수에서 만들기(4) 일반함수, 리턴값o, sum
	//일반함수 : 참조변수 필요 -> ExData_4 ed4 = new ExData_4();
	//매개변수 2개 (int형, int형)
	// x와 y를 더한 int형 변수 sum 을 만듬
	// return  값에 sum을 리턴함
	public int add_3(int x, int y){
		
		System.out.println("ExData_4.add0() 함수의 시작>>>>>:\n");
		
		System.out.println("매개변수 int x에 아규먼트 x로 넘어온 값을 대입 int x = x>>>:"+x);
		System.out.println("매개변수 int x에 아규먼트 y로 넘어온 값을 대입 int y = y>>>:"+y);

		//int형 매개변수 x와 y를 add_3()함수에 호출
		//sum이라는 int형 지역변수에 x + y 값을 대입
		int sum = x + y;
	
		//int형 지역변수 sum 을 호출 -> 콘솔출력
		System.out.println("sum>>>:" + sum);

		System.out.println("\nExData_4.add_3() 함수의 끝 >>>>>>:");	

		//int형 지역변수 sum을 호출하여 return value로 호출
		return sum;

		

	}//end of add_3함수



	//main() 함수 : 콘솔어플리케이션의 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		
		//main함수에서 구현(1)
		//아규먼트를 println하는 과정에서 더한다.
		System.out.println(1+1);
		System.out.println("1+1=" + 1+1); //문자형 숫자 더하기가 되어 11이됨
		System.out.println("1+1=" +(1+1));

		//int형 변수 x와 y에 각각 값(리터럴)을 1로 초기화
		int x = 1;
		int y = 1;

		//main함수에서 구현(2)
		//변수에 값이 초기화된 후 println 하는 과정에서 더한다.
		System.out.println(x+y);

		//main함수에서 구현(3)
		int sum = x + y;

		System.out.println(sum);

		//참조변수 사용 ed4
		//add_0,add_1,add_2,add_3 함수는 모두 일반함수이기 때문에
		//참조변수가 필요해서 new 키워드를 사용함
		ExData_4 ed4 = new ExData_4();

		//add_0와 add_1은 리턴값이 없는 void 함수이기 때문에 println을 사용 불가능
		//함수 아규먼트를 int형 지역변수 값에 전달
		ed4.add_0(x, y);
		ed4.add_1(x, y);

		//add_2와 add_3은 리턴 값이 존재함으로 println  사용 가능
		//return 값을 int형으로 받기 위해서 int sum 변수랑 이어줌
		//함수의 결과 값을 int형 sum3의 결과 값을 콘솔에 출력
		
		int sum2 = ed4.add_2(x, y);

		//지역변수 sum2를 호출해서 sum2의 결과 값을 콘솔에 출력
		System.out.println(sum2);

		
		int sum3 = ed4. add_3(x, y);

		//지역변수 sum3를 호출해서 sum3의 결과 값을 콘솔에 출력
		System.out.println(sum3);


	}//end of main 함수
}//end of ExData_4 클래스

/*
1. 사칙연산 프로그램 만들기
2. 사칙연산자 : +, -, *, /
3. 변수 : main함수 지역변수로 int x, int y
	초기화는 20, 10으로 함
4. 더하기 함수 이름 : public int addM(int x, int y)
5. 빼기 함수 이름 : public int subM(int x, int y)
6. 곱하기 함수 이름 : public int ,mulM(int x, int y)
7. 나누기 함수 이름 : public int dicM(int x, int y)
8. 각 연산은 함수 블럭에서 하고 결과는 int sum으로 받음
9. 각 연산자 함수 블럭에서 리턴은 지역변수 int sum
10. main() 함수에서 각 연산자 함수를 호출해서 결과값을
	하기 지역변수로 받아서 콘솔에 출력한다.
	각 연산자 함수 호출은 참조변수를 이용한다 -> static 사용 X
	int addV, int subV, int mulV, int divV
11. 패키지는 a.b.c.ch3; 
*/

//package
package a.b.c.ch3;

//import

public class ExData_6{
	//상수
	//멤버변수
	//생성자
	
	//함수
	
	//더하기 함수
	//매개변수 2개를 가지는 일반함수 (int 형, int 형)
	//일반함수이기 때문에 main()에서 참조변수 선언 후 사용 가능
	public int addM(int x, int y){

		System.out.println("\naddM함수 시작>>>>>>\n");

		//콘솔에 함수에 들어가는 리터럴을 출력
		System.out.println("ExData.addM() x>>>>>:"+x);
		System.out.println("ExData.addM() y>>>>>:"+y);

		//연산 결과 값을 sum이라는 int형 변수에 대입
		int sum = x + y;

		System.out.println("\nExData.addM() 끝>>>>>>\n");

		//결과 값 변수인 sum을 리턴에 대입
		return sum;



	}//end of addM 함수

	//빼기함수
	//매개변수 2개를 가지는 일반함수 (int 형, int 형)
	//일반함수이기 때문에 main()에서 참조변수 선언 후 사용 가능
	public int subM(int x, int y){
		System.out.println("\nsubM함수 시작>>>>>>\n");

		//콘솔에 함수에 들어가는 리터럴을 출력
		System.out.println("ExData.subM() x>>>>>:"+x);
		System.out.println("ExData.subM() y>>>>>:"+y);

		//연산 결과 값을 sum이라는 int형 변수에 대입
		int sum = x - y;

		System.out.println("\nExData.subM() 끝>>>>>>\n");
		
		//결과 값 변수인 sum을 리턴에 대입
		return sum;



	}//end of addM 함수

	//곱하기함수
	//매개변수 2개를 가지는 일반함수 (int 형, int 형)
	//일반함수이기 때문에 main()에서 참조변수 선언 후 사용 가능
	public int mulM(int x, int y){
		System.out.println("\nmulM함수 시작>>>>>>\n");

		//콘솔에 함수에 들어가는 리터럴을 출력
		System.out.println("ExData.mulM() x>>>>>:"+x);
		System.out.println("ExData.mulM() y>>>>>:"+y);

		//연산 결과 값을 sum이라는 int형 변수에 대입
		int sum = x * y;

		System.out.println("\nExData.mulM() 끝>>>>>>\n");
		
		//결과 값 변수인 sum을 리턴에 대입
		return sum;



	}//end of addM 함수

	//나누기 함수
	//매개변수 2개를 가지는 일반함수 (int 형, int 형)
	//일반함수이기 때문에 main()에서 참조변수 선언 후 사용 가능
	public int divM(int x, int y){
		System.out.println("\ndivM함수 시작>>>>>>\n");

		//콘솔에 함수에 들어가는 리터럴을 출력
		System.out.println("ExData.divM() x>>>>>:"+x);
		System.out.println("ExData.divM() y>>>>>:"+y);
		
		//연산 결과 값을 sum이라는 int형 변수에 대입
		int sum = x / y;


		System.out.println("\nExData.divM() 끝>>>>>>\n");
		
		//결과 값 변수인 sum을 리턴에 대입
		return sum;

	}

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		
		System.out.println("\nmain함수 시작>>>>>>\n");

		//지역변수 선언 및 초기화
		int x = 20;
		int y = 10;

		//참조변수 - new 인스턴스
		//일반함수이기 때문에(static 사용x) 필요
		ExData_6 ed6 = new ExData_6();
		System.out.println("ExData_6() ed6 주소값>>>>>>>"+ ed6);

		//각 함수의 sum 값을 지역변수로 호출 
		//더하기 값 호출
		int addV = ed6.addM(x, y);
		
		//빼기 값 호출
		int subV = ed6.subM(x, y);
		
		//곱하기 값 호출
		int mulV = ed6.mulM(x, y);
		
		//나누기 값 호출
		int divV = ed6.divM(x, y);

		//각 값을 콘솔로 결과 값 출력
		//리턴값이 있는 함수이기 때문에 println 을 이용 할 수 있음
		
		//더하기 결과값
		System.out.println("ed6.addM(x,y);>>>>>:"+addV);
		
		//빼기 결과 값
		System.out.println("ed6.subM(x,y);>>>>>:"+subV);
		
		//곱하기 결과 값
		System.out.println("ed6.mulM(x,y);>>>>>:"+mulV);
		
		//나누기 결과값
		System.out.println("ed6.divM(x,y);>>>>>:"+divV);
		
		
		System.out.println("\nmain함수 끝>>>>>>\n");
	}//end of main 함수
}//end of ExData_6 클래스

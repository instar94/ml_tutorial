//package
package a.b.c.ch3;
//import

public class ExOper_2{
	//상수
	//멤버변수
	//생성자
	
	//함수
	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		
		//관계연산자 : 연산의 결과를 논리 값(boolean)으로 변환
		//boolean : true of false
		System.out.println(3<5);
		System.out.println(3>5);
		System.out.println(3<=5);
		System.out.println(3<=5);

		//== : 상등연산자 cf) = : 대입연산자
		System.out.println(3==5);
		//!: 반대로 != 같지 않으면
		System.out.println(3!=5);

		//기초자료형(boolean) 지역변수 bool 선언
		//bool을 false로 초기화함
		boolean bool = false;

		bool = 3 < 5;
		System.out.println("3 < 5 :"+bool);

		bool = 3 > 5;
		System.out.println("3 > 5 :"+bool);

		bool = 3 <= 5;
		System.out.println("3 <= 5 :"+bool);

		bool = 3 >= 5;
		System.out.println("3 >= 5 :"+bool);

		bool = 3 == 5;
		System.out.println("3 == 5 :"+bool);

		bool = 3 != 5;
		System.out.println("3 != 5"+bool);


		//문자 대소비교
		bool = 'a' < 'b';
		System.out.println("a < b" +bool);

		bool = 'A' < 'B';
		System.out.println("A < B" +bool);

		bool = 'A' < 40;
		System.out.println("A < 40 "+bool);

		bool = 'A'< 0x65;
		System.out.println("A < 0x65" +bool);

		bool= 'a' < '가';
		System.out.println("a < 가 " +bool);
		
		bool= '가' < '나';
		System.out.println("가 < 나 " +bool);

		/*
		
		관계연산자는 기초자료형만 가능
		
		문자열이라서 불가능
		bool= '가나' < '나라';
		System.out.println("가나 < 나라 " +bool);

		"나"를 더블쿼테이션(문자열)로 선언해서 불가능
		bool= '가' < "나";
		System.out.println("가 < 나 " +bool);
		*/

		/*
		논리연산자 : &&,||,!
		T AND T = T
		T AND F = F
		F AND T = F
		F AND F = F

		T OR T = T
		T OR F = T
		F OR T = T
		F OR F = F
		*/
		System.out.println("논리연산 >>>>>>>>\n");

		boolean bVal = 5 > 3 && 5 > 2;
		boolean bVal11 = 5 > 3;
		System.out.println(bVal11);
		boolean bVal12 = 5 > 2;
		System.out.println(bVal12);
		boolean bVal13 = true && true;
		System.out.println(bVal13);

		boolean bv = 5 > 3 || 5 > 2;
		boolean bv1 = 5 > 3;
		System.out.println(bv1);
		boolean bv2 = 5 > 2;
		System.out.println(bv2);
		boolean bv3 = true || true;
		System.out.println(bv3);

		//자바 논리연산의 단축평가 : short-circuit
		//논리연산의 모든 항을 계산하는 것이 아니라 하나만 보고 판단
		//ex) F and T 던 F and F 던 처음이 F면 사실상 false이기 때문에 반만 보고 문제를 품

		int num1 = 10;
		int i = 2;

		//num1 = 30 / i =4 
		//false and true
		//하지만 단축평가로 인해 i는 2값이 들어가있음
		boolean v = ((num1= num1 + 10)) < 10 &&((i = i + 2)< 10);
		System.out.println(v);//콘솔값 : fasle
		System.out.println(num1);//콘솔값 : 20 
		System.out.println(i);//콘솔값 : 2 <- 단축평가현상

		//num1 = 30 / i = 4
		//true or true
		// 둘다 true
		//하지만 단축 평가로 인하여 num1은 30이 대입되지면
		//i는 4가 아닌 2가 들어가있음
		v = ((num1 = num1 + 10) > 10) || ((i = i + 2)< 10);
		System.out.println(v);//콘솔값 : true
		System.out.println(num1);//콘솔값 : 30
		System.out.println(i); //콘솔값 : 2 <-단축평가 현상

		v = ((num1 = num1 + 10) > 10) || ((i = i + 2) < 10);
		System.out.println(v);
		System.out.println(num1);
		System.out.println(i);

		v = ((num1 = num1 + 10) < 10) || ((i = i + 2) < 10);
		System.out.println(v);
		System.out.println(num1);
		System.out.println(i);


		//복합 대입연산자
		//두 가지 연산자를 합쳐서 새로운 의미로 사용하는 연산자
		System.out.println("복합대입 연산자 >>>>>>>>>>");
		
		//기초자료형(int) 지역변수 s 선언
		// s를 리터럴 10으로 초기화
		int s = 10;
		//s를 호출하고 10을 더함
		//+= 왼쪽에 있는거에 값을 더함
		System.out.println(s +=10);
		//-=:왼쪽에 있는 값에 오른쪽 값을 뺌
		System.out.println(s -=10);
		//*=: 왼쪽에 있는 값에 오른쪽 값을 곱함
		System.out.println(s*=10);

		//삼항 연산자 : 조건 연산자
		System.out.println("삼항 연산자 : 조건 연산자 >>>>>>");
		//(조건식) ? 결과1 : 결과2

		//5 > 3이 true면 10 // false 20
		int n = (5 > 3) ? 10 : 20;
		System.out.println(n);

		int n1 = (5 < 3) ? 10 : 20;
		System.out.println(n1);

	}//end of main 함수
}//end of ExOper_2

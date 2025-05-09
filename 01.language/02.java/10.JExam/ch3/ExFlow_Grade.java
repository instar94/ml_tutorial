//package
package a.b.c.ch3;

//import
//nextInt()를 사용하기 위해 Scanner 클래스를 import함
import java.util.Scanner;


public class ExFlow_Grade{

	//상수
	//멤버변수
	//생성자

	//함수
	//일반함수 + void 함수 선언
	//일반함수 : 사용하기 위해서 참조변수를 선언 -> main함수에서 참조함수 선언
	//void 함수 : return 키워드 사용 불가능
	//매개변수로 int score 라는 기초데이터형 지역변수 사용 -> main에서 선언 및 초기화 진행
	public void gradeFun(int score){

		System.out.println("\nExFlow_Grade.gradeFun()함수 시작>>>>\n");
		System.out.println("ExFlow_Grade.gradeFun score 값>>>>" + score);
		
		//성적을 나타낼 문자 데이터 지역변수 선언
		//grade 값을 디폴트값(null)로 초기화
		char grade = '\u0000';
		//char grade=' ';
		//'\u0000'= ' ' 유니코드로 만든 null 값임



		//점수에 따른 분류 if
		//값이 서로 독립적 X => if가 swich보다 나음
		if(score>= 90){ //90~100 : A학점
			grade = 'A';

		}else if (score >= 80){
			grade = 'B';

		}else if (score >= 70){
			grade = 'C';

		}else if (score >= 60){
			grade = 'D';

		}else{
			grade = 'F';

		}
		
		System.out.println("ExFlow_Grade.gradeFun grade 값>>>>" + grade);
		
		System.out.println(score+"점이므로 "+grade+"학점 입니다.");

		System.out.println("\nExFlow_Grade.gradeFun()함수 끝>>>>\n");
		}//end of gradeFun함수
	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.
		System.out.println("\nExFlow_Grade.main()함수 시작>>>>\n");
		System.out.println("점수를 입력해주세요");

		//nextInt();를 사용하기 위해서 Scanner 클래스를 참조변수로 선언
		//매개변수를 System.in으로 호출
		//System.in : 콘솔에서 input을 받아서 값을 가져옴
		Scanner sc = new Scanner(System.in);
		//nextInt(); Intput받은 정수를 가져옴
		//score에서 인풋받은 값을 대입함
		int score = sc.nextInt();

		//0 ~ 100 사이의 숫자가 입력된 경우 학점 계산 실행
		//()안 조건의 결과 값이 true일 경우 실행
		//score : main 함수에서 score 값을 호출함
		if(score > 0 && score <= 100){

			//일반함수인 gradeFun() 함수를 사용하기 위해서 참조변수 선언
			ExFlow_Grade ef_g = new ExFlow_Grade();
			ef_g.gradeFun(score);
		
		}else{
			System.out.println("데이터를 확인해주세요"); //0~100사이 수를 입력하지 않은 경우
		}

		System.out.println("\nExFlow_Grade.main()함수 끝>>>>\n");

	}//end of main 함수
}//end of ExFlow_Grade

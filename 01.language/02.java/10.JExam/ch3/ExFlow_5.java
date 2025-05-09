//package
package a.b.c.ch3;

//import

public class ExFlow_5{

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.
	System.out.println("ExFlow_5.main함수 시작>>>>>>");
	
	//기초자료형 지역변수 ranking 선언 후 1로 초기화
	int ranking = 1;
	//기초자료형 지역변후 medalColor 선언 후 디폴트 값으로 초기화
	char medalColor = '\u0000'; //<- 유니코드로 ' '로 초기화

	/*
	switch
		switch : case를 분기하는 분기문 : if 문과 동일한 기능을 수행
		() : 조건식 jdk1.7 이전에는 숫자만 사용 가능했으나, 
		    1.7부터는 숫자 문자열 사용 가능
		case : 조건식의 값과 case 키워드의 값이 같으면 case에 있는 표현식 수행
		break : 그 구문 혹은 절을 나가시오
		default : if문의 else와 같은 역할
		
		switch문은 사용되는 특정한 부분이 있다.
	*/
	switch(ranking){
		
		case 1: medalColor = 'G';
				break;
		case 2: medalColor = 'S';
				break;
		case 3: medalColor = 'B';
				break;
		default: //if문의 else 역할을 한다.
				medalColor = 'A';
	}//end of switch문
	System.out.println(ranking + "등으로 메달 색은 " +medalColor);
	
	//지역변수 ranking을 3으로 초기화
	ranking =3;
	System.out.println("ranking 값>>>>>"+ranking);
	//지역변수 + 참조변수 String 선언 후 디폴트값("")로 초기화
	//지역변수는 항상 초기화 할것
	String mColor="";
	switch (ranking){

		case 1: mColor = "금메달";
				break;
		case 2: mColor = "은메달";
				break;
		case 3: mColor = "동메달";
				break;
		default :
				mColor = "일반메달";
	
	}//end of switch 문
	
	System.out.println(ranking + "등 이므로 "+mColor+"입니다.");

	//조건문으로 문자열 사용 (jdk 1.7부터 사용가능)
	String medal = "GOLD";
	switch (medal){
	
		case "GOLD":
				System.out.println("금메달 입니다.");
				break;
		case "SILVER":
				System.out.println("은메달 입니다.");
				break;
		case "BRONZE":
				System.out.println("동메달 입니다.");
				break;
		default:
				System.out.println("참가상 입니다.");
				break;
		}//end of switch 문

		System.out.println("ExFlow_5.main함수 끝>>>>>>");
	}//end of main 함수
}//end of ExFlow5 클래스

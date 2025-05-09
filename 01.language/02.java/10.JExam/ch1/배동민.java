package a.b.c.ch1;

public class 배동민 {

	//멤버 변수 선언
	// name과 role이라는 문자열 멤버변수 선언
	public String name;
	public String role;

	//생성자
	//배동민(String role) 객체를 만듬
	//.role이란 것에다가 String role을 넣어주세요
	public 배동민 (String role){
		this.role = role;
	}

	//main 함수 시작 (콘솔 어플의 시작점)
	public static void main(String [] args){

	//배동민 가족
	//배동민 클래스 
	//가족이란 변수
	//new 배동민()를 이용해 배동민()라는 객체로 만들고
	//그 안에 "집안일" 이라는 값을 넣을 거임

	//가족.role
	//가족 = 주소값(@15db9742)을 가져옴
	// 이 주소 값은 배동민이란 클래스에 대한 주소임 = 배동민이란 클래스 호출
	//.role = 배동민 (String role)에 들어간 String role을 가져옴
	// String role은 집안일이됨
	// 가족.role = 배동민("집안일") = 집안일
	배동민 가족 = new 배동민("집안일");
	System.out.println("가족>>>>"+가족);
	System.out.println("가족.role >>>"+가족.role);

	배동민 친구 = new 배동민("카페고?");
	System.out.println("친구>>>>"+친구);
	System.out.println("친구.role >>>>"+친구.role);

	배동민 동기 = new 배동민("공부고?");
	System.out.println("동기>>>>"+동기);
	System.out.println("동기.role >>>>"+동기.role);

	}// end of main 함수
} // end of 배동민 클래스 
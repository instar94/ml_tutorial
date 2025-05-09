package a.b.c.ch1;

public class Ex_Const_1{
	
	//멤버변수 선언
	String name;
	int age;

	//생성자 : 매개 변수 없는 생성자

	public Ex_Const_1(){
		System.out.println("Ex_Const_1() 생성자 >>>>>");
	}

	// 생성자 : 매개변수 1개 (Strint name)

	public Ex_Const_1(String name){
		System.out.println("Ex_Const_1(String name 생성자)");
		System.out.println("String name >>>"+name);
	}

	// 생성자 : 매개변수 1개 (int age)
	
	public Ex_Const_1(int age){
		System.out.println("Ex_Const_1(int_age 생성자)");
		System.out.println("int age >>>"+age);

	}

	// 생성자 : 매개변수 2개 (String name, int age)
	// 첫번째 매개변수 : String name
	// 두번째 매개변수 : int age

	public Ex_Const_1(String name, int age){
		System.out.println("Ex_Const_1(String name,int age) 생성자");
		System.out.println("String name >>>"+name);
		System.out.println("int age >>>"+age);
	}

	// 생성자 : 매개변수 2개 (int age. String name)
	// 첫번째 매개변수 : int age
	// 두번째 매개변수 : String name

	public Ex_Const_1(int age, String name){
		System.out.println("Ex_Const_1(int age,String name) 생성자");
		System.out.println("int age >>>" +age);
		System.out.println("String name >>>" +name);
	}

	

	//main 함수 시작

	public static void main (String [] args){

		//매개변수와 아규먼트는 데이터 타입과 순서만 같으면 된다.
		//변수명은 달라도 괜찮음
		// 생성자 오버로딩
		
		// 아규먼트가 없는 생성자 Ex_Const_1 ()호출
		Ex_Const_1 ex_c_1 = new Ex_Const_1();
		System.out.println("ex_c_1 주소값>>>> : "+ex_c_1);

		//아규먼트가 1개있는 생성자 Ex_Const_1("배동민")호출
		// 이때 "배동민"은 문자열 데이터 타입
		Ex_Const_1 ex_c_2 = new Ex_Const_1("배동민");
		System.out.println("ex_c_2 주소값>>>>"+ex_c_2);
		


	
		//아규먼트가 1개있는 생성자 Ex_Const_1(28)호출
		// 이때 28은 int형 데이터
		Ex_Const_1 ex_c_3 = new Ex_Const_1(28);
		System.out.println("ex_c_3 주소값>>>>"+ex_c_3);


		// 아규먼트가 2개 있는 생성자 Ex_Const_1("배동민",28) 호출
		// 이때 첫번째는 String 데이터 , 두번째는 int형 데이터
		Ex_Const_1 ex_c_4 = new Ex_Const_1("배동민",28);
		System.out.println("ex_c_4 주소값 >>>>"+ex_c_4);
	
		//아규먼트가 2개 있는 생성자 Ex_Const_1(28, "배동민) 호출
		// 이때 첫번째는 int형 , 두번째는 String 형 데이터
		Ex_Const_1 ex_c_5 = new Ex_Const_1(28,"배동민");
		System.out.println("ex_c_5 주소값 >>>> : "+ex_c_5);

	}//end of main 함수

}//end of Ex_Const_1

/*
1. 클래스는 변수와 함수로 구성되어 있다.
2. 클래스는 클래스 키워드 식별자 이름 브레이스 블럭으로 구성되어있다.
3. main () 함수는 콘솔 어플리케이션의 시작이다.
4. New 키워드는 생성자를 찾는다.
*/
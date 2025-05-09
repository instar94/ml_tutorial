//package
package a.b.c.ch3;
//import

public class Test_2{

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.
		
		String str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

		//for(어디부터?;true일때까지;얼마나 증가할래?)
		//length() = 길이(글자수)를 구하는 함수
		//=> str의 글자수만큼 (26자)
		//i에 0부터 25까지 집어넣고
		//26이 도달하면 False 가 되기때문에 반복이 멈춤
		for(int i=0;i<str.length() ;i++){

			//기초데이터형 지역변수 c를 선언
			//지역변수 c는 str의 charAt(i)를 호출해서 초기화한다.
			//charAt=인덱스 순서 (0부터 시작함)
			char c=str.charAt(i);

			//c가 Integer.toBinarySting(c)의 아규먼트로 들어감
			//c는 0부터 하나씩 들어감
			//"0x"차트에 그렇게 들어가 있어서
			System.out.print(Integer.toBinaryString(c) + " : ");
			System.out.print(Integer.toOctalString(c) + " : ");
			System.out.print((int)c + " : ");
			System.out.print("0x"+Integer.toHexString(c)+" : ");
			System.out.println(c);
			

		}//end of for 함수	
		
	}
}

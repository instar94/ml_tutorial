package a.b.c.ch3;

/*
ExData_3클래스에서 
public void primeVal()가 실행되면
byte, char, short, int, float, double의 최댓값/최솟값이 나오도록 할것
*/

public class ExData_3{
//상수
//멤버변수
//생성자


	//함수
	//일반함수 + 리턴이 없음
	//일반함수 = 참조변수를 이용해아함 => new  키워드를 사용
	//사용방법 : 참조변수.함수명();
	//ExData_3 ed3 = new ExData_3();
	//ed3.primeVal();

	public void primeVal(){

		//\n 쓰면 한 줄 스페이싱 가능
		System.out.println("primeVal()함수 시작>>>:\n");
	
		//byte	Byte		:최대값/최소값
		System.out.println("Byte.MAX_VALUE>>>:"+Byte.MAX_VALUE);
		System.out.println("Byte.MIN_VALUE>>>:"+Byte.MIN_VALUE);

		//char	Character	:최대값/최소값
		System.out.println("Character.MAX_VALUE>>>:"+Character.MAX_VALUE);
		System.out.println("Character.MAX_VALUE>>>:"+Character.MIN_VALUE);
		
		//short	Short		:최대값/최소값
		System.out.println("Short.MAX_VALUE>>>:"+Short.MAX_VALUE);
		System.out.println("Short.MIN_VALUE>>>:"+Short.MIN_VALUE);
		
		//int	Integer		:최대값/최소값
		System.out.println("Integer.MAX_VALUE>>>>:"+Integer.MAX_VALUE);
		System.out.println("Integer.MIN_VALUE>>>>:"+Integer.MIN_VALUE);
		
		//long	Long		:최대값/최소값
		System.out.println("Long.MAX_VALUE>>>:"+Long.MAX_VALUE);
		System.out.println("Long.MIN_VALUE>>>:"+Long.MIN_VALUE);
		
		//float	Float		:최대값/최소값
		System.out.println("Float.MAX_VALUE>>>:"+Float.MAX_VALUE);
		System.out.println("Float.MIN_VALUE>>>:"+Float.MIN_VALUE);
		
		//double	Double	:최대값/최소값
		System.out.println("Double.MAX_VALUE>>>:"+Double.MAX_VALUE);
		System.out.println("Double.MIN_VALUE>>>:"+Double.MIN_VALUE);

		System.out.println("\nExData_3 primeVal()함수 끝>>>:");
	}//end of primeVal 함수


	public static void main(String[] args){
	
		System.out.println("ExData_3 main()함수 시작>>>:\n");
	
		//참조변수 선언
		ExData_3 ed3 = new ExData_3();
		
		//void 함수여서 System.out.println을 사용 할 수 없음
		//참조변수.함수명();으로 사용
		ed3.primeVal();
		System.out.println("\nExData_3 main()함수 끝>>>:");

	}//end of main 함수
}//end of ExData_3 클래스
package a.b.c.ch3;

/*
	ExData_2클래스 main 함수에서
	기초자료형 byte, char,short,int,long,float, double의
	제일 큰 값 및 작은 값을 콘솔에 출력하시오

	기초자료형은 객체가 아닌 키워드
	기초자료형에 대응하는 Wrapper Class를 사용해야함
	Wrapper class의 최대값 최소값이 상수로

*/

public class ExData_2{

	public static void main(String[] args){
	
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

	}//end of main 함수

}//end of ExData_2 클래스

/*
Byte.MAX_VALUE>>>:127
Byte.MIN_VALUE>>>:-128

char.MAX_VALUE>>>:? (\uFFFF)
char.MAX_VALUE>>>:

Short.MAX_VALUE>>>:32767
Short.MIN_VALUE>>>:-32768

int.MAX_VALUE>>>>:2147483647
int.MIN_VALUE>>>>:-2147483648

long.MAX_VALUE>>>:9223372036854775807
long.MIN_VALUE>>>:-9223372036854775808

float.MAX_VALUE>>>:3.4028235E38
float.MIN_VALUE>>>:1.4E-45

double.MAX_VALUE>>>:1.7976931348623157E308
double.MIN_VALUE>>>:4.9E-324
*/
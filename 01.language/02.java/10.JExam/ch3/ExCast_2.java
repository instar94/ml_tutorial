//package
package a.b.c.ch3;
//import

public class ExCast_2 {

	//상수
	//멤버변수
	//생성자

	//함수
	
	//함수 : int형 사용자정의 함수 aM()
	//매개변수 : byte형 x1과 y2
	//x1과 y2를 더한 값 = byte형임
	//함수는 int 형이지만 매개변수는 byte형임
	public int aM(byte x1, byte y2){

		System.out.print("\nExCast_2.aM 함수 시작 >>>>>:\n");
		//sum도 byte형임
		byte sum = (byte)(x1 + y2);

		//byte형 sum이 return으로 들어감
		//return과 함수형은 동일해야함
		//return(byte)를 int aM에 넣는 것이기 때문에 묵시적 형변환 발생

		System.out.print("\nExCast_2.aM 함수 끝 >>>>>:\n");
		return sum;

	}//end of aM()함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args) 
	{//TODO Auto-generated method stub.
		
		System.out.print("\nExCast_2.main 함수 시작 >>>>>:\n");
		//기초자료형 변수 x와 y를 선언하고
		//각각 1과 2 값으로 초기화
		byte x = 1;
		byte y = 2;

		//일반함수 aM을 이용하기위해 참조변수 선언
		ExCast_2 ec2 = new ExCast_2();

		//int형 sum에 ec2.aM 함수 값을 대입
		int sum = ec2.aM(x,y);

		//sum 값을 콘솔에 출력함
		System.out.println("sum >>>>>>>:"+sum);

		System.out.print("\nExCast_2.main 함수 끝 >>>>>:\n");
	}//end of main 함수
}//end of ExCast_2 클래스

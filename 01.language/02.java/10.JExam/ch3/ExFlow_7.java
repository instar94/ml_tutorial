//package
package a.b.c.ch3;
//import

public class ExFlow_7 {

	//상수
	//멤버변수
	//생성자

	//함수

	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
	//TODO Auto-generated method stub.
	
		/*for 반복문
		형식 : for (초기화식 ; 조건식; 증감식){
			문장, 수행문
		}
		- 초기화식 : 1번째 루프에 사용하는 변수를 초기화 하는 값
		- 조건식 : 루프의 반복을 결정함 / true 인지 false 인지만 가지고옴
		- 증감식 : 변수를 얼만큼 증감시킬건가
		- 수행문 : 무엇을 수행 시킬 것인가

		for 반복문의 작동 과정
		1. 초기화식 수행ㅇ
		2. 조건식 : 연산 결과의 논리값을 가져옴 (true or false)
		3. 수행문 : 조건문이 true이면 수행
		4. 증감식 수행
		<반복>2~4 :
		2. 조건식을 다시 거쳐 논리값을 가져옴 (true or false)
		3. 수행문 : 조건문이 true이면 수행
		4. 증감식 반복
		<중단>
		2. 조건문의 논리값을 가져옴 => false
		3. 중단

		*/

		//기초자료형 지역변수 i와 sum을 선언
		//값을 초기화 하지 않음 <= 실무에선 잘 안 이럼
		int i;
		int sum;
		//for문
		//초기화식 : i는 1, sum은 0으로 값을 초기화
		//조건식 : i가 10 이하
		//증감식 : i를 1씩 더함
		//수행식 : sum에 i를 더함 (추가로 매 loop별 i값과 sum값을 출력)
		for (i=1, sum=0 ; i<=10 ; i++){
			System.out.println(i + "번째 루프의 i 값>>>>> : " + i);
			sum += i; //sum = sum + i
			System.out.println(i +"번째 루프의 sum 값>>>>>:" + sum);
		}
		System.out.println("최종 i값 >>>>>: " + i);
		System.out.println("1부터 10까지의 합은? :" + sum);
	}//end of main 함수
}//end of ExFlow_7 클래스
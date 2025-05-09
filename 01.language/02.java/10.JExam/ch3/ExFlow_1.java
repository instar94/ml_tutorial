//package
package a.b.c.ch3;
//import

public class ExFlow_1{
	//상수
	//멤버변수
	//생성자
	
	//함수
	
	//main() 함수 : 프로그램 시작점
	public static void main(String[] args){ 
		//TODO Auto-generated method stub.
		
		//if문의 형식 : if (){}
		//() : 조건식을 쓰는 곳
		//if 문은 조건이 true일때만 가능함
		//조건문 혹은 논리식은 모두 true여야함
		//논리식은 단축평가가 발생 할 수 있다. -> 프로그램이 아작 날 수 있다.

		//if의 조건은 true 여야만 돌아간다.
		if (true){
			System.out.println("if문이 조건식의 결과가 true일 경우에만 수행된다.");	
		}

		//if는 조건이 false면 돌아가지 않는다.
		//else를 설정하면 if의 조건이 false일때 돌아간다.
		if (false){
			
		}else{
			System.out.println("else절은 if문이 조건식의 결과가 false일때만 수행된다.");
		}

		//기초자료형 (boolean) 지역변수 bool를 선언하고
		//그 값을 false로 초기화
		boolean bool = false;

		if (!bool){ //!bool=true / 하지만 이 함수에서만 한시적으로 true인 지역변수
			System.out.println("if문이 조건식의 결과가 true일 경우에만 수행된다.");
		}

		if (bool){ //<=bool은 false 이기 때문에 else절이 수행됨
				  //위의 if절에서 !bool을 했다고 bool에 true가 대입된 것은 아니다.
		}else{
			System.out.println("else 절은 if문이 조건식이 결과가 false 일때 수행된다.");
		}
		

		//if는 값이 true일때만
		//else는 값이 false 일때만
		//=> true도 false도 아닌 값이 들어가면 오류가 나옴
		int x = 1;
		int y = 0;
		int sum = x / y; //1 나누기 0은 성립되지 않음

		if(sum>0){
			
		}
	}//end of main 함수
}//end of ExFlow_1

package com.a.b.c; 
// 패키지를 만들면서 디렉토리를 만듬 com 안에 a 안에 b 안에 c
//콘솔에서는 -d로 디렉토리를 생성 할 수 있음
public class HelloWorld {
//HelloWorld라는 클래스를 만들 것임
	public static void main (String[] args){
		System.out.println("Java HelloWord!!");
		System.out.println("자바 패키지 컴파일");
		System.out.println("javac -d . HelloWorld.java");
		System.out.println("-d : 디렉토리를 만드세요 옵션");
		System.out.println(".: 현재디렉토리 옵션");
		System.out.println("java com.a.b.c.HelloWorld");
	}
}
// 패키지 컴파일 
/*
1. javac 컴파일러 선언하기
2. -d : 디렉토리만들기 옵션 d 선언하기 (-:구별자임)
3. . : 현재디렉토리부터 폴더(패키지)를 만드세요 
       현재디렉토리는 컴파일 하려는 자바파일이 있는 위치 
4. HelloWorld.java : 컴파일할 자바파일명을 *확장자*까지 다 쓰기 
javac -d . HelloWorld.java
*/

// 패키지 클래스 실행하기
/*
1. java 실행엔진 선언하기
2. 컴파일한 자바화일 위치에서 패키지명+클래스명 쓰기 (확장자명 XX)
3. 패키지명+클래스명
   패키지명 : com.a.b.c
   클래스명 : HelloWorld
java com.a.b.c.HelloWorld

Type을 원한다면 해당 위치까지 cd 해서 가야함

*/
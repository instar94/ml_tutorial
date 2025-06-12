-- 테이블 생성 : 컬럼명 + 데이터 타입

-- 테이블 조회
SHOW TABLES;

-- 테이블 정보 조회
DESC mytable;

-- 테이블 이름 변경
alter table mytable rename person;
show tables;

-- 컬럼 추가
alter table person add column agee double;
DESC person;

-- 컬럼 데이터 타입 변경
alter table person modify column agee int;
DESC person;

-- 컬럼 이름 변경
alter table person change column agee age int;
DESC person;

-- 컬럼 삭제
alter table person drop column age;
DESC person;

-- 테이블 삭제
drop table person;
show tables;
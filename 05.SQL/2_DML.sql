use zerobase;

-- 1. Insert : 데이터 추가

-- 모든 데이터 추가
insert into person
values (2, "이상순",48,"M");

-- 특정 컬럼만 추가
insert into person (id,name,age,sex)
values (1,"이효리",43,"F");

-- 여러 데이터 추가
insert into person values(3,"이지우",37, "F");
insert into person values(4,"김채연",33, "M");

-- 2. Select : 데이터 조회

-- 모든 데이터 조회
select * from person;

-- 특정 컬럼 조회
select name, age, sex from person;

-- 3. WHERE : 조건 조회
select * from person where sex="F";


-- 4. UPDATE : 데이터 수정
update person set name="윤서연" where id=1;
update person set name="정혜린" where id=2;
select * from person where id<3;

-- 5. DELETE : 데이터 삭제

-- 삭제 데이터 생성
insert into person values(5,"삭제필요",33, "M");
-- 삭제
delete from person where id=5;
-- 삭제 확인
select * from person;


-- Order By : 정렬
-- 테이블 생성
-- order by 용 테이블 생성
create table celeb (
                       ID int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
                       NAME varchar(32) NOT NULL DEFAULT "" ,
                       birthday date,
                       AGE int,
                       SEX char(1),
                       JOB_TITLE varchar(32),
                       AGENCY varchar(32)
);

-- 테이블 생성 확인
desc celeb;

-- 데이터 추가
INSERT INTO celeb (ID, NAME, BIRTHDAY, AGE, SEX, JOB_TITLE, AGENCY) VALUES
    (1, '윤서연', '2003-08-06', 21, 'F', '리더, 댄스', 'AAA'),
    (2, '정혜린', '2007-04-12', 18, 'M', '보컬, 댄스', 'AAA'),
    (3, '이지우', '2005-10-24', 19, 'F', '보컬', 'AAA'),
    (4, '김채연', '2004-12-04', 20, 'M', '보컬', 'AAA'),
    (5, '김유연', '2001-02-09', 24, 'F', '리더, 센터', 'KRE'),
    (6, '김수민', '2007-10-03', 17, 'M', '보컬', 'KRE'),
    (7, '김나경', '2002-10-13', 22, 'F', '보컬, 래퍼', 'KRE'),
    (8, '공유빈', '2005-02-03', 20, 'M', '보컬, 댄스', 'KRE'),
    (9, '카에데', '2005-12-20', 19, 'F', '보컬, 댄스', 'LOVE'),
    (10, '서다현', '2003-01-08', 22, 'M', '리더, 보컬', 'EVOL'),
    (11, '코토네', '2004-03-10', 21, 'F', '래퍼', 'EVOL'),
    (12, '곽연지', '2008-01-08', 17, 'M', '보컬', 'EVOL'),
    (13, '니엔', '2003-06-02', 22, 'F', '보컬', 'LOVE'),
    (14, '박소현', '2002-10-13', 22, 'M', '래퍼, 댄스', 'LOVE'),
    (15, '신위', '2004-05-25', 21, 'F', '래퍼, 댄스', 'EVOL'),
    (16, '마유', '2002-05-12', 23, 'M', '보컬, 댄스', 'EVOL'),
    (17, '린', '2006-04-12', 19, 'F', '보컬', 'NEXT'),
    (18, '주빈', '2009-01-16', 16, 'M', '댄스', 'NEXT'),
    (19, '하연', '2007-08-01', 17, 'F', '래퍼', 'NEXT'),
    (20, '박시온', '2006-04-03', 19, 'M', '보컬', 'NEXT'),
    (21, '김채원', '2007-05-02', 18, 'F', '보컬', 'GLOW'),
    (22, '설린', '2007-12-13', 17, 'M', '보컬', 'GLOW'),
    (23, '서아', '2010-06-11', 15, 'F', '보컬', 'GLOW'),
    (24, '지연', '2008-02-13', 17, 'M', '보컬, 댄스', 'GLOW');

-- 데이터 추가 확인
select * from celeb;

--- 오름차순 조회
select name,age from celeb order by age asc;

--- 내림차순 조회
select name,age from celeb order by age desc;

-- 여러 컬럼 조건 조회
select age,id,name from celeb order by age,id;

-- 컬럼별 조건 조회
select age,id,name from celeb order by age ASC, id DESC ;
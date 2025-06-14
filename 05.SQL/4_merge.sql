-- 실습 환경 세팅
use zerobase;
select *
from celeb;

-- 테스트 테이블 생성
create table test1
(
    no int
);
create table test2
(
    no int
);
show tables;

-- 테스트 데이터 추가
insert into test1
values (1),
       (2),
       (3);
insert into test2
values (4),
       (5),
       (6);
insert into test2
values (3);
-- 데이터 확인
select *
from test1;
select *
from test2;

-- UNION
-- Uunion all
select *
from test1
UNION ALL
(select *
 from test2);

-- UNION
select *
from test1
UNION
(select *
 from test2);

-- 성별 여자  + 소속사가  GLOW인 데이터 검색
-- union all
select name, sex, agency
from celeb
where sex = "F"
UNION ALL
(select name, sex, agency
 from celeb
 where agency = "GLOW");

-- union all
select name, sex, agency
from celeb
where sex = "F"
UNION
(select name, sex, agency
 from celeb
 where agency = "GLOW");


-- join 실습 환경 만들기
create table snl_show
(
    id             int         not null auto_increment primary key,
    season         int         not null,
    episode        int         not null,
    broadcast_date date,
    host           varchar(32) not null
);

-- 데이터 추가
INSERT INTO snl_show
VALUES (1, 8, 7, '2020-09-05', '윤서연');
INSERT INTO snl_show
VALUES (2, 8, 8, '2020-09-12', '정혜린');
INSERT INTO snl_show
VALUES (3, 8, 9, '2020-09-19', '이지우');
INSERT INTO snl_show
VALUES (4, 8, 10, '2020-09-26', '김채연');
INSERT INTO snl_show
VALUES (5, 9, 1, '2021-09-04', '김유연');
INSERT INTO snl_show
VALUES (6, 9, 2, '2021-09-11', '윤아');
INSERT INTO snl_show
VALUES (7, 9, 3, '2021-09-18', '민주');
INSERT INTO snl_show
VALUES (8, 9, 4, '2021-09-25', '모카');
INSERT INTO snl_show
VALUES (9, 9, 5, '2021-10-02', '원희');
INSERT INTO snl_show
VALUES (10, 9, 6, '2021-10-09', '이로하');

-- 데이터 확인
select *
from snl_show;


-- INNER JOIN : 두 테이블의 교집합
-- snl_host로 출연한 celeb 출력
select celeb.id, celeb.name, snl_show.id, snl_show.host
from celeb
         inner join snl_show
                    on celeb.name = snl_show.host;

-- left join : 왼쪽 테이블의 모든 행과 오른쪽 테이블의 일치하는 행을 반환
-- 값이 없는 경우 NULL 출력
select celeb.id, celeb.name, snl_show.id, snl_show.host
from celeb
         left join snl_show
                   on celeb.name = snl_show.host;

-- right join : 오른쪽 테이블의 모든 행과 오른쪽 테이블의 일치하는 행을 반환
-- 값이 없는 경우 NULL 출력
select celeb.id, celeb.name, snl_show.id, snl_show.host
from celeb
         right join snl_show
                    on celeb.name = snl_show.host;

-- full outer join : 두 테이블의 모든 행을 반환 - 합집합
-- left join과 right join을 합친 결과
-- MySQL에서는 지원하지 않으므로 UNION으로 구현
select celeb.id, celeb.name, snl_show.id, snl_show.host
from celeb
         left join snl_show
                   on celeb.name = snl_show.host
union
select celeb.id, celeb.name, snl_show.id, snl_show.host
from celeb
         right join snl_show
                    on celeb.name = snl_show.host
;

-- self join : 테이블을 자기 자신과 조인
-- where 조건을 사용하여 특정 행을 필터링
select celeb.id, celeb.name, snl_show.id, snl_show.host
from celeb,
     snl_show
where celeb.name = snl_show.host;

-- celeb 테이블 연예인 중
-- snl_show 테이블에 출연 + KRE 소속
-- 이름과 직업

select celeb.name, celeb.job_title
from celeb,
     snl_show
where celeb.name = snl_show.host
  and celeb.agency = "KRE";


-- CONCAT : 문자열 결합
select concat("concat", " ", "test");
-- 컬럼데이터를 이용
select concat ("이름 : ", name) from celeb where id < 8 and sex="F";

-- ALIAS : 컬럼에 별칭을 붙여서 사용
-- 컬럼 별칭
select BIRTHDAY as bday from celeb;
-- 테이블 별칭
select c.name, c.job_title from celeb as c;
select concat(name, ":", job_title) as profile from celeb;

-- 여러 테이블 별칭
select s.episode,s.season,s.host, c.name , c.job_title
from celeb as c, snl_show as s
where s.host = c.name;

-- DISTINCT : 중복된 값을 제거
select distinct agency
from celeb;

-- LINIT :
select * from celeb linit 3;
show databases;
use zerobase;

-- 비교 연산자
-- A=B : 같음
select name, id, age
from celeb
where age = 21;

-- A!=B : 다름
select name, id, age
from celeb
where age != 21
order by age;

-- A>B : A가 B보다 큼
select name, id, age
from celeb
where age > 21
order by age;

-- A<B : A가 B보다 작음
select name, id, age
from celeb
where age < 21
order by age;

-- A>=B : A가 B보다 크거나 같음
select name, id, age
from celeb
where age >= 21
order by age;

-- A<=B : A가 B보다 작거나 같음
select name, id, age
from celeb
where age <= 21
order by age;


-- 논리 연산자
-- A AND B : A와 B가 모두 참
select *
from celeb
where age = 21
  and AGENCY != "AAA";

select *
from celeb
where sex = "M"
  and age > 21
order by name;

select *
from celeb
where job_title != "보컬"
  and agency = "LOVE"
order by id desc;


-- A OR B : A 또는 B가 참
select *
from celeb
where age > 21
   or age < 17
order by age;

-- 나이 21세 이하 + 여자
-- 나이 22세 이상 + 남자
-- 나이 성별 순
select *
from celeb
where (age < 21 and sex = "F")
   OR (age > 22 and sex = "M")
order by age, sex;

-- AAA 소속이거나 KRE 소속인데 나이가 21세 이상
select *
from celeb
where (agency = "AAA" OR agency = "KRE")
  and age >= 21
order by age;

-- NOT A : A가 아니면 TRUE
select *
from celeb
where not sex = "F";

--  AAA 이면서 남자가 아님
-- AAA 소속 아니면서 래퍼
select *
from celeb
where not sex = "M"
  and agency = "AAA";
select *
from celeb
where not agency = "AAA"
  and job_title = "래퍼";

select *
from celeb
where (not sex = "M" and agency = "AAA")
   OR (not agency = "AAA" and job_title = "래퍼");

-- 생년이 2005년 이후 + 여자
-- 생년이 2003년 이전 이면서 소속사가 Glow가 아님
select *
from celeb
where (birthday > 20041231 and sex = "F")
   OR (not agency = "AAA" and birthday < 20021231)
order by age;

-- between : 범위 안에 있으면 TRUE
select *
from celeb
where age between 15 and 20
order by age desc;

-- 생년월일이 2004년에서 2010년 사이가 아님 + 여자
-- 혹은 AAA 소속이면서 17세 20세 사이
select *
from celeb
where not birthday between 20040101 and 20101231
  and sex = "F";
select *
from celeb
where agency = "AAA"
  and age between 17 and 20;

select *
from celeb
where (not birthday between 20040101 and 20101231 and sex = "F")
   OR (agency = "AAA" and age between 17 and 20)
order by age, id;

-- in : A가 리스트에 포함되어 있으면 TRUE
-- 나이가 20 혹은 17인 데이터
select *
from celeb
where age in (20, 17);

-- agency가 LOVE 혹은 EVOL, NEXT가 아니면서
-- 성별이 여자 OR 나이가 22세 이상
select *
from celeb
where not agency in ("LOVE", "EVOL", "NEXT")
    AND ( sex= "F" OR age >= 22);

-- like : A 패턴이 있다면 TRUE
select * from celeb where agency like "KRE"

-- 리더로 시작하는 단어
select * from celeb where job_title like "리더%"

-- 댄스있는 데이터
select * from celeb where job_title like "%댄스%"
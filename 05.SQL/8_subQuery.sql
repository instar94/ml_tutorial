use zerobase;

/**은평 경찰서의 강도 검거 건수 + 서울시 경찰서 전체 평균 강도 검거 건수**/
select case_number
from crime
where police_station like "은평"
  and crime_type like "강도", status_type like "검거";

select avg(case_number)
from crime
where crime_type like "강도"
  and status_type like "검거";

select case_number,
       (select avg(case_number)
        from crime
        where crime_type like "강도"
          and status_type like "검거") avg
from crime
where police_station like "은평"
  and crime_type like "강도"
  and status_type like "검거";


-- 인라인 뷰 : from 절의 서브쿼리
/**경찰서 별로 가장 많이 발생한 범죄 건수와 범죄 유형**/
/**경찰서 - 범죄유형 - 케이스건 출력
  Group by 로 인해 crime_type으로 묶임**/
select c.police_station, c.crime_type, c.case_number
from crime c,
    /**가장 많이 발생한 범죄 건수를 조회**/
     (select police_station, max(case_number) count
      from crime
      where status_type like "발생"
      group by police_station) m
/**가장 많이 발생한 건수와 동일하면 출력**/
where c.police_station = m.police_station
  and c.case_number = m.count;


-- nested subquery : where 절의 서브쿼리
-- single row subquery
-- 비교연산자와 사용 -> 컬럼이 무조건 하나여야함
-- where 조건으로 하나만
select name
from celeb
where name = (select host from snl_show where id = 1);

-- multi row subquery
-- snl에 출연한 AAA 소속 조회
select host
from snl_show
where host in (select name from celeb where job_title like "%댄스%");

-- exists 와 같이 사용
-- 범죄 검거 혹은 발생건수가 2천건 보다 큰 경찰서 조회
select name
from police_station p
where exists (select police_station
              from crime c
              where c.case_number > 2000
              and p.name=c.reference);

-- any 와 같이 사용
-- snl 출연했던 연예인 출력
select name
from celeb
where name = any (select host from snl_show);

-- all 과 같이 사용
select name
from celeb
where name = all (select host from snl_show where id = 1);

-- multi column subquery
-- 김유연과 성별 소속사가 같은 연예읜ㅇ의 이름 성별 소속사 조회
select a.name, a.sex, a.agency
from celeb a
where (a.sex, a.agency) in (
    select b.sex, b.agency
    from celeb b
    where b.name = "김유연"
    );
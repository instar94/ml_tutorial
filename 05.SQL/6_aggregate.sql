use zerobase;
select *
from crime;
select *
from police_station;

-- count
-- count(*) : 전체 행의 수
select count(*)
from police_station;

-- count(distinct 컬럼명) : 몇 가지 종류의 값이 있는지
select count(distinct crime.police_station)
from crime;

select count(distinct crime_type)
from crime;

-- sum
select *
from crime
limit 2;
select sum(case_number)
from crime
where status_type = "발생";

select sum(case_number)
from crime
where status_type = "발생"
  and crime_type like "살인";

-- avg : 평균
select avg(crime.case_number)
from crime
where crime_type like "폭력" and status_type = "발생";

-- 중부 경찰서 범죄 평균 발생 건수
select avg(case_number)
from crime
where police_station like "중부" and status_type like "발생";




-- min / max
-- min : 최소값
-- max : 최대값

/** 강도 발생 건수 가장 적은**/
select min(case_number)
from crime
where status_type="발생" and crime_type like "강도";

-- 중부 경찰서에서 가장 낮은 검거 건수
select min(crime.case_number)
from crime
where police_station like "중부" and status_type like "검거";

-- max : 최대값

-- 살인이 가장 많이 검거된 건
select max(case_number)
from crime
where crime_type="살인" and status_type="검거";

-- 강남에서 가장 많이 발생
select max(case_number)
from crime
where police_station like "강남" and status_type="발생";

-- group by : 그룹화 하여 검색

-- 경찰서 별고 그룹화 하여 경찰서 이름 조회
select police_station
from crime
group by police_station
order by police_station
limit 5;


-- 경찰서 별 총 발생 범죄 건수
select police_station, sum(case_number) as "발생건수"
from crime
where status_type like "발생"
group by police_station
order by "발생건수" desc
limit 5;

-- having : 집계 함수에 조건이 있는 경우
-- 경찰서 별로 발생 건수의 합이 4천건 보다 큰 경우
select police_station, sum(case_number) count
from crime
where status_type like "발생"
group by police_station
having count > 4000;
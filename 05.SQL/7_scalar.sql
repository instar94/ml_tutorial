use zerobase;
desc sandwich;

-- ucase : 대문자
select ucase(cafe)
from sandwich
limit 3;

-- 15달러 이상 메뉴 대문자 조회
select ucase(menu), price
from sandwich
where price >= 15;

-- lcase : 소문자
-- 5달러가 안되는 경우
select lcase(menu), price
from sandwich
where price < 5;

-- mid : 문자열 부분
select mid("This is mid test", -3, 3);

-- 11위 카페의 두번째 단어만 조회
select mid(cafe, -4.5)
from sandwich
where ranking = 11;

-- length : 문자열 길이
select length(cafe)
from sandwich
where ranking = 11;
select length(NULL);

--- 탑3 의 주소 길이
select length(address), address
from sandwich
where ranking <= 3;

-- round : 반올림
select round(315.625);
select round(315.625, 0);
select round(315.625, 3);
select round(315.625, -1);

-- 소숫점 자리에서 1달러만 표시
select ranking, price, round(price) as new_price
from sandwich
where round(price) != price
order by ranking desc
limit 5;

-- now() : 현재 시간
select now();

-- format() : 숫자를 천단위 콤마가 있는 형식으로 반환
-- 소수점 표시하지않음
select format(12345315.625, 0);
-- 소수점 표시함 2자리
select format(12345315.625, 2);

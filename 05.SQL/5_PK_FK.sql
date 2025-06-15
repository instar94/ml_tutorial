use zerobase;

-- PK : Primary Key
-- 레코드를 구분하는 기본적인 키
-- PK는 중복된 값을 허용하지 않음
-- PK는 NULL 값을 허용하지 않음
-- PK는 테이블당 하나만 존재할 수 있음

/**하나의 컬럼을 기본키로 설정**/
create table person (
    pid int not null,
    name varchar(16),
    age int,
    sex char,
    primary key (pid)
);

desc person;

/**여러 컬럼을 기본키로 설정**/
/**PK가 2개인 것이 아닌 두 개의 키 조합이 하나의 PK**/
create table animal (
    name varchar(16) not null ,
    type varchar(16) not null,
    age int,
    primary key (name, type)
);

desc animal;


/**PK 삭제**/
alter table person
drop primary key;

desc person;

alter table animal
drop primary key;

desc animal;

/**기존에 있던 테이블에 PK 추가하기**/
alter table person
add primary key (pid);

desc person;

alter table animal
add constraint  PK_animal primary key (name, type);

desc animal;


-- FK : Foreign Key
-- 다른 테이블의 PK를 참조하는 키

create table orders (
    oid int not null,
    order_no varchar(16),
    pid int,
    PRIMARY KEY (oid),
    constraint FK_person FOREIGN KEY (pid) REFERENCES person(pid)
);

desc orders;

/**Create table에서 지정하는 경우 생략 가능**/
create table job(
    jid int not null,
    name varchar(16),
    pid int,
    primary key (jid),
    foreign key (pid) references person(pid)
);

/**자동 생성된 constraint 확인 방법**/
show create table job;

/**FK 삭제**/
alter table orders
drop foreign key  FK_person;

desc orders;

/**이미 생성된 테이블에 왜래키 추가 **/
alter table orders
add foreign key (pid) references person(pid);

desc orders;


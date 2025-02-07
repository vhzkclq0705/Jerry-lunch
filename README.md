# Jerry-lunch

- [ ] 팀원들의 점심 메뉴 수집
- [ ] 점심 데이터 조회
- [ ] 점심 데이터 수 통계
- [ ] 점심 메뉴별 인기 순위 통계
- [ ] 요일별 선호 음식 통계
- [ ] 점심 비용 분포 통계
- [ ] 특정 메뉴에 대한 트렌드 분석
- [ ] 기록하지 않은 사람 조회
- [ ] 기록하지 않은 사람에게 알림 발송 

## READY

### Install DB with Docker
```bash
$ sudo docker run --name local-postgres \
> -e POSTGRES_USER=<USER_NAME> \
> -e POSTGRES_PASSWORD=<PASSWORD> \
> -e POSTGRES_DB=<DB-NAME> \
> -p 5432:5432 \
> -d postgres:15.10
```

### CREATE Table
- postgres

```sql
CREATE TABLE public.lunch_menu (
	id SERIAL NOT NULL,
	menu_name TEXT NOT NULL,
	dt date NOT NULL,
	member_id int NOT NULL,
	CONSTRAINT lunch_menu_pk PRIMARY KEY (id),
	CONSTRAINT unique_member_dt UNIQUE (member_id, dt)
);

CREATE TABLE member(
    id SERIAL NOT NULL,
    name TEXT UNIQUE NOT NULL,
    CONSTRAINT member_pk PRIMARY KEY (id)
);

ALTER TABLE lunch_menu
    ADD CONSTRAINT menu_member_fk
	FOREIGN KEY (member_id)
	REFERENCES member(id)
;
```

## DEV
- DB
```bash
$ sudo docker ps -a
$ sudo docker start local-postgres
$ sudo docker stop local-postgres

# Into Container
$ sudo docker exec -it local-postgres bash
```

- RUN
```bash
# 서버 시작
$ streamlit run App.py
```

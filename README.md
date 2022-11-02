# Get Project With Me

http://gpwm.pythonanywhere.com/



## 1. 아이템 선정 

프로젝트 인원 모집 플랫폼

----------------------- 

## 2. 개요 

+ 프로젝트 명칭 : GetProjectWithMe

+ 개발 인원 : 3명 

+ 개발 기간 : 2022.9.19 ~ 2022.11.02 

+ 주요 기능 : 

  + 게시판 – 사진 첨부, 참여 인원수 체크, 카테고리 필터, 글씨 크기 조절

  + 사용자 – 회원가입, 로그인, 유효성 검사 및 중복 검사, 비밀번호 확인, 마이페이지 내 정보 확인

  + 프로젝트 참여 신청 – 게시판 내 본인 정보입력 

+ 개발 언어 : python 3.7.3 

+ 개발 환경 : Django 3.2.13

+ 데이터베이스 : SQLite3 

+ 형상관리 툴 : GitHub 

+ 간단 소개 : 전반적인 웹의 기본 소양이 되는 게시판을 이용한 프로젝트 인원 모집 플랫폼

-----------------------

## 3. 요구사항 분석 

### 1. 회원 가입 페이지 

+ 유효성 검사 

  + 이메일 형식 패턴 적용해 확인. “@를 포함하세요“ 메시지 보여주기

  + 한 개의 칸이라도 공백 혹은 빈칸이 있는지 확인하고 있다면, "이 입력란을 작성해주세요." 의 메시지 보여주기 

  + 비밀번호 일치하는지 확인. 일치하지 않을시 ”비밀번호를 확인해주세요.“ 메시지 보여주기
 
#### + 중복확인 

  + 데이터베이스에 존재하는 아이디를 입력한 채 가입하기 버튼을 누른 경우 회원가입 페이지를 다시 보여주기

  + 모든 검사가 통과되었다면 로그인 페이지로 이동시키기 

### 2. 로그인 페이지 

#### + 로그인을 하지 않은 경우 아래 페이지만 이용가능 

  + 회원가입 페이지 

  + 로그인 페이지 

  + 소개 페이지 

  + 메인 페이지 

#### + 그 외 로그인을 하지 않거나 올바르지 않은 경로로 접속한 사용자가 로그인이 필요한 경로에 접속한 경우 로그인 페이지로 이동 

  + 로그인 검사 

  + 아이디와 비밀번호가 일치하지 않을 시 로그인 페이지로 다시 이동

  + 모든 검사가 통과되었다면 로그인 후 main 페이지로 이동시키기 


### 3. 게시글 검사 

+ 게시글 작성시 제목과 내용은 공백 혹은 빈칸으로 작성하지 않도록 하기 

+ 로그인을 하지 않고 글 작성 버튼을 누른 경우 로그인 페이지로 이동 

### 4. 참여하기 검사 

+ 참여하기는 로그인한 사용자만 가능하게 하기 

+ 참여하기 버튼을 누를시 사용자의 정보가 나타나게 하기

### 5. 마이페이지 검사

+ 나의 이력 나타내기
+ 작성한 프로젝트 게시 내역 나타내기

----------------------




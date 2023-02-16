# PROJECT : Cocktail How did i make this ?

## Django 를 이용한 웹 개발 프로젝트


<br><br>


### 1. 프로젝트 결과물
> [http://www.howdimt.xyz/](http://www.howdimt.xyz/)
>
> 주류 가격과 칵테일 레시피 정보 공유를 주요 기능으로 내세운 술 커뮤니티 웹 애플리케이션

>[3주차 ORM 발표 ppt](https://drive.google.com/file/d/1SR0sL2E_e0eVl3LOhmga6DvBPivja6zB/view?usp=share_link)
>
> java 와 mybatis 를 사용하는 국비 교육 동료 수강생을 대상으로 ORM 의 개념을 설명하는 발표

<br>

### 2. 기술 스택
>
> * python 3.8
> * Django 4 // web framework
> * PostgreSQL 14 // database
> * gunicorn 20.1 // WSGI server
> * nginx 1.21 // web server
> * Bootstrap // front-end framework
> * docker (for deploying server on NAS)

<br>

### 3. 프로젝트에 대하여
> * 국비교육과정 최종 프로젝트 (개인 프로젝트)
>   * 커리큘럼에서 제시한 목표
>     * CRUD 기능을 포함한 웹 게시판 만들기
>     * 팀 프로젝트
>   * 팀이 아닌 개인으로 프로젝트를 진행한 이유
>     * 1차 프로젝트 이후 취업 목표를 java 개발자가 아닌 python Django 개발자로 전향
>     * java 가 아닌 python 을 다루는 수강생이 본인 이외에 없었음
>     * python 은 기존에 사용해보았던 언어가 아니며 프로젝트를 진행하며 새로 공부함
> * 잠정적 프로젝트 중단
>   * 국비교육 커리큘럼에서 제시한 목표 달성
>   * back-end 개발자를 지망하고 있으나 front-end 개발에 너무 많은 시간이 소요되는 문제 발생
>   * 사용한 기술 거의 대다수를 처음 접했고 목표 달성 시간에 쫓긴 탓에 되돌리기 힘든 구조적 난개발 문제 
>   * 수료 이후 back-end 서버 개발 공부에 집중하기 위하여 개발 중단 결정  

<br>

### 4. 추구한 기술적 목표
>   * python, Django 습득
>   * 웹 개발의 이해
>   * 과정 기록형 프로젝트
>     * 개발 과정을 시간순/주제별로 분류하여 블로그에 기록
>       * [개발 과정 기록 블로그 링크](https://dpcalfola.tistory.com/entry/20220921-Django-pojc-A4)
>     * JavaFX를 사용한 첫 프로젝트가 과정 기록 미흡으로 개발 경험의 지속적 유지 측면에서의 비효율성 인식 
>     * 프로젝트 이후 유사한 개발 환경에서 개발 시 과거 경험을 빠르게 상기시켜 이용할 수 있도록 문서 작성  

<br>

### 5. 배우고 느낀 점
> * Docker-compose의 필요성
>   * 서버를 재시작 할 떄마다 연결돤 도커 컨테이너들을 각각 순서대로 명령어를 통해 실행 시켜야 하는 번거로움 발생   
> * Document convention 의 필요성
>   * 문서 작성 과정에 투입되는 시간과 에너지를 최소화
>   * 제 3자도 문서 이용이 가능하도록 가독성과 접근성 제고

[//]: # (> * 체계적인 구조 설계의 필요성)

[//]: # (>   * )

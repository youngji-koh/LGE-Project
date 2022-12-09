# LGE-Project

## 필드 테스트 및 데이터 수집

* 목적: 스마트 스피커를 활용한 정신 건강 상태 데이터를 수집하는 SW/HW 플랫폼에 대한 필드 테스트를 수행함.  
* 실험 대상 및 기간: KAIST 재학생 10명(여성:4, 남성: 6)을 대상으로 2022년 8월 31일 ~ 2022년 9월 8일 중 7일 간 실험을 진행함. 

## 수집 데이터 항목

### 집 안에 설치된 스마트홈 기기에서 수집되는 데이터

<table>
  <thead>
    <tr>
      <th>카테고리</th>
      <th>데이터 종류</th>
      <th>데이터 필드</th>
      <th>데이터 형식</th>
      <th>수집 주기</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">스피커-사용자 대화 데이터</td>
      <td rowspan="4">정신 건강 설문 응답 데이터</td>
      <td>사용자 답변 텍스트</td>
      <td rowspan="4">JSON</td>
      <td rowspan="4">매 설문 마다 수집</td>
    </tr>
    <tr>
      <td>응답 방식</td>
    </tr>
    <tr>
      <td>답변 시간</td>
    </tr>
    <tr>
      <td>사용자 응답 목소리</td>
    </tr>
     <tr>
      <td rowspan="7">가정 내 환경 데이터</td>
      <td>이미지</td>
      <td>사람 수</td>
      <td rowspan="7">CSV</td>
      <td rowspan="7">1Hz</td>
    </tr>
    <tr>
      <td rowspan="6">환경 정보</td>
      <td>소음(dB)</td>
    </tr>
    <tr>
      <td>조도(lx)</td>
    </tr>
     <tr>
      <td>온도</td>
    </tr>
    <tr>
      <td>습도</td>
    </tr>
    <tr>
     <td>CO2</td>
    </tr>
    <tr>
     <td>TVOC</td>
    </tr>
    <tr>
      <td>음성 데이터</td>
      <td>사용자 응답 목소리</td>
      <td>소리</td>
      <td>3gp 파일</td>
      <td>매 설문 마다 수집</td>
    </tr>
  </tbody>
</table>

---
### 사용자 스마트폰에서 수집되는 데이터
<table>
  <thead>
    <tr>
      <th>카테고리</th>
      <th>데이터 종류</th>
      <th>데이터 필드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">스마트폰 사용 데이터</td>
      <td>사회적 상호 작용 데이터</td>
      <td> 전화 송/수신 횟수 및 통화 시간 <br/> SMS/메신저/SNS 앱 사용 횟수 <br/> 시간 및 알림 기록(메세지 등 콘텐츠 는 저장하지 않으며, 메타 정보만 수집)</td>
    </tr>
     <tr>
      <td>네트워크 및 기기 상태 데이터</td>
      <td>와이파이/블루투스/셀룰러 데이터 연결 <br/> 데이터 송/수신 바이트 양 <br/> 전원 여부 <br/> 알림 모드 <br/> 배터리 레벨/충전 상태 여부 </td>
    </tr>
    <tr>
      <td>키보드 및 미디어 데이터</td>
      <td>키보드 종류 <br/> 입력 문자 종류 <br/> 키 간 거리 <br/> 카메라 사용 이벤트 <br/> 마이크 기록(실제 입력 정보는 수집하지 않고, 메타 정보만 수집) </td>
    </tr>
    <tr>
      <td>활동 데이터</td>
      <td>활동 타입(예: 걷기, 뛰기 등) </td>
    </tr>
  </tbody>
</table>

---

### 스마트 밴드([Fitbit](https://www.fitbit.com/global/kr/home))에서 수집되는 데이터
* 사용자가 착용한 Fitbit에서 수집된 데이터를 [Web API](https://dev.fitbit.com/build/reference/web-api/)를 이용하여 다운로드 받음
* 사용자 UID별로 하루동안 수집된 데이터가 JSON 파일로 저장되어 있음
* [intraday data](https://dev.fitbit.com/build/reference/web-api/intraday/get-activity-intraday-by-date/): 24시간 동안 수집된 시계열 데이터
  * heart-intraday: 기본적으로는 5초 주기로 수집됨
  * 그 외: 1분 주기로 수집됨
  
<table>
  <thead>
    <tr>
      <th>카테고리</th>
      <th>데이터 종류</th>
      <th>데이터 필드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">활동 데이터</td>
      <td rowspan="4">움직인 시간</td>
      <td>minutesSedentary</td>
    </tr>
    <tr>
      <td>minutesLightlyActive</td>
    </tr>
     <tr>
      <td>minutesFairlyActive</td>
    </tr>
     <tr>
      <td>minitesVeryActive</td>
    </tr>
    <tr>
      <td rowspan="2">움직인 거리</td>
      <td>distance</td>
    </tr>
    <tr>
      <td>distance-intraday</td>
    </tr>
    <tr>
      <td rowspan="2">걸음 수</td>
      <td>steps</td>
    </tr>
    <tr>
      <td>steps-intraday</td>
    </tr>
    <tr>
      <td rowspan="2">칼로리 데이터</td>
      <td rowspan="2">소모한 칼로리</td>
      <td>calories</td>
    </tr>
    <tr>
      <td>calories-intrday</td>
    </tr>
    <tr>
      <td rowspan="2">신체 데이터</td>
      <td rowspan="2">심박 수</td>
      <td>heart</td>
    </tr>
    <tr>
      <td>heart-intrday</td>
    </tr>
  </tbody>
</table>



## 데이터 전처리 및 멘탈 상태 예측 모델 생성


## 데이터 분석 및 모델 검증 결과


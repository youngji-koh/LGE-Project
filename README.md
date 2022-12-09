# LGE-Project

## 필드 테스트 및 데이터 수집

* 목적: 스마트 스피커를 활용한 정신 건강 상태 데이터를 수집하는 SW/HW 플랫폼에 대한 필드 테스트를 수행함.  
* 실험 대상 및 기간: KAIST 재학생 10명(여성:4, 남성: 6)을 대상으로 2022년 8월 31일 ~ 2022년 9월 8일 중 7일 간 실험을 진행함. 

## 수집 데이터 항목
실험 기간 동안 수집된 데이터는 아래와 같음 
1. Demographic Information
2. 스마트홈 기기에서 수집되는 스피커-사용자 대화 데이터, 사용자 음성 답변 데이터 및 가정 내 환경 데이터
3. 사용자의 개인 모바일 기기에서 수집되는 스마트폰 사용 데이터
4. 웨어러블 기기에서 수집되는 활동 및 생체 데이터

---
### 1. Demographic Information
* 연령대, 성별, 성격 유형 등의 사용자 정보를 수집함. 
* 수집한 항목은 다음과 같음
  * 연령대, 성별(F/M)
  * Big Five Inventory 10(BFI-10): 성격 유형 검사
  * Patients Health Questionnaire-9: 정신 건강 설문(우울)
  * Generalized Anxiety Disorder-7: 정신 건강 설문(불안 장애)

### 2. 스마트홈 기기에서 수집되는 데이터
* 스피커와 사용자 대화 데이터가 JSON 파일로 저장되어 있음
  * 데이터  경로: [Dataset/](https://github.com/youngji-koh/LGE-Project/tree/main/Dataset/) 
* 가정 내 환경 데이터는 CSV 파일로 저장되어 있음
  * UID 별로 하루동안 수집된 환경데이터 저장
  * 데이터 파일 경로 : [Dataset/Sensors](https://github.com/youngji-koh/LGE-Project/tree/main/Dataset/Sensors) 
* 사용자의 음성 데이터는 3gp 파일로 저장되어 있음
  * UID 별로 설문 전 2분 부터 설문 후 5분 동안의 소리를 녹음한 데이터 저장
  * 각 파일은 1분 간격으로 나뉘어져 있음
  * 데이터 파일 경로 : [Dataset/Voice](https://github.com/youngji-koh/LGE-Project/tree/main/Dataset/Voice) 
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
### 3. 사용자 스마트폰에서 수집되는 데이터
* 데이터 파일 경로: [Dataset/K-Emophone Logger](https://github.com/youngji-koh/LGE-Project/tree/main/Dataset/K-Emophone%20Logger)
* 수집되는 데이터 타입 별로 csv파일 존재

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

### 4. 스마트 밴드([Fitbit](https://www.fitbit.com/global/kr/home))에서 수집되는 데이터
* 사용자가 착용한 Fitbit에서 수집된 데이터를 [Web API](https://dev.fitbit.com/build/reference/web-api/)를 이용하여 다운로드 받음
* 데이터 파일 경로 : [Dataset/Fitbit](https://github.com/youngji-koh/LGE-Project/tree/main/Dataset/Fitbit)
* 사용자 UID 별로 하루동안 수집된 데이터가 JSON 파일로 저장되어 있음
  * 예시: smartspeakertester1-2022-08-31.json (UID 1의 2022년 8월 31일 하루동안 수집된 데이터)
* [intraday data](https://dev.fitbit.com/build/reference/web-api/intraday/get-activity-intraday-by-date/): 24시간 동안 수집된 시계열 데이터
  * heart-intraday: 기본적으로 5초 주기로 수집됨
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
데이터 수집 플랫폼에서 수집된 데이터를 기반으로 정신 건강 상태(스트레스 및 긍/부정 감정)분류를 위한 모델 생성 및 검증하고자 함. 사용자 멘탈 상태 분류 모델 생성을 위해 수집된 센서 데이터에서 피처를 추출하고 사용자의 ESM 정신 건강 설문  답변(스트레스, 긍부정 질문)을 타겟 레이블로 지정함.  

** Data.pkl 설명

(표 여기에 추가해주세요!!)

---


## 데이터 분석 및 모델 검증 결과


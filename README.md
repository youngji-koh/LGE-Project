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
  * 데이터  경로: Dataset/
* 가정 내 환경 데이터는 CSV 파일로 저장되어 있음
  * UID 별로 하루동안 수집된 환경데이터 저장
  * 데이터 파일 경로 : Dataset/Sensors 
* 사용자의 음성 데이터는 3gp 파일로 저장되어 있음
  * UID 별로 설문 전 2분 부터 설문 후 5분 동안의 소리를 녹음한 데이터 저장
  * 각 파일은 1분 간격으로 나뉘어져 있음
  * 데이터 파일 경로 : Dataset/Voice 
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
* 데이터 파일 경로: Dataset/K-Emophone Logger
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
      <td rowspan="4">움직인 시간(분)</td>
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
      <td rowspan="2">움직인 거리(mi)</td>
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
     <tr>
      <td rowspan="4">수면 데이터</td>
      <td rowspan="4">수면 단계(분)</td>
      <td>deep</td>
    </tr>
     <tr>
      <td>light</td>
    </tr>
     <tr>
      <td>rem</td>
    </tr>
     <tr>
      <td>wake</td>
    </tr>
  </body>
</table>



## 데이터 전처리 및 피쳐 추출 
데이터 수집 플랫폼에서 수집된 데이터를 기반으로 정신 건강 상태(스트레스 및 긍/부정 감정)분류를 위한 모델 생성 및 검증하고자 함. 사용자 멘탈 상태 분류 모델 생성을 위해 수집된 센서 데이터에서 피처를 추출하고 사용자의 ESM 정신 건강 설문  답변(스트레스, 긍부정 질문)을 타겟 레이블로 지정함.  

### 데이터 통합 및 전처리
 * 데이터를 통합하는 과정에서 결측 값을 처리하고 모델에 들어가는 입력이 동일한 값의 범위를을 갖도록 데이터를 정규화함. 
 * 또한, 데이터셋 불균형을 해결하기 위해 대표적인 오버 샘플링 기법인 SMOTE를 사용함.
  
### 피쳐 추출 
 * 수집된 데이터에서 추출된 피쳐는 아래 표와 같음. 
 * 환경 및 이미지 데이터의 경우 설문 응답 전 1분 동안의 센서 값 평균 값을 사용함. 
 * 사용자 응답 녹음 데이터의 경우 설문 시작 전 1분, 설문 응답하는 시간 동안 녹음된 오디오 데이터를 활용함. 
   * 해당 데이터는 [YouTube AudioSet](https://research.google.com/audioset/) 데이터셋으로 사전 학습된 [VGGish](https://github.com/tensorflow/models/tree/master/research/audioset/vggish) 모델을 이용하여 임베딩 된 음성 정보를 피쳐로 사용함. 
 * 실험 전 사전 설문을 통해 수집한 사용자 정보(예: 사용자 연령대, 성별, 성격 유형)를 이용하였고 성별 정보의 경우 One-Hot Encoding을 적용함. 
 * 이 외에 스마트 스피커 응답 데이터에서는 각 질문 대화 시간, 응답 방법(터치, 음성) 등을 피쳐로 추출함.

** Data.pkl 설명 (X, y)

(표 여기에 추가해주세요!!)


## 모델 생성 및 검증 결과 
사용자의 정신 건강 중 스트레스 및 긍부정 정도 예측을 목표로 사용자 정신 건강 상태 예측 모델을 생성함. 

### 모델 생성
* 타겟 레이블의 경우, 스마트 스피커를 통한 ESM 설문 답변 중 스트레스 및 긍/부정 질문에 대한 사용자 답변을 활용함. 
* 전체 피쳐 중 타겟 레이블을 제외한 나머지 피처를 다양하게 조합하여 모델을 학습함. 
* 학습 모델로는 SVM, Logistic Regression, K-Neighbors, Decision Tree, Naive Bayes, Random Forest를 사용함. 
* 학습 과정에서 입력 데이터 과적합 방지를 위해 교차 검증을 진행하였으며 작은 데이터셋에 효과적인 LOOCV(Leave-one-out cross validation)를 사용함.

### 모델 검증 결과
스트레스와 긍정/부정 감정 예측 분류에서 Decision Tree 기반의 앙상블 모델인 Random Forest 에서 각각 0.72와 0.79로 가장 높은 정확도를 보임. 
다만, 음성 데이터를 추가한 모델이 더 저조한 성능을 보임. 이는 스피커에서 나오는 음성과 사용자의 목소리 화자 구분이 되어 있지 않아 정확한 피처를 추출하는데 한계가 있 발생한 것으로 예상됨.

<table>
  <thead>
    <tr>
      <th>학습 데이터</th>
      <th>학습 모델</th>
      <th>스트레스 예측 정확도</th>
      <th>긍/부정 감정 예측 정확도</th>
    </tr>
  </thead>
  <body>
    <tr>
      <td rowspan="7">음성 데이터 포함</td>
      <td>SVM</td>
      <td>0.541</td>
      <td>0.716</td>
    </tr>
    <tr>
      <td>Logistic Regression</td>
      <td>0.556</td>
      <td>0.714</td>
    </tr>
    <tr>
      <td>K-Neighbors</td>
      <td>0.551</td>
      <td>0.513</td>
    </tr>  
    <tr>
      <td>Decision Tree</td>
      <td>0.559</td>
      <td>0.722</td>
    </tr>  
    <tr>
      <td>Naive Bayes</td>
      <td>0.561</td>
      <td>0.608</td>
    </tr>  
    <tr>
      <td>Random Forest</td>
      <td>0.554</td>
      <td>0.765</td>
    </tr> 
   <tr>
      <td>평균</td>
      <td>0.554</td>
      <td>0.673</td>
    </tr>  
   <tr>
      <td rowspan="7">음성 데이터 미포함</td>
      <td>SVM</td>
      <td>0.565</td>
      <td>0.629</td>
    </tr>
    <tr>
      <td>Logistic Regression</td>
      <td>0.635</td>
      <td>0.702</td>
    </tr>
    <tr>
      <td>K-Neighbors</td>
      <td>0.650</td>
      <td>0.702</td>
    </tr>  
    <tr>
      <td>Decision Tree</td>
      <td>0.659</td>
      <td>0.708</td>
    </tr>  
    <tr>
      <td>Naive Bayes</td>
      <td>0.694</td>
      <td>0.712</td>
    </tr>  
    <tr>
      <td>Random Forest</td>
      <td>0.721</td>
      <td>0.792</td>
    </tr> 
   <tr>
      <td>평균</td>
      <td>0.654</td>
      <td>0.707</td>
    </tr>  
  </body>
</table>

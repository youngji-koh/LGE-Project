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
* 실험 전 사전 설문을 통해 연령대, 성별, 성격 유형 등의 사용자 정보를 수집함. 
  * 데이터  경로: Dataset/user_demographics.csv
* 수집한 항목은 다음과 같음
  * 사용자 기본 정보 
    * 연령대, 성별(F/M)
  * 사용자 성격 유형 
    * Big Five Inventory 10(BFI-10)설문을 통해 외향성, 성실성 등 5가지 주요 성격 유형에 대해 사용자를 점수화함.   
  * 사용자 정신 건강 상태는 다음과 같은 설문을 통해 수집함. 
    * Patients Health Questionnaire-9(PHQ-9): 우울증
    * Generalized Anxiety Disorder-7(GAD-7): 불안 장애
    * Perceived Stress Scale(PSS) : 인지 스트레스

### 2. 스마트홈 기기에서 수집되는 데이터
* 스피커와 사용자 대화 데이터가 JSON 파일로 저장되어 있음
  * 데이터  경로: Dataset/Smartspeaker_conv/response_data_2022-08-31_2022-09-08.json
* 가정 내 환경 데이터는 CSV 파일로 저장되어 있음
  * 사용자 별로 하루 단위로 수집된 환경데이터 저장
    * 데이터 파일 경로 : Dataset/Sensors
      * 통합 센서 데이터 파일 경로 : Dataset/sensor_data.csv  
* 사용자의 음성 데이터는 3gp 파일로 저장되어 있음
  * 사용자 별로 설문 직전 2분부터 설문 직후 5분까지의 음성 데이터를 저장함. 
  * 3gp 음성 파일은 1분 간격으로 저장
    * 데이터 파일 경로 : Dataset/Voice 
    * 음성 데이터 피처 파일 경로 : Dataset/voice_data.csv
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
### 3. 사용자 스마트폰 사용 데이터 
* 사용자 스마트폰 사용 데이터는 수집 항목 카테고리 별로 csv 파일 로 저장되어 있음(16개)
  * 데이터 디렉토리 경로: Dataset/K-Emophone Logger/ByCategories
  
<table style="undefined;table-layout: fixed; width: 812px">
<colgroup>
<col style="width: 92.88889px">
<col style="width: 148.88889px">
<col style="width: 246.88889px">
<col style="width: 323.77778px">
</colgroup>
<thead>
  <tr>
    <th></th>
    <th>카테고리</th>
    <th>세부 카테고리</th>
    <th>데이터 설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="16">스마트폰 사용 데이터</td>
    <td rowspan="5">사회적 상호 작용 데이터</td>
    <td>APP_USAGE_EVENT</td>
    <td>모바일 앱 내 이벤트 발생 시간 및 유형 기록<br>- type : 앱 이벤트 타입(앱 꺼짐/켜짐 등)</td>
  </tr>
  <tr>
    <td>CALL_LOG</td>
    <td>통화 기록<br>- type : 발신/수신 여부,  수신 거부 여부 등 <br>- duration : 통화  시간</td>
  </tr>
  <tr>
    <td>DEVICE_EVENT</td>
    <td>스마트 폰 기기 이벤트 발생<br>- type : 이벤트 유형, 스크린 켜짐/꺼짐(SCREEN_OFF/SCREEN_ON) 등의 정보</td>
  </tr>
  <tr>
    <td>MESSAGE</td>
    <td>메세지 관련 정보<br>- type : 메세지 발신/수신(SENT/INBOX) 여부 </td>
  </tr>
  <tr>
    <td>NOTIFICATION</td>
    <td>어떤 종류의 알림(메세지, 전화, 에러 등)이 발생했는지 기록</td>
  </tr>
  <tr>
    <td rowspan="5">네트워크 및 기기 상태</td>
    <td>BATTERY</td>
    <td>배터리 레벨 및 충전여부(DISCHARGING/CHARGING)</td>
  </tr>
  <tr>
    <td>BLUETOOTH</td>
    <td>블루투스 연결여부(NONE, BONDED) </td>
  </tr>
  <tr>
    <td>DATA TRAFFIC</td>
    <td>데이터 트래픽 양(rxBytes 와 txBytes 단위로 나타냄)</td>
  </tr>
  <tr>
    <td>INSTALLED APP</td>
    <td>설치된 앱 정보(id로 기록) </td>
  </tr>
  <tr>
    <td>WIFI</td>
    <td>와이파이 연결되어 있을 경우 어떤 Access Point 에 접근했는지 정보</td>
  </tr>
  <tr>
    <td rowspan="2">키보드 및 미디어 데이터 </td>
    <td>KEY_LOG</td>
    <td>키보드 사용 시 키보드 사용 정보(키보드 종류 등) 나타냄</td>
  </tr>
  <tr>
    <td>MEDIA</td>
    <td>사진/동영상 다운로드 하였을 때, 관련 시간 및 미디어 파일 종류(gif, jpeg, png, mp4 등)를 나타냄</td>
  </tr>
  <tr>
    <td rowspan="4">활동 데이터</td>
    <td>FITNESS</td>
    <td>사용자 걸음수, 이동 거리</td>
  </tr>
  <tr>
    <td>LOCATION</td>
    <td>사용자 현재 위치의 위도, 경도, 고도, 속도 기록</td>
  </tr>
  <tr>
    <td>PHYSICAL_ACTIVITY</td>
    <td>사용자 액티비티 유형(뛰기, 걷기, 자전거 탑승 등) </td>
  </tr>
  <tr>
    <td>PHYSICAL_ACTIVITY_TRANLATION</td>
    <td>사용자 액티비티 상태 변화를 기록(뛰기, 걷기, 자전거 탑승 등)</td>
  </tr>
</tbody>
</table>


---

### 4. 스마트 밴드([Fitbit](https://www.fitbit.com/global/kr/home))에서 수집되는 데이터
* [Web API](https://dev.fitbit.com/build/reference/web-api/)를 활용하여 각 사용자 별 Fitbit 스마트 밴드에서 수집된 데이터를 다운
   * 데이터 파일 경로 : Dataset/Fitbit
* 사용자 별로 하루동안 수집된 데이터가 JSON 파일로 저장되어 있음
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
데이터 수집 플랫폼에서 수집된 데이터를 기반으로 정신 건강 상태(스트레스 및 긍부정 감정)분류를 위한 모델 생성 및 검증하고자 함. 사용자 멘탈 상태 분류 모델 생성을 위해 수집된 센서 데이터에서 피처를 추출함. 

### 데이터 통합 및 전처리
 * 여러 소스에서 수집된 데이터를 통합함. 이 과정에서 결측 값을 다른 데이터의 평균값으로 대체함. 또한, 모든 피쳐 별로 동일한 숫자 범위를 갖도록 데이터를 정규화함(StandardScaler()). 
 * 또한, 데이터셋 불균형을 해결하기 위해 대표적인 오버 샘플링 기법인 SMOTE를 사용함.
  
### 피쳐 추출 
 * 수집된 데이터에서 추출된 피쳐는 아래 표와 같음. 
    * 데이터 디렉토리 경로: Dataset/Data.pkl
 * 스마트 스피커 응답 데이터에서는 각 질문 대화 시간, 응답 방법(터치, 음성) 등을 피쳐로 추출함.
 * 환경 센서 데이터의 경우 설문 응답 직전 1분 동안의 평균 센서값을 사용. 
 * 설문 중 사용자 음성 녹음 데이터의 경우 설문 시작 전 1분과 설문 응답 중 오디오 데이터를 활용함. 
   * 해당 데이터는 [YouTube AudioSet](https://research.google.com/audioset/) 데이터셋으로 사전 학습된 [VGGish](https://github.com/tensorflow/models/tree/master/research/audioset/vggish) 모델을 이용하여 임베딩 된 음성 정보를 피쳐로 사용함. 
 * 사용자별 특성을 예측에 반영하기 위해, 실험 전 사전 설문을 통해 수집한 사용자 정보(예: 사용자 연령대, 성별, 성격 유형)를 포함함. 또한, 성별의 경우 One-Hot Encoding을 적용. 


<table>
<thead>
  <tr>
    <th>카테고리</th>
    <th>세부 카테고리</th>
    <th>피쳐 종류</th>
    <th>데이터 설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="6">스피커-사용자 설문 대화 데이터</td>
    <td>대화 길이&nbsp;&nbsp;</td>
    <td>whole_conv_length(sec)</td>
    <td>설문 1회당 소요 시간(초)</td>
  </tr>
  <tr>
    <td>대화 속도 </td>
    <td>dixit_response_rate</td>
    <td>딕싯 그림 설명 사용자 답변 속도, (답변 텍스트 길이)/(답변길이)</td>
  </tr>
  <tr>
    <td rowspan="4">정신 건강 설문 답변</td>
    <td>phq2_result</td>
    <td>사용자 우울증 상태,  우울증이 있을 확률이 높으면(PHQ2 점수 3점 이상) 1, 아니면 0.  </td>
  </tr>
  <tr>
    <td>gad2_result</td>
    <td>사용자 불안 장애 상태, 불안 장애가 있으면(GAD2 점수가 3점이상) 1, 아닐 경우 0</td>
  </tr>
  <tr>
    <td>stress_result</td>
    <td>스트레스 유무, 스트레스가 평균 이상이면 1, 아니면 0</td>
  </tr>
  <tr>
    <td>posNeg_result</td>
    <td>긍부정 감정 정도, 부정적인 감정 상태면 1, 아니면 0</td>
  </tr>
  <tr>
    <td rowspan="6">센서 데이터</td>
    <td rowspan="6">가정 환경 내 센서 데이터 </td>
    <td>dB</td>
    <td>설문 시작 직전 1분 평균 데시벨</td>
  </tr>
  <tr>
    <td>Temperature</td>
    <td>설문 시작 직전 1분 평균 온도</td>
  </tr>
  <tr>
    <td>Humidity</td>
    <td>설문 시작 직전 1분 평균 습도</td>
  </tr>
  <tr>
    <td>CO2</td>
    <td>설문 시작 직전 1분 평균 CO2 농도</td>
  </tr>
  <tr>
    <td>TVOC</td>
    <td>설문 시작 직전 1분 평균 공기질 오염도</td>
  </tr>
  <tr>
    <td>Light</td>
    <td>설문 시작 직전 1분 평균 조도값</td>
  </tr>
  <tr>
    <td rowspan="13">사용자 실험 사전 설문</td>
    <td rowspan="2">성별</td>
    <td>F</td>
    <td>여자면 1, 아닐 경우 0</td>
  </tr>
  <tr>
    <td>M</td>
    <td>남자면 1, 아닐 경우 0</td>
  </tr>
  <tr>
    <td rowspan="5">성격 유형(Big-5 모델 기반)</td>
    <td>Extroversion</td>
    <td>외향성, 외향적일 수록 10에 가까운 점수(0~10)</td>
  </tr>
  <tr>
    <td>Neuroticism</td>
    <td>신경질적 성향, 해당 성향이 높을 수록 10에 가까운 점수(0~10)</td>
  </tr>
  <tr>
    <td>Conscientiousness</td>
    <td>성실성, 해당 성향이 높을 수록 10에 가까운 점수(0~10)</td>
  </tr>
  <tr>
    <td>Agreeable</td>
    <td>해당 성향이 높을 수록 10에 가까운 점수(0~10)</td>
  </tr>
  <tr>
    <td>Openness</td>
    <td>개방성, 해당 성향이 높을 수록 10에 가까운 점수(0~10)</td>
  </tr>
  <tr>
    <td rowspan="6">사전 사용자 정신 건강 상태</td>
    <td>depression_or_not</td>
    <td>사용자의 기존 우울증 유무(PHQ9 설문 기반, 점수 총합이 10점 이상이면 주목할 만한 우울증)</td>
  </tr>
  <tr>
    <td>anxietyDisorder_or_not</td>
    <td>사용자의 기존 불안 장애 유무(GAD7 설문 기반, 점수 총합이 6점이면 불안 장애)</td>
  </tr>
  <tr>
    <td>PSS_pos_score</td>
    <td>Perceived Stress Scale(PSS) 설문 중 긍정 문항 점수 총합</td>
  </tr>
  <tr>
    <td>PSS_neg_score</td>
    <td>Perceived Stress Scale(PSS) 설문 중 부정 문항 점수 총합</td>
  </tr>
  <tr>
    <td>PSS_score</td>
    <td>Perceived Stress Scale(PSS) 설문 총합</td>
  </tr>
  <tr>
    <td>PSS_stress_or_not</td>
    <td>사용자 기존 스트레스 정도(문항 총점이 13점 이상이면, 스트레스 정도가 정상이 아니라고 판단)</td>
  </tr>
  <tr>
    <td rowspan="2">음성 데이터</td>
    <td rowspan="2">사용자 목소리</td>
    <td>before_audio</td>
    <td>설문 시작 전 1분 동안 주위 소리를 녹음한 데이터</td>
  </tr>
  <tr>
    <td>after_audio</td>
    <td>사용자가 스피커와 대화 녹음한 데이터</td>
  </tr>
</tbody>
</table>



## 모델 생성 및 검증 결과 
사용자의 정신 건강 중 스트레스(stress_result) 및 긍부정 정도(posNeg_result) 예측을 목표로 사용자 정신 건강 상태 예측 모델을 생성함. 

### 모델 생성
* 타겟 레이블의 경우, 일상 생활 내 사용자 정신 건강 설문 응답 중 스트레스 및 긍/부정 항목을 활용함
* 전체 피쳐 중 타겟 레이블을 제외한 나머지 피처를 다양하게 조합하여 모델을 학습함. 
* 학습 모델로는 SVM, Logistic Regression, K-Neighbors, Decision Tree, Naive Bayes, Random Forest를 사용함. 
* 학습 과정에서 입력 데이터 과적합 방지를 위해 교차 검증을 진행하였으며 작은 데이터셋에 효과적인 LOOCV(Leave-one-out cross validation)를 사용함.

### 모델 검증 결과
스트레스와 긍정/부정 감정 예측에서 Random Forest(Decision Tree 기반의 앙상블 모델) 에서 각각 0.72와 0.79로 가장 높은 정확도를 보임. 
다만, 음성 데이터를 추가한 모델이 더 저조한 성능을 보임. 이는 스피커에서 나오는 음성과 사용자의 목소리 화자 구분이 되어 있지 않아 정확한 피처를 추출하는데 한계가 있었음.

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

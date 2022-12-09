# LGE-Project

## 필드 테스트 및 데이터 수집

* 목적: 스마트 스피커를 활용한 정신 건강 상태 데이터를 수집하는 SW/HW 플랫폼에 대한 필드 테스트를 수행함.  
* 실험 대상 및 기간: KAIST 재학생 10명(여성:4, 남성: 6)을 대상으로 2022년 8월 31일 ~ 2022년 9월 8일 중 7일 간 실험을 진행함. 

## 수집 데이터 항목

* **스마트홈 기기**

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
      <td rowspan="4">설문 응답 데이터</td>
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
      <td rowspan="8">스마트홈 환경 데이터</td>
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
      <td>사용자 응답 목소리</td>
      <td>소리</td>
      <td>3gp 파일</td>
      <td>매 설문 마다 </td>
    </tr>
  </tbody>
</table>


## 데이터 전처리 및 멘탈 상태 예측 모델 생성


## 데이터 분석 및 모델 검증 결과


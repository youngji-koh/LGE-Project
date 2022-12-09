# LGE-Project

## Overview
**필드 테스트 및 데이터 수집**

* 센서 데이터를 기반으로 사용자 자가보고 정보 수집 시점을 결정하여 정신 건강 상태 데이터를 수집하는 SW/HW 플랫폼에 대한 필드 테스트를 수행함.  
* KAIST 재학생 10명(여성:4, 남성: 6)을 대상으로 8월 31일 ~ 9월 7일 중 7일 간 실험을 진행함. 
  * 기숙사 및 학교 근처에 거주하며 집에서 최소 5시간 이상 시간을 보내는 학생들을 대상으로 데이터 수집을 진행하였으며 기계학습을 위한 충분한 레이블 확보를 위하여 각 참여자 당 하루에 10회 이상 설문에 응답하도록 함.

## 수집된 데이터 항목

** 자체 개발한 스피커



|          카테고리        |        **데이터 종류**        |                                                  **데이터 필드**                                                   |
|:------------------------:|:----------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
|      설문 응답 데이터     |    정신 건강 설문 응답 데이터  |                  사용자 답변 텍스트 <br/> 응답 방식 <br/> 답변 시간 <br/> 사용자 응답 목소리                          |         
|: 스마트홈 환경 데이터 :||: 이미지 :|| 사람 수|
|   ^^    |            환경 정보   |  사람 수                                                                                                  |
|       ^^              |           환경 정보          |     소음(dB) <br/> 조도(lx) <br/> 온도 <br/> 습도 <br/> CO2 <br/> TVOC                                                             |


|       **카테고리**       |        **데이터 종류**       |                                                  **데이터 필드**                                                  |
|:------------------------:|:----------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| 활동 및 생체 신호 데이터 |          활동 데이터         |                                            움직인 시간, 움직인 거리 등                                            |
|                          |         칼로리 데이터        |                                                  소모한 칼로리 등                                                 |
|                          |          수면 데이터         |                                              수면 시간, 수면 단계 등                                              |
|                          |          신체 데이터         |                                                       심박수                                                      |


|       **카테고리**       |        **데이터 종류**       |                                                  **데이터 필드**                                                  |
|:------------------------:|:----------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
|   스마트폰 사용 데이터   |    사회적 상호작용 데이터    |                 전화 송/수신 횟수 및 통화 시간, SMS/메신저/SNS 앱 사용 횟수, 시간 및 알림 기록 등                 |
|                          | 네트워크 및 기기 상태 데이터 | 와이파이/블루투스/셀룰러 데이터 연결, 데이터 송/수신 바이트 양, 전원 여부, 알림 모드, 배터리 레벨/충전 상태 여부  |
|                          |    키보드 및 미디어 데이터   |                      키보드 종류, 입력 문자 종류, 키 간 거리, 카메라 사용 이벤트, 마이크 기록                     |
|                          |          활동 데이터         |                                           활동 타입(예 : 걷기, 뛰기 등)                                           |

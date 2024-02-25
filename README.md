### InvestorRoadmap

- 프로젝트 설명
  - `eXplainable AI(설명 가능한 AI)`를 활용하여 개인 투자자의 **투자 습관을 파악하고 희망하는 투자 형태로 변화**할 수 있도록 도와주는 솔루션입니다.

- 프로젝트 구성
  - 데이터 수집
    - DART 전자공시시스템에서 제공하는 재무 및 현금흐름 데이터 수집 진행
    - KRX 한국거래소 정보데이터시스템에서 제공하는 종목 별 가격 데이터 수집 진행

  - 데이터 전처리
    - Pandas DataFrame 형식으로 데이터 전처리 진행
    - 데이터 plotting 및 이상치에 대한 log 연산 진행
    - 가격 데이터와 재무 데이터를 바탕으로 데이터 선정 및 정규분포화 등 전처리 진행
      - 변동성 지표
        - `ATR` : ATRPP (Average True Range Per Price)
      - 수익성 지표
        - `배당수익률` (Dividend Yield)
        - `순이익률` (Net Profit Margin)
        - `자본회전율` (Asset Turnover)
      - 안정성 지표
        - `부채비율`
      - 가치성 지표
        - `PSR` (Price Sales Ratio)
        - `PBR` (Price Book-value Ratio)
      - 모멘텀 지표
        - `TSF Slope` : TSF (Time Series Forcasting) 지표에 대한 Slope (기울기)

  - 데이터 분석 및 모델링
    - `탐색적 데이터 분석(EDA) 기법`을 통해 유의미한 피쳐 조합을 추출합니다.
    - 지표 데이터의 분포를 바탕으로 `백분위 분석 기법`을 통해 **스코어링 및 라벨링**을 진행합니다.
    - 사용자의 투자 상태를 위 5가지 지표로 표현할 수 있도록 각각의 지표에 `Linear Regression 모델`을 학습합니다.
    - 이전에 학습한 모델에 대하여 `LIME`(Local Interpretable Model-agnostic Explanation) 기법을 적용하여 현재 투자 습관을 파악하도록 합니다.
    - `LIME` 모델에 대하여 quartile 방식으로 설계하였기 때문에, 오차가 큰 지표에 대하여 가장 설명력이 큰 feature 를 구간의 간격만큼 개선합니다.

  - 모델 검증
    - `RMS` (Root Mean Square) 방식을 활용하여 조정 전과 후에 대한 결과 비교(각 투자 지표 별 모델 추론 결과값 바탕)로 설명 모델에 대한 중요도를 파악합니다.
      - 설명력이 강한 Feature 를 바탕으로 개선하는 것과 설명력이 약한 Feature 를 바탕으로 개선하는 것 사이의 성능을 비교합니다.
      - 지표 간의 상관관계 누적합 값을 바탕으로 다양한 지표 조합에 대한 성능을 비교합니다.
   
- 프로젝트 예시
  - 아래와 같이, 입력된 종목에 대한 피쳐들을 변동성, 수익성, 안정성, 가치성, 모멘텀으로 총 5 가지 측면의 지표로 분석하여 정보를 제공합니다.
  - 사용자는 아래 스코어링된 정보를 바탕으로 더 나은 투자의 방향성을 찾을 수 있도록 유도합니다.
    ![24 2 14 XAI 활용 종목 분석](https://github.com/DevTae/InvestorRoadmap/assets/55177359/a0afe329-1a76-446a-8957-6e9035f31c27)

- References
  - https://dart.fss.or.kr/
  - http://data.krx.co.kr/

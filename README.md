### InvestorRoadmap

- 프로젝트 설명
  - `eXplainable AI(설명 가능한 AI)`를 활용하여 개인 투자자의 **투자 습관을 파악하고 희망하는 투자 형태로 변화**할 수 있도록 도와주는 솔루션입니다.

- 프로젝트 구성
  - 데이터 수집
    - DART 전자공시시스템에서 제공하는 재무 및 현금흐름 데이터 수집 진행
    - KRX 한국거래소 정보데이터시스템에서 제공하는 종목 별 가격 데이터 수집 진행

  - 데이터 전처리
    - Pandas DataFrame 형식으로 데이터 전처리 진행
    - 가격 데이터와 재무 데이터를 바탕으로 아래 방식으로 전처리 진행
      - 변동성 지표
        - `ATR` : ATRPP (Average True Range Per Price)
      - 수익성 지표
        - `배당수익률` (Dividend Yield)
        - `순이익률` (Net Profit Margin)
        - `자본회전율` (Asset Turnover)
      - 안정성 지표
        - `Altman Z-Score` (부도 위험도 지표)
        - `부채비율`
      - 가치성 지표
        - `PER` (Price Earning Ratio)
        - `PSR` (Price Sales Ratio)
        - `PBR` (Price Book-value Ratio)
      - 모멘텀 지표
        - `TSF Slope` : TSF (Time Series Forcasting) 지표에 대한 Slope (기울기)

  - 데이터 분석 및 모델링
    - `탐색적 데이터 분석(EDA) 기법`을 통해 유의미한 피쳐를 추출합니다.
    - 지표 데이터의 분포를 바탕으로 `백분위 분석 기법`을 통해 **스코어링 및 라벨링**을 진행합니다.
    - 사용자의 투자 상태를 위 4가지 지표로 표현할 수 있도록 `Linear Regression 모델`을 구축합니다.
    - `LIME`(Local Interpretable Model-agnostic Explanation) 기법을 통해 원하는 투자 습관으로 변화할 수 있도록 방향성을 제시합니다.
   
- 프로젝트 예시
  - 아래와 같이, 입력된 종목에 대한 피쳐들을 변동성, 수익성, 가치성, 모멘텀으로 총 4 가지 측면의 지표로 분석하여 정보를 제공합니다.
  - 사용자는 아래 스코어링된 정보를 바탕으로 더 나은 투자의 방향성을 찾을 수 있습니다.
    ![24 2 14 XAI 활용 종목 분석](https://github.com/DevTae/InvestorRoadmap/assets/55177359/a0afe329-1a76-446a-8957-6e9035f31c27)

- References
  - https://dart.fss.or.kr/
  - http://data.krx.co.kr/

import streamlit as st
import pandas as pd
import numpy as np

# 페이지 기본설정
st.set_page_config(layout="wide", page_title="나만의 포트폴리오", page_icon="🚀")

st.title("🚀 매출 데이터 분석 리포트")
st.markdown("---")

with st.sidebar:
    st.header("설정")
    uploaded_file = st.file_uploader("csv 파일 업로드", type=['csv'])

    chart_type = st.selectbox("차트 종류 선택", ["Line Chart", "Bar Chart", "Area Chart"])

    preview_count = st.slider("데이터 미리보기 개수", 5, 50, 10)

    # 데이터 필터링 체크박스
    st.markdown("---")
    st.header("데이터 필터링")
    apply_filter = st.checkbox("'A' 컬럼 > 0 필터 적용")

# [메인] 데이터 처리 로직
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("파일 업로드 성공")
else:
    # 실습용 더미 데이터 생성 (파일 없는 경우)
    st.info("csv 파일을 업로드 하면 해당 데이터로 분석합니다. 현재는 샘플 데이터입니다.")
    df = pd.DataFrame(
        np.random.randn(50, 3),
        columns = ['A', 'B', 'C']
    )

# 체크박스 선택 시 데이터 필터링
if apply_filter:
    df = df[df['A'] > 0]

# [레이아웃] 다중 컬럼으로 화면 분할
col1, col2 = st.columns(2)

with col1:
    st.subheader("데이터 미리보기")
    st.dataframe(df.head(preview_count))

with col2:
    st.subheader("데이터 시각화")
    if chart_type == "Line Chart":
        st.line_chart(df)
    elif chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type == "Area Chart":
        st.area_chart(df)

# 통계 요약
with st.expander("클릭하여 기초 통계 보기"):
    st.subheader("기초 통계")
    st.write(df.describe())

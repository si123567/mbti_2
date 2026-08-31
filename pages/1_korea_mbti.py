import streamlit as st

st.set_page_config(page_title="한국 MBTI 비율 🇰🇷", page_icon="🇰🇷")
st.title("🇰🇷 우리나라 MBTI 비율")
st.caption("공개된 참고 자료를 그래프로 살펴봐요.")

data = {
"ISTJ":12.8,"ESTJ":12.4,"ENFP":9.7,"ISFJ":8.3,"ESFJ":8.2,"ESFP":7.2,
"INFP":6.7,"ISFP":6.5,"ESTP":4.2,"ISTP":4.1,"ENTP":3.6,"ENTJ":3.5,
"ENFJ":3.3,"INTJ":3.3,"INTP":3.2,"INFJ":2.9
}

st.info("📌 2023년 공개 자료를 참고한 교육용 통계입니다. 자체검사 참여자 기반이므로 대한민국 전체 인구의 절대적인 비율로 해석하지 마세요.")
st.subheader("📊 MBTI 유형별 비율")
st.bar_chart(data)
st.subheader("🏆 TOP 5")
for i,(mbti,rate) in enumerate(sorted(data.items(),key=lambda x:x[1],reverse=True)[:5],1):
    st.write(f"**{i}위 · {mbti}** — {rate}%")
st.caption("참고: 테스트모아 2023년 한국 MBTI 통계.")

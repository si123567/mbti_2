import streamlit as st

st.set_page_config(page_title="나라별 MBTI 🌎", page_icon="🌎")
st.title("🌎 나라별 MBTI 분포")
st.caption("국가별 자료를 비교해 보는 교육용 페이지입니다.")

types=["ISTJ","ESTJ","ENFP","ISFJ","ESFJ","ESFP","INFP","ISFP","ESTP","ISTP","ENTP","ENTJ","ENFJ","INTJ","INTP","INFJ"]
countries={
"한국 🇰🇷":[12.8,12.4,9.7,8.3,8.2,7.2,6.7,6.5,4.2,4.1,3.6,3.5,3.3,3.3,3.2,2.9],
"미국 🇺🇸":[13.8,12.3,11.6,8.7,4.4,3.3,8.1,2.1,8.8,8.5,5.4,4.3,1.5,2.5,3.2,1.8],
"일본 🇯🇵":[14.0,9.8,13.0,5.5,8.2,4.1,6.5,4.1,7.5,5.8,4.2,2.5,2.8,2.2,2.0,1.2],
"영국 🇬🇧":[12.0,9.5,12.5,8.8,4.2,3.8,8.0,2.8,7.2,6.8,5.5,4.2,1.6,2.5,3.8,2.5]
}
st.warning("⚠️ 국가별 표본과 검사 방법이 다르므로 국가 전체 인구의 성격을 나타내는 공식 통계로 보지 마세요.")
country=st.selectbox("🌍 나라 선택",list(countries))
values=dict(zip(types,countries[country]))
st.subheader(f"📊 {country} MBTI 분포")
st.bar_chart(values)
st.subheader("🥇 TOP 3")
for i,(mbti,rate) in enumerate(sorted(values.items(),key=lambda x:x[1],reverse=True)[:3],1):
    st.write(f"**{i}위 · {mbti}** — {rate:.1f}%")

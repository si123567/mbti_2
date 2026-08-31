import streamlit as st

st.set_page_config(page_title="진로 탐색 활동 🚀", page_icon="🚀")
st.title("🚀 나의 진로 탐색 활동")
st.caption("MBTI와 함께 흥미·가치관을 살펴봐요.")

st.info("🧠 MBTI는 직업을 결정하는 검사가 아닙니다. 나를 이해하는 하나의 출발점으로 활용해 보세요.")

likes=st.multiselect("🎯 좋아하는 활동",[
"💻 컴퓨터·코딩","🎨 그림·디자인","🗣️ 사람들과 대화하기","🔬 실험·탐구",
"📚 읽기·글쓰기","🎤 발표·공연","🔧 만들기·고치기","🌱 다른 사람 돕기",
"📊 자료 분석하기","🌎 새로운 곳·문화 탐색"])

values=st.multiselect("💎 진로에서 중요한 가치",[
"💡 창의성","🤝 사람과의 관계","🎯 성취와 목표","🧩 문제 해결",
"🛡️ 안정성","🌱 사회에 도움 주기","💰 경제적 보상","🕊️ 자유로운 환경"])

st.subheader("🔎 추천 탐색 방향")
if not likes and not values:
    st.write("☝️ 활동과 가치를 선택하면 진로 탐색 방향을 보여드려요.")
else:
    if any(x in likes for x in ["💻 컴퓨터·코딩","🔬 실험·탐구","📊 자료 분석하기"]):
        st.success("🔬 탐구·기술 분야: AI, 데이터, 공학, 연구 등을 탐색해 보세요.")
    if any(x in likes for x in ["🎨 그림·디자인","📚 읽기·글쓰기","🎤 발표·공연"]):
        st.success("🎨 창의·콘텐츠 분야: 디자인, 콘텐츠, 영상, 광고 등을 탐색해 보세요.")
    if any(x in likes for x in ["🗣️ 사람들과 대화하기","🌱 다른 사람 돕기"]):
        st.success("🤝 사람·소통 분야: 교육, 상담, 복지, 홍보 등을 탐색해 보세요.")
    if "💡 창의성" in values or "🕊️ 자유로운 환경" in values:
        st.success("💡 창의성과 자율성을 활용하는 직업을 비교해 보세요.")
    if "🛡️ 안정성" in values:
        st.success("🛡️ 안정적인 환경과 체계가 있는 직업도 비교해 보세요.")
    if "🌱 사회에 도움 주기" in values:
        st.success("🌱 사회적 가치와 사람을 돕는 직업을 탐색해 보세요.")

st.divider()
st.subheader("🎯 진로 탐색 3단계")
st.markdown("**① 직업 알아보기** — 관심 직업 3개의 업무를 조사해 보세요.")
st.markdown("**② 필요한 역량 알아보기** — 필요한 지식·기술·공부 방법을 비교해 보세요.")
st.markdown("**③ 작은 경험 해보기** — 동아리·프로젝트·독서·체험 등으로 직접 경험해 보세요.")
st.success("🌱 진로는 한 번에 정답을 고르는 것이 아니라 경험하면서 방향을 찾아가는 과정입니다.")


import streamlit as st

st.set_page_config(
    page_title="MedVision KZ",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 MedVision KZ")
st.subheader("Ми МРТ-суреттерін жасанды интеллект арқылы талдау")

st.write(
    "Медициналық кескіндерді өңдеуге арналған "
    "зерттеу және білім беру жобасы."
)

st.warning(
    "Бұл прототип медициналық диагноз қоймайды. "
    "Нәтижелер дәрігер қорытындысын алмастырмайды."
)

st.divider()

st.header("МРТ зерттеуін жүктеу")

study_type = st.selectbox(
    "Зерттеу түрін таңдаңыз",
    ["Ми МРТ — зерттеу режимі"]
)

st.write(
    "Толық талдау үшін бір зерттеудің T1, T1c, T2 "
    "және FLAIR сериялары қажет."
)

t1 = st.file_uploader("T1 файлы", type=["nii", "gz"])
t1c = st.file_uploader("T1c файлы", type=["nii", "gz"])
t2 = st.file_uploader("T2 файлы", type=["nii", "gz"])
flair = st.file_uploader("FLAIR файлы", type=["nii", "gz"])

if st.button("AI талдауын бастау", type="primary"):
    if all([t1, t1c, t2, flair]):
        st.info(
            "Барлық файл жүктелді. AI моделін келесі "
            "кезеңде осы бетке қосамыз."
        )
    else:
        st.error("Төрт МРТ файлының бәрін жүктеу қажет.")

st.divider()
st.caption("MedVision KZ | Медициналық AI жобасының прототипі")

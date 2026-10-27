
import streamlit as st
import nibabel as nib
import numpy as np
import tempfile
import os

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
    "Бұл прототип диагноз қоймайды. "
    "Нәтижелер дәрігер қорытындысын алмастырмайды."
)

st.divider()
st.header("МРТ зерттеуін жүктеу")

st.info(
    "Бір зерттеуге тиесілі T1, T1c, T2 және FLAIR "
    "көлемдері қажет. Тек рұқсат етілген, "
    "анонимделген оқу деректерін пайдаланыңыз."
)

t1 = st.file_uploader("T1 файлы", type=["nii", "gz"])
t1c = st.file_uploader("T1c файлы", type=["nii", "gz"])
t2 = st.file_uploader("T2 файлы", type=["nii", "gz"])
flair = st.file_uploader("FLAIR файлы", type=["nii", "gz"])

if st.button("MRI файлдарын тексеру", type="primary"):
    files = {
        "T1": t1,
        "T1c": t1c,
        "T2": t2,
        "FLAIR": flair
    }

    if not all(files.values()):
        st.error("Төрт MRI файлының бәрін жүктеңіз.")
    else:
        results = []
        temp_paths = []

        try:
            for name, uploaded_file in files.items():
                with tempfile.NamedTemporaryFile(
                    suffix=".nii.gz", delete=False
                ) as temp_file:
                    temp_file.write(uploaded_file.getvalue())
                    temp_paths.append(temp_file.name)

                image = nib.load(temp_paths[-1])
                shape = image.shape

                if len(shape) != 3:
                    raise ValueError(
                        f"{name}: 3D MRI көлемі қажет. "
                        f"Алынған өлшем: {shape}"
                    )

                results.append((name, shape))

            shapes = [shape for _, shape in results]

            st.subheader("Тексеру нәтижесі")
            for name, shape in results:
                st.write(f"**{name}:** өлшемі {shape}")

            if len(set(shapes)) == 1:
                st.success(
                    "Төрт файлдың өлшемдері бірдей. "
                    "Бұл бастапқы тексерістен өтті."
                )
                st.info(
                    "Бұл тек файлдарды тексеру. "
                    "AI талдауы әлі орындалған жоқ."
                )
            else:
                st.error(
                    "Файлдардың өлшемдері әртүрлі. "
                    "Оларды бірден модельге беруге болмайды."
                )

        except Exception as error:
            st.error(f"Файлды оқу кезінде қате: {error}")

        finally:
            for path in temp_paths:
                if os.path.exists(path):
                    os.remove(path)

st.divider()
st.caption(
    "MedVision KZ | Зерттеу және білім беру прототипі"
)

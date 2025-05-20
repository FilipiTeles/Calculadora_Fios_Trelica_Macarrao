import streamlit as st
import math

st.set_page_config(page_title="Calculadora de Fios de Espaguete", layout="centered")
st.title("🧮 Calculadora de Fios de Espaguete por Barra")

# Constantes
tensao_adm_tracao = 4.267  # N por fio (tensão admissível)
raio_giracao = 0.9  # mm
denominador_compressao = 27906 * (raio_giracao ** 4)

# Histórico
if "historico" not in st.session_state:
    st.session_state.historico = []

# Entrada do usuário
tipo = st.radio("Tipo de esforço", ["Tração", "Compressão"])
forca = st.number_input("Força interna na barra (em N):", min_value=0.01)

comprimento_mm = None
if tipo == "Compressão":
    comprimento_mm = st.number_input("Comprimento da barra (em mm):", min_value=0.01)

if st.button("Calcular"):
    if tipo == "Tração":
        n_fios = math.ceil(forca / tensao_adm_tracao)
    else:
        base = (forca * (comprimento_mm ** 2)) / denominador_compressao
        n_fios = math.ceil(math.sqrt(math.ceil(base)))

    st.success(f"✅ Quantidade mínima de fios: **{n_fios}** fio(s)")

    # Armazenar no histórico
    st.session_state.historico.append({
        "Tipo": tipo,
        "Força (N)": round(forca, 2),
        "Comprimento (mm)": round(comprimento_mm, 1) if comprimento_mm else "-",
        "Fios": n_fios
    })

# Mostrar histórico
if st.session_state.historico:
    st.subheader("📊 Histórico de Cálculos")
    st.table(st.session_state.historico)







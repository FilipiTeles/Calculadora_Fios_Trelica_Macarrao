import streamlit as st
import math

st.title("Calculadora de Fios de Espaguete por Barra")

# Constantes
tensao_adm_tracao = 4.267  # kgf por fio
raio_mm = 0.45
denominador_compressao = 279056 * (raio_mm ** 4)
g = 9.80665  # N/kgf

# Histórico
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Entradas
tipo = st.radio("Tipo de esforço:", ["Tração", "Compressão"])
forca_N = st.number_input("Força interna na barra (N):", min_value=0.01)

if tipo == "Compressão":
    comprimento_cm = st.number_input("Comprimento da barra (cm):", min_value=0.01)
else:
    comprimento_cm = None

if st.button("Calcular"):
    if tipo == "Tração":
        forca_kgf = forca_N / g
        n_fios = math.ceil(forca_kgf / tensao_adm_tracao)
    else:
        numerador = forca_N * (comprimento_cm ** 2)
        n_fios = math.ceil(math.sqrt(numerador / denominador_compressao))

    st.success(f"Quantidade mínima de fios: {n_fios} fio(s)")

    st.session_state.historico.append({
        "Tipo": tipo,
        "Força (N)": forca_N,
        "Comprimento (cm)": comprimento_cm if comprimento_cm else "-",
        "Fios": n_fios
    })

# Mostrar histórico
if st.session_state.historico:
    st.subheader("Histórico")
    st.table(st.session_state.historico)


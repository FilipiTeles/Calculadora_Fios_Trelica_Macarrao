import streamlit as st
import math

st.set_page_config(page_title="Calculadora de Fios de Espaguete", layout="centered")
st.title("🧮 Calculadora de Fios de Espaguete por Barra")

# ======================
# INFORMAÇÕES INICIAIS
# ======================

st.markdown("### 📘 Fórmulas Utilizadas")

st.markdown("""
**1. Para barras em tração:**
> \\[
n_{fios} = \\left\\lceil \\frac{F}{\\sigma_{adm}} \\right\\rceil
\\]
- Onde:
  - \\( F \\): força na barra (em Newtons)
  - \\( \\sigma_{adm} = 4{,}267 \\): resistência à tração por fio (em N)

**2. Para barras em compressão com flambagem:**
> \\[
n_{fios} = \\left\\lceil \\sqrt{\\left\\lceil \\frac{F \\cdot L^2}{27906 \\cdot r^4} \\right\\rceil} \\right\\rceil
\\]
- Onde:
  - \\( F \\): força na barra (N)
  - \\( L \\): comprimento da barra (em mm)
  - \\( r = 0{,}9 \\ mm \\): raio de giração empírico para espaguete
  - \\( 27906 \\): constante empírica para flambagem
""")

st.markdown("### ⚙️ Constantes Utilizadas")
st.markdown("""
- **Tensão admissível à tração**: 4.267 N por fio
- **Raio de giração (compressão)**: 0.9 mm
- **Constante de flambagem**: 27906
""")

# ======================
# CÁLCULOS
# ======================

# Constantes
tensao_adm_tracao = 4.267  # N por fio
raio_giracao = 0.9  # mm
denominador_compressao = 27906 * (raio_giracao ** 4)

# Histórico
if "historico" not in st.session_state:
    st.session_state.historico = []

st.markdown("## 🔢 Calculadora")

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

# ======================
# HISTÓRICO
# ======================

if st.session_state.historico:
    st.markdown("## 📊 Histórico de Cálculos")
    st.table(st.session_state.historico)

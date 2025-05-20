import streamlit as st
import math

st.set_page_config(page_title="Calculadora de Fios de Espaguete", layout="centered")
st.title("🧮 Calculadora de Fios de Espaguete por Barra em Treliça")
st.title("🍝 Barilla N7")

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

# Histórico de cálculos
if st.session_state.historico:
    st.markdown("## 📊 Histórico de Cálculos")
    st.table(st.session_state.historico)

# Explicações finais
st.markdown("---")
st.markdown("## ℹ️ Fórmulas Utilizadas e Constantes")
st.markdown(
    """
### 👉 Para barras em **tração**:
A quantidade de fios é calculada dividindo a força aplicada pela resistência de um único fio.

**Fórmula:**
número de fios = força (em N) ÷ 4.267

---

### 👉 Para barras em **compressão**:
A quantidade de fios considera o risco de flambagem (instabilidade que ocorre quando uma barra comprida é comprimida). A fórmula leva em conta a força, o comprimento da barra e uma constante empírica.

**Fórmula:**
número de fios = raiz quadrada de [(força × comprimento²) ÷ (27906 × (0.9)^4)]

---

### 📌 Constantes Utilizadas:
- Resistência à tração de 1 fio: 4.267 N
- Raio de giração estimado do fio: 0.9 mm
- Constante de flambagem (compressão): 27906
- Comprimento da barra: deve ser informado em milímetros
- Todos os cálculos usam arredondamento para cima para garantir segurança.
"""
)

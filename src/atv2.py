
import numpy as np
import streamlit as st

st.title("Atividade 2 — Bandeira dos Estados Unidos")

def ampliar(imagem, escala=20):
    return np.repeat(
        np.repeat(imagem, escala, axis=0),
        escala,
        axis=1
    )

# Criar a bandeira em pixels
bandeira = np.zeros((13, 26, 3), dtype=np.uint8)

# Cores em RGB
vermelho = (178, 34, 52)
branco = (255, 255, 255)
azul = (60, 59, 110)

# Fundo branco
bandeira[:] = branco

# Sete faixas vermelhas
for linha in range(0, 13, 2):
    bandeira[linha:linha + 1, :] = vermelho

# Retângulo azul no canto superior esquerdo
bandeira[0:7, 0:11] = azul

# Exibir a bandeira ampliada
st.image(ampliar(bandeira), caption="Bandeira dos Estados Unidos")

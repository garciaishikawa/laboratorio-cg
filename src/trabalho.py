
import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

img = np.array(Image.open("imagens/foto_pessoal.jpg").convert("RGB"))


# 4. Tons de cinza
st.header("4. Tons de cinza")

col1, col2 = st.columns(2)

cinza_media = np.mean(img, axis=2).astype(np.uint8)

with col1:
    st.subheader("Média simples")
    st.image(cinza_media, caption="Média dos canais RGB", use_container_width=True)

with col2:
    st.subheader("Média ponderada")

    peso_r = st.slider("Peso R", 0.0, 1.0, 0.30, 0.05)
    peso_g = st.slider("Peso G", 0.0, 1.0, 0.59, 0.05)
    peso_b = st.slider("Peso B", 0.0, 1.0, 0.11, 0.05)

    soma = peso_r + peso_g + peso_b

    if soma > 0:
        cinza_ponderado = (
            img[:, :, 0] * peso_r +
            img[:, :, 1] * peso_g +
            img[:, :, 2] * peso_b
        ) / soma
    else:
        cinza_ponderado = cinza_media

    cinza_ponderado = cinza_ponderado.astype(np.uint8)

    st.image(
        cinza_ponderado,
        caption="Média ponderada",
        use_container_width=True
    )


# 8. Negativo
st.header("8. Negativo")

negativo = 255 - img

st.image(negativo, caption="Imagem negativa", use_container_width=True)


# 11. Espelhamento
st.header("11. Espelhamento")

col1, col2 = st.columns(2)

with col1:
    espelhada_horizontal = np.fliplr(img)
    st.image(
        espelhada_horizontal,
        caption="Espelhamento horizontal",
        use_container_width=True
    )

with col2:
    espelhada_vertical = np.flipud(img)
    st.image(
        espelhada_vertical,
        caption="Espelhamento vertical",
        use_container_width=True
    )


# 12. Simetria
st.header("12. Simetria")

simetria = img.copy()
largura = img.shape[1]
metade = largura // 2

simetria[:, metade:] = np.fliplr(img[:, :largura - metade])

st.image(
    simetria,
    caption="Metade direita espelhada",
    use_container_width=True
)


# 19. Moldura
st.header("19. Moldura")

altura = img.shape[0]
largura = img.shape[1]
max_espessura = max(1, min(altura, largura) // 2)

espessura = st.slider(
    "Espessura da moldura",
    1,
    max_espessura,
    min(20, max_espessura)
)

col1, col2, col3 = st.columns(3)

with col1:
    vermelho = st.slider("Vermelho (R)", 0, 255, 255)

with col2:
    verde = st.slider("Verde (G)", 0, 255, 0)

with col3:
    azul = st.slider("Azul (B)", 0, 255, 0)

moldura = img.copy()
cor = [vermelho, verde, azul]

moldura[:espessura, :] = cor
moldura[-espessura:, :] = cor
moldura[:, :espessura] = cor
moldura[:, -espessura:] = cor

st.image(
    moldura,
    caption="Imagem com moldura",
    use_container_width=True
)

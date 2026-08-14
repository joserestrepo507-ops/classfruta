import streamlit as st
import math

st.title("🍎 ¿Qué fruta es más parecida?")

st.write("Introduce las características de una fruta.")

# Datos de la fruta que queremos analizar
peso = st.number_input("Peso (gramos)", value=180)
diametro = st.number_input("Diámetro (cm)", value=7.0)
dulzor = st.number_input("Dulzor (0 - 10)", value=8.0)

# Convertimos los datos en un vector
fruta_usuario = [peso, diametro, dulzor]

st.write("Vector de tu fruta:", fruta_usuario)

# Frutas conocidas
manzana = [170, 7.0, 7]
banano = [120, 5.0, 9]
naranja = [200, 8.0, 6]
pera = [178, 6.5, 6]

# Calculamos las distancias

distancia_manzana = math.sqrt(
    (fruta_usuario[0] - manzana[0])**2 +
    (fruta_usuario[1] - manzana[1])**2 +
    (fruta_usuario[2] - manzana[2])**2 
)

distancia_banano = math.sqrt(
    (fruta_usuario[0] - banano[0])**2 +
    (fruta_usuario[1] - banano[1])**2 +
    (fruta_usuario[2] - banano[2])**2
)

distancia_naranja = math.sqrt(
    (fruta_usuario[0] - naranja[0])**2 +
    (fruta_usuario[1] - naranja[1])**2 +
    (fruta_usuario[2] - naranja[2])**2
)

distancia_pera = math.sqrt(
    (fruta_usuario[0] - pera[0])**2 +
    (fruta_usuario[1] - pera[1])**2 +
    (fruta_usuario[2] - pera[2])**2
)

# Mostramos las distancias
st.subheader("Distancias")

st.write("🍎 Manzana:", distancia_manzana)
st.write("🍌 Banano:", distancia_banano)
st.write("🍊 Naranja:", distancia_naranja)
st.write("🍐 Pera: ", distancia_pera)

# Buscamos la distancia menor
distancias = {
    "🍎 Manzana": distancia_manzana,
    "🍌 Banano": distancia_banano,
    "🍊 Naranja": distancia_naranja,
    "🍐 Pera ": distancia_pera
}

# Mapeo de cada fruta a su imagen 
imagenes = {
    "🍎 Manzana": "manzana.jpg",
    "🍌 Banano": "banano.jpg",
    "🍊 Naranja": "naranja.jpg",
    "🍐 Pera ": "pera.jpg"
}

fruta_mas_parecida = min(distancias, key=distancias.get)

st.subheader("Resultado")
st.success(f"La fruta más parecida es: {fruta_mas_parecida}")

# Descripciones de cada fruta
descripciones = {
    "🍎 Manzana": "Fruta crujiente y jugosa, de sabor entre dulce y ácido. Rica en fibra y vitamina C.",
    "🍌 Banano": "Fruta suave y muy dulce, excelente fuente de potasio y energía rápida.",
    "🍊 Naranja": "Cítrico jugoso y refrescante, conocido por su alto contenido de vitamina C.",
    "🍐 Pera ": "Fruta suave y dulce, con un toque ligeramente ácido y alto contenido de fibra."
}

# Mostramos la imagen correspondiente
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image(imagenes[fruta_mas_parecida], caption=fruta_mas_parecida, width=250)

# Tarjeta con nombre y descripción
st.markdown(
    f"""
    <div style="
        background-color: #f0f7f0;
        border: 1px solid #cde3cd;
        border-radius: 12px;
        padding: 20px 24px;
        margin-top: 16px;
        text-align: center;
    ">
        <h3 style="margin: 0 0 8px 0; color: #1e4620;">{fruta_mas_parecida.strip()}</h3>
        <p style="margin: 0; color: #33513a; font-size: 15px; line-height: 1.5;">
            {descripciones[fruta_mas_parecida]}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


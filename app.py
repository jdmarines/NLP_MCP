import streamlit as st
import google.generativeai as genai

# Importar las funciones de nuestros agentes
from agents.writer_agent import generate_draft
from agents.editor_agent import review_and_finalize

# --- Configuración de la página y API Key ---
st.set_page_config(
    page_title="Agentes MCP en Acción",
    page_icon="",
    layout="wide"
)

st.title("Demostración de Comunicación entre Agentes (MCP)")

# Configurar la API key de Gemini (igual que antes)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("La API Key de Gemini no ha sido configurada en los secretos de Streamlit.")
    st.stop()

# --- Interfaz de Usuario ---
st.header("Paso 1: Iniciar la Tarea")
user_prompt = st.text_input("Escribe el tema para el texto:", "La importancia de la IA en la educación")

if st.button("Ejecutar Flujo de Agentes"):
    if not user_prompt:
        st.warning("Por favor, introduce un tema.")
    else:
        with st.spinner("Agente 1 (Escritor) está trabajando..."):
            # --- Llamada al Agente 1 ---
            writer_context = generate_draft(user_prompt)

        if writer_context["status"] == "error":
            st.error(f"Error en el Agente Escritor: {writer_context['message']}")
        else:
            st.subheader("Contexto MCP entregado por el Agente 1")
            st.text_area("Borrador Inicial:", value=writer_context['draft_text'], height=150, disabled=True)
            st.json(writer_context) # Muestra el paquete MCP completo

            st.markdown("---")
            
            with st.spinner("Agente 2 (Editor) está revisando el borrador..."):
                # --- Llamada al Agente 2, pasando el contexto del Agente 1 ---
                final_context = review_and_finalize(writer_context)

            if final_context["status"] == "error":
                st.error(f"Error en el Agente Editor: {final_context['message']}")
            else:
                st.subheader("Tarea Completada: Texto Final del Agente 2")
                st.text_area("Texto Final:", value=final_context['final_text'], height=150, disabled=True)
                
                st.subheader("Contexto MCP Final")
                st.json(final_context) # Muestra el paquete MCP final y actualizado

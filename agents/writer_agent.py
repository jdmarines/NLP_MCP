import google.generativeai as genai

def generate_draft(user_prompt: str) -> dict:
    """
    Agente 1: Escritor Creativo.
    Genera un borrador inicial y lo empaqueta en un objeto de contexto (MCP).
    """
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # Prompt específico para este agente
    prompt_for_writer = f"""
    Eres un escritor creativo. Escribe un párrafo sobre el siguiente tema, 
    usando un tono entusiasta y accesible. No te preocupes por la perfección, 
    es solo un primer borrador.

    Tema: "{user_prompt}"
    """
    
    try:
        response = model.generate_content(prompt_for_writer)
        draft_text = response.text
        
        # Crear el "paquete MCP" para pasar al siguiente agente
        mcp_context = {
            "status": "draft_generated",
            "original_prompt": user_prompt,
            "draft_text": draft_text,
            "history": ["Agent 1 (Writer) completed task."]
        }
        return mcp_context
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

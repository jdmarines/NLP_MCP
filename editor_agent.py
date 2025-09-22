import google.generativeai as genai

def review_and_finalize(mcp_context: dict) -> dict:
    """
    Agente 2: Editor y Publicador.
    Recibe el contexto del Agente 1, mejora el texto y lo finaliza.
    """
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # Extraer datos del contexto MCP
    draft = mcp_context.get("draft_text", "")
    
    # Prompt específico para este agente, usando la salida del anterior
    prompt_for_editor = f"""
    Eres un editor profesional. Revisa y mejora el siguiente borrador para que 
    sea más formal, claro y conciso. Corrige cualquier error gramatical.

    Borrador a revisar:
    ---
    {draft}
    ---
    """
    
    try:
        response = model.generate_content(prompt_for_editor)
        final_text = response.text
        
        # Actualizar el paquete MCP con el resultado final
        mcp_context["status"] = "review_completed"
        mcp_context["final_text"] = final_text
        mcp_context["history"].append("Agent 2 (Editor) completed task.")
        
        return mcp_context

    except Exception as e:
        mcp_context["status"] = "error"
        mcp_context["message"] = str(e)
        return mcp_context

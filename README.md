
##  Descripción  
Este proyecto implementa un **sistema multiagente** basado en el **Model Context Protocol (MCP)**, con el objetivo de demostrar cómo múltiples agentes de IA pueden **colaborar secuencialmente** para resolver una tarea compleja.  

El núcleo del sistema está compuesto por:  
- **Agente 1 – Escritor Creativo**: genera un borrador a partir de una idea inicial.  
- **Agente 2 – Editor Profesional**: refina y corrige el borrador para elevar su calidad.  

La comunicación entre agentes se simula mediante un **paquete MCP** (diccionario en Python) que transporta tanto los datos como el contexto (estado del flujo, historial y metadatos).  




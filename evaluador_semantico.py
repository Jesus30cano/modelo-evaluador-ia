import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Cargar modelo al inicio (se mantiene en memoria dentro del contenedor)
modelo = SentenceTransformer("all-MiniLM-L6-v2")

def evaluar_respuesta(csv_path, pregunta, respuesta_usuario):
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        return {"score": 0.0, "estado": f"Error leyendo CSV: {e}", "mejor_respuesta": ""}

    # Filtrar por pregunta
    fila = df[df["pregunta"].str.strip().str.lower() == pregunta.strip().lower()]

    if fila.empty:
        return {"score": 0.0, "estado": "Pregunta no encontrada", "mejor_respuesta": ""}

    # Obtener respuestas correctas
    respuestas_validas = [
        str(fila[col].values[0]) for col in fila.columns if col.startswith("respuesta") and pd.notna(fila[col].values[0])
    ]

    if not respuestas_validas:
        return {"score": 0.0, "estado": "Sin respuestas válidas", "mejor_respuesta": ""}

    # Calcular similitud
    emb_usuario = modelo.encode(respuesta_usuario, convert_to_tensor=True)
    emb_validas = modelo.encode(respuestas_validas, convert_to_tensor=True)
    similitudes = util.cos_sim(emb_usuario, emb_validas)[0]

    mejor_idx = similitudes.argmax().item()
    mejor_score = similitudes[mejor_idx].item()

    if mejor_score >= 0.8:
        estado = "Correcto"
    elif mejor_score >= 0.5:
        estado = "Parcial"
    else:
        estado = "Incorrecto"

    return {
        "score": round(mejor_score, 2),
        "estado": estado,
        "mejor_respuesta": respuestas_validas[mejor_idx]
    }

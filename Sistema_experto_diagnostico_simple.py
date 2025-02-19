def diagnostico(sintomas):
    """Determina un diagnóstico basado en los síntomas ingresados."""
    if "fiebre" in sintomas and "tos" in sintomas and "dificultad para respirar" in sintomas:
        return "Posible infección respiratoria. Se recomienda consultar a un médico."
    elif "dolor de cabeza" in sintomas and "fiebre" in sintomas and "dolor muscular" in sintomas:
        return "Posible gripe. Descanso e hidratación son recomendados."
    elif "dolor abdominal" in sintomas and "náuseas" in sintomas and "vómitos" in sintomas:
        return "Posible intoxicación alimentaria. Beba líquidos y busque asistencia médica si persisten los síntomas."
    elif "estornudos" in sintomas and "congestión nasal" in sintomas and "picazón en los ojos" in sintomas:
        return "Posible alergia. Evite los alérgenos y consulte a un especialista si es necesario."
    else:
        return "Síntomas no reconocidos en la base de datos. Consulte a un profesional de la salud."

# Solicitar síntomas al usuario
if __name__ == "__main__":
    print("Ingrese sus síntomas separados por comas (ejemplo: fiebre, tos, dolor de cabeza)")
    entrada = input("Síntomas: ").lower()
    sintomas_usuario = [s.strip() for s in entrada.split(",")]
    
    resultado = diagnostico(sintomas_usuario)
    print(f"Diagnóstico: {resultado}")
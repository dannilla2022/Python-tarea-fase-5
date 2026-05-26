
def evaluar_jornada_laboral(matriz_horas):
    
    UMBRAL_HORAS = 40
    
    print(" REPORTE DE HORAS SEMANALES ")
    
    for fila in matriz_horas:
        nombre = fila[0]
        horas_semanales = sum(fila[1:])
        if horas_semanales > UMBRAL_HORAS:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
        print(f"Empleado: {nombre} | Total Horas: {horas_semanales} | Condición: {clasificacion}")

registro_horas = [
    ["Diana Delgadillo", 8, 8, 9, 8, 8],       # Total: 41 horas (Sobretiempo)
    ["Paula Perez", 8, 7, 8, 6, 8],             # Total: 37 horas (Estándar)
    ["Maria Lopez", 9, 9, 9, 9, 8],              # Total: 44 horas (Sobretiempo)
    ["Juan Torres", 8, 8, 8, 8, 8]                 # Total: 40 horas (Estándar)
]
evaluar_jornada_laboral(registro_horas)
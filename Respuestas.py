import re
import funciones

def obtener_info(pregunta):
    pregunta = pregunta.lower()

    if re.search(r"\b(sistema operativo|os|sistema|operativo|plataforma)\b", pregunta):
        return funciones.obtener_sistema()

    elif re.search(r"\b(procesador|cpu|microprocesador|unidad central|unidad de procesamiento)\b", pregunta):
        return funciones.obtener_procesador()

    elif re.search(r"\b(ram|memoria|memoria ram|memoria principal|random access memory)\b", pregunta):
        return funciones.obtener_ram()

    elif re.search(r"\b(espacio|disco|almacenamiento|capacidad|espacio en disco)\b", pregunta):
        return funciones.obtener_disco()

    elif re.search(r"\b(bateria|carga|batería de la laptop|nivel de batería|estado de batería)\b", pregunta):
        return funciones.obtener_bateria()

    elif re.search(r"\b(temperatura.*cpu|calor.*cpu|temp.*cpu|temperatura del procesador|calor del procesador|temperatura)\b", pregunta):
        return funciones.obtener_temperatura_cpu()

    elif re.search(r"\b(drivers|controladores|módulos|drivers del sistema|controladores del sistema)\b", pregunta):
        return funciones.obtener_drivers()

    elif re.search(r"\b(bios|firmware|bios de la laptop|información de la bios)\b", pregunta):
        return funciones.obtener_bios()

    elif re.search(r"\b(ayuda|ayúdame|información|info|ayuda por favor)\b", pregunta):
        return (
            "Puedes preguntar sobre: 'sistema operativo', 'procesador', 'RAM',\n"
            "'disco', 'batería', 'temperatura CPU', 'drivers', 'bios'"
        )

    return (
        "No entiendo esa pregunta.\n"
        "Puedes preguntar sobre: 'sistema operativo', 'procesador', 'RAM',\n"
        "'disco', 'batería', 'temperatura CPU', 'drivers', 'bios'"
    )

def chatbot():
    print("Hola, soy CMR, tu chatbot de confianza. ¿En qué puedo ayudarte?")
    print("Si deseas salir de la conversación, escribe 'salir'.")
    
    while True:
        pregunta = input("Dame tu pregunta: ")
        if "salir" in pregunta.lower():
            print("¡Hasta luego!")
            break
        respuesta = obtener_info(pregunta)
        print(respuesta)
        
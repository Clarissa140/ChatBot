import re
import funciones

def obtener_info(pregunta):
    pregunta = pregunta.lower()

    if re.search(r"sistema operativo|os|sistema|operativo|plataforma", pregunta):
        return funciones.obtener_sistema()

    elif re.search(r"procesador|cpu|microprocesador|unidad central|unidad de procesamiento", pregunta):
        return funciones.obtener_procesador()

    elif re.search(r"ram|memoria|memoria ram|memoria principal|random access memory", pregunta):
        return funciones.obtener_ram()

    elif re.search(r"espacio|disco|almacenamiento|capacidad|espacio en disco", pregunta):
        return funciones.obtener_disco()

    elif re.search(r"bateria|carga|batería de la laptop|nivel de batería|estado de batería", pregunta):
        return funciones.obtener_bateria()

    elif re.search(r"temperatura.*cpu|calor.*cpu|temp.*cpu|temperatura del procesador|calor del procesador|temperatura", pregunta):
        return funciones.obtener_temperatura_cpu()

    elif re.search(r"drivers|controladores|módulos|drivers del sistema|controladores del sistema", pregunta):
        return funciones.obtener_drivers()

    return (
        "No entiendo esa pregunta.\n"
        "Puedes preguntar sobre: 'sistema operativo', 'procesador', 'RAM',\n"
        "'disco', 'batería', 'temperatura CPU', 'drivers'"
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
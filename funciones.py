import platform
import psutil
import nltk
import re
import subprocess

nltk.download("punkt")

def obtener_sistema():
    return f"Tu laptop usa {platform.system()} {platform.version()}."

def obtener_procesador():
    try:
        resultado = subprocess.check_output("lshw -C cpu", shell=True, text=True)
        for linea in resultado.splitlines():
            if "producto:" in linea:
                modelo = linea.split(":", 1)[1].strip()
                return f"Tu laptop tiene un procesador {modelo}."
        return "No se encontró información detallada del procesador."
    except Exception as e:
        return f"No se pudo obtener la información del procesador: {e}"

def obtener_ram():
    try:
        resultado = subprocess.check_output("grep MemTotal /proc/meminfo", shell=True, text=True)
        partes = resultado.split()
        mem_kb = int(partes[1])
        mem_gb = round(mem_kb / (1024 ** 2), 1)
        return f"Tu laptop tiene {mem_gb} GB de memoria RAM."
    except Exception as e:
        return f"No se pudo obtener la información de la RAM: {e}"

def obtener_disco():
    disco = round(psutil.disk_usage('/').total / (1024**3), 1)
    return f"Tu laptop tiene un disco de {disco} GB de capacidad."

def obtener_bateria():
    bateria = psutil.sensors_battery()
    if bateria:
        return f"La batería está al {bateria.percent}% de carga."
    else:
        return "No se encontró información de la batería."

def obtener_temperatura_cpu():
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for sensor, entries in temps.items():
                if entries:
                    temp = round(entries[0].current, 1)
                    return f"La temperatura actual de la CPU es de {temp}°C (obtenida vía psutil)."
        result = subprocess.check_output("sensors", shell=True, text=True)
        for line in result.splitlines():
            if re.search(r"temp\d+:\s+\+?([\d\.]+)", line):
                return f"Temperatura (desde 'sensors'): {line.strip()}"
    except Exception as e:
        return f"Error al obtener la temperatura: {e}"
    return "No se encontró información de temperatura en tu sistema."

def obtener_drivers():
    try:
        result = subprocess.check_output("lsmod", shell=True, text=True)
        lines = result.strip().splitlines()
        count = len(lines) - 1  
        return f"Tu sistema tiene {count} drivers cargados."
    except Exception:
        return "No se pudo obtener la información de los drivers."

def obtener_bios():
    try:
        salida = subprocess.check_output("sudo dmidecode", shell=True, text=True)
        
        # Buscar el bloque "BIOS Information"
        bloque_bios = re.search(r"BIOS Information(.*?)(\n\n|\Z)", salida, re.DOTALL)
        if not bloque_bios:
            return "No se encontró información de la BIOS."
        
        info_bios = bloque_bios.group(1)
        datos_importantes = []
        
        # Extraer líneas con Vendor, Version y Release Date
        for linea in info_bios.splitlines():
            if re.search(r"(Vendor|Version|Release Date)", linea, re.IGNORECASE):
                datos_importantes.append(linea.strip())
        
        if datos_importantes:
            return "\n".join(datos_importantes)
        else:
            return "No se encontraron datos importantes de la BIOS."
        
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener la información de la BIOS: {e}")
        return None

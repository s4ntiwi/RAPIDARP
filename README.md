# RAPIDARP
Escaner rápido de la red local
# RapidARP

**RapidARP** es una herramienta en Python que utiliza `arp-scan` para escanear la red local y detectar los dispositivos activos. El script obtiene las direcciones IP de los dispositivos conectados a la misma red y las guarda en un archivo de texto, que luego se abre en `nano` para su visualización.

## 🚀 Características
- Escanea toda la red local utilizando `arp-scan`.
- Detecta dispositivos activos en la red.
- Guarda las IPs activas en un archivo de texto `active_hosts.txt`.
- Abre el archivo con `nano` para visualización inmediata.

## 📌 Requisitos
Antes de ejecutar el script, asegúrate de tener instalados:
- **Python 3.x**
- **arp-scan** (para escanear la red local)

### Instalación en Linux
1. Instala `arp-scan`:
```bash
sudo apt install arp-scan
```
2. Instala Python y las dependencias necesarias:
```bash
sudo apt install python3
```

## 🛠 Instalación y Uso
1. Clona este repositorio:
```bash
git clone https://github.com/tu_usuario/rapidarp.git
cd rapidarp
```
2. Ejecuta el script con permisos de superusuario para que `arp-scan` funcione correctamente:
```bash
sudo python3 scanner.py
```
3. El script escaneará la red local, detectará los dispositivos activos y guardará las IPs encontradas en `active_hosts.txt`.
4. Al final, abrirá el archivo con `nano` para que puedas verlo de inmediato.

## 📌 Ejemplo de Uso
```
Escaneando la red local con arp-scan...
Host activo encontrado: 192.168.1.1
Host activo encontrado: 192.168.1.3
Host activo encontrado: 192.168.1.4

Resultados guardados en active_hosts.txt
```

## ⚠️ Disclaimer
Este script está destinado **solo para fines educativos o con autorización**. No me hago responsable de su uso indebido.

---
✍️ Desarrollado por SANTI

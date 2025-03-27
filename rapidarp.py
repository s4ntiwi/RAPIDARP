import os
import subprocess

def scan_local_network():
    print("Escaneando la red local con arp-scan...")
    try:
        output = subprocess.check_output("sudo arp-scan --localnet", shell=True, stderr=subprocess.DEVNULL).decode()
    except subprocess.CalledProcessError:
        print("Error al ejecutar arp-scan. Asegúrate de tenerlo instalado y permisos suficientes.")
        return []
    
    active_hosts = []
    for line in output.split('\n'):
        parts = line.split('\t')
        if len(parts) > 1 and "." in parts[0]:  # Filtra líneas con direcciones IP
            active_hosts.append(parts[0])
            print(f"Host activo encontrado: {parts[0]}")
    
    return active_hosts

def save_results(hosts):
    with open("active_hosts.txt", "w") as file:
        for host in hosts:
            file.write(host + "\n")
    print("\nResultados guardados en active_hosts.txt")
    os.system("nano active_hosts.txt")

def main():
    active_hosts = scan_local_network()
    if active_hosts:
        save_results(active_hosts)
    else:
        print("No se encontraron hosts activos.")

if __name__ == "__main__":
    main()

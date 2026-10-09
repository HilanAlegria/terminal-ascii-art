# img2ascii-cli

Herramienta de línea de comandos (CLI) ligera para Linux que convierte imágenes (PNG, JPG, WEBP) en arte ASCII, con soporte para colores ANSI TrueColor de 24 bits, ajuste de densidad de caracteres y exportación de archivos.

---

## Características

- Conversión en tiempo real con proporción de aspecto adaptada a fuentes monoespaciadas.
- Soporte para color real (TrueColor de 24 bits).
- Dos rampas de caracteres: básica (10 niveles) y detallada (70 niveles).
- Inversión de brillo para terminales con fondos claros.
- Exportación directa a archivos de texto plano o visualización en la terminal.

---

## Requisitos previos

- Python 3.10 o superior
- `pip`
- Terminal compatible con ANSI / TrueColor (Kitty, Alacritty, GNOME Terminal, Konsole, etc.)

---

##Capturas de como se ve

<img width="1920" height="1036" alt="Screenshot_20261008_113000" src="https://github.com/user-attachments/assets/005049ad-674e-48d3-9dbb-0c6a566c0f3a" />
<img width="1920" height="1036" alt="Screenshot_20261008_112942" src="https://github.com/user-attachments/assets/c46c50c6-5c28-4d6c-a014-70a70003e0e1" />
<img width="1920" height="1036" alt="Screenshot_20261008_113035" src="https://github.com/user-attachments/assets/c9de4c3e-f7cd-4194-9abf-95c9a1c7248b" />
<img width="1920" height="1036" alt="Screenshot_20261008_113025" src="https://github.com/user-attachments/assets/20b006e5-9196-4071-a1e6-9ffe9d2a5f9b" />
<img width="1920" height="1036" alt="Screenshot_20261008_113012" src="https://github.com/user-attachments/assets/d043f264-e17e-4ea1-8259-5a9511d580b6" />

---

## Instalación

### Método 1: Instalación rápida (Recomendado)

Clona el repositorio y ejecuta el script de instalación:

```bash
git clone [https://github.com/TU_USUARIO/img2ascii-cli.git](https://github.com/TU_USUARIO/img2ascii-cli.git)
cd img2ascii-cli
chmod +x install.sh
./install.sh

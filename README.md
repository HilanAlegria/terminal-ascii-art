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

le agradezco a Jose Molina por la idea y poder hacer esto para linux. :D

---

## Instalación

### Método 1: Instalación rápida (Recomendado)

Clona el repositorio y ejecuta el script de instalación:

```bash
git clone [https://github.com/TU_USUARIO/img2ascii-cli.git](https://github.com/TU_USUARIO/img2ascii-cli.git)
cd img2ascii-cli
chmod +x install.sh
./install.sh

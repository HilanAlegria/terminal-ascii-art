#!/usr/bin/env bash
set -e

echo "Instalando dependencias..."
pip3 install -r requirements.txt --break-system-packages

echo "Instalando binario en ~/.local/bin/img2ascii..."
mkdir -p ~/.local/bin
cp img2ascii.py ~/.local/bin/img2ascii
chmod +x ~/.local/bin/img2ascii

echo "Listo. Puedes ejecutar 'img2ascii ruta/imagen.png' desde cualquier terminal."
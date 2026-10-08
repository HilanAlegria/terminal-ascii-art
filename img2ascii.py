#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from PIL import Image

ASCII_CHARS_DETAILED = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ASCII_CHARS_SIMPLE = " .:-=+*#%@"
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
RESET_ANSI = "\033[0m"

def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.52)
    return image.resize((new_width, max(1, new_height)))

def select_image_interactively(folder_path="."):
    path = Path(folder_path).expanduser().resolve()

    if not path.exists() or not path.is_dir():
        sys.exit(f"Error: La ruta '{folder_path}' no es un directorio valido.")

    images = sorted([
        f for f in path.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ])

    if not images:
        sys.exit(f"No se encontraron imagenes compatibles en: {path}")

    print(f"\nImagenes encontradas en {path}:")
    for idx, img in enumerate(images, start=1):
        print(f"  [{idx}] {img.name}")

    while True:
        try:
            choice = input(f"\nSelecciona un numero (1-{len(images)}) o 'q' para salir: ").strip()
            if choice.lower() == 'q':
                sys.exit(0)
            selected_idx = int(choice)
            if 1 <= selected_idx <= len(images):
                return str(images[selected_idx - 1])
            print("Numero fuera de rango.")
        except ValueError:
            print("Entrada no valida. Ingresa un numero.")

def convert_to_ascii(image_path, width=100, colored=False, invert=False, detailed=False):
    try:
        img = Image.open(image_path)
    except Exception as e:
        sys.exit(f"Error al abrir la imagen: {e}")

    char_set = ASCII_CHARS_DETAILED if detailed else ASCII_CHARS_SIMPLE
    if invert:
        char_set = char_set[::-1]

    img = img.convert("RGBA")
    img_resized = resize_image(img, width)

    grayscale = img_resized.convert("L")
    gray_pixels = list(grayscale.getdata())
    color_pixels = list(img_resized.getdata())

    ascii_str = []
    num_chars = len(char_set)
    img_w, _ = img_resized.size

    for i, (gray, (r, g, b, a)) in enumerate(zip(gray_pixels, color_pixels)):
        if a < 128:
            ascii_str.append(" ")
        else:
            char_idx = int((gray / 255) * (num_chars - 1))
            char = char_set[char_idx]
            if colored:
                ascii_str.append(f"{rgb_to_ansi(r, g, b)}{char}")
            else:
                ascii_str.append(char)

        if (i + 1) % img_w == 0:
            if colored:
                ascii_str.append(RESET_ANSI)
            ascii_str.append("\n")

    return "".join(ascii_str)

def main():
    parser = argparse.ArgumentParser(
        description="Convierte imagenes a arte ASCII para terminales Linux."
    )
    parser.add_argument(
        "image",
        nargs="?",
        default=None,
        help="Ruta de la imagen o carpeta (si se omite, busca en el directorio actual)"
    )
    parser.add_argument("-w", "--width", type=int, default=100, help="Ancho en columnas (por defecto: 100)")
    parser.add_argument("-c", "--color", action="store_true", help="Habilitar colores ANSI TrueColor de 24 bits")
    parser.add_argument("-i", "--invert", action="store_true", help="Invertir rampa de brillo (util para fondos claros)")
    parser.add_argument("-d", "--detailed", action="store_true", help="Usar rampa ampliada de 70 caracteres")
    parser.add_argument("-o", "--output", help="Guardar la salida en un archivo de texto en lugar de imprimirlo")

    args = parser.parse_args()

    target_path = args.image

    if target_path is None or Path(target_path).is_dir():
        folder = target_path if target_path else "."
        target_path = select_image_interactively(folder)

    result = convert_to_ascii(
        target_path,
        width=args.width,
        colored=args.color,
        invert=args.invert,
        detailed=args.detailed
    )

    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"Arte ASCII guardado en: {args.output}")
    else:
        print(result)

if __name__ == "__main__":
    main()
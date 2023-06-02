import shutil
import markdown
from jinja2 import Environment, FileSystemLoader
import os

# Directorios de la estructura del sitio
SITE_DIR = "site"
ASSETS_DIR = os.path.join(SITE_DIR, "assets")
PAGES_DIR = os.path.join(SITE_DIR, "pages")
TEMPLATES_DIR = os.path.join(SITE_DIR, "templates")
MARKDOWNS_DIR = os.path.join(SITE_DIR, "markdowns")

# Eliminar el directorio de destino si existe
if os.path.exists(PAGES_DIR):
    shutil.rmtree(PAGES_DIR)

# Crear directorio de destino
os.makedirs(PAGES_DIR)

# Copiar assets al directorio de páginas
shutil.copytree(ASSETS_DIR, os.path.join(PAGES_DIR, "assets"))

# Configurar el entorno de Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def generar_html_desde_markdown(archivo_md, archivo_html, template_name=None):
    """
    Genera un archivo HTML a partir de un archivo Markdown y un template.

    Args:
        archivo_md (str): Nombre del archivo Markdown.
        archivo_html (str): Nombre del archivo HTML de salida.
        template_name (str, optional): Nombre del template a utilizar. Si no se proporciona,
            se utiliza "base.html" como template por defecto.
    """
    # Leer el contenido del archivo Markdown
    with open(os.path.join(MARKDOWNS_DIR, archivo_md), "r", encoding="utf-8") as f:
        contenido_md = f.read()

    # Convertir el contenido Markdown a HTML
    md = markdown.Markdown(extensions=["toc", "tables", "fenced_code", "codehilite", "md_in_html"])
    contenido_html = md.convert(contenido_md)

    # Renderizar el contenido con el template
    template = env.get_template(template_name) if template_name else env.get_template("base.html")
    contenido_renderizado = template.render(content=contenido_html, toc=md.toc)

    # Escribir el contenido en el archivo HTML
    with open(os.path.join(PAGES_DIR, archivo_html), "w", encoding="utf-8") as f:
        f.write(contenido_renderizado)
        print(f"> Escrito {archivo_html}")

# Generar páginas individuales
pages = [
    {
        "md_file": "index.md",
        "html_file": "index.html",
        "template_name": "base.html"
    },
    # Agrega más páginas aquí
]

# Generar páginas individuales
for page in pages:
    generar_html_desde_markdown(page["md_file"], page["html_file"], page.get("template_name"))

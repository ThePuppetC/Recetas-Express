import os
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
import re

def sanitize_filename(username):
    """Sanitiza username: lowercase, sin espacios, sin acentos"""
    u = username.lower().replace('@', '').replace(' ', '')
    return re.sub(r'[^a-z0-9_-]', '', u)

def process_recipe_image(image, username):
    """Procesa imagen: WebP, múltiples tamaños, naming consistente"""
    img = Image.open(image).convert('RGB')
    aspect = img.width / img.height
    base = sanitize_filename(username)
    
    # Contar imágenes previas del usuario
    from django.db.models import Max
    from .models import Receta
    max_num = Receta.objects.filter(autor__username__iexact=username).aggregate(
        m=Max('imagen_numero'))['m'] or -1
    num = max_num + 1
    filename = f"{base}_{num}.webp"
    
    sizes = {'original': 1920, 'medium': 800, 'thumbnail': 300}
    images = {}
    
    for size_name, max_width in sizes.items():
        new_width = min(int(max_width), img.width)
        new_height = int(new_width / aspect)
        resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        buffer = BytesIO()
        resized.save(buffer, format='WEBP', quality=80)
        images[size_name] = ContentFile(buffer.getvalue(), name=filename)
    
    return images, filename, num

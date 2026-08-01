from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
import os

ALLOWED_MIME = {'image/jpeg', 'image/png', 'image/webp', 'image/gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def validate_image_upload(file: UploadedFile):
    """Valida uploads: MIME, tamaño, extensión"""
    if not file:
        raise ValidationError("No se seleccionó archivo")
    
    if file.size > MAX_FILE_SIZE:
        raise ValidationError(f"Máximo {MAX_FILE_SIZE // (1024*1024)}MB")
    
    mime = file.content_type
    if mime not in ALLOWED_MIME:
        raise ValidationError("Solo JPEG, PNG, GIF, WebP")
    
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in {'.jpg', '.jpeg', '.png', '.gif', '.webp'}:
        raise ValidationError("Extensión no válida")
    
    return file

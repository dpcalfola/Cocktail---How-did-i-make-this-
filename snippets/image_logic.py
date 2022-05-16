from io import BytesIO
from PIL import Image
from django.core.files import File


# Image compression method
def compress_image(image):
    temp_image = Image.open(image).convert('RGB')
    temp_image_io = BytesIO()
    temp_image.save(temp_image_io, 'jpeg', quality=80)
    new_image = File(temp_image_io, name=image.name)
    return new_image

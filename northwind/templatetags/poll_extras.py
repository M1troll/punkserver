from django import template
from base64 import b64encode

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image
import io


register = template.Library()


@register.filter
def bin_2_img(_bin):
    if _bin is not None:
        return b64encode(_bin).decode('utf-8')


@register.filter
def display_img(image_bytes):
    # from io import BytesIO
    # file_data = BytesIO(image_bytes)
    # temp_image_io = io.BytesIO()
    
    # # import ipdb ; ipdb.set_trace()

    # with Image.open(file_data) as image:
    #     image.save(temp_image_io, format='JPEG')

    # temp_image_io.seek(0)
    # image_file = ContentFile(temp_image_io.read())
    # image_name = 'image.jpg'
    # image_path = default_storage.save(image_name, image_file)
    return None
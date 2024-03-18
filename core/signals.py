# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from PIL import Image as pilImage

# from core.models import Image

# @receiver(post_save, sender=Image)
# def resize_img(sender, instance, created, **kwargs):
#     if created:
#         target_size = (900, 900)
        
#         print("created")

#         img = pilImage.open(instance.image)

#         if img.height != 900 and img.width != 900:
#             if hasattr(img, '_getexif'):
#                 exif = img._getexif()
#                 if exif:
#                     orientation = exif.get(0x0112)
#                     if orientation == 3:
#                         img = img.rotate(180, expand=True)
#                     elif orientation == 6:
#                         img = img.rotate(270, expand=True)
#                     elif orientation == 8:
#                         img = img.rotate(90, expand=True)
#             print("due")
#             resized_img = img.thumbnail(target_size)
#             with open(instance.image.path, 'wb') as f:
#                     resized_img.save(f)

#                 # Ustaw zmieniony obraz jako nowy obraz w instancji
#             instance.image = instance.image.name
#             instance.save()
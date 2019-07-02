#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
from PIL import Image


api = InstagramAPI("cosmic_wild", "05300501Mythology053")
api.login()  # login

photo_path = 'Sarajevo.jpg'
caption = "Sarajevo."


image = Image.open(photo_path)
new_path = photo_path.replace(".jpg", "")+ "_low.jpg"
image.save(new_path)

api.uploadPhoto(new_path, caption=caption)

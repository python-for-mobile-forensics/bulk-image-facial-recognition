import face_recognition
from PIL import Image
import os, os.path

def get_image_directory(path):
  imgs = []
  valid_images = [".jpg",".gif",".png",".tga"]
  for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
      continue
    imgs.append(os.path.join(path,f))
  return imgs

def recognize_faces(path):
  image = face_recognition.load_image_file(path)
  face_locations = face_recognition.face_locations(image)
  i = 0
  for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save( 'output/' + str(i)+".png")
    i+=1

images = get_image_directory('images/')

for image_file in images:
  recognize_faces(image_file)

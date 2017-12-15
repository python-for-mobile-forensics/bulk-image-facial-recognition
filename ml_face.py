import face_recognition
import os, os.path
import ntpath
from PIL import Image

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
  file_name = path_leaf(path)
  image = face_recognition.load_image_file(path)
  face_locations = face_recognition.face_locations(image, model="cnn")
  i = 0
  for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save( 'output/' + str(file_name) + '_' +str(i)+".png")
    i+=1

def compare_faces(unknown_image, known_images):
  try:
    unknown_comparison_image = create_face_comparison_encoding(image)
  except (IndexError, ValueError):
    return false
  for k_image in known_images:
    try:
      results = face_recognition.compare_faces([k_image],unknown_comparison_image)
    except (IndexError, ValueError):
      continue
    if results[0] == True:
      print("This person appears familiar!")
      print("Writing the faces to output folder!")
      recognize_faces(image)
    else:
      print("This doesn't appear to be familiar!")

def path_leaf(path):
  head, tail = ntpath.split(path)
  return tail or ntpath.basename(head)

def create_face_comparison_encoding(image):
  known_image = face_recognition.load_image_file(image)
  known_image_encoding = face_recognition.face_encodings(known_image)[0]
  return known_image_encoding

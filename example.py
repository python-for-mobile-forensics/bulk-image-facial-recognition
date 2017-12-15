#!/usr/bin/python3
from ml_face import *
from concurrent.futures import ProcessPoolExecutor

##
# The Program
##
unknown_persons = get_image_directory('images/') # Unknown Persons Directory
known_persons = get_image_directory('known_person/') # Known Persons Directory
known_list = [] # Empty List
for k_per in known_persons:
  known_comparison_image = create_face_comparison_encoding(k_per)
  known_list.append(known_comparison_image)

##
# Multi Processing
##
executor = ProcessPoolExecutor(max_workers=10)
futures = []
for image in unknown_persons:
  work = executor.submit(compare_faces(image,known_list))
  futures.append(work)

from ml_face import *
import threading

##
# The Program
##
unknown_persons = get_image_directory('images/') # Unknown Persons Directory
known_persons = get_image_directory('known_person/') # Known Persons Directory
known_list = [] # Empty List
for k_per in known_persons:
  known_comparison_image = create_face_comparison_encoding(k_per)
  known_list.append(known_comparison_image)

if not unknown_persons:
  t = threading.Thread(target=compare_faces, args=(unknown_persons.pop(), known_list) )
  threads.append(t)
  t.start()

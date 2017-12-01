from ml_face import *

##
# The Program
##
unknown_persons = get_image_directory('images/') # Unknown Persons Directory
known_persons = get_image_directory('known_person/') # Known Persons Directory
known_list = [] # Empty List
for k_per in known_persons:
  known_comparison_image = create_face_comparison_encoding(k_per)
  known_list.append(known_comparison_image)
compare_faces(unknown_persons,known_list)

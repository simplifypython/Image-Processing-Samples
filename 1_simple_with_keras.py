# Step-1: Import the Library 
from keras.preprocessing import image

# Step-2: Set the variables containing Input Image and Output Image Path
input_image_path = 'input_images/img1.png' # Replace with your Image Path
output_image_path = 'output_images/img1.jpg' # Replace with desired Image Path

# Step-3: Load the Image
img_raw = image.load_img(input_image_path)
print(img_raw)

# Step-4: Convert the Image into NumPy Array
img_arr = image.img_to_array(img_raw)
# print(img_arr)
print(img_arr.shape)

# Step-5: Generate the Image from NumPy Array
img_new = image.array_to_img(img_arr)
print(img_new)
img_new.save(output_image_path)

# General Instructions
To use the python and julia project clone the repository running the following command in terminal:

git clone https://github.com/Sharad117/image_gen_julia.git

Ensure that you have installed python and julia compilers and added them to your system path.


# Approach

The images were generated using diffusers library and StableDiffusionXLPipeline. The prompt used was "A natural night scene of a serene fantasy world, with bright colors and hues". Three images were created by running the StableDiffusionXL API in a loop, and the generated images were saved.

Preprocessing was done completely using openCV. Images were resized, converted to grayscale and then normalized. It must be ensured that normalization takes place after using cv2.cvtColor() as cv2.cvtColor() expects pixel values between [0,255]. Normalization before converting color would convert the pixel values to [0,1] throwing an error.

While viewing the images, use either matplotlib to view it in grayscale using cmap='gray' or multiply the image by 255 before using cv2.imshow()
Viewing the image using normal image viewers will give a complete black image, as it is a normalized image with pixel values between [0,1]

For the CNN model, Julia's Flux and Image libraries were used. A simple model with 2 CNN models and 2 Dense layers was made, and a forward pass was made for each of the generated images. While loading the images, no loading pipeline was used, but the images were reshaped to [224,224,1,1] corresponding to a grayscale image and a batch size 1.
# Generation and Preprocessing

The generation and preprocessing is handled by generate.py and preprocess.py respectively. Before running the main file, we need to install dependencies by running the following command in terminal 


pip install -r requirements.txt



Once the dependencies are installed run the following command in the terminal to generate and view the images 

python main.py

For a more interactive execution of the code, you can run the image_gen.ipynb and preprocess.ipynb jupyter notebooks. 
# Convolution Forward pass

Open terminal and change directory to my_project by using the command

"cd my_project"

Open a Julia REPL by running the command 

"julia" in the terminal. Then enter the package manager mode by typing ']'. Now within the package manager activate the project by typing

"activate ."

Install all the dependencies in Project.toml by running

"instantiate"

Exit the package manager by pressing backspace, and exit the REPL by typing in "exit()". Go back to parent directory of my_project, i.e., image_gen_julia. Run the julia file by running the command

"julia my_project/model.jl"

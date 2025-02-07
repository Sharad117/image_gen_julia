# General Instructions
To use the python and julia project clone the repository running the following command in terminal:

git clone https://github.com/Sharad117/image_gen_julia.git

Ensure that you have installed python and julia compilers and added them to your system path.

# Generation and Preprocessing

The generation and preprocessing is handled by generate.py and preprocess.py respectively. Before running the main file, we need to install dependencies by running the following command in terminal 


pip install -r requirements.txt



Once the dependencies are installed run the following command in the terminal to generate and view the images 

python main.py


# Convolution Forward pass

Open terminal and change directory to my_project by using the command

cd my_project

Open a Julia REPL by running the command 

julia in the terminal. Then enter the package manager mode by typing ']'. Now within the package manager activate the project by typing

activate .

Install all the dependencies in Project.toml by running

instantiate

Exit the REPL and go back to parent directory of my_project. Run the julia file by running the command

julia my_project/model.jl

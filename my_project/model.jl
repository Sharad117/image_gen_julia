import Pkg
Pkg.add("Images")
Pkg.add("Flux")
using Pkg
Pkg.activate(".")

using Flux
using Images

# Define the model
model = Chain(
    Conv((3, 3), 1=>16, relu),
    MaxPool((2, 2)),
    Conv((3, 3), 16=>32, relu),
    MaxPool((2, 2)),
    Flux.flatten,
    Dense(32*54*54, 128, relu),
    Dense(128, 10)
)


# Load and preprocess images

image_paths = ["images\\preprocessed\\preprocessed_1.png", "images\\preprocessed\\preprocessed_2.png", "images\\preprocessed\\preprocessed_3.png"]
images = [load(path) for path in image_paths]

# Perform forward pass
for img in images
    img_batch = reshape(img, (224, 224, 1, 1))  # Reshape to (height, width, channels, batch_size)
    output = model(img_batch)
    println("Output: ", output)
    println("\n\n")
end
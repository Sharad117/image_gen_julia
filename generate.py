import os
import torch
from diffusers import StableDiffusionXLPipeline
def gen():
    if not os.path.exists('images/original'):
        os.makedirs('images/original')

    pipe = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        use_safetensors=True,
    ).to('cuda')


    prompt = "A natural night scene of a serene fantasy world, with bright colors and hues"

    for i in range(3):
        output = pipe(prompt, num_images_per_prompt=1).images
        output[0].save(f'images/original/image{i+1}.png')
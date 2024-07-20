from django.shortcuts import render
from diffusers import DiffusionPipeline
import os
import uuid
# Create your views here.

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images')


def image_form(request):
    return render(request, 'pixel_forge/index.html')

def image_view(request):
    image = None
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            image = generate_image(prompt)
    print(image)
    return render(request, 'pixel_forge/index.html', {'image': image})


#######################################
# GENERATE YOUR IMAGES
########################################
def generate_image(prompt):
    # Loading the diffusion model
    pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipeline.load_lora_weights("Melonie/text_to_image_finetuned")
    
    # Generating & saving the image from the prompt
    image = pipeline(prompt).images[0]
    image_filename = f"{uuid.uuid4()}.png"
    image_path = os.path.join(OUTPUT_DIR, image_filename)
    image.save(image_path)
    return image_filename


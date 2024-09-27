import os
from PIL import Image

def check_gpu():
    try:
        import GPUtil
        gpus = GPUtil.getAvailable(order='first', limit=1, maxLoad=0.5, maxMemory=0.5)
        return len(gpus) > 0
    except ImportError:
        print("GPUtil module not installed. GPU checks will be skipped.")
        return False

def convert_images(input_folder, output_folder, quality):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            png_filename = filename.replace('.jpg', '.png')
            png_path = os.path.join(output_folder, png_filename)
            img.save(png_path, 'PNG', quality=quality)
            print(f"Converted {filename} to {png_filename} with quality {quality}")

def main():
    input_folder = input("Enter the path to the folder containing JPG images: ")
    output_folder = input("Enter the path to the folder where PNG images will be saved: ")
    
    # Get user input for compression quality
    quality = int(input("Enter the compression strength (1-100, where 100 is best quality): "))
    
    # Check for GPU availability
    if check_gpu():
        print("GPU is available. Processing might be faster.")
    else:
        print("No GPU available. Processing will use CPU.")

    convert_images(input_folder, output_folder, quality)

if __name__ == "__main__":
    main()

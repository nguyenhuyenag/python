from PIL import Image


def merge_images(image_paths, output_path, target_width, target_height):
    resized_images = []
    for path in image_paths:
        image = Image.open(path)
        resized_image = image.resize((target_width, target_height))
        resized_images.append(resized_image)

    merged_image = Image.new("RGB", (target_width * len(image_paths), target_height))

    for i, img in enumerate(resized_images):
        merged_image.paste(img, (i * target_width, 0))

    merged_image.save(output_path)
    merged_image.show()


image_paths = ["img1.jpg", "img2.jpg"]
output_path = r"D:\WORK\Cloud\OneDrive\Desktop\merged_image.jpg"
target_width = 600
target_height = 500

merge_images(image_paths, output_path, target_width, target_height)

print("OK")

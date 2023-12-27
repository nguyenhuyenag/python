from PIL import Image


def merge_images(image_path1, image_path2, output_path, target_width, target_height):
    # Open the images
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Resize both images to the specified target width and height
    resized_image1 = image1.resize((target_width, target_height))
    resized_image2 = image2.resize((target_width, target_height))

    # Create a new image with double the width
    merged_image = Image.new("RGB", (target_width * 2, target_height))

    # Paste the resized images side by side
    merged_image.paste(resized_image1, (0, 0))
    merged_image.paste(resized_image2, (target_width, 0))

    # Save the merged image
    merged_image.save(output_path)


# Example usage:
# image_path1 = "image1.png"
# image_path2 = "image2.jpg"
# image_path1 = "image3.jpg"
# image_path2 = "image4.png"
# output_path = "merged_image.jpg"

target_width = 1000  # Specify the desired width
target_height = 700  # Specify the desired height

merge_images("image1.png", "image2.jpg", "merge_out1.jpg", target_width, target_height)
merge_images("image3.jpg", "image4.png", "merge_out2.jpg", target_width, target_height)

print("OK")

import numpy as np
def load_image(image_path):  
    return np.array(Image.open(image_path))

def smooth_image(image, kernel_size=3):
    pad_size=kernel_size//2
    padded_image=np.pad(image,pad_size,mode='reflect')
    rows,cols=image.shape
    smoothed_image=np.zeroes_like(image)

    for i in range(rows):
        for j in range(cols):
            neighborhood=padded_image[i:i+kernel_size, j:j+kernel_size]
            average_value= np.mean(neighborhood)
            smoothed_image[i,j]=int(average_value)
            return smoothed_image

if __name__ == "__main__":
    image_path = "your_image.jpg"  
    image = load_image(image_path)
    smoothed = smooth_image(image)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title("Smoothed Image")
    plt.imshow(smoothed, cmap='gray')
    plt.show()
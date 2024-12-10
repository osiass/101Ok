import numpy as np
import cv2
import matplotlib.pyplot as plt

def process_image(file_path, region):
    """
    Dosya yolundan görüntüyü açar, belirtilen bölgeyi keser ve RGB değerlerini işler.

    Args:
        file_path (str): PNG dosyasının yolu.
        region (tuple): Kesilecek bölgenin koordinatları (x, y, width, height).

    Returns:
        numpy.ndarray: Kesilen bölgenin RGB renklerinin numpy 2D dizisi.
        tuple: RGB ortalama değerleri (r_mean, g_mean, b_mean).
    """
    # Görüntüyü okuma
    image = cv2.imread(file_path)

    # Kesilecek bölgenin koordinatları
    x, y, width, height = region

    # Bölgeyi kesme
    cropped_image = image[y:y+height, x:x+width]

    # BGR'den RGB'ye dönüşüm
    cropped_image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

    # RGB değerlerini numpy array'e dönüştürme
    pixel_array = np.array(cropped_image_rgb)

    # RGB değerlerinin ortalamasını hesaplama
    r_mean = np.mean(pixel_array[:, :, 0])
    g_mean = np.mean(pixel_array[:, :, 1])
    b_mean = np.mean(pixel_array[:, :, 2])

    # Matplotlib ile kesilen bölgeyi görselleştirme
    plt.imshow(cropped_image_rgb)
    plt.title("Kesilen Bölge")
    plt.axis("off")
    plt.show()

    return pixel_array, (r_mean, g_mean, b_mean)

# Örnek kullanım
file_path = "turuncu.png"  # PNG dosyasının yolu
region = (100, 100, 100, 100)  # Kesilecek bölgenin koordinatları: (x, y, width, height)

pixel_array, rgb_mean = process_image(file_path, region)

print("RGB Ortalamaları:", rgb_mean)

from PIL import Image
import os

# Görüntüyü yükleme
input_image_path = "renklerarka1.png"  # İşlenecek PNG dosyasının yolu
output_image_path = "sonuc_siyah_beyaz.png"  # Kaydedilecek görüntü yolu

# Görüntüyü aç ve gri tonlamaya çevir
image = Image.open(input_image_path).convert("L")

# Görüntüyü tamamen siyah-beyaz yapma
threshold = 145# Eşik değeri 218 alt sınır
bw_image = image.point(lambda x: 255 if x > threshold else 0, '1')  # Siyah-beyaz dönüştürme

# Manipüle edilen görüntüyü kaydet
bw_image.save(output_image_path)

print(f"Görüntü başarıyla işlenip kaydedildi: {output_image_path}")

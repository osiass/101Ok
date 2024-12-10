import cv2
from ultralytics import YOLO

# YOLOv8 modelini yükle
model = YOLO('yolov8n.pt')  # Nano model, hızlı ve hafif

# Kamerayı başlat
cap = cv2.VideoCapture(0)  # 0, varsayılan kamera içindir. Harici bir kamera kullanıyorsanız, ilgili indeksi girin.

if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()

print("Kamera açıldı. Çıkmak için 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()  # Kameradan bir kare al
    if not ret:
        print("Kamera akışı alınamadı.")
        break

    # YOLO modelini kullanarak tahmin yap
    results = model(frame)

    # Tahmin edilen sonuçları görselleştir
    annotated_frame = results[0].plot()  # Tespit edilen nesnelerle birlikte çerçeveyi çiz

    # Çerçeveyi ekranda göster
    cv2.imshow("YOLOv8 Nesne Tespiti", annotated_frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()

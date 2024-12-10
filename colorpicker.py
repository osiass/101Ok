import pyautogui
import time
from PIL import ImageGrab

# Sürekli döngü
while True:
    # Mouse pozisyonunu al
    x, y = pyautogui.position()

    # Ekran görüntüsünü al ve mouse'un olduğu yerin rengini bul
    screen = ImageGrab.grab()
    rgb = screen.getpixel((x, y))

    # Koordinat ve renk bilgilerini yazdır
    print(f"Koordinatlar: ({x}, {y}), RGB: {rgb}")

    # 0.5 saniye bekle
    time.sleep(2)
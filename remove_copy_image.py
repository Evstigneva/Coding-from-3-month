import os
from PIL import Image
import hashlib

def remove_duplicate_images(directory):
    # Создаем словарь для хранения хэшей изображений
    image_hashes = {}
    
    for root, _, files in os.walk(directory):
        for file_name in files:
            if not file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue  # Пропускаем файлы, которые не являются изображениями
            
            file_path = os.path.join(root, file_name)
            
            try:
                with open(file_path, 'rb') as f:
                    img_data = f.read()
                
                # Преобразуем изображение в MD5-хэш
                md5_hash = hashlib.md5(img_data).hexdigest()
                
                if md5_hash in image_hashes:
                    print(f"Удаляем дубликат файла: {file_path}")
                    os.remove(file_path)  # Удаление дублирующего файла
                else:
                    image_hashes[md5_hash] = file_path  # Сохраняем путь к оригинальному файлу
            except Exception as e:
                print(f"Ошибка при обработке файла {file_path}: {e}")

if __name__ == "__main__":
    directory = "/home/evstigneva/proda/craion_dataset_craion/realistik"  # Указываем директорию с изображениями
    remove_duplicate_images(directory)

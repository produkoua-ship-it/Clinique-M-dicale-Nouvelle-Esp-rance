import base64
import os
import json

def image_to_base64(image_path):
    """Convert image to base64 string"""
    try:
        with open(image_path, 'rb') as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
        # Detect mime type from extension
        ext = os.path.splitext(image_path)[1].lower()
        mime_types = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml',
            '.webp': 'image/webp'
        }
        mime_type = mime_types.get(ext, 'image/png')
        return f"data:{mime_type};base64,{encoded}"
    except Exception as e:
        print(f"Error converting {image_path}: {e}")
        return None

def convert_all_images():
    base_dir = "D:/Utilisateur/Documents/Antigravity/clients/Clinique médicale Nouvelle Espérance"

    images_data = {}

    # Main images
    main_images = ['logo.png', 'favicon.png', 'accueille.png']
    for img in main_images:
        path = os.path.join(base_dir, img)
        if os.path.exists(path):
            images_data[img.split('.')[0]] = image_to_base64(path)
            print(f"Converted {img}")

    # Photo hero folders
    folders = {
        'hero': 'Photo hero/hero',
        'equipe': 'Photo hero/equipe',
        'patients': 'Photo hero/patients',
        'ambiance': 'Photo hero/ambiance'
    }

    for key, folder in folders.items():
        folder_path = os.path.join(base_dir, folder)
        if os.path.exists(folder_path):
            images_data[key] = []
            for filename in sorted(os.listdir(folder_path)):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    file_path = os.path.join(folder_path, filename)
                    encoded = image_to_base64(file_path)
                    if encoded:
                        images_data[key].append({
                            'name': filename,
                            'data': encoded
                        })
                        print(f"Converted {folder}/{filename}")

    # Save to JSON file
    output_path = os.path.join(base_dir, 'images_data.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(images_data, f, indent=2)

    print(f"\nAll images converted and saved to {output_path}")
    return images_data

if __name__ == '__main__':
    convert_all_images()

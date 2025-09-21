import os

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
}

sample_files = [
    "Scripting課程大綱.pdf",
    "期中報告草稿.docx",
    "cat_meme.jpg",
    "lofi_music.mp3",
    "screenshot_2025.png",
    "final_project.zip",
]

def create_downloads_with_files(base_dir):
    """建立 Downloads 資料夾與示範檔案（避免重複建立）"""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print("已建立 Downloads 資料夾。")

    for filename in sample_files:
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("")
            print(f"已建立檔案: {filename}")
        else:
            print(f"檔案已存在，略過: {filename}")

def get_unique_filename(folder, filename):
    """避免檔案覆蓋：同名則自動加編號"""
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = f"{name}({counter}){ext}"
        counter += 1
    return new_filename

def organize_downloads(base_dir):
    """分類 Downloads 裡的檔案（避免覆蓋）"""
    for filename in os.listdir(base_dir):
        file_path = os.path.join(base_dir, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        target_folder = "Others"
        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = folder
                break

        target_dir = os.path.join(base_dir, target_folder)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        unique_name = get_unique_filename(target_dir, filename)
        new_path = os.path.join(target_dir, unique_name)

        os.rename(file_path, new_path)
        print(f"{filename} - {target_folder}/{unique_name}")

    print("\n分類完成")

if __name__ == "__main__":
    base_dir = os.path.join(os.getcwd(), "Downloads")
    create_downloads_with_files(base_dir)
    organize_downloads(base_dir)

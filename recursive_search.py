# 複雑な入れ子構造（ファイルシステムのようなもの）
file_system = {
    "home": {
        "user": {
            "documents": {
                "work": {},
                "private": {
                    "photo.jpg": "image data",
                    "secret.txt": "my secret"
                }
            },
            "downloads": {
                "installer.exe": "binary"
            }
        }
    },
    "etc": {
        "config": "settings"
    }
}

def find_file_recursive(current_folder, target_filename, path=""):
    """再帰を使った探索（コードがシンプル）"""
    for name, content in current_folder.items():
        current_path = f"{path}/{name}"
        if name == target_filename:
            return current_path
        
        if isinstance(content, dict):
            result = find_file_recursive(content, target_filename, current_path)
            if result: return result
    return None

def find_file_loop(root_folder, target_filename):
    """ループを使った探索（スタックを手動で管理する必要がある）"""
    # (現在のフォルダ, パス) のタプルをスタックに入れる
    stack = [(root_folder, "")]
    
    while stack:
        folder, path = stack.pop()
        for name, content in folder.items():
            current_path = f"{path}/{name}"
            if name == target_filename:
                return current_path
            
            if isinstance(content, dict):
                stack.append((content, current_path))
    return None

if __name__ == "__main__":
    target = "secret.txt"
    
    print(f"--- 探索対象: {target} ---")
    
    # 再帰版の実行
    path_rec = find_file_recursive(file_system, target)
    print(f"再帰版での結果: {path_rec}")
    
    # ループ版の実行
    path_loop = find_file_loop(file_system, target)
    print(f"ループ版での結果: {path_loop}")

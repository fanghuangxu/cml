import os

def find_java_path(start_dirs=None):
    # 如果没有指定起始目录，则使用常见的Java安装目录
    if not start_dirs:
        start_dirs = [
            "C:\\\\",
            "D:\\\\",
            "E:\\\\",
            "F:\\\\",
            "G:\\\\",

            # 可以添加更多的常见路径
        ]

    # 用于存储找到的Java路径
    java_paths = []

    # 遍历起始目录
    for start_dir in start_dirs:
        if os.path.exists(start_dir):
            # 递归遍历目录树
            for root, dirs, files in os.walk(start_dir):
                for file in files:
                    if file.lower() in ['java', 'java.exe']:
                        java_path = os.path.join(root, file)
                        java_paths.append(java_path)

    return java_paths

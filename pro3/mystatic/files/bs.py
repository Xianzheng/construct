import os
import shutil

def mycopyAndPaste(src,des):
    source_path = os.path.abspath(r'{}'.format(src))
    target_path = os.path.abspath(r'{}'.format(des))

    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)

    shutil.copytree(source_path, target_path)
    print('copy dir finished!')




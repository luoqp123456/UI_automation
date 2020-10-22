import os

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的绝对路径的上一级，__file__指当前文件
log_path = os.path.join(prj_path, 'log')
picture_path = os.path.join(prj_path, 'Picture')
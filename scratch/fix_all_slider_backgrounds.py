import os
import glob
import re

slider_old_style = 'style="width: 100%; height: 8px; border-radius: 4px; outline: none; -webkit-appearance: none; appearance: none; background: #E2DDD5; cursor: pointer; accent-color: #C89B3C;"'
slider_new_style = 'style="width: 100%; height: 8px; border-radius: 4px; outline: none; -webkit-appearance: none; appearance: none; background: linear-gradient(to right, #C89B3C 0%, #C89B3C 50%, #363636 50%, #363636 100%); cursor: pointer; accent-color: #C89B3C;"'

# 1. Update build.py
build_py_path = "/Users/aadityamohansamadhiya/the credit lane/build.py"
with open(build_py_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("background: #E2DDD5;", "background: linear-gradient(to right, #C89B3C 0%, #C89B3C 50%, #363636 50%, #363636 100%);")
with open(build_py_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build.py")

# 2. Update PHP files in credit-lane-theme
php_files = glob.glob("/Users/aadityamohansamadhiya/the credit lane/credit-lane-theme/**/*.php", recursive=True)
for pfile in php_files:
    with open(pfile, "r", encoding="utf-8") as f:
        pcontent = f.read()
    
    if "background: #E2DDD5" in pcontent or "background: #e2ddd5" in pcontent:
        pcontent = pcontent.replace("background: #E2DDD5;", "background: linear-gradient(to right, #C89B3C 0%, #C89B3C 50%, #363636 50%, #363636 100%);")
        pcontent = pcontent.replace("background: #e2ddd5;", "background: linear-gradient(to right, #C89B3C 0%, #C89B3C 50%, #363636 50%, #363636 100%);")
        with open(pfile, "w", encoding="utf-8") as f:
            f.write(pcontent)
        print(f"Updated PHP file: {pfile}")

print("Completed updating slider backgrounds.")

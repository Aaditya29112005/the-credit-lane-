import os
import glob
import re

html_files = glob.glob("**/*.html", recursive=True)
missing_imgs = []
missing_hrefs = []

for file in html_files:
    dir_path = os.path.dirname(file)
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check img srcs
    srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    for src in srcs:
        if src.startswith("http://") or src.startswith("https://") or src.startswith("data:") or src.startswith("tel:") or src.startswith("mailto:"):
            continue
        clean_src = src.split("?")[0].split("#")[0]
        target_path = os.path.normpath(os.path.join(dir_path, clean_src))
        if not os.path.exists(target_path):
            missing_imgs.append((file, src, target_path))

    # Check internal hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        if href.startswith("http://") or href.startswith("https://") or href.startswith("data:") or href.startswith("tel:") or href.startswith("mailto:") or href.startswith("#"):
            continue
        clean_href = href.split("?")[0].split("#")[0]
        if not clean_href:
            continue
        target_path = os.path.normpath(os.path.join(dir_path, clean_href))
        if not os.path.exists(target_path):
            missing_hrefs.append((file, href, target_path))

print(f"Total HTML files checked: {len(html_files)}")
print(f"Missing Image Sources: {len(missing_imgs)}")
for f, s, t in missing_imgs:
    print(f"  [IMG] In {f}: src='{s}' -> {t}")

print(f"Missing Internal Hrefs: {len(missing_hrefs)}")
for f, h, t in missing_hrefs:
    print(f"  [HREF] In {f}: href='{h}' -> {t}")

if not missing_imgs and not missing_hrefs:
    print("✨ ALL IMAGES AND LINKS ARE 100% VALID ACROSS THE ENTIRE WEBSITE! ✨")

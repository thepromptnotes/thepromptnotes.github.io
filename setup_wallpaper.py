#!/usr/bin/env python3
"""
Wallpaper Setup Script
Copies and resizes the screenshot to use as blog wallpaper
"""

import os
import shutil
from PIL import Image

def setup_wallpaper():
    """Copy and resize the screenshot for use as wallpaper"""
    
    # Source and destination paths
    source_file = "/Users/occ-studio/Documents/dev/promptnotes_proj/github-pages-blog/thumbnails/Screenshot 2025-10-24 at 2.53.31 PM.png"
    dest_file = "/Users/occ-studio/Documents/dev/promptnotes_proj/github-pages-blog/images/wallpaper.png"
    
    print("🖼️ Setting up wallpaper...")
    
    if os.path.exists(source_file):
        try:
            # Copy the file first
            shutil.copy2(source_file, dest_file)
            print(f"✅ Copied wallpaper to: {dest_file}")
            
            # Check the image dimensions
            with Image.open(dest_file) as img:
                print(f"📐 Original dimensions: {img.size}")
                
                # If it's too large, resize it for web optimization
                if img.width > 1920 or img.height > 1080:
                    # Resize to fit within 1920x1080 while maintaining aspect ratio
                    img.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
                    img.save(dest_file, 'PNG', optimize=True)
                    print(f"📐 Resized to: {img.size}")
                
                file_size = os.path.getsize(dest_file)
                print(f"💾 File size: {file_size:,} bytes")
                
        except Exception as e:
            print(f"❌ Error processing wallpaper: {e}")
    else:
        print(f"❌ Source file not found: {source_file}")
        print("Available files in thumbnails:")
        thumbnails_dir = "/Users/occ-studio/Documents/dev/promptnotes_proj/github-pages-blog/thumbnails"
        if os.path.exists(thumbnails_dir):
            for file in os.listdir(thumbnails_dir):
                print(f"   - {file}")

if __name__ == "__main__":
    setup_wallpaper()

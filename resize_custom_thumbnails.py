#!/usr/bin/env python3
"""
Custom Thumbnail Resizer and Matcher
Resizes custom thumbnails to 400x200 and matches them to the correct blog posts
"""

import os
from PIL import Image
import shutil

def resize_and_match_thumbnails():
    """Resize custom thumbnails and match them to blog posts"""
    
    # Source directory
    thumbnails_dir = "/Users/occ-studio/Documents/dev/promptnotes_proj/github-pages-blog/thumbnails"
    
    # Target directory
    images_dir = "/Users/occ-studio/Documents/dev/promptnotes_proj/github-pages-blog/images"
    
    # Mapping of custom thumbnails to blog post filenames
    thumbnail_mapping = {
        "Ai Brain.png": "ai-brain-thumbnail.png",
        "temporal.png": "temporal-coherence-thumbnail.png", 
        "visual-language-of-ai-computer-vision-vfx-production.png": "computer-vision-thumbnail.png"
    }
    
    print("🎨 Processing custom thumbnails...")
    
    for source_file, target_file in thumbnail_mapping.items():
        source_path = os.path.join(thumbnails_dir, source_file)
        target_path = os.path.join(images_dir, target_file)
        
        if os.path.exists(source_path):
            try:
                # Open and resize the image
                with Image.open(source_path) as img:
                    print(f"📸 Processing: {source_file}")
                    print(f"   Original size: {img.size}")
                    
                    # Resize to 400x200 (blog thumbnail size)
                    resized_img = img.resize((400, 200), Image.Resampling.LANCZOS)
                    
                    # Save the resized image
                    resized_img.save(target_path, 'PNG', optimize=True)
                    
                    # Get file size
                    file_size = os.path.getsize(target_path)
                    print(f"   ✅ Resized to: {resized_img.size}")
                    print(f"   📁 Saved as: {target_file}")
                    print(f"   💾 File size: {file_size:,} bytes")
                    print()
                    
            except Exception as e:
                print(f"❌ Error processing {source_file}: {e}")
        else:
            print(f"⚠️ File not found: {source_file}")
    
    print("🎉 Thumbnail processing complete!")
    print("\n📋 Summary of changes:")
    print("- ai-brain-thumbnail.png: Updated with custom AI Brain image")
    print("- temporal-coherence-thumbnail.png: Updated with custom temporal image") 
    print("- computer-vision-thumbnail.png: Updated with custom visual language image")
    print("\n💡 Next steps:")
    print("1. Commit and push these changes to GitHub")
    print("2. Wait for GitHub Pages to rebuild")
    print("3. Check your live blog for the new thumbnails!")

if __name__ == "__main__":
    resize_and_match_thumbnails()

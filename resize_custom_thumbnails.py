#!/usr/bin/env python3
"""
Custom Thumbnail Resizer and Matcher
Resizes custom thumbnails to 400x200 and matches them to the correct blog posts

USAGE:
1. Add new thumbnail images to the /thumbnails/ directory
2. Update the thumbnail_mapping dictionary below with new entries
3. Run: python resize_custom_thumbnails.py
4. Commit and push the changes

The script will automatically:
- Resize images from any size to 400x200
- Optimize for web delivery
- Match them to the correct blog post filenames
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
    # ADD NEW THUMBNAILS HERE:
    thumbnail_mapping = {
        "Ai Brain.png": "ai-brain-thumbnail.png",
        "temporal.png": "temporal-coherence-thumbnail.png", 
        "visual-language-of-ai-computer-vision-vfx-production.png": "computer-vision-thumbnail.png",
        # Add new mappings here as you create more thumbnails
        # "your-new-thumbnail.png": "target-blog-post-thumbnail.png",
    }
    
    print("🎨 Processing custom thumbnails...")
    print(f"📁 Source directory: {thumbnails_dir}")
    print(f"📁 Target directory: {images_dir}")
    print()
    
    processed_count = 0
    
    for source_file, target_file in thumbnail_mapping.items():
        source_path = os.path.join(thumbnails_dir, source_file)
        target_path = os.path.join(images_dir, target_file)
        
        if os.path.exists(source_path):
            try:
                # Open and resize the image
                with Image.open(source_path) as img:
                    print(f"📸 Processing: {source_file}")
                    print(f"   Original size: {img.size}")
                    
                    # Resize to fit 400x200 while maintaining aspect ratio
                    # Calculate the scaling factor to fit within 400x200
                    width_ratio = 400 / img.width
                    height_ratio = 200 / img.height
                    scale_factor = min(width_ratio, height_ratio)
                    
                    new_width = int(img.width * scale_factor)
                    new_height = int(img.height * scale_factor)
                    
                    # Resize maintaining aspect ratio
                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    
                    # Create a 400x200 canvas with white background
                    canvas = Image.new('RGB', (400, 200), 'white')
                    
                    # Calculate position to center the image
                    x_offset = (400 - new_width) // 2
                    y_offset = (200 - new_height) // 2
                    
                    # Paste the resized image onto the canvas
                    canvas.paste(resized_img, (x_offset, y_offset))
                    resized_img = canvas
                    
                    # Save the resized image
                    resized_img.save(target_path, 'PNG', optimize=True)
                    
                    # Get file size
                    file_size = os.path.getsize(target_path)
                    print(f"   ✅ Resized to: {resized_img.size}")
                    print(f"   📁 Saved as: {target_file}")
                    print(f"   💾 File size: {file_size:,} bytes")
                    print()
                    
                    processed_count += 1
                    
            except Exception as e:
                print(f"❌ Error processing {source_file}: {e}")
        else:
            print(f"⚠️ File not found: {source_file}")
    
    print(f"🎉 Thumbnail processing complete! ({processed_count} images processed)")
    
    if processed_count > 0:
        print("\n📋 Next steps:")
        print("1. git add images/")
        print("2. git commit -m 'Update thumbnails with custom images'")
        print("3. git push origin main")
        print("4. Wait for GitHub Pages to rebuild")
        print("5. Check your live blog!")
    
    print("\n💡 To add more thumbnails:")
    print("1. Add images to /thumbnails/ directory")
    print("2. Update thumbnail_mapping in this script")
    print("3. Run this script again")

def list_available_thumbnails():
    """List all available thumbnail files in the thumbnails directory"""
    thumbnails_dir = "/Users/occ-studio/Documents/dev/promptnotes_proj/github-pages-blog/thumbnails"
    
    if os.path.exists(thumbnails_dir):
        files = [f for f in os.listdir(thumbnails_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if files:
            print("📁 Available thumbnail files:")
            for file in sorted(files):
                file_path = os.path.join(thumbnails_dir, file)
                file_size = os.path.getsize(file_path)
                print(f"   - {file} ({file_size:,} bytes)")
        else:
            print("📁 No image files found in thumbnails directory")
    else:
        print("❌ Thumbnails directory not found")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        list_available_thumbnails()
    else:
        resize_and_match_thumbnails()

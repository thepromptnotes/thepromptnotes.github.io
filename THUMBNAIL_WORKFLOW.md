# Custom Thumbnail Workflow Guide

## 🎨 Adding New Thumbnails to Your Blog

### Quick Workflow:
1. **Add your custom thumbnail** to `/thumbnails/` directory
2. **Update the mapping** in `resize_custom_thumbnails.py`
3. **Run the script**: `python resize_custom_thumbnails.py`
4. **Deploy**: `git add . && git commit -m "Add new thumbnail" && git push`

### 📁 Current Thumbnail Mappings:

| Custom File | Blog Post Thumbnail | Blog Post Title |
|-------------|-------------------|-----------------|
| `Ai Brain.png` | `ai-brain-thumbnail.png` | "The AI Brain: How Intelligence Processes Visual Data in VFX Production" |
| `temporal.png` | `temporal-coherence-thumbnail.png` | "Building a Temporal Coherence Pipeline That Producers Understand" |
| `visual-language-of-ai-computer-vision-vfx-production.png` | `computer-vision-thumbnail.png` | "The Visual Language of AI: How Computer Vision Translates to VFX Production" |

### 🔧 Script Commands:

```bash
# Process all thumbnails
python resize_custom_thumbnails.py

# List available thumbnail files
python resize_custom_thumbnails.py --list
```

### 📝 Adding New Thumbnails:

1. **Add your image** to `/thumbnails/your-image-name.png`
2. **Edit `resize_custom_thumbnails.py`** and add to the mapping:
   ```python
   thumbnail_mapping = {
       # ... existing mappings ...
       "your-image-name.png": "target-blog-post-thumbnail.png",
   }
   ```
3. **Run the script** to resize and deploy

### 🎯 Blog Post Thumbnail Names:

Based on your current blog posts, here are the thumbnail filenames you'll need:

- `ai-infrastructure-thumbnail.png` - "Why Hollywood's AI Revolution Is Stuck in the Render Queue"
- `ai-translators-thumbnail.png` - "Stop Hiring 'AI Artists' — You Need AI Translators"
- `temporal-coherence-thumbnail.png` - "Building a Temporal Coherence Pipeline That Producers Understand" ✅
- `computer-vision-thumbnail.png` - "The Visual Language of AI: How Computer Vision Translates to VFX Production" ✅
- `ai-brain-thumbnail.png` - "The AI Brain: How Intelligence Processes Visual Data in VFX Production" ✅

### 💡 Tips:

- **Image size**: Any size works - script automatically resizes to 400x200
- **File formats**: PNG, JPG, JPEG supported
- **Quality**: Higher resolution source images = better final quality
- **Naming**: Use descriptive names that match your blog post topics

### 🚀 Deployment:

After running the script, always:
1. `git add images/`
2. `git commit -m "Update thumbnails"`
3. `git push origin main`
4. Wait 2-3 minutes for GitHub Pages to rebuild
5. Check your live blog!

---

**Your thumbnail workflow is now streamlined and ready for continuous updates!** 🎨✨

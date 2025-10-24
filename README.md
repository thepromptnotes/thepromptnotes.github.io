# AI in Entertainment Blog

A minimal, technical blog focused on AI applications in VFX and entertainment, built with Jekyll and GitHub Pages.

## Quick Setup Instructions

### 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `yourusername.github.io` (replace with your actual GitHub username)
3. Make it public
4. Don't initialize with README (we're providing our own files)

### 2. Upload These Files

Clone your new repository and add these files:

```bash
git clone https://github.com/yourusername/yourusername.github.io.git
cd yourusername.github.io
```

Copy all the files from this setup into your repository:

```
yourusername.github.io/
├── _config.yml
├── _layouts/
│   ├── default.html
│   └── post.html
├── _posts/
│   └── 2024-10-24-understanding-nerfs-virtual-production.md
├── index.html
├── about.md
├── archive.md
└── README.md
```

### 3. Customize Your Configuration

Edit `_config.yml`:
- Change `title` to your blog name
- Update `author` with your name
- Modify `description` to match your focus
- Update `url` with your GitHub Pages URL

### 4. Push to GitHub

```bash
git add .
git commit -m "Initial blog setup"
git push origin main
```

### 5. Enable GitHub Pages

1. Go to your repository settings on GitHub
2. Scroll to "Pages" section
3. Under "Source", select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Click "Save"

Your blog will be live at `https://yourusername.github.io` within a few minutes!

## Writing Posts

### Creating a New Post

1. Create a new file in `_posts/` folder
2. Name it: `YYYY-MM-DD-your-post-title.md`
3. Add front matter:

```yaml
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD
categories: [AI, VFX]
excerpt: "A brief description of your post"
cover_image: /images/your-image.png (optional)
---

Your post content in Markdown...
```

### Adding Images

1. Create an `images/` folder in your repository root
2. Add images there
3. Reference in posts: `![Alt text](/images/your-image.png)`

### Using Math Notation

Write LaTeX between `$$` for display math:

```
$$
\nabla_\theta \mathcal{L} = \frac{1}{N} \sum_{i=1}^{N} \nabla_\theta \log p_\theta(x_i)
$$
```

Or use `$` for inline math: `$\alpha + \beta = \gamma$`

### Creating Diagrams

For technical diagrams like Olah's blog:

1. **Option A**: Create SVGs in Figma/Illustrator, add to `images/`
2. **Option B**: Use Mermaid diagrams (requires adding Mermaid.js)
3. **Option C**: Embed interactive demos with D3.js or Three.js

## Advanced Customization

### Adding Interactive Visualizations

In your post, add:

```html
<div class="interactive-demo">
  <canvas id="demo-canvas"></canvas>
  <script>
    // Your Three.js or D3.js code here
  </script>
</div>
```

### Customizing Styles

Edit the `<style>` sections in layout files or create a separate `assets/css/main.css` file.

### Adding Comments

Consider adding [Utterances](https://utteranc.es/) (uses GitHub issues) or [Disqus](https://disqus.com/).

## Local Development (Optional)

To preview your blog locally before pushing:

1. Install Ruby and Jekyll:
```bash
gem install bundler jekyll
```

2. Create a `Gemfile`:
```ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
```

3. Run locally:
```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview.

## Tips for Technical Blogging

1. **Focus on Clarity**: Explain complex concepts step-by-step
2. **Use Visuals**: Diagrams often explain better than text
3. **Provide Code Examples**: Include practical implementations
4. **Show Real Results**: Include before/after comparisons, benchmarks
5. **Link to Resources**: Cite papers, GitHub repos, documentation

## Inspiration

- [Christopher Olah's Blog](https://colah.github.io/)
- [Distill.pub](https://distill.pub/)
- [Lil'Log](https://lilianweng.github.io/)

## License

Your content, your choice. Consider CC BY 4.0 for maximum impact.

---

Need help? Open an issue or reach out!
# Force GitHub Pages rebuild - Fri Oct 24 14:32:52 PDT 2025

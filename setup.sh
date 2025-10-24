#!/bin/bash

# GitHub Pages Blog Setup Script
# This script helps you deploy your blog to GitHub Pages

echo "🚀 GitHub Pages Blog Setup"
echo "========================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Use thepromptnotes username
github_username="thepromptnotes"
echo "Using GitHub username: $github_username"

# Repository name
repo_name="${github_username}.github.io"

echo "📝 Configuration:"
echo "  Repository: $repo_name"
echo "  URL: https://$repo_name"
echo ""

# Update _config.yml with actual username
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/yourusername/$github_username/g" _config.yml
else
    # Linux
    sed -i "s/yourusername/$github_username/g" _config.yml
fi

echo "✅ Updated _config.yml with your GitHub username"

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git branch -M main
fi

# Add remote if not already added
if ! git remote | grep -q origin; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin "https://github.com/${github_username}/${repo_name}.git"
else
    echo "📍 Remote already configured"
fi

# Stage all files
echo "📁 Staging files..."
git add .

# Commit
echo "💾 Creating initial commit..."
git commit -m "Initial blog setup with Jekyll" 2>/dev/null || echo "ℹ️  No changes to commit"

echo ""
echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a repository on GitHub named: $repo_name"
echo "   Go to: https://github.com/new"
echo ""
echo "2. Push your blog to GitHub:"
echo "   git push -u origin main"
echo ""
echo "3. Enable GitHub Pages in repository settings:"
echo "   https://github.com/${github_username}/${repo_name}/settings/pages"
echo "   - Source: Deploy from a branch"
echo "   - Branch: main"
echo "   - Folder: / (root)"
echo ""
echo "4. Your blog will be live at: https://${repo_name}"
echo "   (This may take a few minutes)"
echo ""
echo "📝 To create new posts:"
echo "   Add markdown files to _posts/ folder"
echo "   Format: YYYY-MM-DD-post-title.md"
echo ""
echo "Happy blogging! 🎉"

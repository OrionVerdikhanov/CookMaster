#!/bin/bash

# Set your repository URL
REPO_URL="https://github.com/OrionVerdikhanov/CookMaster.git"

# Navigate to project directory
cd /Users/feitullaverdikhanov/Desktop/GB_project || {
    echo "Error: Could not navigate to project directory"
    exit 1
}

# Ensure the remote is set correctly
git remote remove origin 2>/dev/null
git remote add origin $REPO_URL

# Pull latest changes first
git pull origin main || {
    echo "Error: Could not pull latest changes"
    exit 1
}

# Load new fixture data
python manage.py loaddata recipes/fixtures/initial_data.json || {
    echo "Error: Could not load fixture data"
    exit 1
}

# Stage all changes
git add .

# Create a commit with a descriptive message
git commit -m "Update repository with new recipes and categories"

# Push changes to the main branch
git push -u origin main || {
    echo "Error: Could not push to repository"
    exit 1
}

echo "Repository has been updated successfully!"

# Change directory
cd "C:\Users\shiyablue\Desktop\bon\ccnp21"

# Set user email
git config --global user.email "vonherbertfaborada@gmail.com"

# Set user name
git config --global user.name "rivan16"

# Add all changes
git add .

# Commit changes
git commit -m "CCNp21 Day 3"

# Add remote repository
git remote add origin https://github.com/rivan16/ccnp41.git

# Set default branch
git config --global init.defaultBranch main

# Pull changes from the main branch
git pull origin main



# Git 

## create a new repository on the command line

echo "# oc-ml-project-5" >> README.md
git init
git add README.md (or git add .)
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/EyaaaMD/oc-ml-project-5.git
git push -u origin main

## …or push an existing repository from the command line
git remote add origin https://github.com/EyaaaMD/oc-ml-project-5.git
git branch -M main
git push -u origin main
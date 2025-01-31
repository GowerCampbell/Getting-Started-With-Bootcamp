# Git Basics

Git is a distributed version control system that helps developers track changes in their code, collaborate with others, and manage projects efficiently. This guide covers the basics of Git, including setup, common commands, and workflows.

---

## Table of Contents
1. [What is Git?](#what-is-git)
2. [Setting Up Git](#setting-up-git)
3. [Basic Git Commands](#basic-git-commands)
   - [git init](#git-init)
   - [git clone](#git-clone)
   - [git add](#git-add)
   - [git commit](#git-commit)
   - [git status](#git-status)
   - [git log](#git-log)
   - [git push](#git-push)
   - [git pull](#git-pull)
   - [git branch](#git-branch)
   - [git checkout](#git-checkout)
   - [git merge](#git-merge)
4. [Git Workflow](#git-workflow)
5. [Best Practices](#best-practices)
6. [Resources](#resources)

---

## What is Git?
Git is a version control system that tracks changes to files over time. It allows multiple developers to work on the same project simultaneously without overwriting each other's work. Git also enables you to revert to previous versions of your code, create branches for new features, and collaborate with others through platforms like GitHub, GitLab, or Bitbucket.

---

## Setting Up Git

### Install Git
1. **Windows**: Download Git from [git-scm.com](https://git-scm.com/) and follow the installation instructions.
2. **macOS**: Use Homebrew to install Git:
   ```bash
   brew install git
   ```
3. **Linux**: Use your package manager to install Git:
   ```bash
   sudo apt-get install git  # For Debian/Ubuntu
   sudo yum install git      # For CentOS/Fedora
   ```

### Configure Git
After installation, configure your Git username and email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Basic Git Commands

### `git init`
Initializes a new Git repository in the current directory.
```bash
git init
```

### `git clone`
Clones an existing repository from a remote URL to your local machine.
```bash
git clone https://github.com/username/repository.git
```

### `git add`
Stages changes for the next commit. Use `.` to stage all changes or specify a file.
```bash
git add .              # Stage all changes
git add filename.txt   # Stage a specific file
```

### `git commit`
Creates a snapshot of the staged changes with a message describing the changes.
```bash
git commit -m "Your commit message"
```

### `git status`
Shows the status of your working directory, including staged and untracked files.
```bash
git status
```

### `git log`
Displays a history of commits in the current branch.
```bash
git log
```

### `git push`
Uploads local commits to a remote repository.
```bash
git push origin main  # Replace 'main' with your branch name
```

### `git pull`
Downloads changes from a remote repository and merges them into your local branch.
```bash
git pull origin main  # Replace 'main' with your branch name
```

### `git branch`
Lists, creates, or deletes branches.
```bash
git branch                  # List all branches
git branch new-branch       # Create a new branch
git branch -d branch-name   # Delete a branch
```

### `git checkout`
Switches to a different branch or commit.
```bash
git checkout branch-name    # Switch to a branch
git checkout -b new-branch  # Create and switch to a new branch
```

### `git merge`
Merges changes from one branch into another.
```bash
git checkout main          # Switch to the target branch
git merge feature-branch   # Merge changes from 'feature-branch'
```

---

## Git Workflow

### Basic Workflow
1. **Initialize or Clone a Repository**:
   - Start a new project with `git init` or clone an existing one with `git clone`.
2. **Make Changes**:
   - Edit files in your working directory.
3. **Stage Changes**:
   - Use `git add` to stage changes for the next commit.
4. **Commit Changes**:
   - Use `git commit` to save your changes with a descriptive message.
5. **Push Changes**:
   - Use `git push` to upload your commits to a remote repository.

### Branching Workflow
1. **Create a New Branch**:
   - Use `git checkout -b new-branch` to create and switch to a new branch.
2. **Make Changes**:
   - Edit files and commit changes in the new branch.
3. **Merge Changes**:
   - Switch back to the main branch (`git checkout main`) and merge the new branch (`git merge new-branch`).
4. **Push Changes**:
   - Push the merged changes to the remote repository.

---

## Best Practices
1. **Write Clear Commit Messages**:
   - Use concise and descriptive messages to explain what each commit does.
2. **Commit Often**:
   - Make small, frequent commits to track changes effectively.
3. **Use Branches**:
   - Create separate branches for new features or bug fixes to avoid disrupting the main codebase.
4. **Pull Before Push**:
   - Always pull the latest changes from the remote repository before pushing your commits.
5. **Review Changes**:
   - Use `git status` and `git diff` to review changes before committing.

---

## Resources
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Pro Git Book](https://git-scm.com/book/en/v2)



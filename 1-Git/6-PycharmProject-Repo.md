## 🔧 Prerequisites

1. **Git Installed**
   PyCharm relies on your system’s Git. [Download Git](https://git-scm.com/downloads) if you haven’t already.

2. **A GitHub Account**
   Sign up at [github.com](https://github.com) if you don’t have one.

3. **GitHub Connected to PyCharm**

   * Go to `File → Settings` (or `PyCharm → Preferences` on macOS).
   * Navigate to `Version Control → GitHub`.
   * Click the `+` icon and choose **"Log In with Token…"** or **"Log In via GitHub…"** to link your account.

---


## 🚀 How to Share Your Project on GitHub (Using PyCharm)

### Step 1: Open Your Project

Launch PyCharm and open the project you want to share.

### Step 2: Share via GitHub

Go to `VCS → Share Project on GitHub`.

> If you don’t see this, try `Git → GitHub → Share Project on GitHub`.


### Step 3: Configure Repository

A dialog will appear. Fill in the details:

* **Repository Name**: Defaults to your project name (you can change it).
* **Private**: ✅ Check this if you want only invited users to see the repo.
* **Remote**: Leave as `origin` (default).
* **Description**: Optional, but helpful.

Click **Share** to proceed.


### Step 4: Initial Commit

Another dialog opens to prepare your first commit:

* **Files**: PyCharm usually selects all needed files and auto-creates a `.gitignore` to exclude unneeded files (like `venv/`, `.idea/`, etc.).
* **Commit Message**: Use something like `"Initial commit"`.

Click **Add** or **Commit**. PyCharm will now push your project to GitHub.

### Step 5: Confirm on GitHub

Go to your GitHub profile. You’ll see your newly uploaded repository listed.

---


## 💻 Command Line Alternative

If PyCharm’s GitHub integration doesn’t work, use the terminal:

### 1. Create a New Repo on GitHub

Leave it **empty** (no README, .gitignore, or license).

### 2. In PyCharm Terminal:

```bash
# Initialize Git in your project
git init

# Track all project files
git add .

# Create your first commit
git commit -m "Initial commit"

# Set the default branch to main
git branch -M main

# Link to your GitHub repo
git remote add origin https://github.com/your-username/your-repo-name.git ( repo url )

# Push your code to GitHub
git push -u origin main
```

---

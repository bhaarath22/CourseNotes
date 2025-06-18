
## 📘 Table of Contents

1. [Git Project Creation and Workflow](#git-project-creation-and-workflow)
2. [Remote Repositories (Collaboration)](#remote-repositories-collaboration)
3. [Creating and Pushing to a Remote Repository (GitHub)](#creating-and-pushing-to-a-remote-repository-github)

---
  ### Git Project Creation and Workflow

*   **Git's Language Agnosticism**: Git doesn't care about the programming language; it tracks files and statements regardless of their content (e.g., Java, Python, JavaScript, or plain text).
*   **Editor/IDE**: The instructor uses **VS Code**. You can use any editor, but VS Code has an inbuilt terminal.
*   **Creating a Project Folder**: Create a folder for your project; this is your **Working Directory**.
    *   Example: Create a folder named `first_project`.

    
*   **Git Areas (Conceptual)**:
  
    *   **Working Directory (Working Area)**: This is where you create and edit your files. Git has no idea what you're doing here until explicitly told.
    *   **Staging Area**: A temporary area where you place files you want Git to track for the next commit. You must explicitly add files here.
    *   **Commit History (Local Commits/Local Repository)**: Where Git stores committed versions of your files. Each commit creates a version.
    *   **Remote Repository**: A server (like GitHub) where you can push your local repository to collaborate or back up.

      
*   **Initializing a Local Git Repository**:
  
    *   Navigate to your project folder in the terminal.
    *   **Checking Git Status (Pre-Initialization)**:
        *   **Command**: `git status`
        *   **Output**: "fatal: not a git repository" if not initialized.
    *   **Initialize the Repository**:
        *   **Command**: **`git init`**
        *   **Output**: "Initialized empty Git repository in C:/.../first_project/.git/".
        *   This creates a **hidden `.git` folder** inside your working directory. This folder is where Git stores all its tracking information, including the staging area and commit history.
        *   By default, `git init` might create a `master` branch.
    *   **Deleting a `.git` Folder**: To remove Git from a project (e.g., if you want to re-initialize with a different branch name):
        *   Manually delete the hidden `.git` folder from your file explorer, or using command line (e.g., `rm -rf .git` on Linux/Mac, or `Remove-Item .git -Recurse -Force` on PowerShell).
    *   **Initializing with a Specific Branch Name (e.g., `main`)**:
        *   **Command**: **`git init -b main`**
        *   **Output**: "Initialized empty Git repository in C:/.../first_project/.git/".
        *   **Verification**: Run `git status` to confirm "On branch main".
*   **Creating and Managing Files**:
    *   Create a simple text file in your working directory (e.g., `my_first_code.txt`).
    *   Add some content (e.g., "Hello World") and **save the file**.
    *   **Checking File Status**:
        *   **Command**: `git status`
        *   **Output**: "Untracked files: my_first_code.txt". This means Git knows the file exists but isn't tracking it for version control.
          ---
        
*   **Adding Files to the Staging Area**:
    *   You need to tell Git which files to prepare for a commit.
    *   **Command**: **`git add <file_name>`** (e.g., `git add my_first_code.txt`)
    *   **Verification**: Run `git status` again.
        *   **Output**: "Changes to be committed: new file: my_first_code.txt". This indicates the file is now in the staging area.
    *   **Untracking from Staging**: (Mentioned, not used) `git rm --cached <file>`.
      
*   **Committing Changes (Saving a Version Locally)**:
    *   Committing creates a snapshot of the files in the staging area and records it in the commit history.
    *   **Checking Commit History (Pre-Commit)**:
        *   **Command**: `git log`
        *   **Output**: "Your current branch main does not have any commits yet".
    *   **Committing with a Message**: A commit message is essential to describe the changes.
        *   **Command**: **`git commit -m "Your commit message"`** (e.g., `git commit -m "My first commit"`)
            *   `-m`: Specifies the commit message directly.
            *   **Recommendation**: "Commit early and commit often". Commit messages should be logical (e.g., what features added, bugs resolved, issue tracking numbers).
        *   **Output**: Shows `1 file changed, 1 insertion`, and the commit hash.
  
    *   **Verification**:
        *   `git status` now shows "nothing to commit, working tree clean".
        *   `git log` now displays the commit details:
            *   **Commit Hash (Checksum)**: A unique 40-character SHA-1 hexadecimal number generated for every commit. Even a small change in data alters the checksum. Git typically displays the first 7 characters for brevity.
            *   Author (username and email).
            *   Date and time.
            *   Commit message.
            *   **Head**: A pointer indicating the currently active commit.
         
            ---

*   **Modifying an Existing File and Committing**:
    *   Modify `my_first_code.txt` (e.g., add an exclamation mark) and **save the file**.
    *   **Check Status**: `git status` will show "Changes not staged for commit: modified: my_first_code.txt".
    *   **Add to Staging**: **`git add my_first_code.txt`**
    *   **Commit**: **`git commit -m "My second commit"`**
    *   **Verification**: `git log` will show both commits, with the new one at the top.
      
*   **Skipping the Staging Area for Commits**:
    *   For tracked files that are modified, you can commit directly from the working directory.
    *   **Command**: **`git commit -a -m "Your commit message"`** (e.g., `git commit -a -m "Third commit"`)
        *   `-a` (or `--all`): Automatically stages all modified, tracked files before committing.
    *   **Verification**: `git log` will show the new commit.
      
*   **Finding Differences (`git diff`)**:
    *   Purpose: To see what changes have been made in files.
    *   Modify `my_first_code.txt` again (e.g., add new lines) and **save**.
    *   **Viewing changes in the Working Directory (not staged)**:
        *   **Command**: **`git diff`**
        *   **Output**: Shows lines added (green with `+`) and removed (red with `-`).
    *   **Adding to Staging**: **`git add my_first_code.txt`**
    *   **Viewing Changes in the Staging Area (staged but not committed)**:
        *   **Command**: **`git diff --staged`**
        *   If no changes in staging, it will show no difference.
    *   **Commit**: **`git commit -m "Story 3.1: User input"`**
    *   **Verification**: `git log`.
      ---
    
*   **Removing Files from Git Repository**:
    *   **Scenario**: You accidentally added a sensitive file (e.g., `credentials.txt`) containing passwords to your Git repository and committed it.
    *   **Adding Multiple Files to Staging**:
        *   Create `credentials.txt` (with sensitive info) and `readme.md`.
        *   Make changes to `my_first_code.txt`.
        *   `git status` shows modified and untracked files.
        *   **Command to add all files in the current directory to staging**: **`git add .`**
        *   `git status` now shows all files as "new file" or "modified".
        *   **Commit**: `git commit -m "Readme and Story 3.2"`.
    *   **Problem with direct deletion**: If you physically delete `credentials.txt` from your working directory, `git status` will show it as "deleted" but it's still in Git's history. You don't want to commit this deletion because the file's content would still be in past commits.
      
    *   **Correct Removal Process for Tracked Files (to remove from Git's history)**:
        1.  **Remove the file from Git's tracking (but keep local copy)**:
            *   **Command**: **`git rm --cached <file_name>`** (e.g., `git rm --cached credits.txt`)
            *   **Output**: "rm 'credits.txt'". `git status` will show "deleted" for the file, and it is now untracked (no longer under Git's version control).
        2.  **Physically delete the file from your working directory**: Manually delete `credits.txt` from the folder.
        3.  **Commit the removal**:
            *   **Command**: **`git commit -m "Remove the credits file"`**
        *   This ensures the file is no longer tracked by Git and its removal is recorded in the history, preventing accidental upload of future changes to this file.
---  
### Remote Repositories (Collaboration)

*   **Purpose**: To collaborate with others and share your local repository publicly or privately.
*   **Types of Remote Repository Hosting Platforms**:
    *   **GitHub**: Most famous for public repositories.
    *   **GitLab**: Often used by companies for private features.
    *   **Bitbucket**: Provided by Atlassian.
*   **GitHub Profile**: Having a GitHub profile is important, especially for interviews.
*   **Creating a GitHub Account**: Sign up on github.com.
*   **Exploring GitHub Projects**:
    *   You can search for any project, e.g., "Linux kernel".
    *   Project pages show:
        *   Source code, owner (e.g., Linus Torvalds for Linux kernel).
        *   Languages used (e.g., C, Shell, Python for Linux).
        *   Number of **contributors** (e.g., 14,000+ for Linux).
        *   **Stars**: To show appreciation for a project.
        *   **Forks**: Creating a personal copy of someone else's repository.
    *   **Getting Source Code from GitHub**:
        *   **Download Zip**: Downloads the entire source code as a compressed file.
        *   **Clone**: Copies the repository directly to your machine using Git.
            *   **Protocols**: **HTTPS** and **SSH** are two common protocols for cloning.
            *   **Command**: **`git clone <repository_URL>`** (e.g., `git clone https://github.com/torvalds/linux.git`). This downloads the entire project and its history.
---  

### Creating and Pushing to a Remote Repository (GitHub)

*   **Creating Your Own Remote Repository on GitHub**:
    1.  Log in to GitHub.
    2.  Click the **"+" icon** (top right) and select **"New repository"**.
    3.  **Owner**: Your GitHub ID.
    4.  **Repository Name**: Choose a unique name (e.g., `git-course`).
    5.  **Description**: Optional, but good practice (e.g., "Git course demo").
    6.  **Visibility**: Choose **Public** (anyone can see it) or **Private** (only invited collaborators can see it).
    7.  **Initialize with a README**: Optional. A `README.md` file typically describes the project, how to run it, and how to contribute.
    8.  **Add .gitignore**: (Mentioned, discussed later in the course not covered in this excerpt).
    9.  **Choose a license**: (Optional).
    10. Click **"Create repository"**.
    *   The new repository page will display a unique link for cloning/pushing (HTTPS and SSH options).
---  

*   **Connecting Your Local Repository to the Remote (SSH)**:
    *   **Advantages of SSH**: No need to repeatedly enter username/password for authentication when pushing/pulling. You set up your machine once with a key. HTTPS requires login every time.
    *   **Generating SSH Keys (Do this only once per machine)**:
        1.  Open your terminal.
        2.  **Command**: **`ssh-keygen -o`**
            *   **Output**: "Generating public/private rsa key pair.".
            *   **Enter file in which to save the key**: Press Enter for the default location (e.g., `~/.ssh/id_rsa`).
            *   **Enter passphrase (empty for no passphrase)**: Press Enter twice to leave it empty for simplicity.
            *   This creates two files: `id_rsa` (private key) and `id_rsa.pub` (public key) in your `~/.ssh` directory.
    *   **Viewing Your Public Key**:
        1.  Navigate to the SSH directory: `cd ~/.ssh`.
        2.  **Command**: **`cat id_rsa.pub`**
        3.  Copy the entire output (your public key).
    *   **Adding Your Public Key to GitHub**:
        1.  On GitHub, click your **profile picture** (top right) -> **Settings**.
        2.  In the left sidebar, click **"SSH and GPG keys"**.
        3.  Click **"New SSH key"**.
        4.  **Title**: Give it a descriptive name (e.g., "git course one").
        5.  **Key**: Paste your copied public key into the text area.
        6.  Click **"Add SSH key"**.
        *   Your local machine is now authenticated to interact with GitHub via SSH.
---  

*   **Pushing Your Local Project to the Remote Repository**:
  
    1.  **Prepare Local Project**:
        *   Create a local folder (e.g., `git_course`).
        *   Navigate into it: `cd git_course`.
        *   Create a sample file: **`echo "git course demo" > readme.md`**.
        *   Verify content: `cat readme.md`.
        *   Initialize Git locally: **`git init`** (or `git init -b main` if you prefer to start with main).
        *   Add file to staging: **`git add readme.md`**.
        *   Commit locally: **`git commit -m "First commit"`**.
        *   **Create/Rename Branch to `main`**: (If `git init` created `master` branch) **`git branch -M main`** (This command renames the current branch, typically `master`, to `main`.)
            *   *Note: The transcript shows `git branch main` which creates a `main` branch. If the current branch is still `master`, you would need to switch to `main` using `git switch main` or `git checkout main`.*
              
    2.  **Connect Local to Remote**:
        *   Go to your GitHub repository page and copy the **SSH URL** (e.g., `git@github.com:your_username/git-course.git`).
        *   **Command**: **`git remote add origin <SSH_URL>`** (e.g., `git remote add origin git@github.com:naveen/git-course.git`)
            *   `origin` is the default alias given to the remote repository. You can view remote origins with `git remote -v`.
              
    3.  **Push to Remote**:
        *   **Command**: **`git push -u origin main`**
            *   `-u` (or `--set-upstream`): Sets the upstream tracking reference. This means future `git push` or `git pull` commands from this branch won't need `origin main`.
        *   It will verify the SSH key.
        *   **Output**: Shows progress and completion.
          
    4.  **Verification**: Refresh your GitHub repository page to see the `readme.md` file and the commit.

*   **Subsequent Pushes after Initial Setup**:
    1.  Open your project in VS Code (or your editor).
    2.  Create a new file (e.g., `user_service.txt`), add content, and save.
    3.  Check status: `git status` (shows `user_service.txt` as untracked).
    4.  Add to staging: **`git add user_service.txt`**.
    5.  Commit locally: **`git commit -m "User service created"`**.
    6.  Push to remote: **`git push origin main`**.
    7.  Verify on GitHub; the new file and commit will appear.
    *   You can navigate GitHub's interface to see different commits and file changes within them.
---  

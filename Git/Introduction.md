
### Introduction to Git

*   **Purpose of Git**:
    *   **Version Control**: Tracking changes to files over time.
    *   **Collaboration**: Enabling multiple people to work on the same project efficiently.
      ---
*   **Application-Agnostic**: Git can be used for any type of application (mobile, web, enterprise) and even for non-software projects like writing a book or making videos.

  
*   **Ease of Use**: The tool itself is easy, but the concepts might be new.
*   **Interaction Methods**:
    *   Primarily through **commands** (command line).
    *   Can also be done via **GUI** (Graphical User Interface) provided by most IDEs (Integrated Development Environments). Working with the command line offers more power.
  ---  
  
### Understanding Version Control

*   **Definition of Git**: Git is a **distributed version control system**.
  
*   **Core Problem Git Solves**: When you work on a project (software, book, video), you create multiple updates or versions.
    *   **Issue with saving the same file**: Overwrites previous work, losing history.
    *   **Issue with creating new files/folders for each update**: Leads to messy directories like `quiz_app_final_final_final`.
    *   **Need to go back**: If new features introduce bugs, you might need to revert to a previous working version.
*   **Version Control Defined**: The ability to have versions or the power to go back to any previous version.
*   **Version Control System (VCS)**: A software system used to achieve version control. VCS also helps in **collaboration** when multiple people work on the same project.

---

### Types of Version Control Systems (VCS)

Version Control Systems can be categorized into three types:

1.  **Local Version Control Systems (LVCS)**:
   
    *   **Concept**: Developers save different versions of their work on their own local machine.
    *   **Methods**: Could involve folders within folders or a dedicated database on the machine.
    *   **Problems**:
        *   **Collaboration**: Difficult for multiple people to work on the same project.
        *   **Data Loss**: If the local machine crashes, all project data can be lost.
          
3.  **Centralized Version Control Systems (CVCS)**:
   
    *   **Concept**: Uses a **central repository** (a remote server) where all project files and their history are stored.
    *   **Process**: Users get a copy from the central system, make changes, and then save (commit) them back to the central system.
    *   **Advantage**: Everyone has access to the most recent code and can see what others are doing.
    *   **Problem**: **Single point of failure**. If the central server goes down, all data (history and current versions) is lost. While local copies of the *current* version might exist, the entire history would be gone.
      
4.  **Distributed Version Control Systems (DVCS)**:
   
    *   **Concept**: Each developer gets a **full local copy of the entire repository**, including its complete commit history, not just the current version.
    *   **Collaboration**: Developers can collaborate by sharing changes between their local repositories.
    *   **Advantages**:
        *   **Redundancy**: If the central server goes down, other developers still have the full history locally, preventing data loss.
        *   **Offline Work**: Developers can work on projects even without internet access because the entire history is on their local machine.
    *   **Examples of Remote Repositories for DVCS**: **GitHub**, **GitLab**, **Bitbucket** (Bitbucket is provided by Atlassian).

---  

### History of Git

*   **Open Source Context**: Git emerged from the needs of open-source projects, where many people worldwide contribute to a single project.
*   **Linux Kernel**: The Linux kernel, founded by **Linus Torvalds**, is a prime example of a large open-source project.
*   **Early Days (1991-2002)**: Contributions to Linux were managed by sending **patches** or **archive files**.
*   **BitKeeper Era (2002)**: The Linux community started using a **proprietary tool called BitKeeper** to manage contributions, which streamlined the process of sending code and merging. BitKeeper was initially free.
  
*   **The Shift (2005)**: BitKeeper changed its policy and started charging for its use. Since Linux was free and used globally, the community decided to move away from BitKeeper.
*   **Git's Creation**: **Linus Torvalds created Git in 2005** specifically to be different from BitKeeper and to address the community's needs.
  
*   **Key Features of Git**: It offers amazing features that make it stand out:
    *   **Simple to use**.
    *   **Fast**.
    *   Allows **branching** (a powerful concept for development).
    *   Is **fully distributed**, making it very famous.

---  

### Installing Git

*   **Why Command Line?**: To master Git and use its full features, working with the **command line is the way to go**.
*   **Verifying Git Installation**:
    *   Open your **Command Prompt (CMD)** or **PowerShell** on Windows, or **Terminal** on Mac.
    *   **Command**: `git version`
    *   **Mac**: If you have Xcode installed, Git is often installed by default.
    *   **Windows**: Git is typically not pre-installed.
    *   If Git is not installed, you'll see a message like "git is not recognized as a command".
      
*   **Downloading Git**:
  
    *   Go to **Google** and search for "git download" or visit the official website: **git-scm.com**.
    *   Select your **Operating System (OS)** (Windows, Mac, or Linux).
    *   For Windows, choose the **Standard Installer** (for single machine setup) or Portable (for multiple machines).
    *   Select the **bit version** (e.g., 64-bit) matching your machine.
      ---
    
*   **Git Setup Process (Windows Example)**:
  
    *   Run the downloaded installer (`.exe`).
    *   Click **Yes** to the prompt.
    *   **Accept the GNU General Public License**.
    *   Choose the **installation location** (default is usually fine).
    *   Select components (keep defaults, including **Git Bash** but the instructor prefers normal CMD).
    *   Choose your **default editor for Git**: The instructor recommends **Notepad** for beginners to avoid confusion with Vim commands.

      
    *   **Adjusting the Initial Branch Name**:
      
        *   By default, Git used to create a **"master"** branch.
        *   Recently, Git changed the default to **"main"** due to terminology sensitivity.
        *   Choose **"Let Git decide"** to use "main" as the default branch name for new repositories.
    *   Choose **"Git from the command line and also from 3rd-party software"** (recommended for CMD use).
    *   Use **OpenSSH**.
    *   Choose **OpenSSL library**.
    *   Configure **line ending conversions** (default is usually fine).
    *   Choose **fast-forward or merge** (default is fine).
    *   Enable **system caching**.
    *   Do not enable experimental features for beginners.
    *   Click **Install**.

*   **Post-Installation Verification**:
    *   After installation, **restart your Command Prompt/PowerShell**.
    *   Run **`git version`** again to confirm Git is recognized and shows its version.

---  

### Configuring Git Identity

*   **Importance**: Git needs to know who is making changes (committing code) because multiple people work on the same project. Each commit is associated with an identity.
  
*   **Checking Existing Configuration**:
    *   **Command**: `git config`
    *   To list all global configurations: **`git config --global --list`**
      
*   **Setting Your User Identity**: You need to set at least your username and email.
    *   **Setting Username**:
        *   **Command**: **`git config --global user.name "Your Name"`** (Replace "Your Name" with your actual name, e.g., "Naveen").
    *   **Setting Email**:
        *   **Command**: **`git config --global user.email "your_email@example.com"`** (Use the same email as your public repository account like GitHub).
    *   **Verification**: Run `git config --global --list` again to confirm the details are set.

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

### Tags

*   **Purpose**: Tags are used to mark specific points in the repository's history as important. They are typically used to mark **release versions** of software (e.g., V1.0, V2.0).
*   **Checking Existing Tags**:
    *   **Command**: **`git tag`**
    *   Initially, it will show no output if no tags exist.
*   **Types of Tags**:
    *   **Annotated Tagging**: Recommended for releases. It stores more information like the tagger's name, email, date, and a message. This information is stored as a full Git object.
    *   **Lightweight Tagging**: Simple pointer to a commit, no extra info stored.
*   **Creating an Annotated Tag**:
    *   **Command**: **`git tag -a <tag_name> -m "Tag message"`** (e.g., `git tag -a V1.0 -m "First release"`)
        *   `-a`: Specifies an annotated tag.
*   **Verifying Local Tags**:
    *   **Command**: `git tag` (will show `V1.0`).
*   **Viewing Tag Details**:
    *   **Command**: **`git show <tag_name>`** (e.g., `git show V1.0`)
    *   **Output**: Shows the tagger's information, the commit hash the tag points to, and the tag message.
*   **Pushing Tags to Remote Repository**:
    *   **Tags are NOT automatically pushed with `git push origin main`**.
    *   You must push them separately.
    *   **Command to push a specific tag**: **`git push origin <tag_name>`** (e.g., `git push origin V1.0`)
    *   **Command to push all tags**: **`git push origin --tags`** (not explicitly shown for all tags, but is the general command).
    *   **Process Example**:
        1.  Make changes to a file (e.g., `user_service.txt`) and save.
        2.  Stage: `git add user_service.txt`.
        3.  Commit: `git commit -m "Processing user data"`.
        4.  Push code to remote: `git push origin main`.
        5.  Create a new tag for the updated version: `git tag -a V1.1 -m "Daily release"`.
        6.  Verify local tags: `git tag` (shows `V1.0`, `V1.1`).
        7.  Push new tag to remote: `git push origin V1.1`.
    *   **Verification on GitHub**: Go to your repository on GitHub, click on "Tags" to see the pushed tags. You can download the source code at any specific tag.
---  

### Working with Other People's Repositories (Cloning and Exploring)

*   **Cloning for Exploration**: You can clone public repositories to explore their source code, commit history, and tags.
    *   **Example**: Cloning the **VS Code source code** from GitHub.
    *   Search for "vs code" on GitHub and find the official Microsoft repository.
    *   Observe its features: many stars, contributors, languages (TypeScript, JavaScript, CSS, HTML).
    *   Review tags and commit history on GitHub.
      
*   **Cloning the Repository**:
    1.  Copy the **HTTPS URL** for the repository (e.g., for VS Code).
    2.  Open your terminal (not in VS Code, for this example).
    3.  Navigate to your desired directory (e.g., your home folder).
    4.  **Command**: **`git clone <HTTPS_URL>`** (e.g., `git clone https://github.com/microsoft/vscode.git`).
        *   This will download the entire project history and files to your local machine.
          
*   **Exploring the Cloned Repository**:
    1.  Open the cloned folder in VS Code.
    2.  Open the terminal within VS Code.
    3.  **Viewing Commit History**:
        *   **Command**: **`git log`**
        *   **Output**: Shows a long list of commits with author, date, and message.
        *   Press `Q` to quit the log view.
        *   **Concise Log**: **`git log --pretty=oneline`**
            *   **Output**: Shows each commit on a single line with its hash and message. Useful for seeing how others write commit messages.      
    4.  **Viewing Tags**:
        *   **Command**: **`git tag`**
        *   **Output**: Displays all the tags (versions) of the project.
    5.  **Viewing Specific Tag Details**:
        *   **Command**: **`git show <tag_name>`** (e.g., `git show 1.79.0`)
        *   **Output**: Shows the tag information and the commit it points to.
      
      ---
    
*   **Attempting to Push Changes to a Cloned Public Repository**:
    1.  Make a change in one of the files in the cloned repository (e.g., in `cli.ts` in VS Code source) and save.
    2.  Check status: `git status` (shows modified file).
    3.  Stage changes: **`git add <file_path>`** (e.g., `git add src/vs/cli.ts`).
    4.  Commit locally: **`git commit -m "Major update"`**.
    5.  Attempt to push: **`git push origin main`**.
    6.  **Result**: You will get a "Permission denied" error. This is because you are not a direct contributor to the original repository.
    *   **Alternative**: To contribute to a public project, you typically **fork** the repository first (create your own copy on GitHub), make changes on your fork, and then create a **pull request** to the original repository (not covered in detail).
---  

### Branching

*   **Core Concept**: Branching is a powerful Git feature that makes it one of the best version control systems.
*   **What is a Branch?**: A branch represents an independent line of development.
*   **Main Branch**: By default, your work is done and pushed to the **`main`** branch (or `master` in older versions).
*   **Purpose of Branches**: To work on **experimental features, new features, or bug fixes** without affecting the stable `main` branch. This allows parallel development.
    *   If experimental code causes issues, it doesn't break the `main` branch.
    *   You can "time travel" between commits, but branches offer a cleaner workflow.
      
*   **Checking Current Branch**:
    *   **Command**: `git status` (shows "On branch main").
    *   **Command**: **`git branch`** (shows a list of local branches with a `*` next to the active one).
    *   **Command**: **`git branch --all`** (shows both local and remote branches).
      
*   **Creating a New Branch**:
    *   **Older Command (still widely used)**: **`git checkout -b <new_branch_name>`** (e.g., `git checkout -b feature_one`)
        *   `-b`: Creates the new branch.
        *   Automatically **switches** to the newly created branch.
        *   **Output**: "Switched to a new branch 'feature_one'".
    *   **Newer Command (Git 2.23+ for clarity)**: **`git switch -c <new_branch_name>`** (e.g., `git switch -c feature_two`)
        *   `-c` (or `--create`): Creates the new branch.
        *   Automatically **switches** to the newly created branch.
     
  
*   **Working on a Feature Branch**:
    1.  Ensure you are on the feature branch (check `git branch` for the `*`).
    2.  Make changes to your files (e.g., add a line "create an avatar for user" to `user_service.txt`) and save.
    3.  Check status: `git status` (shows "modified" files on `feature_one` branch).
    4.  Stage: `git add user_service.txt`.
    5.  Commit: **`git commit -m "Experimenting with user avatar"`**.
        *   This commit happens only on `feature_one`; the `main` branch has no idea about it.
    6.  Verify local commit: `git log` (shows the new commit on `feature_one`).
      
*   **Switching Between Branches**:
    *   **Command**: **`git switch <branch_name>`** (e.g., `git switch main`)
    *   **Command (Alternative)**: `git checkout <branch_name>`
    *   **Observe**: When you switch, the files in your working directory change to reflect the state of the branch you switched to.
    *   **Shortcut to Previous Branch**:
        *   **Command**: **`git switch -`** (This switches you back to the branch you were on immediately before).
          
*   **Deleting a Local Branch**:
    *   **Command**: **`git branch -d <branch_name>`** (e.g., `git branch -d feature_two`)
        *   `-d` (or `--delete`): Deletes the specified branch.
        *   You cannot delete the branch you are currently on.
    *   **Verification**: `git branch` (will show fewer branches).
      
*   **Pushing a Local Branch to Remote (GitHub)**:
    1.  Ensure you are on the branch you want to push (e.g., `feature_one`).
    2.  Make any desired changes (e.g., create `admin_service.txt` with content) and save.
    3.  Stage: `git add admin_service.txt`.
    4.  Commit: `git commit -m "Adding admin service"`.
    5.  Push the branch: **`git push origin <branch_name>`** (e.g., `git push origin feature_one`)
        *   **Output**: Confirms that a new branch was created on the remote.
    6.  **Verification on GitHub**: Refresh your repository page. You will now see multiple branches (e.g., `main` and `feature_one`). Switching to `feature_one` on GitHub will show the new files.

--- 
*   **How Branching Works (Under the Hood)**:
    *   When `git init` occurs, a `.git` folder is created.
    *   Each **commit** creates a **snapshot** of your files.
    *   Each snapshot is assigned a unique **commit ID (checksum/hash)**.
    *   **Pointers**:
        *   Branches are essentially **pointers** to specific commits.
        *   The **`HEAD`** pointer indicates the currently active branch or commit.
    *   **Commit Chain**: Each commit typically points to its **parent commit** (the commit immediately before it), forming a chronological chain.
    *   **Creating a Branch**: When you create a new branch (e.g., `feature_one`) from `main`, **both `main` and `feature_one` initially point to the same latest commit**.
    *   **Committing on a Feature Branch**: When you make new commits on `feature_one`, only the `feature_one` pointer moves forward to the new commit. The `main` branch pointer remains at the older commit, preserving its state.
      
    *   **Visualizing Branches**:
        *   **Command**: **`git log --graph`** (shows a textual representation of the commit history graph).
        *   **VS Code Git Graph Extension**:
            1.  Go to Extensions in VS Code.
            2.  Search for "Git Graph" and **install** it.
            3.  Click the Git/Source Control icon in the sidebar.
            4.  Click the "View Git Graph" button.
            *   This provides a visual representation of your commits, branches, and their relationships, showing parent commits and how branches diverge and merge.
---  
### Merging Branches

*   **Purpose**: To combine the changes from one branch (e.g., a feature branch) into another branch (e.g., `main`).
*   **Merge vs. Rebase**: Two primary ways to integrate changes. This section focuses on **`merge`**.
*   **Merging Process**:
    1.  **Ensure Current Branch is the Target**:
        *   You must be on the branch where you want to incorporate the changes (e.g., `main` branch).
        *   **Command**: **`git switch main`** (or `git checkout main`).
    2.  **Perform the Merge**:
        *   **Command**: **`git merge <source_branch_name>`** (e.g., **`git merge feature_one`**)
        *   **Output (if successful)**: Indicates that the merge is complete, often with a message like "Updating..." or "Merge made by the 'recursive' strategy".
        *   **Merge Conflicts**: Sometimes, Git cannot automatically combine changes (e.g., if the same lines of code were modified differently in both branches). This results in a "merge conflict," which needs to be manually resolved (not explicitly demonstrated in this section).
    3.  **Verification (Local)**:
        *   Check files in your working directory; the changes from the merged branch should now be present.
        *   Check commit history: `git log` or `git graph` will show the merge commit and the integrated changes.
*   **Best Practice Before Merging (Pulling Remote Changes)**:
    *   Before merging local branches, it's a good practice to **pull the latest changes from the remote repository** for the target branch. This ensures your local target branch is up-to-date with any changes pushed by collaborators, minimizing potential conflicts.
    *   **Command**: **`git pull origin <target_branch_name>`** (e.g., `git pull origin main`).
*   **Pushing Merged Changes to Remote**:
    *   After a successful local merge, the changes only exist in your local repository.
    *   You need to push these merged changes to the remote repository.
    *   **Command**: **`git push origin <target_branch_name>`** (e.g., `git push origin main`).
*   **Verification (Remote)**: Refresh your GitHub repository page and switch to the target branch (e.g., `main`). You will see the merged files and commits reflected.

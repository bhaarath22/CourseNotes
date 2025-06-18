---

## 📚 Index  

1. [Introduction to Git](#introduction-to-git)
2. [Understanding Version Control](#understanding-version-control)
3. [Types of Version Control Systems (VCS)](#types-of-version-control-systems-vcs)
4. [History of Git](#history-of-git)
5. [Installing Git](#installing-git)
6. [Configuring Git Identity](#configuring-git-identity)

---
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

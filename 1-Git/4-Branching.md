# Index

- [Branching](#branching)
- [Merging Branches](#merging-branches)

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

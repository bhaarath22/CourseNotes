# Index

- [Tags in Git](#tags-in-git)
- [Working with Other People's Repositories](#working-with-other-peoples-repositories)
- [Attempting to Push Changes to a Cloned Public Repository](#attempting-to-push-changes-to-a-cloned-public-repository)

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

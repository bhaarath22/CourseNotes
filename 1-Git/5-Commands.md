
### **1. Setup & Configuration**
| Command | Description |
|---------|-------------|
| `git config --global user.name "Name"` | Set global username |
| `git config --global user.email "email@example.com"` | Set global email |
| `git config --global core.editor "code --wait"` | Set default text editor (e.g., VSCode) |
| `git config --list` | List all Git configurations |
| `git help <command>` | Show help for a Git command |

---

### **2. Repository Management**
| Command | Description |
|---------|-------------|
| `git init` | Initialize a new Git repo |
| `git clone <repo-url>` | Clone a remote repo |
| `git remote add origin <url>` | Add a remote repository |
| `git remote -v` | List remote repositories |
| `git remote remove <name>` | Remove a remote |
| `git fetch` | Download remote changes (no merge) |
| `git pull` | Fetch + merge remote changes |
| `git push` | Upload local changes to remote |

---

### **3. Basic Workflow**
| Command | Description |
|---------|-------------|
| `git status` | Show changed/untracked files |
| `git add <file>` | Stage a file |
| `git add .` | Stage all changes |
| `git commit -m "Message"` | Commit staged changes |
| `git commit -am "Message"` | Stage & commit tracked files (skips `git add`) |
| `git log` | Show commit history |
| `git log --oneline` | Compact commit history |
| `git log --graph` | Show branch graph |
| `git show <commit-hash>` | Show changes in a commit |

---

### **4. Branching & Merging**
| Command | Description |
|---------|-------------|
| `git branch` | List local branches |
| `git branch -a` | List all branches (local + remote) |
| `git branch <branch-name>` | Create a new branch |
| `git checkout <branch>` | Switch to a branch |
| `git checkout -b <branch>` | Create & switch to new branch |
| `git switch <branch>` | Newer way to switch branches |
| `git merge <branch>` | Merge a branch into current branch |
| `git rebase <branch>` | Rebase current branch onto another |
| `git branch -d <branch>` | Delete a branch (safe) |
| `git branch -D <branch>` | Force delete a branch (unmerged) |

---

### **5. Undoing Changes**
| Command | Description |
|---------|-------------|
| `git restore <file>` | Discard unstaged changes |
| `git restore --staged <file>` | Unstage a file |
| `git reset --soft <commit>` | Undo commits (keeps changes staged) |
| `git reset --mixed <commit>` | Undo commits (keeps changes unstaged) |
| `git reset --hard <commit>` | **Danger!** Discard all changes |
| `git revert <commit>` | Create a new commit that undoes a previous commit |
| `git commit --amend` | Edit the last commit |

---

### **6. Stashing**
| Command | Description |
|---------|-------------|
| `git stash` | Temporarily stash changes |
| `git stash list` | List stashed changes |
| `git stash pop` | Apply & remove last stash |
| `git stash apply` | Apply stash (keep it in list) |
| `git stash drop` | Delete a stash |
| `git stash clear` | Delete all stashes |

---

### **7. Tagging**
| Command | Description |
|---------|-------------|
| `git tag` | List tags |
| `git tag v1.0.0` | Create a lightweight tag |
| `git tag -a v1.0.0 -m "Release"` | Create an annotated tag |
| `git push --tags` | Push tags to remote |
| `git tag -d v1.0.0` | Delete a local tag |
| `git push origin --delete v1.0.0` | Delete a remote tag |

---

### **8. Advanced & Useful Commands**
| Command | Description |
|---------|-------------|
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git blame <file>` | Show who changed each line |
| `git bisect` | Binary search to find buggy commit |
| `git cherry-pick <commit>` | Apply a specific commit |
| `git reflog` | Show all Git actions (helps recover lost commits) |

---

### **9. GitHub-Specific Commands**
| Command | Description |
|---------|-------------|
| `git push -u origin main` | Push & set upstream branch |
| `git push --force-with-lease` | Safer force push |
| `git pull --rebase` | Pull & rebase instead of merge |
| `git submodule add <repo-url>` | Add a submodule |

---

### **10. Cleanup & Maintenance**
| Command | Description |
|---------|-------------|
| `git gc` | Garbage collection (optimize repo) |
| `git prune` | Remove unreachable objects |
| `git clean -n` | **Dry run**: show files to be deleted |
| `git clean -f` | **Danger!** Delete untracked files |

---

### **Best Practices**
- **Before pushing**, always:
  ```bash
  git pull --rebase
  ```
- **Force push carefully**:
  ```bash
  git push --force-with-lease
  ```
- **Recover lost commits** using:
  ```bash
  git reflog
  git reset --hard <commit-hash>
  ```
---  
### **Basic `ls` Commands**
| Command | Description |
|---------|-------------|
| `ls` | List files/folders in current directory |
| `ls -l` | Long format (permissions, size, date) |
| `ls -a` | Show **hidden files** (starts with `.`) |
| `ls -lh` | Human-readable sizes (KB, MB) |
| `ls -t` | Sort by modification time (newest first) |
| `ls -R` | Recursive (show subfolder contents) |
| `ls -1` | One file/folder per line |

---

### **Git-Specific `ls` Usage**
| Command | Description |
|---------|-------------|
| `ls .git/` | List Git's internal files (CAUTION: Don't modify these!) |
| `ls --git-ignore` | Show files ignored by Git (requires modern `ls` versions) |
| `git ls-files` | **Better alternative**: List all tracked files |

---

### **Combining `ls` with Git**
1. **List only Git-tracked files:**
   ```bash
   ls $(git ls-files)
   ```

2. **List untracked files (not in Git):**
   ```bash
   ls --ignore=$(git ls-files | tr '\n' '|')
   ```

3. **List recently modified files (Git-aware):**
   ```bash
   ls -lt $(git ls-files)
   ```

---

### **Colorized Output**
| Command | Description |
|---------|-------------|
| `ls --color=auto` | Auto-colorize by file type |
| `ls --color=always` | Force colors (for piping) |
| `ls --group-directories-first` | Folders first |

---

### **Filtering Output**
| Command | Description |
|---------|-------------|
| `ls *.js` | List only `.js` files |
| `ls docs/` | List contents of `docs/` folder |
| `ls -d */` | List only directories |

---

### **Pro Tips**
1. **Alias for better `ls`:**  
   Add to your `~/.bashrc` or `~/.zshrc`:
   ```bash
   alias ll='ls -alFh --color=auto --group-directories-first'
   ```

2. **Git + `ls` combo:**  
   To see changed files:
   ```bash
   ls $(git diff --name-only)
   ```

3. **Count files:**  
   ```bash
   ls | wc -l  # Total files/folders
   git ls-files | wc -l  # Tracked files
   ```

---

### **Step-by-Step Creating a folder Commands**

#### **1. Navigate to Your Git Repository**
```bash
cd /path/to/your/repo
```
- Replace `/path/to/your/repo` with your actual repo path (e.g., `~/projects/my-repo`).

#### **2. Create a New Folder**
```bash
mkdir new-folder
```
- Replace `new-folder` with your desired folder name (e.g., `scripts`, `docs`).

#### **3. Navigate into the New Folder (Optional)**
```bash
cd new-folder
```
- (Optional) Move into the folder to add files later.

#### **4. Create a File Inside the Folder (Optional)**
```bash
touch file.txt
```
- Creates an empty file (e.g., `file.txt`) inside `new-folder`.

#### **5. Stage the New Folder for Git Tracking**
```bash
git add new-folder/
```
- Stages the folder and its contents (if any).

#### **6. Commit the Changes**
```bash
git commit -m "Add new-folder to the repo"
```

#### **7. Push to Remote (e.g., GitHub)**
```bash
git push origin main
```
- Replace `main` with your branch name if different (e.g., `master`).

---

### **Full Example Workflow**
```bash
# 1. Go to your repo
cd ~/projects/my-repo

# 2. Create a folder
mkdir assets

# 3. (Optional) Add a file inside it
touch assets/script.js

# 4. Stage the folder
git add assets/

# 5. Commit
git commit -m "Add assets folder for JavaScript files"

# 6. Push to GitHub
git push origin main
```

---

### **Key Notes**
- **If the folder is empty**, Git won’t track it until you add a file inside.
- Use `ls` to verify the folder was created.
- Use `git status` to check staged/unstaged changes.

### **Step-by-Step Creating a folder (with Rebase)**
#### **1. Navigate to Your Repo**
```bash
cd /path/to/your/repo
```

#### **2. Sync with Remote (Fetch + Rebase)**
```bash
git fetch origin
git rebase origin/main   # or your target branch (e.g., master)
```
- Ensures your local branch is up-to-date *without* merge commits.

#### **3. Create a New Folder**
```bash
mkdir new-folder
```

#### **4. Add a File (Optional)**
```bash
touch new-folder/example.txt
```

#### **5. Stage and Commit**
```bash
git add new-folder/
git commit -m "Add new-folder"
```

#### **6. Rebase Again (If Remote Changed)**
```bash
git fetch origin
git rebase origin/main
```
- Resolve any conflicts if they occur (edit files → `git add` → `git rebase --continue`).

#### **7. Push to Remote**
```bash
git push origin main
```
- If the push fails (due to rebase changing history), use:
  ```bash
  git push --force-with-lease
  ```

---

### **Why This Workflow?**
1. **Clean History**  
   - Avoids unnecessary merge commits (`Merge branch 'main' into...`).  
   - Keeps commits in a straight line.  

2. **Safer Than `git pull`**  
   - `git pull` does a merge by default, which can clutter history.  
   - `git fetch + git rebase` gives you control.  

3. **Force Push Safely**  
   - `--force-with-lease` ensures you don’t overwrite others’ work.  

---

### **Key Rebase Commands**
| Command | Purpose |
|---------|---------|
| `git rebase <branch>` | Rebase current branch onto `<branch>` |
| `git rebase --continue` | After resolving conflicts |
| `git rebase --abort` | Cancel rebase if something goes wrong |
| `git push --force-with-lease` | Safer alternative to `--force` |

---

### **Example Conflict Resolution**
1. During rebase, Git stops at conflicting files.  
2. Edit the files to fix conflicts.  
3. Mark as resolved:  
   ```bash
   git add conflicted-file.txt
   git rebase --continue
   ```

---

### **When NOT to Rebase**
- **Shared branches** (e.g., `main`/`master`) → Use `git merge` to avoid confusing others.  
- **Public commits** → Rebasing rewrites history, breaking others’ repos.  

---

### **Final Tip**  
For daily workflow, alias `git pull --rebase`:  
```bash
git config --global pull.rebase true
```
Now `git pull` will always rebase instead of merge!  

---  
### **1. `git rebase origin/main` (✅ Correct)**
```bash
git rebase origin/main
```
- **Meaning:** Rebase your current branch onto the **remote** `main` branch (fetched from `origin`)
- **What it does:**
  1. Fetches latest `main` from `origin` (if not already up-to-date)
  2. Replays your local commits on top of `origin/main`
- **When to use:** 99% of cases when you want to update your branch with remote changes.

### **2. `git rebase origin main` (❌ Usually Wrong)**
```bash
git rebase origin main
```
- **Meaning:** Tries to rebase **two arguments** (`origin` and `main`) onto your current branch (not what you want!)
- **What happens:**
  - Git gets confused (treats `origin` and `main` as two separate refs)
  - Often results in errors like:
    ```
    fatal: invalid upstream 'origin main'
    ```
- **Fix:** Remove the space (use `origin/main` instead).

---

### **Key Takeaways**
| Command | Correct? | Purpose |
|---------|----------|---------|
| `git rebase origin/main` | ✅ Yes | Rebase onto remote `main` branch |
| `git rebase origin main` | ❌ No | Git will reject this syntax |

---

### **Proper Rebase Workflow**
1. **Fetch latest changes first:**
   ```bash
   git fetch origin
   ```
2. **Rebase onto updated remote branch:**
   ```bash
   git rebase origin/main
   ```
3. **Resolve conflicts (if any), then continue:**
   ```bash
   git add .
   git rebase --continue
   ```
4. **Push (force if needed):**
   ```bash
   git push --force-with-lease
   ```

---

### **Why This Matters**
- `origin/main` refers to the **remote tracking branch** (what Git knows about the remote).
- Just `main` refers to your **local branch** (which may be outdated).
- The space in `origin main` makes Git look for two unrelated things.

---

### **Common Mistake Scenario**
```bash
# ❌ Wrong (space causes error)
git rebase origin main

# ✅ Correct (slash is needed)
git rebase origin/main
```
- `origin/main` = "the main branch on the server"
- `main` = "your local main branch"
- `origin main` = Gibberish to Git 😅

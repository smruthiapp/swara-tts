# 🤗 Contributing to Swara TTS
> **Note:** You can also refer to the [Github Official Docs](https://docs.github.com/en/pull-requests) for detailed steps.

## Steps To Follow
[1. Fork the Repository](#-1-fork-the-repository) <br>
[2. Clone Your Fork](#-2-clone-your-fork) <br>
[3. Navigate to the Cloned Repository](#-3-navigate-to-the-cloned-repository) <br>
[4. Create a New Branch](#-4-create-a-new-branch) <br>
[5. Make Changes](#-5-make-changes) <br>
[6. Commit Changes](#-6-commit-changes) <br>
[7. Push Changes](#-7-push-changes) <br>
[8. Create a Pull Request](#-8-create-a-pull-request) <br>
[9. Wait for Review](#-9-wait-for-review) <br>
[10. Keep Your Fork Updated](#-10-keep-your-fork-updated) <br>

## 🍴 1. Fork the Repository
- Visit the GitHub repository you want to contribute to.
- Click the "Fork" button in the top right corner of the repository's page.
- This creates a copy (fork) of the repository in your GitHub account.

## 📋 2. Clone Your Fork
Open your terminal or Git Bash.
Clone your forked repository to your local machine
```bash
git clone https://github.com/smruthiapp/swara-tts.git
```

## 📂 3. Navigate to the Cloned Repository
- Change into the directory of the cloned repository
```bash
cd repository
```

## 🌲 4. Create a New Branch
- Create a new branch for your changes. This helps keep your changes isolated:
```bash
git checkout -b feature-branch
```

## 📝 5. Make Changes
- Make the necessary changes to the files in your local repository using your preferred text editor or IDE.

## 💬 6. Commit Changes
- Stage the changes
```bash
git add .
```
- Commit the changes
```bash
git commit -m "Add a meaningful commit message"
```

## ⬆️ 7. Push Changes
- Push the changes to your fork on GitHub:
```bash
git push origin feature-branch
```

## 📩 8. Create a Pull Request
- Open your browser and go to your fork on GitHub.
- Switch to the branch you created (feature-branch).
- Click on the "New Pull Request" button.
- Set the base repository and branch to the original repository and branch.
- Set the head repository and branch to your fork and branch.
- Click "Create Pull Request."

## ⌛ 9. Wait for Review
- Repository maintainers will review your changes, ask for any necessary modifications, and eventually merge the pull request.

## 🌚 10. Keep Your Fork Updated
- Periodically, sync your fork with the original repository to incorporate any changes made by others:
```bash
git checkout main
git pull
git checkout feature-branch
git merge main
```


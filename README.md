# rvs: The Memory-Aware CLI for Developers

`rvs` (Revise) is a lightweight CLI tool designed for developers to master new concepts through **Spaced (1,3,7,14) Repetition Revision**. Stop forgetting what you learn in DSA, System Design, Development, or any other learning domain where you prepare notes.



## Installation

The recommended way to install `rvs` is using **pipx**. This ensures the tool is available globally and handles your system PATH automatically without requiring administrator rights.

### 1. Install pipx (If not already installed, run:)
- **Linux / macOS:**
  ```bash
  python3 -m pip install --user pipx
  python3 -m pipx ensurepath
  ```
  (Note: Restart your terminal or run source ~/.bashrc after this)

- **Windows**
  ```bash
  py -m pip install --user pipx
  py -m pipx ensurepath
  ```
  (Note: Close and restart your cmd/PowerShell after this)

### 2. Install rvs 
- **Clone the repository and install it globally, run:**
     ```bash
     git clone [https://github.com/hitesh-mulwani/rvs-tool.git](https://github.com/hitesh-mulwani/rvs-tool.git)
     cd rvs-tool
     pipx install .
     ```

### 3. Verify Installation 
- **To check if the tool is installed successfully, run:**
     ```bash
     rvs --help
     ```
     (If you see the rvs help menu, you are ready to go!)

## Universal Compatibility
Once installed via `pipx`, the `rvs` command works anywhere you have a terminal:

- **Standard Terminals:** Bash, Zsh, PowerShell, CMD.

- **IDE Terminals:** Integrated terminals inside VS Code, IntelliJ, PyCharm, etc.

-- **Any Directory:** You can use it in your Java/Cpp/Python projects, WebDev folders, or personal notes folders,etc.

## Usage
1. **Initialize tracking in your root directory (any folder in which you want to track you notes files):**
     Command: rvs init

2. **Add a file(in which you have taken notes) to start the tracking cycle (1, 3, 7, 14 days):**
     Command: rvs add file_name
     , eg: rvs add arrays.txt

3. **Check what you need to revise today:** 
     Command: rvs status  (run this command in the root directory, to see a table listing all the notes files and their revision status)

4. **Complete a revision session, mark it done and push it further the tracking cycle:**  
     Command: rvs done file_name
     , eg: rvs done arrays.txt

5. **Remove a file from tracking cycle:**
     Command: rvs remove file_name
     , eg: rvs remove arrays.txt

## How it works
`rvs` uses a simplified version of the Leitner System. When you mark a note as done, it schedules the next review based on increasing intervals. 

Stage 1: +1 Day 

Stage 2: +3 Days 

Stage 3: +7 Days 

Stage 4: +14 Days 

. After **4** successful reviews, the note is marked as **MASTERED**.

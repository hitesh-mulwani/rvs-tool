# rvs: The Memory-Aware CLI for Developers

`rvs` (Revise) is a lightweight CLI tool designed for developers to master new concepts through **Spaced Repetition**. Stop forgetting what you learn in DSA, System Design, Development or new documentation.



## 🚀 Installation

1. **Clone the repository:**
   git clone [https://github.com/hitesh-mulwani/rvs-tool.git](https://github.com/hitesh-mulwani/rvs-tool.git)

2. **Open in terminal:**
   cd rvs-tool

3. **Install locally:**
   pip install .

## 🛠 Usage
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

## 📊 How it works
`rvs` uses a simplified version of the Leitner System. When you mark a note as done, it schedules the next review based on increasing intervals. 

Stage 1: +1 Day 

Stage 2: +3 Days 

Stage 3: +7 Days 

Stage 4: +14 Days 

. After **4** successful reviews, the note is marked as **MASTERED**.

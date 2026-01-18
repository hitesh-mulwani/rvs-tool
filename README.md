# rvs: The Memory-Aware CLI for Developers

`rvs` (Revise) is a lightweight CLI tool designed for developers to master new concepts through **Spaced Repetition**. Stop forgetting what you learn in DSA, System Design, Development or new documentation.



## 🚀 Installation

1. **Clone the repository:**
   git clone [https://github.com/YOUR_USERNAME/rvs-tool.git](https://github.com/YOUR_USERNAME/rvs-tool.git)
   cd rvs-tool

2. **Install locally:**
   pip install .

## 🛠 Usage
1. **Initialize tracking in your notes directory:**
     rvs init

2. **Add a file to start the tracking cycle (1, 3, 7, 14 days):**
     rvs add arrays.txt

3. **Check what you need to revise today:** 
     rvs status

4. **Complete a revision session, mark it done and push it further the tracking cycle:**  
     rvs done arrays.txt

5. **Remove a file from tracking cycle:** 
     rvs remove arrays.txt

## 📊 How it works
`rvs` uses a simplified version of the Leitner System. When you mark a note as done, it schedules the next review based on increasing intervals. After **4** successful reviews, the note is marked as **MASTERED**.

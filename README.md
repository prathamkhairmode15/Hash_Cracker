# 🔐 Hash Cracker – Version 1

Hash Cracker is an **educational cybersecurity project** designed to demonstrate how cryptographic hash functions work and how weak passwords can be cracked using a **dictionary attack**.

This project is built strictly for **learning purposes**, helping students understand password security, hashing algorithms, and basic attack methodologies.

---

## 🎯 Objective

The main goal of Version 1 is to:
- Understand how hashing works
- Learn how dictionary attacks operate
- Demonstrate why weak passwords are dangerous
- Build a strong foundation for advanced versions

---

## 🧩 Features (Version 1)

### 1️⃣ Hash Generator
- Generates hashes from plain text input
- Supported algorithms:
  - MD5
  - SHA-1
  - SHA-256
- Helps verify and test hash cracking logic

---

### 2️⃣ Dictionary Attack Engine
- Cracks hashes using a predefined wordlist
- Reads passwords line-by-line from a `.txt` file
- Compares generated hashes with the target hash
- Stops immediately when a match is found

---

### 3️⃣ Result Panel
Displays clear and structured output:
- Cracking status (Success / Failure)
- Cracked password (if found)
- Hash algorithm used
- Number of attempts
- Time taken for the attack

---

### 4️⃣ Input Validation
- Prevents empty or invalid inputs
- Validates hash length based on algorithm
- Ensures correct algorithm selection

---

## 🏗️ Project Scope (Version 1)

- Dictionary-based attack only
- Single-threaded execution
- Small wordlist support (1k–10k words)
- CPU-based processing
- Local execution only
- No database usage
- No brute-force or hybrid attacks

---

## 🛠️ Technologies (Planned)
- Frontend: HTML, CSS, JavaScript
- Backend: Python
- Hashing Libraries: Built-in cryptographic libraries

---

## ⚠️ Ethical Disclaimer

> This project is intended **strictly for educational and learning purposes**.  
> Do not use this tool on real systems, leaked databases, or unauthorized data.

The developer is **not responsible** for misuse of this software.

---

## 🚀 Future Roadmap

- Version 2: Brute-force attacks, rule-based mutations
- Version 3: Advanced attacks, performance optimization, analytics
- Integration into a larger cybersecurity platform

---

## 📚 Learning Outcomes

By completing this project, you will understand:
- How hash functions work internally
- Why password salting is important
- How attackers exploit weak passwords
- Fundamentals of ethical cybersecurity research

---

## 📌 Status
🚧 Version 1 – Planning & Development Phase

---

## 🤝 Contributions
This project is currently under active development.  
Suggestions and improvements are welcome for learning purposes.

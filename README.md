# 🔐 Task 03 – Advanced Password Strength Checker

## 📌 Overview
This project is developed as **Task 03** of the **Cyber Security Internship**.  
It is an **advanced password strength checker** that evaluates passwords using **security-focused logic** rather than simple UI-based validation.

The tool analyzes passwords based on:
- Structural complexity
- Entropy (randomness)
- Common password risks
- Estimated crack time
- Real-world usage suitability

All processing is done **locally**, and **no passwords are stored or logged**.

---

## 🎯 Objectives
- Evaluate password strength using multiple security parameters
- Go beyond basic rule-based validation
- Detect commonly used and weak passwords
- Estimate resistance against brute-force attacks
- Provide actionable security feedback
- Maintain ethical handling of sensitive input

---

## 🔐 Password Evaluation Criteria

### ✅ Basic Security Checks
- Minimum length requirement
- Uppercase letters
- Lowercase letters
- Numeric characters
- Special characters

---

### 🔎 Advanced Security Analysis
- **Common Password Detection**  
  Identifies passwords found in widely used password lists

- **Entropy Calculation**  
  Measures actual randomness instead of just password length

- **Crack-Time Estimation**  
  Estimates how long an offline brute-force attack might take

- **Usage Recommendation**  
  Suggests appropriate use cases (e.g., social media, banking, admin)

- **Password Improvement Suggestion**  
  Generates a stronger alternative without storing the original password

---

## 🧱 Project Structure
```

SCT_CS_3/
│
├── main.py                   # CLI program with professional output
├── password_checker.py       # Core password analysis logic
├── common_passwords.txt      # List of commonly used weak passwords
└── README.md

````

---

## 🛠 Technologies Used
- Python 3
- Regular Expressions (`re`)
- Mathematical analysis (`math`)
- `getpass` module for secure input
- Standard Python libraries

---

## ⚙ How to Run
```bash
python main.py
````

> Password input is hidden to prevent shoulder surfing.

---

## 🖥 Command-Line Features

* Clean, professional CLI output
* Visual strength indicator
* Clear security feedback
* No graphical interface (logic-focused design)
* Continuous password checking loop

---

## 🔒 Security & Ethics

* Passwords are **never stored**
* Passwords are **never logged**
* No network communication
* All evaluation happens in memory
* Designed strictly for educational and ethical purposes


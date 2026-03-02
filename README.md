# ```               Automation Project               ```

# 🚀 LinkedIn Job Application Automation Bot (Python + Selenium)

> Automated LinkedIn job applications using Python and Selenium WebDriver.

A powerful **LinkedIn Job Application Automation Bot** built with **Python and Selenium** that automatically logs into LinkedIn, searches for targeted jobs (e.g., Python Developer roles), and applies to job listings with Easy Apply.

This project is ideal for:

* 🧑‍💻 Developers automating job search workflows
* 🎓 Students applying to multiple tech jobs
* 🤖 Python automation learners
* 🔎 Anyone exploring Selenium web automation

---

## 📌 Features

* 🔐 Secure LinkedIn login via credentials config
* 🔎 Automated job search (e.g., Python Developer in London)
* ⚡ Auto-apply to Easy Apply jobs
* 🧠 Customizable job filters
* 🛠 Built with Selenium WebDriver
* 📂 Config-based credential management
* 🧩 Easy to extend and modify

---

## 🛠 Tech Stack

* **Python 3**
* **Selenium WebDriver**
* **ChromeDriver**
* ConfigParser (for credentials management)

---

## 📂 Project Structure

```
linkedin-job-automation/
│
├── linkedin_job_automation.py   # Main automation script
├── config.ini                   # Stores LinkedIn credentials
├── requirements.txt             # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NoorMahammad-S/linkedin-job-automation.git
cd linkedin-job-automation
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* **Mac/Linux**

```bash
source venv/bin/activate
```

* **Windows**

```bash
.\venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install ChromeDriver

Download ChromeDriver matching your Chrome browser version and add it to your system PATH.

---

## 🔐 Configuration

Update the `config.ini` file:

```ini
[LinkedIn]
email = your_email@example.com
password = your_password
```

⚠️ **Security Tip:**
Never upload your real credentials to GitHub. Add `config.ini` to `.gitignore`.

---

## ▶️ How to Run

```bash
python linkedin_job_automation.py
```

The bot will:

1. Log in to LinkedIn
2. Search for "Python Developer" jobs in London
3. Automatically apply to Easy Apply job listings

You can modify:

* Job title
* Location
* Filters
* Application logic

---

## 🎯 Use Cases

* Automating repetitive job applications
* Learning Selenium browser automation
* Building resume-worthy Python automation projects
* Demonstrating real-world automation skills

---

## 🔎 SEO Keywords (for discoverability)

LinkedIn automation bot, LinkedIn job application bot, Python Selenium project, job automation script, LinkedIn Easy Apply bot, Python web automation, Selenium LinkedIn bot, automated job search Python.

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.

Automating LinkedIn actions may violate LinkedIn’s Terms of Service. Use responsibly and at your own risk.

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to:

* Improve automation logic
* Add smarter filtering
* Implement CAPTCHA handling
* Add logging & error handling
* Improve performance

Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

---

## ⭐ Support

If you found this project helpful:

* Star ⭐ the repository
* Share it with others
* Connect and collaborate

---

# Phone-Number-Filter
A simple Python script that extracts and filters Indian phone numbers from a text file, explicitly targeting numbers starting with a custom prefix (e.g., 6301). Supports both plain 10-digit numbers and numbers prefixed with +91.
# 📱 Phone Number Filter

This Python script extracts phone numbers from a text file and filters them based on a custom prefix (e.g., `6301`). It supports Indian phone numbers in the format `+91XXXXXXXXXX` or `XXXXXXXXXX. '

## ✅ Features

- Extracts all valid 10-digit Indian mobile numbers
- Supports both `+91` and plain formats
- Filters numbers based on custom prefix (e.g., `6301`)
- Saves filtered results to a text file
- Simple and easy-to-use

---

## 🧠 Use Case

You have a messy text file full of phone numbers and want to extract only those that start with a specific prefix like `6301.

---

## 🛠️ How It Works

1. Reads data from an input `.txt` file.
2. Extracts phone numbers using a regular expression.
3. Filters numbers that start with the desired prefix.
4. Writes filtered numbers to an output `.txt` file.

---

## 📂 Example

**Input File:**

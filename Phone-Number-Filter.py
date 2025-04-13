
---

## ▶️ Usage

### 🧾 Script

```python
import re

def extract_and_filter_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = file.readlines()

        phone_pattern = re.compile(r'\+91\d{10}|\d{10}')
        filtered_numbers = []

        for line in data:
            numbers = phone_pattern.findall(line)
            for number in numbers:
                number = number.lstrip('+91')
                if number.startswith('6301'):
                    filtered_numbers.append(number)

        with open(output_file, 'w') as file:
            file.write('\n'.join(filtered_numbers))

        print(f"Filtered numbers saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = r"C:\path\to\your\input.txt"
output_file = r"C:\path\to\your\output.txt"
extract_and_filter_numbers(input_file, output_file)

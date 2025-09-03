# IntputLib
[![PyPI](https://img.shields.io/pypi/v/intputlib?label=PyPI)](https://pypi.org/project/intputlib)

**Because typing `int(input())` everywhere is a rite of passage we'd rather skip.**

>⚠️ Disclaimer: This started as a joke among friends after someone accidentally typed intput. Don't take it too seriously.

---

## What is this?

IntputLib is a tiny Python library designed to save you from the repetitive strain of capturing numerical input from users. It handles the boring `try-except` loops so you can focus on the fun parts of your code.

No more writing this masterpiece of error-handling over and over again:

```python
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
```

---

## Installation

Just a simple pip install away (if only everything in life were this easy):

```bash
pip install intputlib
```

---

## Usage

Here’s how you can reclaim your time and sanity.

### Basic Integer Input

Use `intput()` as a smarter, more patient version of `int(input())`.

```python
from intputlib import intput

age = intput("Enter your age (or fake it, we won't judge): ")
print(f"You are {age} years old!")
```

### Integer Input with a Custom Error Message

Tired of the generic "invalid input"? Give your users a custom message.

```python
from intputlib import intput

score = intput("Enter your score: ", error_msg="Come on, numbers only!")
print(f"Your score: {score}")
```

### Integer Input within a Range

Keep your users in line by specifying a minimum and maximum value.

```python
from intputlib import intput_range

level = intput_range("Choose a level (1-10): ", min_val=1, max_val=10)
print(f"You selected level {level}!")
```

### Custom Error Message for Range Input

You can also customize the error message for out-of-range inputs.

```python
difficulty = intput_range(
    "Select difficulty (1-5): ",
    min_val=1,
    max_val=5,
    error_msg="Oops! Only numbers between 1 and 5 are allowed."
)
print(f"Difficulty set to {difficulty}")
```

### Basic Float Input

For when you need those decimal points.

```python
from intputlib import floatput

height = floatput("Enter your height in meters (e.g., 1.75): ")
print(f"Your height: {height} m")
```

---

## Features

-   **Simplified Input:** Read integers and floats with a single, clean function call.
-   **Hassle-Free Validation:** Automatically handles `ValueError` and keeps asking until a valid number is entered.
-   **Range Enforcement:** Easily restrict integer inputs to a specified range.
-   **Customizable Prompts:** Tailor your input prompts and error messages.
-   **No More Crashes:** Saves your scripts from the dreaded `ValueError` when a user types "abc" instead of "123".

---

## Why Use This?

Because life is too short to write the same validation loop for the hundredth time. Let `intput()` handle the nagging for you, so you can get back to building amazing things.

---

## License

MIT License. Because sharing is caring.


---



https://github.com/KaykCaputo/Intput-Lib

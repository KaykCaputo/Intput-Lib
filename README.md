# IntputLib

**Because typing `int(input())` everywhere is too mainstream.**

> ⚠️ Just a fun little project that started as a joke among friends.  
> Not meant to be taken too seriously.

---

## What is this?

IntputLib is a tiny Python library that solves the age-old struggle of reading integers from the user without the headache.  
No more repeating:

```python
x = int(input("Enter a number: "))
```

Over. And. Over. And over again.

> Remember, this started as a joke. Use responsibly (or not).

---

## Installation

Just install it with pip (if only life were this easy):

```bash
pip install intputlib
```

---

## Usage

### Basic integer input

```python
from intputlib import intput

age = intput("Enter your age (or fake it, we won't judge): ")
print(f"You are {age} years old!")
```

### Integer input with custom error message

```python
from intputlib import intput

score = intput("Enter your score: ", error_msg="Come on, numbers only!")
print(f"Your score: {score}")
```

### Integer input within a range

```python
from intputlib import intput_range

level = intput_range("Choose a level (1-10): ", min_val=1, max_val=10)
print(f"You selected level {level}!")
```

### Custom error message for range input

```python
difficulty = intput_range(
    "Select difficulty (1-5): ",
    min_val=1,
    max_val=5,
    error_msg="Oops! Only numbers between 1 and 5 are allowed."
)
print(f"Difficulty set to {difficulty}")
```

### Basic float input

```python
from intputlib import floatput

height = floatput("Enter your height in meters (e.g., 1.75): ")
print(f"Your height: {height} m")
```

### Float input with custom error message

```python
from intputlib import floatput

temperature = floatput(
    "Enter the current temperature in Celsius: ",
    error_msg="That's not a valid temperature! Please enter a number."
)
print(f"Current temperature: {temperature}°C")
```

---

## Features

- Reads an integer or float from user input.
- Customizable error messages.
- Supports integer input within a specified range.
- Keeps asking until you actually enter a valid number (like a patient yet persistent friend).
- Saves you from the eternal curse of `ValueError`.
- Purely for fun – not a serious library.

---

## Why use this?

Because `int(input())` is a pain, and life is too short for repetitive error handling.  
Just use `intput()`, `intput_range()` or `floatput()` and let Python handle the nagging for you.

> Remember, this library started as a joke among friends. Don't take it too seriously.

---

## License

MIT License. Because sharing is caring.

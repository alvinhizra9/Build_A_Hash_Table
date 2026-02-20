# HashTable Implementation

## Overview

This project demonstrates a custom implementation of a Hash Table data structure in Python. A hash table is a data structure that implements an associative array, a structure that can map keys to values.

---

## Skills Demonstrated

### 1. Object-Oriented Programming (OOP)
- **Class Definition**: Creating a `HashTable` class to encapsulate data and behavior
- **Constructor**: Using `__init__` to initialize the internal data structure
- **Methods**: Defining instance methods (`add`, `remove`, `lookup`, `hash`) that operate on instance data

### 2. Data Structures
- **Dictionary Operations**: Using Python's built-in `dict` as the underlying storage
- **Nested Dictionaries**: Implementing collision handling using nested dictionary structures
- **Hashing**: Creating a custom hash function to convert string keys into numerical indices

### 3. String Manipulation
- **Type Conversion**: Converting input parameters to strings using `str(param)`
- **Iteration**: Looping through string characters using `for char in param`
- **ASCII Values**: Using `ord()` function to get character ASCII values

### 4. Algorithm Concepts
- **Hash Function**: Implementing a simple additive hash function
- **Collision Handling**: Using chaining (nested dictionaries) to handle hash collisions
- **Time Complexity**: Basic operations (add, remove, lookup) have O(n) in worst case due to collision chaining, but typically O(1) for well-distributed keys

### 5. Python Fundamentals
- **Variable Assignment**: Storing values in instance and local variables
- **Conditional Statements**: Using `if`, `else`, and nested conditionals
- **Membership Testing**: Checking key existence with `in` operator
- **Dictionary Methods**: Using `.get()` for safe value retrieval

---

## Method Breakdown

| Method | Description | Skills Used |
|--------|-------------|-------------|
| `__init__` | Initializes empty collection | OOP, Dictionary initialization |
| `hash` | Converts key to hash value | String manipulation, iteration, ASCII |
| `add` | Inserts key-value pair | Dictionary nesting, conditionals |
| `remove` | Deletes key-value pair | Dictionary deletion, membership |
| `lookup` | Retrieves value by key | Dictionary access, None handling |

---

## Usage Example

```python
# Create a hash table instance
ht = HashTable()

# Add key-value pairs
ht.add("name", "John")
ht.add("age", 25)
ht.add("city", "Jakarta")

# Lookup values
print(ht.lookup("name"))  # Output: John
print(ht.lookup("age"))   # Output: 25

# Remove a key
ht.remove("age")
print(ht.lookup("age"))   # Output: None
```

---

## Key Python Concepts Applied

1. **Encapsulation**: Bundling data and methods that operate on that data within a class
2. **Abstraction**: Hiding the internal implementation details from the user
3. **Error Handling**: Gracefully handling cases where keys don't exist
4ic Code. **Python**: Using Python's idiomatic patterns like dictionary comprehensions and the `in` operator

---

## Conclusion

This HashTable implementation demonstrates proficiency in fundamental Python programming concepts including OOP, data structures, algorithms, and Python's built-in functions. It serves as a practical example of how to build a core data structure from scratch while applying best practices in Python code organization and documentation.

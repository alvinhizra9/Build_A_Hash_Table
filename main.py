class HashTable:
    """
    A simple hash table implementation that stores key-value pairs.
    Uses a basic hashing function to map keys to bucket indices.
    """
    
    def __init__(self):
        """
        Initialize an empty hash table.
        The collection dictionary will store hashed keys as outer keys,
        and nested dictionaries will hold the actual key-value pairs.
        """
        self.collection = {}
    
    def hash(self, param):
        """
        Generate a hash value for a given parameter.
        
        Args:
            param: The value to hash (will be converted to string)
            
        Returns:
            An integer hash value calculated by summing ASCII values
            of all characters in the string representation of the parameter
        """
        param = str(param)  # Convert input to string for character processing
        hashed_value = 0    # Initialize hash accumulator
        # Iterate through each character and add its ASCII value
        for char in param:
            hashed_value += ord(char)
        return hashed_value
    
    def add(self, key, value):
        """
        Add a key-value pair to the hash table.
        If the hashed key already exists, it will update the value
        or add a new key to that bucket.
        
        Args:
            key: The key to store
            value: The value to associate with the key
        """
        hashed_key = self.hash(key)  # Compute hash for the given key
        
        if hashed_key not in self.collection:
            # If this is the first entry for this hash, create a new bucket
            self.collection[hashed_key] = {key: value}
        else:
            # If bucket exists, either update existing key or add new key to bucket
            self.collection[hashed_key][key] = value
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        
        Args:
            key: The key to remove
            
        Note:
            Does nothing if the key or its hash doesn't exist in the table.
        """
        hashed_key = self.hash(key)  # Compute hash for the given key
        
        if hashed_key in self.collection:
            # Check if the specific key exists in the bucket
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]  # Delete the key-value pair
    
    def lookup(self, key):
        """
        Look up a value by its key in the hash table.
        
        Args:
            key: The key to search for
            
        Returns:
            The value associated with the key if found, None otherwise
        """
        hashed_key = self.hash(key)  # Compute hash for the given key
        
        if hashed_key in self.collection:
            # Return the value if key exists in the bucket, or None if not found
            return self.collection[hashed_key].get(key, None)
        
        return None  # Return None if the hash bucket doesn't exist


# Example usage demonstration
if __name__ == "__main__":
    # Create a new hash table instance
    ht = HashTable()
    
    # Add some key-value pairs
    ht.add("name", "John")
    ht.add("age", 30)
    ht.add("city", "New York")
    
    # Look up values
    print("Name:", ht.lookup("name"))    # Output: John
    print("Age:", ht.lookup("age"))       # Output: 30
    print("City:", ht.lookup("city"))     # Output: New York
    print("Unknown:", ht.lookup("email")) # Output: None
    
    # Remove a key
    ht.remove("age")
    print("Age after removal:", ht.lookup("age"))  # Output: None

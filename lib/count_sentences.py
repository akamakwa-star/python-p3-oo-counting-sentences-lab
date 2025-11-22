#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith(".")
    
    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
        if not self.value:
            return 0
        
        # Count sentences by counting sentence-ending punctuation marks
        # but treat consecutive punctuation as a single sentence
        count = 0
        in_punctuation = False
        
        for char in self.value:
            if char in ".?!":
                if not in_punctuation:
                    count += 1
                    in_punctuation = True
            else:
                in_punctuation = False
        
        return count

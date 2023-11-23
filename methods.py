class WordSet:
    def __init__(self):
        self.words = set()
        
    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
            
    def cleanText(text):
        # chaining functions
        text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
        return text.lower()
    
        
wordSet = WordSet()

wordSet.addText('Hi, I\'m Ryan! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
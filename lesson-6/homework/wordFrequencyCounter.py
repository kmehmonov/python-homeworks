
file_name = r"lesson-6/homework/sample.txt"

#decorator for cleaning string from punctuations
def clean_string(func):
    def wrapper(*args, **kwargs):
        """
        Clean string from .,!?;:
        """
        chars_for_deleting = ",.!?:;"
        table = str.maketrans("", "", chars_for_deleting)
        text = func(*args, **kwargs)
        return text.translate(table)
    return wrapper

#read text file and return cleaned content
@clean_string
def read_text(file_name) -> str:
    """
    Read the txt file
    """
    try:
        with open(file=file_name, mode="r") as f:
            file_content = f.read().lower()
            return file_content
    except IOError:
        print(f"{file_name} not found!")

text = read_text(file_name)

#convert word's list into set and get unique words
unique_words_set = set(text.split())

#count every unique word
uniquewordcounter = [(word, text.count(word)) for word in unique_words_set]

#sort unique word from many to small
uniquewordcounter = sorted(uniquewordcounter, key=lambda x: x[1], reverse=True)


#print top n common words
n = 5  # for default case
while True:
    print(f"Top common {n} word(s):")
    for i in range(n):
        print(f"{i + 1}. {uniquewordcounter[i][0]} - {uniquewordcounter[i][1]} times")
    
    try:
        n = int(input("To see top n common words, enter value of n: "))
    except ValueError:
        print("Please enter a valid number.")

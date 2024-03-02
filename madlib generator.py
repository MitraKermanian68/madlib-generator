with open("story.txt", "r") as f:
    story = f.read()
words = set()#set of words which are not repeated
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i +1]
        words.add(word)#set of words which are not repeated
        start_of_word = -1

# answers  ={ "<name>":"Mitra",
#            "<adjective1>": "beautiful",
#            "<place>": "NYC",
#            "<animal>": "horse",
#            "<emotion>": "sad",
#            "<object>": "owner",
#            "<character>": "girl",
#            "<terrain>": "grassy grounds",
#            "<weather_condition>": "rainy weather",
#            "<place2>": "cottage",
#            "<emotion2>": "happy",
#            "<adverb>": "happily"
#            }
        
answers = {}

for word in words:
    answer = input(f"Enter a {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
print(story)

#if you want to save the story in a file
# with open("story.txt", "w") as f:
#     f.write(story)
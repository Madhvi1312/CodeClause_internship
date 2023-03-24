from time import time

print('Press Enter to start typing or to break a new line')
print('Press Enter twice to finish typing')
input('--------------------------------------------------')

# record timestamp when user starts and finishes typing
start = time()

text = []
while True:
    line = input()
    if not line:
        break
    text.append(line)
    
end = time()

print('--------------------------------------------------')

elapsed_time = (end-start) / 60
chars_count = sum(len(item) for item in text)
words_count = chars_count / 5

wpm = round(words_count / elapsed_time)

print(f'Your average Words Per Minute (WPM) is {wpm}')

if wpm < 30:
    print('You should practice more to improve your typing speed.')
elif wpm < 40:
    print('Not bad, but still you need more practice.')
elif wpm < 50:
    print('You are an average typist.')
elif wpm < 60:
    print('Congratulations! You are above average.')
else:
    print('Awesome, you can now be a pro.')
    


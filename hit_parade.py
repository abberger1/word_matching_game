wc = 0
level = 0
score = 0
groups = {}

group = input('group: ')
game = input('match, word, or definition? (m/w/d): ')
print()

with open('group%s.txt' % group, 'r') as grouptxt:
    for line in grouptxt:
        line = line.strip('\n').split(',')
        groups[line[0]] = line[1:]

if game == 'w':  # guess the word
    for word in groups.keys():
        if level > 9:
            break
        print(groups[word][1])
        answer = input('word: ')
        if answer == word:
            print('correct')
            score += 1
        else:
            print('%s (%s)' % (word, groups[word][0]))
        level += 1
        print()

elif game == 'd':  # guess the definition
    for word in groups.keys():
        if level > 9:
            break
        wc = 0
        print(word)
        answer = input('definition: ')
        for i in groups[word][1].split(' '):
            i = i.replace(';', '')
            if i in answer:
                wc += 1
        if wc > 1:
            print('correct: %s' % (groups[word][1]))
            score += 1
        else:
            print('%s' % (groups[word][1]))
        level += 1
        print()

elif game == 'm':  # matching game
        n = 5 
        words, defs = list(groups.keys()), list(groups.values())
        while level < 5:

                vocab = words[level*n:(level*n)+n]
                answers = [x[1] for x in defs[level*n:(level*n)+n]]

                correct_pairs = sorted(list(zip(vocab, answers)), key=lambda x: x[0])
                jambled = sorted(list(zip(vocab, set(answers))), key=lambda x: x[0])

                for v, a in enumerate(jambled):
                    print(v, a)
                print()

                correct_order = map(int, input().split(' '))
                print()
                    
                marks = [jambled[x] for x in correct_order]

                for x in range(n):
                        if marks[x][1] ==  correct_pairs[x][1]:
                            print('correct')
                            score += 1
                        else:
                            print(correct_pairs[x][0])
                level += 1
                print("score: %s/%s" % ((score, level*n)))
                print()
        level *= n

else:
    raise ValueError('Incorrect game type, exiting')

        
print('score: %s/%s' % (score, level))
with open('scores.csv', 'a') as scores:
        scores.write('\n')
        scores.write('%s,%f,%s,%s' % (game, score/level, group, len(groups.keys())))
        
with open('scores.csv', 'r') as scores:
        marks, samples = 0, 0
        for line in scores:
                line = line.strip().split(',')
                if line[0] == game and line[2] == group:
                        marks += float(line[1])
                        samples += 1
        average = marks / samples
        print("game: %s group: %s avg_score: %s" % (game, group, round(average, 2)))

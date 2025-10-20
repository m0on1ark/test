print('mini quiz starts')
score = 0
question =[ {
        'question':'Who is pidoras',
        "options":['Nikita','Ilya','Ruslan'],
        'answer':'3'
    },
    {
        'question':'Who is loser',
        "options":['Nikita','Ilya','Ruslan'],
        'answer':'3'
    }
]
for i in range(0, len(question)):
    print(question[i]['question'])
    for q in range(0, len(question[i]["options"])):
        print(q+1 , question[i]["options"][q])
    answer = input()
    if answer == question[i]['answer']:
        print('right')
        score += 1    
    else:
        print('Incorrect')
print('your score is', score)
        




result = [('Kaixenix', '["2", "2", "4", "1", "1"]', '2023-05-06 15:15:44'), ('A', '["3", "3", "3", "3", "3"]', '2023-05-07 08:44:50'), ('ewr3', '["4", "3", "4", "3", "4"]', '2023-05-07 09:26:41'), ('ewr34354', '["4", "1", "3", "3", "3"]', '2023-05-07 09:27:29'), ('Kaixenix111', '["4", "3", "3", "3", "1"]', '2023-05-07 09:36:00'), ('Kaixenix32', '["1", "3", "3", "1", "3"]', '2023-05-07 09:37:27')]

import json
# print([].extend(1))

print(result)
scores = {}
for i in range(len(json.loads(result[0][1]))):
    i = i+1
    scores[i] = []
    for j, data in enumerate(result):
        lst = json.loads(data[1])
        print(scores)
        scores[i].append(int(lst[i-1]))
    
    scores[i] = sorted(scores[i])
        
        
print(scores)
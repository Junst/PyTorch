import torch

train_data = 'Arashi is the Japanese Idol Group which is doing dance and sing'

# 중복을 제거한 단어들의 집합인 단어 집합 생성.
word_set = set(train_data.split())

# 단어 집합의 각 단어에 고유한 정수 맵핑.
vocab = {word: i+2 for i, word in enumerate(word_set)}
vocab['<unk>']=0
vocab['<pad>']=1
print(vocab)
'''
# 단어 집합의 크기만큼의 행을 가지는 테이블 생성.
embedding_table = torch.FloatTensor([
                               [ 0.0,  0.0,  0.0],
                               [ 0.0,  0.0,  0.0],
                               [ 0.2,  0.9,  0.3],
                               [ 0.1,  0.5,  0.7],
                               [ 0.2,  0.1,  0.8],
                               [ 0.4,  0.1,  0.1],
                               [ 0.1,  0.8,  0.9],
                               [ 0.6,  0.1,  0.1],
                                [0.1,0.3,0.1],
                                [0.9,0.5,0.5],
                                [0.5,0.2,0.3],
                                [0.3,0.8,0.2],
])

sample = 'you sing the Arashi song'.split()
idxes = []

# 각 단어를 정수로 변환
for word in sample:
    try:
        idxes.append(vocab[word])
    # 단어 집합에 없는 단어일 경우 <unk>로 대체된다.
    except KeyError:
        idxes.append(vocab['<unk>'])
idxes = torch.LongTensor(idxes)

# 각 정수를 Index로 Embedding Table에서 값을 가져온다.
lookup_result = embedding_table[idxes, :]
print(lookup_result)

'''

import torch.nn as nn
embedding_layer = nn.Embedding(num_embeddings=len(vocab),
                               embedding_dim=3,
                               padding_idx=1)

print(embedding_layer.weight)

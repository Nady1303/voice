# https://github.com/snakers4/silero-models/
# V4
import os
import torch

import numpy as np

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'
file_name = 'output2.mp3'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

example_text = 'Старый дуб, весь преображенный, раскинувшись шатром сочной, ' \
               'темной зелени, млел, чуть колыхаясь в лучах вечернего солнца. ' \
               'Ни корявых пальцев, ни болячек, ни старого горя и недоверия – ничего не было видно. ' \
               'Сквозь столетнюю жесткую кору пробились без сучков сочные, молодые листья, так что верить нельзя было, ' \
               'что это старик произвел их. «Да это тот самый дуб», – подумал князь Андрей, и на него вдруг нашло ' \
               'беспричинное весеннее чувство радости и обновления.'
sample_rate = 48000
# `speaker` should be in aidar, baya, kseniya, xenia, eugene, random
speaker = 'aidar'

audio_paths = model.save_wav(text=example_text,
                             speaker=speaker,
                             sample_rate=sample_rate)
os.rename(audio_paths, file_name)
print(audio_paths)

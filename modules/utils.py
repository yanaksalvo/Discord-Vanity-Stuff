import itertools, threading, os, time

__lock__ = threading.RLock()

class FileManager:
    def __init__(self):
        self.xd = None

    def saveStats(data):
        with threading.Lock:
            with open(f'../data/results/result.txt', 'a+') as f:
                    f.write(f'{data}\n\n')
    
    @staticmethod
    def removeLiveFromFile(content: str, filePath: str):
        print(content)
        with __lock__:
            with open(filePath, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()

            with open(filePath, 'w', encoding='utf-8', errors='ignore') as f:
                for line in lines:
                    if line.strip('\n') != content:
                        f.write(line)
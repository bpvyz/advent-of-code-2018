from datetime import datetime as dt


with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


timeline = list()
for line in lines:
    event = dict()
    event['timestamp'] = dt.strptime(line.split(']')[0][1:], '%Y-%m-%d %H:%M')
    event['msg'] = line.split('] ', 1)[1].strip()
    timeline.append(event)

timeline = sorted(timeline, key=lambda k: k['timestamp'])

f = open("input_sorted.txt", "w+")
for elem in timeline:
    f.write(str(elem['timestamp'].month)+', '+str(elem['timestamp'].day)+', '+str(elem['timestamp'].hour)+', '+str(elem['timestamp'].minute)+', '+elem['msg']+'\n')
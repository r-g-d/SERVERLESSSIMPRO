with open('Trace\First500.txt','r') as f:
    for line in f:
        data=line.split(',')
        print(data[2])
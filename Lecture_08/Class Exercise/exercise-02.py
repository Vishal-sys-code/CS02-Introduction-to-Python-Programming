file = open("mbox-short.txt", "r")
count = 0
total = 0

for line in file:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    finding_float = line.find("0")
    float_indexing = line[finding_float:]
    float_num = float(float_indexing)
    total += float_num
    count += 1
average = total/count
print("Average Spam Confidence: ", average)
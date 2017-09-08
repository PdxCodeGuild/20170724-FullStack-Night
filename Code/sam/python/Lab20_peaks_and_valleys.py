data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    list_peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i+1] and data[i] > data[i-1]:
            list_peaks.append(i)
    return list_peaks
print(peaks(data))

def valleys(data):
    list_valleys = []
    for i in range(1, len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            list_valleys.append(i)
    return list_valleys
print(valleys(data))

def peak_and_valleys(data):
    list_combined = peaks(data)
    list_combined.extend(valleys(data))
    return list_combined

print(peak_and_valleys(data))
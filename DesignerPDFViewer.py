def designerPdfViewer(h, word):
    # Write your code here
    a = []
    dim = 0
    count = 0
    for i in word:
        count += 1
        dim = ord(i) % 97
        a.append(h[dim])
    
    return (max(a) * count)

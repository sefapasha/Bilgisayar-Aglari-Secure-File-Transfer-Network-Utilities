def fragment(data, size=1024):
    return [data[i:i+size] for i in range(0, len(data), size)]

def reassemble(fragments):
    return b''.join(fragments)

import psutil

def print_memory_usage():
    mem = psutil.virtual_memory()
    print(f"현재 사용 메모리: {mem.used / (1024 ** 2):.2f} MB")
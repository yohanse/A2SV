#dont pick and stay here 
import sys, threading
from functools import lru_cache
input = sys.stdin.readline


def main():
    pass


sys.setrecursionlimit( 1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()
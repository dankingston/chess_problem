from abc import ABC

import redis


class Store(ABC):
    """
    Abstract class for solution storage
    """
    def add_solutions(self, solutions: tuple):
        raise NotImplementedError

    def get_solutions(self) -> set:
        raise NotImplementedError

    def get_solution_count(self) -> int:
        raise NotImplementedError


class RedisStore(Store):
    """
    Stores solutions in redis.
    Slower than MemoryStore, but more stable for complex problems
    """
    key = "chess_solutions"

    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.clear()

    def add_solutions(self, solutions: tuple):
        self.r.sadd(self.key, *solutions)

    def get_solution_count(self) -> int:
        return self.r.scard(self.key)

    def get_solutions(self):
        return self.r.smembers(self.key)

    def clear(self):
        self.r.delete(self.key)


class MemoryStore(Store):
    """
    Stores solutions in a python set
    """
    def __init__(self):
        self.store = set([])

    def add_solutions(self, solutions: tuple):
        self.store.update(solutions)

    def get_solution_count(self) -> int:
        return len(self.store)

    def get_solutions(self):
        return self.store

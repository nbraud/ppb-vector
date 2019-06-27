from hypothesis import given

from ppb_vector import Vector
from utils import vector_likes, vectors


@given(v=vectors())
def test_hash_tuple(v: Vector):
    assert hash(v) == hash(tuple(v))


@given(v=vectors())
def test_hash_vector_like(v: Vector):
    h = hash(v)
    for v_like in vector_likes(v):
        try:
            assert hash(v_like) == h
        except TypeError:
            pass

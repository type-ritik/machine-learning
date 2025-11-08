import numpy as np

v = np.array([[4, 5, 6]])  # Row
w = np.array([[10, 20, 30]])  # Row
u = np.array([0, 3, 6, 9])


def vec_add(v, w):
    """ "Vector Addition"""
    print("\nVector Addition:\n")

    # Row + Row
    v_plus_w = v + w
    # u_plus_w = u + w  # error! dimensions mismatched!

    print(f"v + w = {v_plus_w}")

    # Row + Column
    w = w.T  # w become column
    v_plus_w = v + w
    print(v_plus_w)


print("\n")


def vec_sub(v, w):
    """ "Vector Subtraction"""
    print("\nVector Subtraction:\n")

    # Row - Row
    v_minus_w = v - w
    # u_plus_w = u + w  # error! dimensions mismatched!

    print(f"v - w = {v_minus_w}")

    # Row - Column
    w = w.T  # w become column
    v_minus_w = v - w
    print(v_minus_w)


def sca_vecmul():
    """Scalar Vector Multiplication"""
    print("\nScalar Vector Multiplication:\n")
    s = 2
    a = [3, 4, 5]  # as list
    b = np.array(a)  # as np array
    # print(a * s)
    print(b * s)


def sca_vec_add():
    """Scalar Vector Addition"""
    print("\nScalar Vector Addition:\n")
    s = 2
    v = np.array([3, 6])
    print(s + v)


def vec_brc():
    """Vector BroadCasting"""
    v = np.array([[1, 2, 3]]).T  # col vector
    w = np.array([[10, 20]])  # row vector

    print(v + w)  # addtion with broadcasting
    print("\n")
    print(v.T + w.T)  # v : row vector, w : col vector


vec_brc()

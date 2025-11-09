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


def mag_uni_vec():
    """Vector Magnitude"""
    print("\nVector Magnitude:\n")
    v = np.array([1, 2, 3, 7, 8, 9])
    v_dim = len(v)  # math dimensionality
    v_mag = np.linalg.norm(v)  # math magnitude, length, or norm
    print(f"Vector Dimention: {v_dim}")
    print(f"Vector norm: {v_mag}")


def vec_dot_pro():
    """Vector Dot Product"""
    print("\nVector dot product:\n")
    v = np.array([1, 2, 3, 4])
    w = np.array([5, 6, 7, 8])
    s = -1  # Scalar
    dot = np.dot(v, w)
    dot_scale = np.dot(s * v, w)
    print(dot)
    print(dot_scale)


def dot_pro_dis():
    """Dot Product Distributive"""
    print("\nDot product distributive:\n")
    a = np.array([0, 1, 2])
    b = np.array([3, 5, 8])
    c = np.array([13, 21, 34])

    # the dot product is distributive
    res1 = np.dot(a, b + c)
    res2 = np.dot(a, b) + np.dot(a, c)

    print(res1)
    print(res2)


def hadamard_mult():
    """Hadamard Multiplication"""
    print("\nHadamard multiplication:\n")
    a = np.array([5, 4, 8, 2])
    b = np.array([1, 0, 0.5, -1])
    hadamard = a * b
    print(hadamard)


def out_pro():
    """Outer Product Multiplication"""
    print("\nOuter product multiplication:\n")
    a = np.array([1, 2, 3])
    b = np.array([4, 5]).T
    print(np.outer(a, b))


out_pro()

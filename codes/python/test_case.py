def test_1():
    from numpy import sqrt
    from mysqrt import sqroot
    small=1.0e-14

    xvalues=[0, 2, 100, 10000, 0.0001, 1e8]
    for x in xvalues:
        s=sqroot(x)
        s_numpy=sqrt(x)
        print(f"x={x} s={s} s_numpy={s_numpy}")
        assert (s-s_numpy) < small, f"square root disagrees with numpy square root for x={x}"

def test_2():
    from numpy import sqrt
    from mysqrt import sqroot
    small=1.0e-14

    xvalues=[0.0000000001, 100]
    for x in xvalues:
        s=sqroot(x)
        s_numpy=sqrt(x)
        print(f"x={x} s={s} s_numpy={s_numpy}")
        assert (s-s_numpy) < small, f"square root disagrees with numpy square root for x={x}"
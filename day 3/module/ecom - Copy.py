def discount(tp, per):
    dis = tp * per / 100
    tp1 = tp - dis
    return tp1

def gst(tp, gper=18):
    gp = tp * gper / 100
    tp2 = tp + gp
    return tp2

def generate(cart, dpr=0, gpr=18):
    tp = sum(cart.values())
    print(f"Cart Items: {cart}")
    print(f"Sub total: {tp}")
    dis = discount(tp, dpr)
    print(f"After {dpr}% discount: {dis}")
    gt = gst(dis, gpr)
    print(f"After {gpr}% GST: {gt}")
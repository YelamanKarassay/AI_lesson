# importing math and plot libraries
import numpy as np
import matplotlib.pyplot as plt


# finding h(x) function
def h(x):
    if x < - 1 or x > 1:
        y = 0
    else:
        y = (np.cos(50*x) + np.sin(20*x))
    return y


hv = np.vectorize(h)
X = np.linspace(-1, 2, num=1000)
plt.plot(X, hv(X))
plt.show()


def simple_greedy_search(func, start=0, N=100):
    x = start
    history = []
    for i in range(N):
        history.append(x)  # keep track steps
        u = 0.001  # np.random.rand() # some noise
        x_left, x_right = x - u, x + u
        y_left, y_right = func(x_left), func(x_right)
        if y_left > y_right:
            x = x_left
        else:
            x = x_right
    return x, history


x0, history = simple_greedy_search(hv, start=-0.02, N=100)
plt.plot(X, hv(X))
plt.scatter(x0, h(x0), marker='x', s=100)
plt.plot(history, hv(history))
plt.show()


def SA(search_space, func, T):
    scale = np.sqrt(T)
    start = np.random.choice(search_space)
    x = start * 1
    cur = func(x)
    history = [x]
    for i in range(1000):
        prop = x + np.random.normal()*scale
        if prop > 1 or prop < 0 or np.log(np.random.rand()) * T > ( func(prop) - cur):
            prop = x
        x = prop
        cur = func(x)
        T = 0.9 * T  # reduce Temperature by 10% each iteration
        history.append(x)
    return x, history


X = np.linspace(-1, 1, num=1000)
x1, history = SA(X, h, T=4)
plt.plot(X, hv(X))
plt.scatter(x1, hv(x1), marker='x')
plt.plot(history, hv(history))
plt.show()
print(h(history[-1]))







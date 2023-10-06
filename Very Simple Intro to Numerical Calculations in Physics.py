# import module
import matplotlib.pyplot as plt

# input parameters
s = 2
g = 9.8
a = -g
v = 0
t = 0
dt = 0.1
t_list = []
s_list = []
s2_list = []

# numerical calculation
while s>0:
    v = v + a*dt
    s = s + v * dt
    t = t + dt
    s_list.append(s)
    t_list.append(t)

# visualization
plt.plot(t_list, s_list)
plt.show()


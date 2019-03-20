import matplotlib.pyplot as plt
import numpy as np

degRad = np.pi / 180
radDeg = 1 / degRad


def input_not_empty_only_numbers(msg):
    errmsg = 'Error : Please enter a number'
    inp = input(msg)
    if len(inp) == 0:
        print(errmsg)
        inp = input_not_empty_only_numbers(msg)

    inpnum = 0
    try:
        inpnum = float(inp)
    except:
        print(errmsg)
        inpnum = input_not_empty_only_numbers(msg)

    return inpnum


def input_not_empty_only_pos_numbers(msg):
    errmsg = 'Error : Please enter a positive number'

    inpnum = input_not_empty_only_numbers(msg)

    if inpnum < 0:
        print(errmsg)
        inpnum = input_not_empty_only_pos_numbers(msg)

    return inpnum


l1 = input_not_empty_only_pos_numbers('L1 : ')
l2 = input_not_empty_only_pos_numbers('L2 : ')
l3 = input_not_empty_only_pos_numbers('L3 : ')

q1s = input_not_empty_only_numbers('q1 start angle : ') * degRad
q1e = input_not_empty_only_numbers('q1 end angle : ') * degRad
while q1e < q1s:
    print('ERROR : q1 end angle must be greater than q1 start angle')
    q1e = input_not_empty_only_numbers('q1 end angle : ') * degRad

q2s = input_not_empty_only_numbers('q2 start angle : ') * degRad
q2e = input_not_empty_only_numbers('q2 end angle : ') * degRad
while q2e < q2s:
    print('ERROR : q2 end angle must be greater than q2 start angle')
    q2e = input_not_empty_only_numbers('q2 end angle : ') * degRad

q3s = input_not_empty_only_numbers('q3 start angle : ') * degRad
q3e = input_not_empty_only_numbers('q3 end angle : ') * degRad
while q3e < q3s:
    print('ERROR : q3 end angle must be greater than q3 start angle')
    q3e = input_not_empty_only_numbers('q3 end angle : ') * degRad

# l1 = 1
# l2 = 1
# l3 = 1
#
# q1s = 0 * degRad
# q1e = 90 * degRad
#
# q2s = -20 * degRad
# q2e = 20 * degRad
#
# q3s = 0 * degRad
# q3e = 160 * degRad

inc = input_not_empty_only_numbers('speed (The higher the speed the lower the accuracy) [1:10] : ')
while not (0 <= inc <= 10):
    print('ERROR : speed must be between 1 & 10 inclusive')
    inc = input_not_empty_only_numbers('speed [1:10] : ')

inc *= degRad

print('------------------------ In Progress ------------------------')

x = []
y = []

q1_Iterations = np.ceil((abs(q1s - q1e) * radDeg + 1) / (inc * radDeg))
q2_Iterations = np.ceil((abs(q2s - q2e) * radDeg + 1) / (inc * radDeg))
q3_Iterations = np.ceil((abs(q3s - q3e) * radDeg + 1) / (inc * radDeg))

# if q1_Iterations == 0:
#     q1_Iterations=1
# if q2_Iterations == 0:
#     q2_Iterations=1
# if q3_Iterations == 0:
#     q3_Iterations=1

noOfIterations = int(q1_Iterations * q2_Iterations * q3_Iterations)
counter = 0

i = q1s
while i <= q1e:

    if counter % 5 == 0:
        print(int(counter / noOfIterations * 100), '%')

    j = q2s
    while j <= q2e:

        k = q3s
        while k <= q3e:
            x.append(l1 * np.cos(i) + l2 * np.cos((i + j)) + l3 * np.cos((i + j + k)))
            y.append(l1 * np.sin(i) + l2 * np.sin((i + j)) + l3 * np.sin((i + j + k)))

            counter += 1

            k += inc

        j += inc

    i += inc

print(100, '%')
# print('counter =', counter, '-- noOfIteration', noOfIterations)

plt.rcParams['figure.figsize'] = [6.5, 6.5]

l123 = l1 + l2 + l3
plt.axis([-l123 * 1.1, l123 * 1.1, -l123 * 1.1, l123 * 1.1])

plt.plot(x, y, 'c.', [0, l1, l1 + l2, l123], [0, 0, 0, 0], 'rx')

plt.grid(True)
plt.show()

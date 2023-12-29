import matplotlib.pyplot as plt
import math

data = [i.split(",") for i in open("logs.txt").readlines()][1::]


def generate_plot_points(logs):

    plot_points_coordinates = [[], []]

    for i in range(0, len(logs)):
        log_set = logs[i]

        time = float(log_set[0])
        speed = float(log_set[2])
        g_force = float(log_set[3])
        aoa = float(log_set[4])
        athmosphere = float(log_set[-4])
        mass = float(log_set[-3])
        t_force = float(log_set[-1])

        if 80 < 90 - abs(aoa) < 100:
            snp = 120
        if 45 < 90 - abs(aoa) < 80:
            snp = 600
        if 90 - abs(aoa) < 45:
            snp = 500

        if i > 0:
            mpt = float(logs[i - 1][-3])
        else:
            mpt = mass

        vxt = (t_force / mpt) - (g_force / math.sin(math.radians(90 - abs(aoa)))) - ((0.82 * athmosphere * (speed ** 2) * snp) / (mpt * 90))
        vyt = (t_force / mpt) - (g_force / math.cos(math.radians(90 - abs(aoa)))) - ((0.82 * athmosphere * (speed ** 2) * snp) / (mpt * 90))

        plot_points_coordinates[0].append(time)
        plot_points_coordinates[1].append((((vxt ** 2) + (vyt ** 2)) ** 0.5) * time)

    return plot_points_coordinates


def graph(plot_points_coordinates):
    plt.plot(plot_points_coordinates)
    plt.xlabel("Время полета")
    plt.ylabel("Скорость аппарата")
    plt.show()


graph(generate_plot_points(data))

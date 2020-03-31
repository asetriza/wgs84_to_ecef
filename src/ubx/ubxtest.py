from mpl_toolkits.mplot3d import axes3d

import matplotlib.pyplot as plt


def main():
    gpgga = []
    f = open("ubxfile.ubx", "r", encoding="latin-1")
    a = f.read()
    s = a.split("\n")
    for i in s:
        g = i.find("GPGGA")
        if g != -1:
            gpgga.append(i)
        else:
            pass
    return gpgga


def convert(main):
    x_list = []
    y_list = []
    z_list = []
    for split in main:
        split1 = split.split(",")
        degr0 = "".join(map(str, list(str(split1[2]))[:2]))
        min0 = "".join(map(str, list(str(split1[2]))[2:]))
        split1[2] = float(degr0) + float(min0) * 0.0166667
        degr1 = "".join(map(str, list(str(split1[4]))[1:3]))
        min1 = "".join(map(str, list(str(split1[4]))[3:]))
        split1[4] = float(degr1) + float(min1) * 0.0166667
        split1[9] = float(split1[9]) + float(split1[11])
        x = split1[2]
        x_list.append(x)
        y = split1[4]
        y_list.append(y)
        z = split1[9]
        z_list.append(z)

    return x_list, y_list, z_list


x_list, y_list, z_list = convert(main())

# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")
# ax.scatter(x_list, y_list, z_list, c="r", marker="o")

# ax.set_xlabel("x axis")
# ax.set_ylabel("y axis")
# ax.set_zlabel("z axis")

# plt.show()


import pyproj


def wgstoecef():
    ecef = pyproj.Proj(proj="geocent", ellps="WGS84", datum="WGS84")
    lla = pyproj.Proj(proj="latlong", ellps="WGS84", datum="WGS84")
    lon, lat, alt = pyproj.transform(lla, ecef, x_list, y_list, z_list, radians=False)
    return lon, lat, alt


x1, y1, z1 = wgstoecef()

x_list_fd = []
y_list_fd = []
z_list_fd = []


for x_list_ff in x1[1:]:
    x_list_fa = x1[0] - x_list_ff
    x_list_fd.append(x_list_fa)

for y_list_ff in y1[1:]:
    y_list_fa = y1[0] - y_list_ff
    y_list_fd.append(y_list_fa)

for z_list_ff in z1[1:]:
    z_list_fa = z1[0] - z_list_ff
    z_list_fd.append(z_list_fa)


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x_list_fd, y_list_fd, z_list_fd, c="r", marker="o")

ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

plt.show()


if __name__ == "__main__":
    main()

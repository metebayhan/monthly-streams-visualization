import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

monthly_visitors = [9695, 7909, 10831, 12942, 12495, 16794,
                    14161, 12762, 12777, 12439, 10309, 8724]

edm_streams = [92, 109, 124, 70, 101, 79, 106, 101, 103, 90, 102, 106]
rock_streams = [67, 51, 57, 54, 83, 90, 52, 63, 51, 44, 64, 78]
hiphop_streams = [75, 75, 76, 71, 74, 77, 69, 80, 63, 69, 73, 82]

plt.figure(figsize=(12, 8))

ax1 = plt.subplot(1, 2, 1)

x_values = range(len(months))

ax1.plot(x_values, monthly_visitors, linestyle="-", marker="o")
ax1.set_xlabel("Months")
ax1.set_ylabel("Visitors")
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
ax1.set_title("Platform Visitors", y=1.05)

ax2 = plt.subplot(1, 2, 2)

ax2.plot(x_values, edm_streams,
         color="blue", linestyle="--", marker="s", label="EDM")

ax2.plot(x_values, rock_streams,
         color="orange", linestyle=":", marker="o", label="Rock")

ax2.plot(x_values, hiphop_streams,
         color="red", linestyle="-", marker="D", label="Hip-Hop")

ax2.legend(loc="upper right")
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
ax2.set_title("Monthly Streams", y=1.05)

plt.suptitle("Music Platform Analytics")

plt.savefig("music_platform.png")
plt.show()

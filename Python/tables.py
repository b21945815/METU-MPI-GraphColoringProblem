import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

columns = [
    "Algorithm Name", "Vertices Number", "Total Colors Used", "Execution Time (s)", "Edges Number", "Processor Number", "Speed Up", "Speed Up Compared To Sequential", "Efficiency"]
data = []

# Sequential Algorithm data
graph1Time = 0.00642
graph2Time = 0.16823
graph3Time = 8.45500
graph4Time = 12.10912
graph5Time = 42.58931
data.append(["Sequential Algorithm", 120, 9, graph1Time, 1276, 1, 1, 1, 1])
data.append(["Sequential Algorithm", 450, 27, graph2Time, 16750, 1, 1, 1, 1])
data.append(["Sequential Algorithm", 900, 124, graph3Time, 307350, 1, 1, 1, 1,])
data.append(["Sequential Algorithm", 2000, 212, graph4Time, 999836, 1, 1, 1, 1])
data.append(["Sequential Algorithm", 4000, 387, graph5Time, 4000268, 1, 1, 1, 1])


# Algorithm 3 data (20 process)
data.append(["Algorithm 3", 120, 9, 0.02517, 1276, 20, None, None, None])
data.append(["Algorithm 3", 450, 33,  0.79418, 16750, 20, None, None, None])
data.append(["Algorithm 3", 900, 194, 14.55715, 307350, 20, None, None, None])
data.append(["Algorithm 3", 2000, 234, 76.02719, 999836, 20, None, None, None])
data.append(["Algorithm 3", 4000, 414, 302.38693, 4000268, 20, None, None, None])

# Algorithm 3 data (10 process)
data.append(["Algorithm 3", 120, 10, 0.01293, 1276, 10, None, None, None])
data.append(["Algorithm 3", 450, 33, 0.37853, 16750, 10, None, None, None])
data.append(["Algorithm 3", 900, 223, 7.75743, 307350, 10, None, None, None])
data.append(["Algorithm 3", 2000, 235, 26.09329, 999836, 10, None, None, None])
data.append(["Algorithm 3", 4000, 427, 108.69300, 4000268, 10, None, None, None])

# Algorithm 3 data (5 process)
data.append(["Algorithm 3", 120, 9, 0.00676, 1276, 5, None, None, None])
data.append(["Algorithm 3", 450, 35, 0.16115, 16750, 5, None, None, None])
data.append(["Algorithm 3", 900, 257, 4.11753, 307350, 5, None, None, None])
data.append(["Algorithm 3", 2000, 238, 11.22696, 999836, 5, None, None, None])
data.append(["Algorithm 3", 4000, 432, 46.64757, 4000268, 5, None, None, None])

# Algorithm 3 data (1 process)
data.append(["Algorithm 3", 120, 9, 0.00220, 1276, 1, None, None, None])
data.append(["Algorithm 3", 450, 31, 0.03745, 16750, 1, None, None, None])
data.append(["Algorithm 3", 900, 213, 0.68530, 307350, 1, None, None, None])
data.append(["Algorithm 3", 2000, 226, 2.02227, 999836, 1, None, None, None])
data.append(["Algorithm 3", 4000, 402, 8.07757, 4000268, 1, None, None, None])

# Algorithm 2 Parallel data (20 process)
data.append(["Algorithm 2 Parallel", 120, 9, 0.00464, 1276, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 37, 0.03994, 16750, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 254, 0.82451, 307350, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 237, 3.40984, 999836, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 422, 15.20990, 4000268, 20, None, None, None])

# Algorithm 2 Parallel data (10 process)
data.append(["Algorithm 2 Parallel", 120, 10, 0.00671, 1276, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 36, 0.03755, 16750, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 256, 0.97374, 307350, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 238, 3.33260, 999836, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 427, 13.66263, 4000268, 10, None, None, None])

# Algorithm 2 Parallel data (5 process)
data.append(["Algorithm 2 Parallel", 120, 9, 0.01021, 1276, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 34,  0.05111, 16750, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 257, 1.01852, 307350, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 239, 3.35643, 999836, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 431, 13.81820, 4000268, 5, None, None, None])

# Algorithm 2 Parallel data (1 process)
data.append(["Algorithm 2 Parallel", 120, 9, 0.01136, 1276, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 31, 0.03829, 16750, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 213, 0.63781, 307350, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 226, 2.03849, 999836, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 402, 7.91643, 4000268, 1, None, None, None])

# Algorithm 2 Asynchronous data (20 process)
data.append(["Algorithm 2 Asynchronous", 120, 9, 0.01169, 1276, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 35, 0.02514, 16750, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 254, 0.44853, 307350, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 237, 2.39856, 999836, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 423, 10.55994, 4000268, 20, None, None, None])

# Algorithm 2 Asynchronous data (10 process)
data.append(["Algorithm 2 Asynchronous", 120, 10, 0.00515, 1276, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 36, 0.02864, 16750, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 256, 0.56731, 307350, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 239, 2.13509, 999836, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 427, 9.10110, 4000268, 10, None, None, None])

# Algorithm 2 Asynchronous data (5 process)
data.append(["Algorithm 2 Asynchronous", 120, 9, 0.01276, 1276, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 35, 0.02978, 16750, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 257, 0.63706, 307350, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 238, 2.19126, 999836, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 432, 9.20871, 4000268, 5, None, None, None])

# Algorithm 2 Asynchronous data (1 process)
data.append(["Algorithm 2 Asynchronous", 120, 9, 0.00256, 1276, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 31, 0.04092, 16750, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 213, 0.62861, 307350, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 226, 1.99119, 999836, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 402, 7.81853, 4000268, 1, None, None, None])

# Algorithm 2 Half Asynchronous data (20 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 9, 0.00126, 1276, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 35, 0.02901, 16750, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 254, 0.45066, 307350, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 237, 2.35325, 999836, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 423, 10.30127, 4000268, 20, None, None, None])

# Algorithm 2 Half Asynchronous data (10 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 10, 0.00099, 1276, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 36, 0.02854, 16750, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 256, 0.58485, 307350, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 239, 2.18218, 999836, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 427, 9.37863, 4000268, 10, None, None, None])

# Algorithm 2 Half Asynchronous data (5 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 9, 0.00117, 1276, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 35, 0.02925, 16750, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 257, 0.63806, 307350, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 238, 2.21830, 999836, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 432, 9.39012, 4000268, 5, None, None, None])

# Algorithm 2 Half Asynchronous data (1 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 9, 0.00221, 1276, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 31, 0.03734, 16750, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 213, 0.61871, 307350, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 226, 1.97406, 999836, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 402, 7.85125, 4000268, 1, None, None, None])

# Algorithm 2 Basic data (20 process)
data.append(["Algorithm 2 Basic", 120, 9, 0.00507, 1276, 20, None, None, None])
data.append(["Algorithm 2 Basic", 450, 34, 0.05127, 16750, 20, None, None, None])
data.append(["Algorithm 2 Basic", 900, 248, 1.31956, 307350, 20, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 229, 3.66196, 999836, 20, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 416, 15.38489, 4000268, 20, None, None, None])

# Algorithm 2 Basic data (10 process)
data.append(["Algorithm 2 Basic", 120, 9, 0.00504, 1276, 10, None, None, None])
data.append(["Algorithm 2 Basic", 450, 33, 0.05153, 16750, 10, None, None, None])
data.append(["Algorithm 2 Basic", 900, 282, 1.36041, 307350, 10, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 234, 3.69370, 999836, 10, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 425, 15.09729, 4000268, 10, None, None, None])

# Algorithm 2 Basic data (5 process)
data.append(["Algorithm 2 Basic", 120, 9, 0.00248, 1276, 5, None, None, None])
data.append(["Algorithm 2 Basic", 450, 33, 0.05550, 16750, 5, None, None, None])
data.append(["Algorithm 2 Basic", 900, 281, 1.27173, 307350, 5, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 240, 3.55083, 999836, 5, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 425, 14.39740, 4000268, 5, None, None, None])

# Algorithm 2 Basic data (1 process)
data.append(["Algorithm 2 Basic", 120, 9, 0.00237, 1276, 1, None, None, None])
data.append(["Algorithm 2 Basic", 450, 31, 0.03827, 16750, 1, None, None, None])
data.append(["Algorithm 2 Basic", 900, 213, 0.63627, 307350, 1, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 226, 2.02293, 999836, 1, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 402, 8.01947, 4000268, 1, None, None, None])

# Algorithm 1 Basic data (20 process)
data.append(["Algorithm 1 Basic", 120, 9, 0.00483, 1276, 20, None, None, None])
data.append(["Algorithm 1 Basic", 450, 34, 0.04726, 16750, 20, None, None, None])
data.append(["Algorithm 1 Basic", 900, 248, 0.92595, 307350, 20, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 229, 2.59361, 999836, 20, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 418, 10.84994, 4000268, 20, None, None, None])

# Algorithm 1 Basic data (10 process)
data.append(["Algorithm 1 Basic", 120, 10, 0.00414, 1276, 10, None, None, None])
data.append(["Algorithm 1 Basic", 450, 34, 0.04898, 16750, 10, None, None, None])
data.append(["Algorithm 1 Basic", 900, 282, 0.95736, 307350, 10, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 238, 2.48175, 999836, 10, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 421, 10.53467, 4000268, 10, None, None, None])

# Algorithm 1 Basic data (5 process)
data.append(["Algorithm 1 Basic", 120, 10, 0.00369, 1276, 5, None, None, None])
data.append(["Algorithm 1 Basic", 450, 32, 0.04558, 16750, 5, None, None, None])
data.append(["Algorithm 1 Basic", 900, 281, 0.87929, 307350, 5, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 241, 2.32715, 999836, 5, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 426, 9.80880, 4000268, 5, None, None, None])

# Algorithm 1 Basic data (1 process)
data.append(["Algorithm 1 Basic", 120, 9, 0.00096, 1276, 1, None, None, None])
data.append(["Algorithm 1 Basic", 450, 31, 0.01410, 16750, 1, None, None, None])
data.append(["Algorithm 1 Basic", 900, 213, 0.23319, 307350, 1, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 226, 0.74761, 999836, 1, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 402, 2.87307, 4000268, 1, None, None, None])

# Algorithm 1 Half Asynchronous data (20 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 9, 0.00386, 1276, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 35, 0.03047, 16750, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 254, 0.43247, 307350, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 237, 2.25712, 999836, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 423, 9.91814, 4000268, 20, None, None, None])

# Algorithm 1 Half Asynchronous data (10 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 10, 0.00099, 1276, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 36, 0.02748, 16750, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 256, 0.57172, 307350, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 239, 2.19140, 999836, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 427, 9.12877, 4000268, 10, None, None, None])

# Algorithm 1 Half Asynchronous data (5 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 9, 0.00110, 1276, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 35, 0.02812, 16750, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 257, 0.60912, 307350, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 238, 2.15515, 999836, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 432, 9.07190, 4000268, 5, None, None, None])

# Algorithm 1 Half Asynchronous data (1 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 9, 0.00086, 1276, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 31, 0.01478, 16750, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 213, 0.22940, 307350, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 226, 0.85918, 999836, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 402, 2.93826, 4000268, 1, None, None, None])
 
# Algorithm 1 Asynchronous data (20 process)
data.append(["Algorithm 1 Asynchronous", 120, 9, 0.00098, 1276, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 35, 0.03003, 16750, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 254, 0.44964, 307350, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 237, 2.39372, 999836, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 423, 10.11507, 4000268, 20, None, None, None])

# Algorithm 1 Asynchronous data (10 process)
data.append(["Algorithm 1 Asynchronous", 120, 10, 0.00103, 1276, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 36, 0.02599, 16750, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 256, 0.55460, 307350, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 239, 2.13714, 999836, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 427, 9.07619, 4000268, 10, None, None, None])

# Algorithm 1 Asynchronous data (5 process)
data.append(["Algorithm 1 Asynchronous", 120, 9, 0.00103, 1276, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 35, 0.02777, 16750, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 257, 0.60827, 307350, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 238, 2.12836, 999836, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 432, 8.99333, 4000268, 5, None, None, None])

# Algorithm 1 Asynchronous data (1 process)
data.append(["Algorithm 1 Asynchronous", 120, 9, 0.00086, 1276, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 31, 0.01393, 16750, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 213, 0.24091, 307350, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 226, 0.78135, 999836, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 402, 2.96202, 4000268, 1, None, None, None])

df = pd.DataFrame(data, columns=columns)


# Speed Up Compared To Sequential
df.loc[df['Vertices Number'] == 120, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 120, 'Execution Time (s)'].apply(
    lambda x: graph1Time / x
)
df.loc[df['Vertices Number'] == 450, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 450, 'Execution Time (s)'].apply(
    lambda x: graph2Time / x
)
df.loc[df['Vertices Number'] == 900, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 900, 'Execution Time (s)'].apply(
    lambda x: graph3Time / x
)
df.loc[df['Vertices Number'] == 2000, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 2000, 'Execution Time (s)'].apply(
    lambda x: graph4Time / x
)
df.loc[df['Vertices Number'] == 4000, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 4000, 'Execution Time (s)'].apply(
    lambda x: graph5Time / x
)


# Speed Up
for algorithm in df["Algorithm Name"].unique():
    if algorithm == "Sequential Algorithm":
        pass
    for vertices in df["Vertices Number"].unique():
        one_processor_time = df.loc[(df["Algorithm Name"] == algorithm) & (df["Vertices Number"] == vertices) & (df["Processor Number"] == 1), "Execution Time (s)"].values[0]
        
        df.loc[(df["Algorithm Name"] == algorithm) & (df["Vertices Number"] == vertices), "Speed Up"] = one_processor_time / df["Execution Time (s)"]


# Efficiency
df['Efficiency'] = df['Speed Up'] / df['Processor Number']


# Efficiency plot
filtered_df = df[(df["Vertices Number"] == 4000) & (df["Algorithm Name"] != "Sequential Algorithm") & (df["Processor Number"] != 1)]

plot_data = filtered_df.pivot(index="Processor Number", columns="Algorithm Name", values="Efficiency")

plot_data.plot(kind="bar", figsize=(10, 6), width=0.8)

plt.title("Efficiency Plot for 4000 Vertices")
plt.xlabel("Number of Processors")
plt.ylabel("Efficiency")
plt.xticks(rotation=0)
plt.legend(title="Algorithm Name")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.savefig("efficiency_plot_4000_vertices.png", dpi=300)


# Scalability plot against to sequential algorithm
filtered_df = df[(df["Vertices Number"] == 4000) & (df["Algorithm Name"] != "Sequential Algorithm")]

plt.figure(figsize=(10, 6))
for algorithm in filtered_df["Algorithm Name"].unique():
    algorithm_data = filtered_df[filtered_df["Algorithm Name"] == algorithm]
    plt.plot(
        algorithm_data["Processor Number"],
        algorithm_data["Speed Up Compared To Sequential"],
        marker="o",
        label=algorithm
    )

plt.title("Strong Scalability: Execution Time vs Number of Processors (4000 Vertices)")
plt.xlabel("Number of Processors")
plt.ylabel("Speed Up Compared To Sequential")
plt.xticks([1, 5, 10, 20]) 
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(title="Algorithm Name")
plt.tight_layout()

plt.savefig("strong_scalability_4000_vertices_against_sequential.png", dpi=300)


# Scalability plot
filtered_df = df[(df["Vertices Number"] == 4000) & (df["Algorithm Name"] != "Sequential Algorithm")]

plt.figure(figsize=(10, 6))
for algorithm in filtered_df["Algorithm Name"].unique():
    algorithm_data = filtered_df[filtered_df["Algorithm Name"] == algorithm]
    plt.plot(
        algorithm_data["Processor Number"],
        algorithm_data["Execution Time (s)"],
        marker="o",
        label=algorithm
    )

plt.title("Strong Scalability: Execution Time vs Number of Processors (4000 Vertices)")
plt.xlabel("Number of Processors")
plt.ylabel("Execution Time (s)")
plt.yscale("log") 
plt.xticks([1, 5, 10, 20]) 
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(title="Algorithm Name")
plt.tight_layout()

plt.savefig("strong_scalability_4000_vertices.png", dpi=300)


# Table
plt.figure(figsize=(12, 6))

plt.axis('off') 

table = plt.table(
    cellText=df.values, 
    colLabels=df.columns, 
    cellLoc='center', 
    loc='center', 
    colLoc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(columns))))

output_path = 'algorithm_performance_table.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')


# Small Table
df_formatted = df.copy()

numeric_cols = ["Execution Time (s)", "Speed Up", "Speed Up Compared To Sequential", "Efficiency"]
df_formatted[numeric_cols] = df_formatted[numeric_cols].map(lambda x: round(x, 3))
df_formatted = df_formatted.rename(columns={"Speed Up Compared To Sequential": "Speed Up S"})
filtered_df = df_formatted[df_formatted["Vertices Number"] == 4000]
columns_reordered = [
    "Algorithm Name", "Processor Number", "Total Colors Used", 
    "Execution Time (s)", "Speed Up", "Speed Up S", "Efficiency"
]
filtered_df_reordered = filtered_df[columns_reordered]
plt.figure(figsize=(12, 6))

plt.axis('off') 

table = plt.table(
    cellText=filtered_df_reordered.values, 
    colLabels=filtered_df_reordered.columns, 
    cellLoc='center', 
    loc='center', 
    colLoc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(columns))))
output_path = 'algorithm_performance_table_small.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')


# Number of Colors
filtered_data_for_plot = df[df["Vertices Number"] == 4000]

sequential_data = pd.DataFrame([
    ["Sequential Algorithm", 4000, 387, graph5Time, 4000268, 5, 1, 1, 1],
    ["Sequential Algorithm", 4000, 387, graph5Time, 4000268, 10, 1, 1, 1],
    ["Sequential Algorithm", 4000, 387, graph5Time, 4000268, 20, 1, 1, 1]
], columns=df.columns)

filtered_data_for_plot = pd.concat([filtered_data_for_plot, sequential_data], ignore_index=True)

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=filtered_data_for_plot,
    x="Processor Number",
    y="Total Colors Used",
    hue="Algorithm Name",
    marker="o"

)
plt.title("Number of Colors Used vs. Processors (4000 Vertices)", fontsize=14)
plt.xlabel("Number of Processors", fontsize=12)
plt.ylabel("Total Colors Used", fontsize=12)
plt.legend(title="Algorithm", fontsize=10)
plt.grid(True)
line_graph_path = 'colors_vs_processors_4000_vertices.png'
plt.savefig(line_graph_path, dpi=300, bbox_inches='tight')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

columns = [
    "Algorithm Name", "Vertices Number", "Total Colors Used", "Execution Time (ms)", "Edges Number", "Processor Number", "Speed Up", "Speed Up Compared To Sequential", "Efficiency"]
data = []

# Sequential Algorithm data
graph1Time = 8.452
graph2Time = 158.932
graph3Time = 8271.475
graph4Time = 12004.907
graph5Time = 45884.307
data.append(["Sequential Algorithm", 120, 9, graph1Time, 1276, 1, 1, 1, 1])
data.append(["Sequential Algorithm", 450, 31, graph2Time, 16750, 1, 1, 1, 1])
data.append(["Sequential Algorithm", 900, 213, graph3Time, 307350, 1, 1, 1, 1,])
data.append(["Sequential Algorithm", 2000, 226, graph4Time, 999836, 1, 1, 1, 1])
data.append(["Sequential Algorithm", 4000, 402, graph5Time, 4000268, 1, 1, 1, 1])


# Algorithm 3 data (20 process)
data.append(["Algorithm 3", 120, 9, 46.800, 1276, 20, None, None, None])
data.append(["Algorithm 3", 450, 33, 770.282, 16750, 20, None, None, None])
data.append(["Algorithm 3", 900, 194, 14207.009, 307350, 20, None, None, None])
data.append(["Algorithm 3", 2000, 234, 72957.942, 999836, 20, None, None, None])
data.append(["Algorithm 3", 4000, 414, 299794.850, 4000268, 20, None, None, None])

# Algorithm 3 data (10 process)
data.append(["Algorithm 3", 120, 10, 20.700, 1276, 10, None, None, None])
data.append(["Algorithm 3", 450, 33, 383.543, 16750, 10, None, None, None])
data.append(["Algorithm 3", 900, 223, 7877.266, 307350, 10, None, None, None])
data.append(["Algorithm 3", 2000, 235, 26453.797, 999836, 10, None, None, None])
data.append(["Algorithm 3", 4000, 427, 108753.795, 4000268, 10, None, None, None])

# Algorithm 3 data (5 process)
data.append(["Algorithm 3", 120, 9, 20.155, 1276, 5, None, None, None])
data.append(["Algorithm 3", 450, 35, 159.862, 16750, 5, None, None, None])
data.append(["Algorithm 3", 900, 257, 4184.521, 307350, 5, None, None, None])
data.append(["Algorithm 3", 2000, 238, 11334.316, 999836, 5, None, None, None])
data.append(["Algorithm 3", 4000, 432, 47136.295, 4000268, 5, None, None, None])

# Algorithm 3 data (1 process)
data.append(["Algorithm 3", 120, 9, 4.569, 1276, 1, None, None, None])
data.append(["Algorithm 3", 450, 31, 37.665, 16750, 1, None, None, None])
data.append(["Algorithm 3", 900, 213, 622.790, 307350, 1, None, None, None])
data.append(["Algorithm 3", 2000, 226, 1997.849, 999836, 1, None, None, None])
data.append(["Algorithm 3", 4000, 402, 7853.366, 4000268, 1, None, None, None])

# Algorithm 2 Parallel data (20 process)
data.append(["Algorithm 2 Parallel", 120, 9, 6.782, 1276, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 37, 32.713, 16750, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 254, 897.463, 307350, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 237, 3525.022, 999836, 20, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 422, 15262.056, 4000268, 20, None, None, None])

# Algorithm 2 Parallel data (10 process)
data.append(["Algorithm 2 Parallel", 120, 10, 2.397, 1276, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 36, 37.774, 16750, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 256, 981.186, 307350, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 238, 3356.692, 999836, 10, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 427, 13663.099, 4000268, 10, None, None, None])

# Algorithm 2 Parallel data (5 process)
data.append(["Algorithm 2 Parallel", 120, 9, 2.546, 1276, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 34, 49.453, 16750, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 257, 1021.068, 307350, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 239, 3401.228, 999836, 5, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 431, 13911.217, 4000268, 5, None, None, None])

# Algorithm 2 Parallel data (1 process)
data.append(["Algorithm 2 Parallel", 120, 9, 3.474, 1276, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 450, 31, 38.329, 16750, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 900, 213, 641.551, 307350, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 2000, 226, 2041.851, 999836, 1, None, None, None])
data.append(["Algorithm 2 Parallel", 4000, 402, 8049.329, 4000268, 1, None, None, None])

# Algorithm 2 Asynchronous data (20 process)
data.append(["Algorithm 2 Asynchronous", 120, 9, 1.633, 1276, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 35, 29.710, 16750, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 254, 456.145, 307350, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 237, 2449.661, 999836, 20, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 423, 10023.430, 4000268, 20, None, None, None])

# Algorithm 2 Asynchronous data (10 process)
data.append(["Algorithm 2 Asynchronous", 120, 10, 2.154, 1276, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 36, 25.158, 16750, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 256, 576.555, 307350, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 239, 2186.442, 999836, 10, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 427, 9205.074, 4000268, 10, None, None, None])

# Algorithm 2 Asynchronous data (5 process)
data.append(["Algorithm 2 Asynchronous", 120, 9, 1.700, 1276, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 35, 29.005, 16750, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 257, 639.132, 307350, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 238, 2225.327, 999836, 5, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 432, 9417.461, 4000268, 5, None, None, None])

# Algorithm 2 Asynchronous data (1 process)
data.append(["Algorithm 2 Asynchronous", 120, 9, 3.523, 1276, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 450, 31, 38.294, 16750, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 900, 213, 633.132, 307350, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 2000, 226, 1982.646, 999836, 1, None, None, None])
data.append(["Algorithm 2 Asynchronous", 4000, 402, 7874.620, 4000268, 1, None, None, None])

# Algorithm 2 Half Asynchronous data (20 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 9, 4.676, 1276, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 35, 29.268, 16750, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 254, 447.625, 307350, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 237, 2603.000, 999836, 20, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 423, 10489.482, 4000268, 20, None, None, None])

# Algorithm 2 Half Asynchronous data (10 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 10, 1.530, 1276, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 36, 25.745, 16750, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 256, 586.994, 307350, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 239, 2205.266, 999836, 10, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 427, 9414.263, 4000268, 10, None, None, None])

# Algorithm 2 Half Asynchronous data (5 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 9, 1.631, 1276, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 35, 30.800, 16750, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 257, 647.012, 307350, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 238, 2228.096, 999836, 5, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 432, 9434.396, 4000268, 5, None, None, None])

# Algorithm 2 Half Asynchronous data (1 process)
data.append(["Algorithm 2 Half Asynchronous", 120, 9, 3.301, 1276, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 450, 31, 41.391, 16750, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 900, 213, 632.419, 307350, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 2000, 226, 2009.661, 999836, 1, None, None, None])
data.append(["Algorithm 2 Half Asynchronous", 4000, 402, 7902.970, 4000268, 1, None, None, None])

# Algorithm 2 Basic data (20 process)
data.append(["Algorithm 2 Basic", 120, 9, 6.241, 1276, 20, None, None, None])
data.append(["Algorithm 2 Basic", 450, 34, 50.956, 16750, 20, None, None, None])
data.append(["Algorithm 2 Basic", 900, 248, 1335.502, 307350, 20, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 229, 3675.329, 999836, 20, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 416, 15570.496, 4000268, 20, None, None, None])

# Algorithm 2 Basic data (10 process)
data.append(["Algorithm 2 Basic", 120, 9, 3.020, 1276, 10, None, None, None])
data.append(["Algorithm 2 Basic", 450, 33, 52.920, 16750, 10, None, None, None])
data.append(["Algorithm 2 Basic", 900, 282, 1392.148, 307350, 10, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 234, 3776.056, 999836, 10, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 425, 15466.500, 4000268, 10, None, None, None])

# Algorithm 2 Basic data (5 process)
data.append(["Algorithm 2 Basic", 120, 9, 3.207, 1276, 5, None, None, None])
data.append(["Algorithm 2 Basic", 450, 33, 55.353, 16750, 5, None, None, None])
data.append(["Algorithm 2 Basic", 900, 281, 1272.174, 307350, 5, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 240, 3554.024, 999836, 5, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 425, 14531.024, 4000268, 5, None, None, None])

# Algorithm 2 Basic data (1 process)
data.append(["Algorithm 2 Basic", 120, 9, 3.454, 1276, 1, None, None, None])
data.append(["Algorithm 2 Basic", 450, 31, 38.110, 16750, 1, None, None, None])
data.append(["Algorithm 2 Basic", 900, 213, 631.266, 307350, 1, None, None, None])
data.append(["Algorithm 2 Basic", 2000, 226, 1988.701, 999836, 1, None, None, None])
data.append(["Algorithm 2 Basic", 4000, 402, 7969.456, 4000268, 1, None, None, None])

# Algorithm 1 Basic data (20 process)
data.append(["Algorithm 1 Basic", 120, 9, 6.907, 1276, 20, None, None, None])
data.append(["Algorithm 1 Basic", 450, 34, 48.888, 16750, 20, None, None, None])
data.append(["Algorithm 1 Basic", 900, 248, 947.621, 307350, 20, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 229, 2670.318, 999836, 20, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 418, 11000.017, 4000268, 20, None, None, None])

# Algorithm 1 Basic data (10 process)
data.append(["Algorithm 1 Basic", 120, 10, 24.956, 1276, 10, None, None, None])
data.append(["Algorithm 1 Basic", 450, 34, 80.331, 16750, 10, None, None, None])
data.append(["Algorithm 1 Basic", 900, 282, 1597.161, 307350, 10, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 238, 4208.394, 999836, 10, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 421, 16740.322, 4000268, 10, None, None, None])

# Algorithm 1 Basic data (5 process)
data.append(["Algorithm 1 Basic", 120, 10, 3.925, 1276, 5, None, None, None])
data.append(["Algorithm 1 Basic", 450, 32, 35.738, 16750, 5, None, None, None])
data.append(["Algorithm 1 Basic", 900, 281, 897.672, 307350, 5, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 241, 2418.635, 999836, 5, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 426, 9820.658, 4000268, 5, None, None, None])

# Algorithm 1 Basic data (1 process)
data.append(["Algorithm 1 Basic", 120, 9, 1.427, 1276, 1, None, None, None])
data.append(["Algorithm 1 Basic", 450, 31, 14.166, 16750, 1, None, None, None])
data.append(["Algorithm 1 Basic", 900, 213, 231.408, 307350, 1, None, None, None])
data.append(["Algorithm 1 Basic", 2000, 226, 739.419, 999836, 1, None, None, None])
data.append(["Algorithm 1 Basic", 4000, 402, 2828.746, 4000268, 1, None, None, None])

# Algorithm 1 Half Asynchronous data (20 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 9, 1.533, 1276, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 35, 26.328, 16750, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 254, 478.222, 307350, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 237, 2543.514, 999836, 20, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 423, 10332.066, 4000268, 20, None, None, None])

# Algorithm 1 Half Asynchronous data (10 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 10, 1.358, 1276, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 36, 29.690, 16750, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 256, 570.779, 307350, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 239, 2181.457, 999836, 10, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 427, 9260.948, 4000268, 10, None, None, None])

# Algorithm 1 Half Asynchronous data (5 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 9, 1.708, 1276, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 35, 28.789, 16750, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 257, 623.153, 307350, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 238, 2199.885, 999836, 5, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 432, 9216.474, 4000268, 5, None, None, None])

# Algorithm 1 Half Asynchronous data (1 process)
data.append(["Algorithm 1 Half Asynchronous", 120, 9, 1.399, 1276, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 450, 31, 13.864, 16750, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 900, 213, 233.49, 307350, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 2000, 226, 723.029, 999836, 1, None, None, None])
data.append(["Algorithm 1 Half Asynchronous", 4000, 402, 2882.596, 4000268, 1, None, None, None])
 
# Algorithm 1 Asynchronous data (20 process)
data.append(["Algorithm 1 Asynchronous", 120, 9, 1.568, 1276, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 35, 25.190, 16750, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 254, 433.054, 307350, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 237, 2238.551, 999836, 20, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 423, 10248.238, 4000268, 20, None, None, None])

# Algorithm 1 Asynchronous data (10 process)
data.append(["Algorithm 1 Asynchronous", 120, 10, 1.473, 1276, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 36, 27.766, 16750, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 256, 568.418, 307350, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 239, 2173.699, 999836, 10, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 427, 9205.467, 4000268, 10, None, None, None])

# Algorithm 1 Asynchronous data (5 process)
data.append(["Algorithm 1 Asynchronous", 120, 9, 1.704, 1276, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 35, 30.058, 16750, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 257, 614.497, 307350, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 238, 2162.219, 999836, 5, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 432, 8877.042, 4000268, 5, None, None, None])

# Algorithm 1 Asynchronous data (1 process)
data.append(["Algorithm 1 Asynchronous", 120, 9, 1.240, 1276, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 450, 31, 13.798, 16750, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 900, 213, 233.790, 307350, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 2000, 226, 737.270, 999836, 1, None, None, None])
data.append(["Algorithm 1 Asynchronous", 4000, 402, 2531.584, 4000268, 1, None, None, None])

df = pd.DataFrame(data, columns=columns)


# Speed Up Compared To Sequential
df.loc[df['Vertices Number'] == 120, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 120, 'Execution Time (ms)'].apply(
    lambda x: graph1Time / x
)
df.loc[df['Vertices Number'] == 450, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 450, 'Execution Time (ms)'].apply(
    lambda x: graph2Time / x
)
df.loc[df['Vertices Number'] == 900, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 900, 'Execution Time (ms)'].apply(
    lambda x: graph3Time / x
)
df.loc[df['Vertices Number'] == 2000, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 2000, 'Execution Time (ms)'].apply(
    lambda x: graph4Time / x
)
df.loc[df['Vertices Number'] == 4000, 'Speed Up Compared To Sequential'] = df.loc[df['Vertices Number'] == 4000, 'Execution Time (ms)'].apply(
    lambda x: graph5Time / x
)


# Speed Up
for algorithm in df["Algorithm Name"].unique():
    if algorithm == "Sequential Algorithm":
        pass
    for vertices in df["Vertices Number"].unique():
        one_processor_time = df.loc[(df["Algorithm Name"] == algorithm) & (df["Vertices Number"] == vertices) & (df["Processor Number"] == 1), "Execution Time (ms)"].values[0]
        
        df.loc[(df["Algorithm Name"] == algorithm) & (df["Vertices Number"] == vertices), "Speed Up"] = one_processor_time / df["Execution Time (ms)"]


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
        algorithm_data["Execution Time (ms)"],
        marker="o",
        label=algorithm
    )

plt.title("Strong Scalability: Execution Time vs Number of Processors (4000 Vertices)")
plt.xlabel("Number of Processors")
plt.ylabel("Execution Time (ms)")
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

numeric_cols = ["Execution Time (ms)", "Speed Up", "Speed Up Compared To Sequential", "Efficiency"]
df_formatted[numeric_cols] = df_formatted[numeric_cols].map(lambda x: round(x, 3))
df_formatted = df_formatted.rename(columns={"Speed Up Compared To Sequential": "Speed Up S"})
filtered_df = df_formatted[df_formatted["Vertices Number"] == 4000]
columns_reordered = [
    "Algorithm Name", "Processor Number", "Total Colors Used", 
    "Execution Time (ms)", "Speed Up", "Speed Up S", "Efficiency"
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
    ["Sequential Algorithm", 4000, 402, graph5Time, 4000268, 5, 1, 1, 1],
    ["Sequential Algorithm", 4000, 402, graph5Time, 4000268, 10, 1, 1, 1],
    ["Sequential Algorithm", 4000, 402, graph5Time, 4000268, 20, 1, 1, 1]
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

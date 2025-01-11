import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.table as tbl

data = {
    'Graph': ['games120.col', 'latin_square_10.col', 'le450_15d.col', 'C2000-5.mtx', 'C4000-5.mtx'],
    'Vertices': [120, 900, 450, 2000, 4000],
    'Edges': [1276, 307350, 16750, 999836, 4000268],
    'Source': [
        'https://mat.tepper.cmu.edu/COLOR/instances.html',
        'https://mat.tepper.cmu.edu/COLOR/instances.html',
        'https://mat.tepper.cmu.edu/COLOR/instances.html',
        'https://networkrepository.com/dimacs.php',
        'https://networkrepository.com/dimacs.php'
    ]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 2)) 
ax.axis('tight')
ax.axis('off')

table_data = [df.columns.to_list()] + df.values.tolist()
table = tbl.table(ax, cellText=table_data, colLabels=None, loc='center', cellLoc='center', colWidths=[0.2, 0.1, 0.1, 0.4])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.savefig('graph_data_table.png', bbox_inches='tight', dpi=300)
plt.show()
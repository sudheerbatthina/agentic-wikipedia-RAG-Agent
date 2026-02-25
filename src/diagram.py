# Create a clean, properly aligned enterprise architecture diagram
# and save it as a PNG file

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create figure
fig, ax = plt.subplots(figsize=(16, 4))
ax.set_xlim(0, 16)
ax.set_ylim(0, 4)
ax.axis('off')

# Box settings
box_width = 2.5
box_height = 1
y = 1.5

# X positions (evenly spaced)
x_positions = [0.5, 3.5, 6.5, 9.5, 12.5]

labels = [
    "User Question",
    "Retrieval Layer\n(Query Rewrite + FAISS + BGE)",
    "Reasoning Layer\n(Claims + Validation)",
    "Self-Reflection\n(Critique + Retry)",
    "Final Answer"
]

colors = [
    "#D9D9D9",   # Light Gray
    "#B7D7E8",   # Light Blue
    "#B6E3B6",   # Light Green
    "#F9E79F",   # Light Yellow
    "#D5B6E8"    # Light Purple
]

# Draw boxes
for x, label, color in zip(x_positions, labels, colors):
    rect = Rectangle((x, y), box_width, box_height, facecolor=color, edgecolor="black")
    ax.add_patch(rect)
    ax.text(x + box_width/2, y + box_height/2, label,
            ha='center', va='center', fontsize=10)

# Draw arrows
for i in range(len(x_positions) - 1):
    x_start = x_positions[i] + box_width
    x_end = x_positions[i + 1]
    ax.annotate("",
                xy=(x_end, y + box_height/2),
                xytext=(x_start, y + box_height/2),
                arrowprops=dict(arrowstyle="->"))

# Title
plt.title("Agentic Wikipedia QA System – Enterprise Architecture",
          fontsize=16, pad=20)

# Save file
output_path = str(Path(__file__).resolve().parents[1] / "assets" / "Agentic_Wikipedia_QA_Enterprise_Architecture.png")
plt.savefig(output_path, bbox_inches='tight', dpi=300)
plt.close()

output_path

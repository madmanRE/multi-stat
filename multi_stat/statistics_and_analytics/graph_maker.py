import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from .static.img.multistat.reviewer import check_files


def make_graph(data, page):
    date = str(data[page - 1][0].created)[:10]

    if check_files(f"{date}.jpg"):
        return f"img/multistat/{date}.jpg"

    else:
        title = [d.title for d in data[page - 1]]
        value = [d.income - d.all_expense for d in data[page - 1]]

        norm = Normalize(vmin=min(value), vmax=max(value))
        colors = [cm.viridis_r(norm(v)) for v in value]

        fig, ax = plt.subplots(figsize=(10, 6))

        bars = ax.barh(title, value, color=colors)

        ax.set_xlabel("Каналы трафика")
        ax.set_title(f"Прибыльность канала ({date})")
        ax.invert_yaxis()
        plt.tight_layout()
        plt.savefig(
            f"statistics_and_analytics/static/img/multistat/{date}.jpg", format="jpg"
        )
        return f"img/multistat/{date}.jpg"

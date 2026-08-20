from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = r"C:\Windows\Fonts\meiryo.ttc"
font_manager.fontManager.addfont(FONT)
plt.rcParams["font.family"] = "Meiryo"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42


def canvas(width: float, height: float):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    return fig, ax


def box(ax, xy, text, fc, ec, fs=10.0, lw=1.5, bold=False):
    x, y, w, h = xy
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.03,rounding_size=2.8",
            facecolor=fc,
            edgecolor=ec,
            linewidth=lw,
        )
    )
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        fontweight="bold" if bold else "normal",
        color="#172033",
        linespacing=1.08,
    )


def arrow(ax, start, end, color="#475569", lw=1.55, mutation_scale=13):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=mutation_scale,
            linewidth=lw,
            color=color,
            shrinkA=2,
            shrinkB=2,
        )
    )


def sharp_arrow(ax, start, end, color="#000000", lw=1.05, ms=13):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="->",
            mutation_scale=ms,
            linewidth=lw,
            color=color,
            shrinkA=1,
            shrinkB=1,
        )
    )


def elbow_arrow(ax, points, color="#000000", lw=1.05, ms=12):
    xs = [p[0] for p in points[:-1]]
    ys = [p[1] for p in points[:-1]]
    ax.plot(xs, ys, color=color, linewidth=lw, solid_capstyle="butt", solid_joinstyle="miter")
    ax.add_patch(
        FancyArrowPatch(
            points[-2],
            points[-1],
            arrowstyle="->",
            mutation_scale=ms,
            linewidth=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def tacseq_framework():
    """Exact-layout English-label copy of thesis generate_compact_pictures.py fig_3_1()."""
    fig, ax = canvas(8.8, 4.9)

    def rbox(x, y, w, h, text, fc="#f8fafc", ec="#9ca3af", fs=8.8, lw=0.9, bold=False):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=lw))
        ax.text(
            x + w / 2,
            y + h / 2,
            text,
            ha="center",
            va="center",
            fontsize=fs,
            fontweight="bold" if bold else "normal",
            color="#111827",
            linespacing=1.15,
        )

    def seq_bar(x, y, labels, colors, cell_w=3.7, cell_h=4.6):
        cur = x
        for lab, color in zip(labels, colors):
            ax.add_patch(Rectangle((cur, y), cell_w, cell_h, facecolor=color, edgecolor="#111827", linewidth=0.55))
            ax.text(cur + cell_w / 2, y + cell_h / 2, lab, ha="center", va="center", fontsize=6.8, fontweight="bold")
            cur += cell_w

    def seq_segments(x, y, segments, colors, unit_w=3.0, cell_h=4.6):
        cur = x
        for (lab, span), color in zip(segments, colors):
            width = unit_w * span
            ax.add_patch(Rectangle((cur, y), width, cell_h, facecolor=color, edgecolor="#111827", linewidth=0.55))
            ax.text(cur + width / 2, y + cell_h / 2, lab, ha="center", va="center", fontsize=6.2, fontweight="bold")
            cur += width
        return cur

    labels = ["P1", "P2", "P3", "P4", "P5"]
    base_colors = ["#dbeafe", "#dbeafe", "#dbeafe", "#dbeafe", "#dbeafe"]

    seq_bar(6.5, 76, labels, base_colors, cell_w=3.9)
    ax.text(16.3, 70.6, "Original PPI length sequence", ha="center", fontsize=8.0)
    rbox(29.4, 75.4, 12.2, 5.8, "Batch load", fc="#f1f5f9", fs=7.8)
    sharp_arrow(ax, (26.4, 78.3), (29.4, 78.3), lw=0.9, ms=10)

    rbox(46.4, 84.0, 13.5, 5.6, "Repetition", fc="#fee2e2", ec="#ef4444", fs=7.8)
    rbox(46.4, 66.8, 13.5, 5.6, "Shift", fc="#fef3c7", ec="#f59e0b", fs=7.8)
    sharp_arrow(ax, (41.6, 78.4), (46.4, 86.8), lw=0.9, ms=10)
    sharp_arrow(ax, (41.6, 78.4), (46.4, 69.6), lw=0.9, ms=10)

    rbox(62.0, 84.0, 13.5, 5.6, "Aggregation", fc="#ecfeff", ec="#0891b2", fs=7.8)
    rbox(62.0, 66.8, 13.5, 5.6, "Aggregation", fc="#ecfeff", ec="#0891b2", fs=7.8)
    sharp_arrow(ax, (59.9, 86.8), (62.0, 86.8), lw=0.9, ms=10)
    sharp_arrow(ax, (59.9, 69.6), (62.0, 69.6), lw=0.9, ms=10)

    rep_end = seq_segments(
        79.0,
        84.6,
        [("P1+P2", 2), ("P3", 1), ("P4", 1), ("P5", 1), ("P3", 1)],
        ["#fed7aa", "#fed7aa", "#fed7aa", "#fed7aa", "#fecaca"],
        unit_w=2.45,
        cell_h=4.5,
    )
    shift_end = seq_segments(
        79.0,
        67.4,
        [("P1+P2", 2), ("P4", 1), ("P3", 1), ("P5", 1)],
        ["#fde68a", "#fde68a", "#fef08a", "#fde68a"],
        unit_w=2.45,
        cell_h=4.5,
    )
    ax.text((rep_end + 97.6) / 2, 88.2, "$X_i$", ha="center", va="bottom", fontsize=8.0)
    ax.text((shift_end + 95.0) / 2, 71.0, "$X_j$", ha="center", va="bottom", fontsize=8.0)
    sharp_arrow(ax, (75.5, 86.8), (79.0, 86.8), lw=0.9, ms=10)
    sharp_arrow(ax, (75.5, 69.6), (79.0, 69.6), lw=0.9, ms=10)

    enc_x, enc_y, enc_w, enc_h = 62, 19, 20, 35
    ax.add_patch(Rectangle((enc_x, enc_y), enc_w, enc_h, facecolor="none", edgecolor="#93c5fd", linewidth=1.4))
    ax.text(enc_x + enc_w / 2, enc_y + enc_h + 1.4, "Encoder", ha="center", va="bottom", fontsize=8.4)
    enc_box_x, enc_box_w, enc_box_h, enc_gap = 64.5, 15, 5.8, 2.0
    enc_box_ys = [44.7, 36.9, 29.1, 21.3]
    enc_labels = ["Input sequence", "BiLSTM", "Attention pooling", "Representation $h$"]
    enc_colors = ["#e5e7eb", "#dbeafe", "#dcfce7", "#e0f2fe"]
    for y, label, color in zip(enc_box_ys, enc_labels, enc_colors):
        rbox(enc_box_x, y, enc_box_w, enc_box_h, label, fc=color, fs=8.0)
    enc_mid_x = enc_box_x + enc_box_w / 2
    for y in enc_box_ys[:-1]:
        ax.plot([enc_mid_x, enc_mid_x], [y, y - enc_gap], color="#111827", linewidth=0.8)

    elbow_arrow(ax, [(shift_end, 69.7), (95.0, 69.7), (95.0, 51.5), (82.0, 51.5)], lw=0.9, ms=10)
    elbow_arrow(ax, [(rep_end, 86.9), (97.6, 86.9), (97.6, 46.0), (82.0, 46.0)], lw=0.9, ms=10)

    proj_x, proj_y, proj_w, proj_h = 30, 18.5, 25, 31
    ax.add_patch(Rectangle((proj_x, proj_y), proj_w, proj_h, facecolor="none", edgecolor="#cbd5e1", linewidth=1.1))
    ax.text(proj_x + proj_w / 2, proj_y + proj_h + 1.4, "Projection head", ha="center", va="bottom", fontsize=8.4)
    proj_box_x, proj_box_w, proj_box_h, proj_gap = 33, 19, 5.8, 1.7
    proj_box_ys = [40.5, 33.0, 25.5]
    proj_labels = ["Linear 512→512", "LayerNorm + ReLU", "Linear 512→128"]
    for y, label in zip(proj_box_ys, proj_labels):
        rbox(proj_box_x, y, proj_box_w, proj_box_h, label, fc="#e5e7eb", fs=7.6)
    proj_mid_x = proj_box_x + proj_box_w / 2
    for y in proj_box_ys[:-1]:
        ax.plot([proj_mid_x, proj_mid_x], [y, y - proj_gap], color="#111827", linewidth=0.8)

    sharp_arrow(ax, (62, 43.6), (55, 43.6), lw=0.9, ms=10)
    sharp_arrow(ax, (62, 23.5), (55, 23.5), lw=0.9, ms=10)
    ax.text(58.5, 45.5, "$h_i$", ha="center", fontsize=8.0)
    ax.text(58.5, 25.4, "$h_j$", ha="center", fontsize=8.0)

    rbox(9, 31.0, 15, 9.0, "NT-Xent\nLoss", fc="#eff6ff", ec="#60a5fa", fs=8.4)
    elbow_arrow(ax, [(30, 43.6), (27, 43.6), (27, 37.5), (24, 37.5)], lw=0.9, ms=10)
    elbow_arrow(ax, [(30, 23.5), (27, 23.5), (27, 33.4), (24, 33.4)], lw=0.9, ms=10)
    ax.text(28.5, 45.6, "$u_i$", ha="center", fontsize=8.0)
    ax.text(28.5, 25.4, "$u_j$", ha="center", fontsize=8.0)

    cls_x, cls_w, cls_h = 86, 9.5, 6.2
    cls_y, out_y = 34.0, 24.0
    rbox(cls_x, cls_y, cls_w, cls_h, "Classifier", fc="#f0f9ff", ec="#38bdf8", fs=8.0)
    rbox(cls_x, out_y, cls_w, cls_h, "8 classes", fc="#f0fdf4", ec="#22c55e", fs=8.0)
    cls_mid_x = cls_x + cls_w / 2
    cls_mid_y = cls_y + cls_h / 2
    sharp_arrow(ax, (82, cls_mid_y), (cls_x, cls_mid_y), lw=0.8, ms=9)
    sharp_arrow(ax, (cls_mid_x, cls_y), (cls_mid_x, out_y + cls_h), lw=0.8, ms=9)
    ax.set_xlim(5.6, 98.4)
    ax.set_ylim(17.2, 93.2)

    fig.savefig(OUT / "tacseq-framework-en.pdf", bbox_inches="tight", pad_inches=0.04)
    fig.savefig(OUT / "tacseq-framework-en.png", dpi=360, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


def doh_framework():
    fig, ax = canvas(4.85, 2.75)

    def rbox(x, y, w, h, text, fc="#f8fafc", ec="#9ca3af", fs=6.0, lw=0.9, bold=False):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=lw))
        ax.text(
            x + w / 2,
            y + h / 2,
            text,
            ha="center",
            va="center",
            fontsize=fs,
            fontweight="bold" if bold else "normal",
            color="#111827",
            linespacing=1.16,
        )

    rbox(
        23,
        84,
        54,
        12,
        "Input: TLS flows (per host)\nno payload / resolver IP / SNI",
        fc="#f1f5f9",
        ec="#94a3b8",
        fs=6.0,
    )

    ax.plot([50, 50], [84, 76], color="#111827", linewidth=0.75)
    ax.plot([22, 78], [76, 76], color="#111827", linewidth=0.75)
    sharp_arrow(ax, (22, 76), (22, 67), lw=0.75, ms=8)
    sharp_arrow(ax, (78, 76), (78, 67), lw=0.75, ms=8)

    rbox(6, 58, 32, 9.5, "Single-flow metadata", fc="#f8fafc", ec="#94a3b8", fs=5.9)
    sharp_arrow(ax, (22, 58), (22, 47), lw=0.75, ms=8)
    rbox(8, 37, 28, 9.5, "Classifier\n(baseline)", fc="#e5e7eb", ec="#9ca3af", fs=5.8)

    rbox(62, 58, 32, 9.5, "Host window\n(length = W)", fc="#eff6ff", ec="#60a5fa", fs=5.8)
    sharp_arrow(ax, (78, 58), (78, 47), lw=0.75, ms=8)
    rbox(
        61,
        37,
        34,
        10.5,
        "Aggregate statistics\nflow count / spacing / size-dir",
        fc="#dcfce7",
        ec="#22c55e",
        fs=5.4,
    )
    sharp_arrow(ax, (78, 37), (78, 25), lw=0.75, ms=8)
    rbox(62, 15, 32, 9.5, "Classifier\n(context-aware)", fc="#f0f9ff", ec="#38bdf8", fs=5.6)

    elbow_arrow(ax, [(22, 37), (22, 7), (36, 7)], lw=0.7, ms=8)
    elbow_arrow(ax, [(78, 15), (78, 7), (64, 7)], lw=0.7, ms=8)
    rbox(36, 2, 28, 10, "Detection output\nshort-lived DoH or not", fc="#fff7ed", ec="#f97316", fs=5.4)

    fig.savefig(OUT / "doh-host-context-en.pdf", bbox_inches="tight", pad_inches=0.04)
    fig.savefig(OUT / "doh-host-context-en.png", dpi=360, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


if __name__ == "__main__":
    tacseq_framework()
    doh_framework()

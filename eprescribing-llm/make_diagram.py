"""Generate the use case diagram from domain.py.

Writes diagrams/usecase.puml (PlantUML) and diagrams/usecase.mmd (Mermaid flowchart).
If matplotlib is installed, also draws diagrams/usecase.png.
    python make_diagram.py
"""
from __future__ import annotations

import config
import domain

ACTOR_ORDER = ["Prescriber", "Pharmacy system", "Drug knowledge base", "Credential provider", "Compliance officer"]


def _actor_id(name: str) -> str:
    return "A" + str(ACTOR_ORDER.index(name) + 1)


def plantuml() -> str:
    out = ["@startuml", "left to right direction", "skinparam shadowing false", ""]
    for a in ACTOR_ORDER:
        out.append(f'actor "{a}" as {_actor_id(a)}')
    out += ["", 'rectangle "e-Prescribing System" {']
    for u in domain.USE_CASES:
        out.append(f'  usecase "{u["name"]}" as {u["id"]}')
    out += ["}", ""]
    for u in domain.USE_CASES:
        out.append(f"{_actor_id(u['actor'])} --> {u['id']}")
    out.append("")
    for u in domain.USE_CASES:
        for inc in u["includes"]:
            out.append(f"{u['id']} ..> {inc} : <<include>>")
        if u["extends"]:
            out.append(f"{u['id']} ..> {u['extends']} : <<extend>>\\n({u['condition']})")
    out.append("@enduml")
    return "\n".join(out) + "\n"


def mermaid() -> str:
    out = ["flowchart LR"]
    for a in ACTOR_ORDER:
        out.append(f'  {_actor_id(a)}(["{a}"])')
    out.append('  subgraph SYS["e-Prescribing System"]')
    for u in domain.USE_CASES:
        out.append(f'    {u["id"]}(("{u["name"]}"))')
    out.append("  end")
    for u in domain.USE_CASES:
        out.append(f"  {_actor_id(u['actor'])} --- {u['id']}")
    for u in domain.USE_CASES:
        for inc in u["includes"]:
            out.append(f'  {u["id"]} -. "include" .-> {inc}')
        if u["extends"]:
            out.append(f'  {u["id"]} -. "extend: {u["condition"]}" .-> {u["extends"]}')
    return "\n".join(out) + "\n"


def png(path) -> bool:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.patches import Ellipse, FancyArrowPatch
    except ImportError:
        return False

    A, B = 1.7, 0.65  # ellipse half-width / half-height
    pos = {
        "UC1": (4, 8.8), "UC2": (9, 8.8),
        "UC3": (4, 6.6), "UC4": (9, 6.6),
        "UC5": (9, 4.4), "UC6": (9, 2.2), "UC7": (14, 2.2),
        "UC8": (4, 0.3), "UC9": (9, 0.3),
    }
    actor_pos = {
        "Prescriber": (0.4, 5.0), "Drug knowledge base": (18.6, 8.8), "Pharmacy system": (18.6, 6.6),
        "Credential provider": (18.6, 2.2), "Compliance officer": (6.5, -1.7),
    }
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.set_xlim(-1.2, 20.8); ax.set_ylim(-2.4, 10.6); ax.axis("off")
    ax.add_patch(plt.Rectangle((2.0, -0.7), 14.4, 10.7, fill=False, lw=1.5))
    ax.text(9.2, 9.75, "e-Prescribing System", ha="center", fontsize=12, weight="bold")

    for u in domain.USE_CASES:  # actor associations (drawn first, hidden behind shapes)
        ax_, ay_ = actor_pos[u["actor"]]
        x, y = pos[u["id"]]
        ax.plot([ax_, x], [ay_, y], color="gray", lw=0.9, zorder=1)
    for name, (x, y) in actor_pos.items():
        ax.text(x, y, name, ha="center", va="center", fontsize=9, zorder=4,
                bbox=dict(boxstyle="round", fc="#e8eeff", ec="#335"))
    for u in domain.USE_CASES:
        x, y = pos[u["id"]]
        ax.add_patch(Ellipse((x, y), 2 * A, 2 * B, fc="#fff8e1", ec="black", zorder=2))
        ax.text(x, y, u["name"], ha="center", va="center", fontsize=8.5, zorder=3)

    def edge(frm, to):
        (x1, y1), (x2, y2) = pos[frm], pos[to]
        dx, dy = x2 - x1, y2 - y1
        t = 1 / ((dx / A) ** 2 + (dy / B) ** 2) ** 0.5
        return x1 + dx * t * 1.04, y1 + dy * t * 1.04

    def arrow(a, b, label):
        p1, p2 = edge(a, b), edge(b, a)
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="->", linestyle="--", mutation_scale=13,
                                     color="#444", zorder=5))
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        if abs(p1[0] - p2[0]) > abs(p1[1] - p2[1]):   # horizontal: label above
            ax.text(mx, my + 0.28, label, fontsize=7.5, ha="center", va="bottom", color="#a00", zorder=6)
        else:                                          # vertical: label to the right
            ax.text(mx + 0.15, my, label, fontsize=7.5, ha="left", va="center", color="#a00", zorder=6)

    for u in domain.USE_CASES:
        for inc in u["includes"]:
            arrow(u["id"], inc, "<<include>>")
        if u["extends"]:
            arrow(u["id"], u["extends"], f"<<extend>>\n{u['condition']}")
    fig.savefig(path, dpi=160, bbox_inches="tight")
    return True


if __name__ == "__main__":
    config.DIAGRAM_DIR.mkdir(exist_ok=True)
    (config.DIAGRAM_DIR / "usecase.puml").write_text(plantuml(), encoding="utf-8")
    (config.DIAGRAM_DIR / "usecase.mmd").write_text(mermaid(), encoding="utf-8")
    print("wrote diagrams/usecase.puml and diagrams/usecase.mmd")
    if png(config.DIAGRAM_DIR / "usecase.png"):
        print("wrote diagrams/usecase.png")
    else:
        print("matplotlib not installed: skipped PNG (pip install matplotlib), or paste the .puml into plantuml.com")

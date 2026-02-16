import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample"
OUT = ROOT / "docs"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA / "google_ads_sample.csv")

    total_cost = df["cost"].sum()
    total_conv = df["conversions"].sum()
    total_value = df["conversion_value"].sum()

    roas = total_value / total_cost
    cpa = total_cost / total_conv

    report = f"""
# AI + PPC Demo Report

Total Spend: ${total_cost:,.2f}
Total Conversions: {total_conv}
Total Revenue: ${total_value:,.2f}
ROAS: {roas:.2f}x
CPA: ${cpa:.2f}
"""

    (OUT / "demo_report.md").write_text(report)
    print("Report generated in docs/demo_report.md")

if __name__ == "__main__":
    main()

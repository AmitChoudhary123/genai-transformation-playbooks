from pathlib import Path
from src.transformation_playbooks.main import load_initiatives, rank_transformation_portfolio

if __name__ == "__main__":
    for item in rank_transformation_portfolio(load_initiatives(Path("data/genai_initiatives.csv"))):
        print(f"{item['priority']} | {item['score']:5.1f} | {item['initiative']} | {item['governance']}")
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("lab_2d_perception_student.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell["cell_type"] == "markdown":
        source = "".join(cell["source"])
        for line in source.split("\n"):
            if "?" in line:
                print("MARKDOWN:", line.strip())
    elif cell["cell_type"] == "code":
        source = "".join(cell["source"])
        q_matches = re.finditer(r"^(Q\d{1,2})\s*=\s*\"\"\"(.*?)\"\"\"", source, flags=re.MULTILINE | re.DOTALL)
        for m in q_matches:
            q_num = m.group(1)
            q_ans = m.group(2).strip()
            print(f"{q_num} ANSWER: {q_ans}\n")

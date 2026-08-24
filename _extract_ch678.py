import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from pypdf import PdfReader

reader = PdfReader(r"d:\Notes\knowledge-base-obsidian\10th-english-maths-1_compressed.pdf")
out = r"d:\Notes\knowledge-base-obsidian\_ch678.txt"
with open(out, "w", encoding="utf-8") as f:
    for i in range(128, min(165, len(reader.pages))):
        text = reader.pages[i].extract_text() or ""
        f.write(f"\n===== PDF {i+1} =====\n")
        f.write(text)
print("pages", len(reader.pages), "wrote ch678")

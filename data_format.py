
import json


input_file = "output.jsonl"
output_file = "patch.jsonl"

def fix_patch_string(patch_text: str) -> str:
    lines = patch_text.splitlines()
    fixed_lines = []

    for i, line in enumerate(lines):
        fixed_lines.append(line)

        # If this line indicates missing newline at EOF
        if line.strip() == r"\ No newline at end of file":
            # Insert a blank line if next diff starts immediately
            if i + 1 < len(lines) and lines[i + 1].startswith("diff --git"):
                fixed_lines.append("")

    # Ensure patch ends with newline
    return "\n".join(fixed_lines) + "\n"


tmp={}
with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    cnt = 1 
    for line in fin:
        line = line.strip()
        if not line:
            continue
        
        data = json.loads(line)
        item = data
        new_item = {}
        diff_str = fix_patch_string(item["test_result"]["git_patch"])
        tmp[item["instance_id"]] = {"model_patch":diff_str}
    fout.write(json.dumps(tmp, ensure_ascii=False))



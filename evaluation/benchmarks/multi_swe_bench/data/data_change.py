import json


import re
input_file = "/home/kjh/main/OpenHands/evaluation/benchmarks/multi_swe_bench/data/java_examples.jsonl"
output_file = '/home/kjh/main/OpenHands/evaluation/benchmarks/multi_swe_bench/data/new_java_examples.jsonl'

with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        
        data = json.loads(line)
        item = data
        
        docker_image = item.get("docker_image","")

        number = str(item.get("number", ""))  
        

        new_item = {}
        
        new_item["repo"] = "java"

        new_item["instance_id"] = item.get("instance_id","")
        new_item["problem_statement"] = item.get("PR_Title", "")
        new_item["FAIL_TO_PASS"] = []
        new_item["PASS_TO_PASS"] = []
        new_item["base_commit"] = item.get("base_commit","")
        new_item["version"] = "0.1" # depends
        output_data = new_item
        print(new_item)
        fout.write(json.dumps(output_data, ensure_ascii=False) + "\n")
import json

def extract_failed_mutants(jsonl_path, output_path):
    with open(jsonl_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            try:
                data = json.loads(line)
                if data.get("status") != "success":
                    outfile.write(data.get("item") + "\n")
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON line: {e}")

# Example usage
extract_failed_mutants("mutants-report.jsonl", "failed_code.txt")

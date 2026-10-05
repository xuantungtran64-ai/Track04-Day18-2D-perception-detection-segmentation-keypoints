import json
import re

with open('lab_2d_perception_student.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

todos = []
questions = []
lifelines = []

for cell in nb.get('cells', []):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        # find TODOs (ellipsis)
        if re.search(r'(^|=|return)\s*\.\.\.\s*(#.*)?$', source, flags=re.MULTILINE):
            # Extract first line or function name
            match = re.search(r'def\s+([a-zA-Z_]\w*)\s*\(', source)
            if match:
                todos.append(match.group(1))
            else:
                todos.append('Unknown code block with ...')
                
        # Check for questions
        q_matches = re.finditer(r'^(Q\d{1,2})\s*=\s*\"\"\"(.*?)\"\"\"', source, flags=re.MULTILINE | re.DOTALL)
        for m in q_matches:
            q_num = m.group(1)
            q_ans = m.group(2).strip()
            if 'Ðây là câu tr? l?i chi ti?t và d?y d?' in q_ans or q_ans == '' or '...' in q_ans:
                questions.append(q_num)
                
        # Check for lifelines
        if re.search(r'gate\(.*lifeline=True', source):
            lifelines.append(source.split('\n')[0][:50])

print(f'TODOs remaining ({len(todos)}):')
for t in todos:
    print(' - ' + t)

print(f'\nUnanswered questions ({len(questions)}):')
for q in questions:
    print(' - ' + q)
    
print(f'\nLifelines used ({len(lifelines)}):')
for l in lifelines:
    print(' - ' + l)

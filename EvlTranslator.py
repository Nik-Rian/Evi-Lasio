import os
import re
import sys

def replace_operators(condition):
    replacements = {
        'Neh?': '!=',
        'meh?': '<',
        'Meh?': '>',
        'eh?': '=='
    }
    
    for custom_op, c_op in replacements.items():
        condition = condition.replace(custom_op, c_op)
    
    return condition

def translate_to_c(custom_code):
    custom_code = custom_code.strip()

    if not custom_code:
        return ""
    
    if custom_code.endswith("vil?") and " eh " in custom_code:
        var_name = custom_code.split(" eh ")[0].strip()
        return f'scanf("%d", &{var_name});'

    if custom_code.startswith("evilas(") and custom_code.endswith("):"):
        inner_content = custom_code[len("evilas("):-len("):")].strip()
        
        variable_pattern = r'\*(\w+)\*'
        matches = re.findall(variable_pattern, inner_content)
        
        if matches:
            format_string = inner_content
            for var in matches:
                format_string = format_string.replace(f"*{var}*", "%d", 1)

            arguments = ', '.join(matches)
            return f'printf({format_string}, {arguments});'
        else:
            return f'printf({inner_content});'

    if custom_code.startswith("lasio(") and custom_code.endswith(")"):
        condition = custom_code[len("lasio("):-1].strip()
        condition = replace_operators(condition)
        return f'while({condition})'
    
    if custom_code.startswith("lasi(") and custom_code.endswith(")"):
        condition = custom_code[len("lasi("):-1].strip()
        condition = replace_operators(condition)
        return f'if({condition})'
    
    if custom_code == "evi":
        return "else"
    
    if custom_code.startswith("evil ") and " eh " in custom_code and custom_code.endswith(":"):
        var_declaration = custom_code[len("evil "):-len(":")].strip()
        var_name, var_value = var_declaration.split(" eh ")
        return f'int {var_name.strip()} = {var_value.strip()};'
    
    if custom_code.startswith("evil ") and custom_code.endswith(":"):
        var_name = custom_code[len("evil "):-len(":")].strip()
        return f'int {var_name.strip()};'

    match = re.match(r'(\w+) eh (\w+)\s*([\+\-\*\/])\s*(\w+):', custom_code)
    if match:
        var_name, left_var, operation, right_var = match.groups()
        return f'{var_name} = {left_var} {operation} {right_var};'

    if custom_code == ">":
        return "{"
    if custom_code == "<":
        return "}"

    raise SyntaxError("Invalid evlasio statement format")

def read_evl_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_c_file(output_path, c_code_lines):
    with open(output_path, 'w') as file:
        file.write('#include <stdio.h>\n\n')
        file.write('int main() {\n')

        for line in c_code_lines:
            if line.strip() == "":
                file.write('\n')
            else:
                file.write(f'    {line}\n')

        file.write('    return 0;\n')
        file.write('}\n')

def main():
    # Check if a file is passed as an argument
    if len(sys.argv) > 1:
        evl_file = sys.argv[1]
    else:
        evl_file = 'main.evl'

    # Check for optional output argument
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        output_path = ''

    c_file_name = os.path.basename(evl_file).replace('.evl', '.c')

    if output_path and os.path.isdir(output_path):
        c_file = os.path.join(output_path, c_file_name)
    elif output_path and output_path.endswith('.c'):
        c_file = output_path
    else:
        c_file = c_file_name

    if not os.path.exists(evl_file):
        raise FileNotFoundError(f"{evl_file} not found")

    evl_code_lines = read_evl_file(evl_file)
    c_code_lines = []

    for evl_line in evl_code_lines:
        c_line = translate_to_c(evl_line)
        c_code_lines.append(c_line)

    write_c_file(c_file, c_code_lines)
    print(f"Translation complete. C code saved to {c_file}")

if __name__ == "__main__":
    main()
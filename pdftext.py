def read_lines_from_text_file(file_path):
    lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line.strip())  # 去除每行末尾的换行符
    return lines



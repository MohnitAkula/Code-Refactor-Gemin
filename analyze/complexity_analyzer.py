import lizard


def run_lizard(path):
    result = lizard.analyze([path])
    complexity_data = []
    for file in result:
        for function in file.function_list:
            complexity_data.append({
                'file': file.filename,
                'name': function.name,
                'start_line': function.start_line,
                'end_line': function.end_line,
                'cyclomatic_complexity': function.cyclomatic_complexity,
                'nloc': function.length
            })
    complexity_data.sort(
        key=lambda x: x['cyclomatic_complexity'], reverse=True)
    return complexity_data

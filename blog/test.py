new_results = [{k: str(v) if k != 'no' else v for k, v in row.items()} for row in results]

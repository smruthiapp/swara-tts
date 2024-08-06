def extract_between(text, start_str, end_str):
    # Find the starting index of the substring after the start_str
    start_idx = text.find(start_str)
    if start_idx == -1:
        return "Start string not found"
    
    # Adjust start_idx to the end of start_str
    start_idx += len(start_str)
    
    # Find the ending index of the substring before the end_str
    end_idx = text.find(end_str, start_idx)
    if end_idx == -1:
        return "End string not found"
    
    # Extract the substring between start_idx and end_idx
    return text[start_idx:end_idx].strip()
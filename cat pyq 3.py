original_list=["Ram","sam","Tom","Ram","Karan","Tom"]
modified_list=[]
for name in original_list:
    if name not in modified_list:
        modified_list.append(name)
print(f"Orginal list:{original_list}")
print(f"Modified list:{modified_list}")
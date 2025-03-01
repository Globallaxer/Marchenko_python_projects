# 2. Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми
# кодами.
with open('text18-14.txt','r',encoding='utf-8') as file:
    content = file.readlines()
with open('text18-14.txt','r',encoding='utf-8') as file:
    content_for_spaces = file.read()
    spaces = content_for_spaces.count(' ')
    print(f'Абоба, вот твои пробелы: {spaces}')   
    for line in content:
        print(line,end="")
    if len(content) >= 3:
        line_ascii = [str(ord(char)) for char in content[2]]
        content[2] = ' '.join(line_ascii)+ "\n"
    with open("text18-14_mod.txt",'w', encoding='utf-8') as new_file:
        new_file.writelines(content)
        
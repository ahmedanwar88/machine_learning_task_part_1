from bs4 import BeautifulSoup
import sys

def read_file(path):
    text_file = open(path, "r")
    data = text_file.read()
    text_file.close()
    return data

def write_file(path, data):
    text_file = open(path, "w")
    n = text_file.write(data)
    text_file.close()

def clean_data(data):
    soup = BeautifulSoup(data, "html.parser")
    for txt in soup(['style', 'script']):
        txt.decompose()
    return ' '.join(soup.stripped_strings)

def main():
    path_read = r'F:\Work\git_repos\machine_learning_task_part_1\news_sample_ner.txt'
    path_write = r'F:\Work\git_repos\machine_learning_task_part_1\news_sample_ner_cleaned.txt'
    data = read_file(path_read)
    cleaned_data = clean_data(data)
    write_file(path_write, cleaned_data)

if __name__ == '__main__':
    main()
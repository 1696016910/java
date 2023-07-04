import os
path = "./javaee"
files= os.listdir(path) #得到文件夹下的所有文件名称
html = ""
for file in files: #遍历文件夹
    arr = file.split('.')
    str = f'- <a href="./javaee/{file}" target="_blank">{arr[0]}</a>\n'
    html += str

print(html)
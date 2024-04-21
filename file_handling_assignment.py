with open('my_file.txt', 'w') as file:
    file.writelines('Hello world \nThis is my 2nd line \n today is on 21st of 04 2023')

with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)

with open('my_file.txt', 'a') as file:
    file.write('\n Cyber security \n')
    file.write('Cloud computing \n')
    file.write('Data Science \n')

with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)

try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')
except Exception as e:
    print('An error occured', e)
finally:
    print('Block executed')
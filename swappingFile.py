def swapFileData():
    file1 = open('C:\python_programs\python_TxT_file_1.txt', 'r+')
    file2 = open('C:\python_programs\python_TxT_file_2.txt', 'r+')
    file1 = file2
    savedData=file2
    savedData=file1
    o=file1
    p=o
    x = p.read()
    print(x)
swapFileData()

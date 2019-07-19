students={
    '01' : {
    '순번': '01',
    '이름': '김성훈'
},
'02': {
    '순번': '02',
    '이름': '김은정'
}
}
students2 = {}


# with open ('a.csv', 'w', encoding='utf-8') as f:
#     f.write('번호, 이름 \n')
#     for number, name in students.items():
#         f.write(f'{number}, {name}\n')



import csv
with open('b.csv','w', encoding = 'utf-8') as f:
        fieldnames = ['순번', '이름']
        csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
        csv_writer.writeheader()
       
        for item in students.values():
            print(item)
            csv_writer.writerow(item)
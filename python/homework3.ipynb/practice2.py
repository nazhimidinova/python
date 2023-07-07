squares = [i**2 for i in range(1, 11)]
print(squares)

even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)

candidate1 = ('Sadyr Zhaparov', 'Ata-jurt', 10)
candidate2 = ('Sooronbay Zheenbekov', 'Bar-Bol', 20)
candidate3 = ('Almazbek Atambaev', 'SDPK', 15)

candidates = [('Sadyr Zhaparov', 'Ata-jurt', 10), ('Sooronbay Zheenbekov', 'Bar-Bol', 20), ('Almazbek Atambaev', 'SDPK', 15)]
for candidate in candidates:
    print('Name:', candidate[0], ', Party:',
          candidate[1], ', Years in politics:', candidate[2])




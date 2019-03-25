class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

m0 = Mahasiswa('Ika', 10, 'Sukoharjo', 240000)
m1 = Mahasiswa('Ahmad', 2, 'Surakarta', 250000)
m2 = Mahasiswa('Chandra', 18, 'Surakarta', 235000)
m3 = Mahasiswa('Eka', 4, 'Boyolali', 240000)
m4 = Mahasiswa('Fandi', 31, 'Salatiga', 250000)
m5 = Mahasiswa('Deni', 13, 'Klaten', 245000)
m6 = Mahasiswa('Galuh', 5, 'Wonogiri', 245000)
m7 = Mahasiswa('Janto', 23, 'Klaten', 245000)
m8 = Mahasiswa('Hasan', 64, 'Karanganyar', 270000)
m9 = Mahasiswa('Khalid', 29, 'Purwodadi', 265000)
m10 = Mahasiswa('Budi', 51, 'Klaten', 210000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

-----------------NO.1-----------------------
def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko
-----------------NO.2-----------------------
def UangSakuTerkecil(kumpulan) :
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
    return terkecil
-----------------NO.3-----------------------
def DaftarSakuTerkecil(kumpulan) :
    kecil = []
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
            kecil.append(kumpulan.index(i))
    return kecil
-----------------NO.4-----------------------
def DaftarSakuKecil(kumpulan):
    kecil = []
    for i in kumpulan :
        if i.uangsaku < 250000 :
            kecil.append(kumpulan.index(i))



class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self): 
        self.head = None
        
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        
    def pushAk(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head

    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"

-----------------NO.5-----------------------
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

m0 = Mahasiswa('Ika', 10, 'Sukoharjo', 240000)
m1 = Mahasiswa('Ahmad', 2, 'Surakarta', 250000)
m2 = Mahasiswa('Chandra', 18, 'Surakarta', 235000)
m3 = Mahasiswa('Eka', 4, 'Boyolali', 240000)
m4 = Mahasiswa('Fandi', 31, 'Salatiga', 250000)
m5 = Mahasiswa('Deni', 13, 'Klaten', 245000)
m6 = Mahasiswa('Galuh', 5, 'Wonogiri', 245000)
m7 = Mahasiswa('Janto', 23, 'Klaten', 245000)
m8 = Mahasiswa('Hasan', 64, 'Karanganyar', 270000)
m9 = Mahasiswa('Khalid', 29, 'Purwodadi', 265000)
m10 = Mahasiswa('Budi', 51, 'Klaten', 210000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko

def UangSakuTerkecil(kumpulan) :
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
    return terkecil

def DaftarSakuTerkecil(kumpulan) :
    kecil = []
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
            kecil.append(kumpulan.index(i))
    return kecil

def DaftarSakuKecil(kumpulan):
    kecil = []
    for i in kumpulan :
        if i.uangsaku < 250000 :
            kecil.append(kumpulan.index(i))
    return kecil

-----------------NO.6-----------------------
def binary_search(kumpulan, target):
    jml = []
    kiri = 0
    kanan = len(kumpulan) - 1

    while kiri <= kanan :
        mid = (kiri + kanan) // 2
        if kumpulan[mid] == target :
            jml.append(kumpulan.index(target))
            return jml
        elif target < kumpulan[mid]:
            kanan = mid - 1
        else :
            kiri = mid + 1
    return False

d = [1, 2, 3, 3, 4, 5, 5, 5, 5, 133, 134, 157, 157, 189, 200, 230, 235,345]

-----------------NO.7-----------------------
class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

m0 = Mahasiswa('Ika', 10, 'Sukoharjo', 240000)
m1 = Mahasiswa('Ahmad', 2, 'Surakarta', 250000)
m2 = Mahasiswa('Chandra', 18, 'Surakarta', 235000)
m3 = Mahasiswa('Eka', 4, 'Boyolali', 240000)
m4 = Mahasiswa('Fandi', 31, 'Salatiga', 250000)
m5 = Mahasiswa('Deni', 13, 'Klaten', 245000)
m6 = Mahasiswa('Galuh', 5, 'Wonogiri', 245000)
m7 = Mahasiswa('Janto', 23, 'Klaten', 245000)
m8 = Mahasiswa('Hasan', 64, 'Karanganyar', 270000)
m9 = Mahasiswa('Khalid', 29, 'Purwodadi', 265000)
m10 = Mahasiswa('Budi', 51, 'Klaten', 210000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]


def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko

def UangSakuTerkecil(kumpulan) :
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
    return terkecil

def DaftarSakuTerkecil(kumpulan) :
    return kecil

-----------------NO.8-----------------------

def binery_search(kumpulan, target) :
    kiri = 0
    kanan = len(kumpulan) - 1

    while kiri <= kanan :
        tengah = (kiri + kanan) // 2

        if kumpulan[tengah] == target :
            return tengah

        elif kumpulan[tengah] < target :
            kiri = tengah + 1

        else :
            kanan = tengah - 1

    return -1

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

"""
Untuk mencari berapa tabakan yang digunakan Binary Search, menggunakan Logaritma basis 2 (Log2(n))
misal :
    - apabila terdapat element array berjumlah 100 maka akan memilki maksimal 7 kali tebakan.
      perhitungannya log2(100) = 6.643856189774725 kita tambahkan 1 menjadi 7.643856189774725 sehingga kita bulatkan ke bawah menjadi 7
      selain itu 7 didapatkan dari log2(128) = 7, dimana 100 paling mendekati dengan 128.
    - apabila itu terdapat 1000 element maka perhitungan akan sama.
      log2(1000) = 9.965784284662087 kita tambahkan 1 menjadi 10.965784284662087 dibulatkan ke bawah menjadi 10.
      bisa didapat dari log2(1024) = 10, dimana 1000 paling mendekati 1024.
"""

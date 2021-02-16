import os

namafile = input("Masukkan nama file: ")
# Kode periksa nama file
if os.path.isfile("./" + namafile):
    print("Mencari file {}...".format(namafile))
    print("File Ditemukan!")
    action = input(
        "Apa yang ingin Anda lakukan dengan file tersebut?\n Tindakan yang mungkin dilakukan adalah: baca, hapus, tambahkan, ganti\n")
    if action == "baca":
        print("Isi file:")
        with open(namafile, "r") as read_file:
            print(read_file.read())
    elif action == "tambahkan":
        text = input("Harap masukkan catatan Anda: ")
        with open(namafile, "a") as append_file:
            append_file.write(text + "\n")
    elif action == "delete":
        os.remove("./" + namafile)
        print("{} telah dihapus.".format(namafile))
       
        with open(namafile, "w") as write_file:
            write_file.write("")
    elif action == "ganti":
        line_num = int(
            input("Harap masukkan nomor baris untuk penggantinya: "))
        text = input("Harap masukkan catatan Anda: ")
        with open(namafile, "r") as read_file:
            lines = read_file.readlines()
        with open(namafile, "w") as write_file:
            for idx, line in enumerate(lines):
                # print(idx, line)
                if idx == line_num - 1:
                    print("Baris dengan nomor{} perlu diganti!".format(line_num))
                    write_file.write(text + "\n")
                else:
                    print("Tulis \"{}\"".format(line))
                    write_file.write(line)

    else:
        print("Maaf, aksi tidak dikenal 😢")
else:
    print("Tidak, file ini tidak ada, saya akan membuatnya untuk Anda! 😄")
    text = input("Harap masukkan catatan Anda: ")
    with open(namafile, "w") as write_file:
        write_file.write(text + "\n")
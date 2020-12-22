import random
import datetime

from customer import Customer

atm = Customer(id)

while True:
    id = int(input('Masukkan PIN Anda: '))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('PIN Anda Salah. Silakan Masukkan Lagi:'))
        trial += 1

        if trial == 3:
            print('Error. Silakan Ambil Kartu Anda dan Coba Lagi.')
            exit()

    print('\n SELAMAT DATANG')
    print('1-Cek Saldo. 2-Debet.  3-Simpan. 4-Ganti PIN.  5-Keluar.')
    option = int(input('Masukkan Angka Sesuai Pilihan Anda: '))

    if option == 1:
        print('Saldo Anda Rp ' + str(atm.checkBalance()) + '\n')

    elif option == 2:
        nominal = int(input('Masukkan Nominal Saldo: Rp '))

        if nominal < atm.checkBalance():
            atm.withdrawBalance(nominal)
            print('Transaksi Berhasil. Saldo Anda Sekarang: Rp' + str(atm.checkBalance()) + '\n')
        else:
            print('Maaf Saldo Anda Tidak Mencukupi Untuk Transaksi Ini.' + '\n')

    elif option == 3:
        nominal = int(input('Masukkan Nominal Saldo: Rp '))

        atm.depositBalance(nominal)
        print('Transaksi Berhasil. Saldo Anda Sekarang: Rp' + str(atm.checkBalance()) + '. Terima Kasih. \n')

    elif option == 4:
        pin_lama = int(input('Masukkan PIN Lama Anda: '))

        while pin_lama != int(atm.checkPin()):
            print('PIN Anda Salah.')
            exit()

        update_pin = int(input('Masukkan PIN Baru: '))
        print('Berhasil. PIN Anda Berhasil Diganti. ')

        pin_baru = int(input('Masukkan PIN Baru Anda: '))

        if  pin_baru == update_pin:
            print('PIN Berhasil Diganti! \n')
        else:
            print('Pin Anda Salah. Coba Lagi. \n')
            break

    elif option == 5:
        print('\nHarap Menyimpan Resi Ini Sebagai Bukti Transaksi Anda!')
        print('\nNo. Transaksi : ', random.randint(10000, 1000000))
        print('Tanggal : ', datetime.datetime.now())
        print('Saldo Akhir : Rp. ', atm.checkBalance())
        exit(" \nTerimakasih!")
    else:
        print('Error')

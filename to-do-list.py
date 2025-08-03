tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")
    
    choice = input("Pilih menu (1/2/3/4): ")

    if choice == "1":
        if not tasks:
            print("Belum ada tugas.")
        else:
            print("Daftar tugas:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    elif choice == "2":
        new_task = input("Masukkan nama tugas: ")
        tasks.append(new_task)
        print(f"Tugas '{new_task}' berhasil ditambahkan!")

    elif choice == "3":
        if not tasks:
            print("Tidak ada tugas yang bisa dihapus.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            try:
                task_number = int(input("Masukkan nomor tugas yang mau dihapus: "))
                if 1 <= task_number <= len(tasks):
                    deleted = tasks.pop(task_number - 1)
                    print(f"Tugas '{deleted}' berhasil dihapus!")
                else:
                    print("Nomor tugas tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid ya.")

    elif choice == "4":
        print("Dadah! Semangat ngerjain tugasnya ✌️")
        break
    
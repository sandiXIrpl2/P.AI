def welcome_message():
    print("Selamat datang di Tes Pemahaman Python!")
    print("Program ini akan menguji pemahaman dasar Anda tentang Python.")
    print("Jawab setiap pertanyaan dengan benar untuk melanjutkan.")
    print("Anda akan menerima umpan balik untuk setiap jawaban.")
    print("Selamat mengerjakan!\n")


def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Jawaban Anda (masukkan nomor): "))
            if answer == correct_option:
                print("Benar!\n")
                return True
            else:
                print(
                    "Salah. Jawaban yang benar adalah:",
                    options[correct_option - 1],
                    "\n",
                )
                return False
        except ValueError:
            print("Masukkan nomor yang valid.\n")


def quiz():
    score = 0
    total_questions = 5

    # Pertanyaan 1
    question1 = "Apa tipe data yang digunakan untuk menyimpan teks di Python?"
    options1 = ["int", "str", "list", "bool"]
    correct_option1 = 2
    if ask_question(question1, options1, correct_option1):
        score += 1

    # Pertanyaan 2
    question2 = (
        "Struktur data mana yang digunakan untuk menyimpan pasangan kunci-nilai?"
    )
    options2 = ["List", "Tuple", "Dictionary", "Set"]
    correct_option2 = 3
    if ask_question(question2, options2, correct_option2):
        score += 1

    # Pertanyaan 3
    question3 = "Apa hasil dari kode berikut: 3 + 5 * 2 ?"
    options3 = ["16", "13", "10", "11"]
    correct_option3 = 2
    if ask_question(question3, options3, correct_option3):
        score += 1

    # Pertanyaan 4
    question4 = "Fungsi mana yang digunakan untuk menambahkan elemen ke list di Python?"
    options4 = ["insert()", "append()", "extend()", "add()"]
    correct_option4 = 2
    if ask_question(question4, options4, correct_option4):
        score += 1

    # Pertanyaan 5
    question5 = "Apa yang dilakukan oleh pernyataan berikut: for i in range(5):"
    options5 = [
        "Mengulang dari 0 hingga 5 termasuk",
        "Mengulang dari 1 hingga 5 termasuk",
        "Mengulang dari 0 hingga 4",
        "Mengulang dari 1 hingga 4",
    ]
    correct_option5 = 3
    if ask_question(question5, options5, correct_option5):
        score += 1

    # Tampilkan hasil akhir
    print(f"Tes Selesai! Skor Anda: {score} dari {total_questions}")
    if score == total_questions:
        print("Luar biasa! Anda memahami dasar Python dengan sangat baik.")
    elif score >= 3:
        print("Bagus! Anda memiliki pemahaman yang cukup kuat tentang Python.")
    else:
        print("Anda perlu belajar lebih banyak. Cobalah lagi!")


welcome_message()
quiz()

from multiprocessing import Process
import time

# tugas 1 : menghitung faktorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        time.sleep(0.2)

    print(f"[Tugas 1] Faktorial dari {n} = {result}")



# tugas 2 : penjumlahan total penjumlahan
def total_sum(numbers):
    total = sum(numbers)
    time.sleep(1)

    print(f"[Tugas 2] Jumlah dari {numbers} = {total}")

# tugas 3 : mencari nilai terbesar
def find_max(numbers):
    maximum = max(numbers)
    time.sleep(1)

    print(f"[Tugas 3] nilai terbesar dari {numbers} = {maximum}")


if __name__ == '__main__':

    p1 = Process(target=factorial, args=(5,))
    p2 = Process(target=total_sum, args=([10, 20, 30, 40],))
    p3 = Process(target=find_max, args=([3, 7, 2, 9, 5],))
   
    # mulai proses paralel
    p1.start()
    p2.start()
    p3.start()

    # tunggu semua proses selesai
    p1.join()
    p2.join()
    p3.join()

    print("\nSemua tugas paralel telah selesai.")
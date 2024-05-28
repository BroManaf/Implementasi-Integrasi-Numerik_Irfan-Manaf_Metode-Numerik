import numpy as np
import time

def trapezoidal_integration_verbose(f, a, b, N):
    # Menghitung panjang langkah (h)
    h = (b - a) / N
    # Membuat array titik-titik evaluasi dari a sampai b dengan N+1 titik
    x = np.linspace(a, b, N+1)
    # Menghitung nilai fungsi f(x) pada titik-titik evaluasi x
    y = f(x)
    
    # Mencetak panjang langkah dan nilai-nilai x serta y
    print(f"h (step size) = (b - a) / N = ({b} - {a}) / {N} = {h}")
    print(f"x values: {x}")
    print(f"y values (f(x)): {y}")
    
    # Menghitung aproksimasi integral dengan metode trapezoid
    I = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    
    # Mencetak langkah-langkah perhitungan integral
    print(f"Integral approximation (I):")
    print(f"I = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])")
    print(f"I = ({h} / 2) * ({y[0]} + 2 * {np.sum(y[1:-1])} + {y[-1]})")
    print(f"I = {I}\n")
    
    # Mengembalikan hasil aproksimasi integral
    return I

# Mendefinisikan fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Menghitung galat RMS antara nilai pi yang diestimasi dan nilai referensi pi
def compute_rms_error(estimated_pi, true_pi):
    return np.sqrt((estimated_pi - true_pi) ** 2)

# Daftar nilai N yang akan diuji
N_values = [10, 100, 1000, 10000]
# Nilai referensi pi
true_pi = 3.14159265358979323846

# Melakukan pengujian untuk setiap nilai N dalam N_values
for N in N_values:
    print(f"Testing with N = {N}")
    # Mengukur waktu mulai eksekusi
    start_time = time.time()
    # Menghitung nilai pi yang diestimasi dengan metode trapezoid
    estimated_pi = trapezoidal_integration_verbose(f, 0, 1, N)
    # Mengukur waktu selesai eksekusi
    end_time = time.time()
    
    # Menghitung galat RMS antara nilai pi yang diestimasi dan nilai referensi
    rms_error = compute_rms_error(estimated_pi, true_pi)
    # Menghitung waktu eksekusi
    execution_time = end_time - start_time
    
    # Mencetak hasil estimasi pi, galat RMS, dan waktu eksekusi
    print(f"Estimated Pi: {estimated_pi}")
    print(f"RMS Error: {rms_error}")
    print(f"Execution Time: {execution_time} seconds\n")
    print("="*50 + "\n")

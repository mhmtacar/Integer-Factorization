import tkinter as tk
import random
arayüz = tk.Tk()
arayüz.title("Şifre")
arayüz.geometry("400x200")

def factorize(n):

    factors = []
    d = 2

    while n > 1:
        # Try to divide by small primes using trial division
        while n % d == 0:
            factors.append(d)
            n //= d

        # If n is still not 1, use Pollard's Rho algorithm
        if n > 1:
            x = random.randint(2, n-1)
            y = x
            c = random.randint(1, n-1)
            g = 1

            while g == 1:
                x = (x*x + c) % n
                y = (y*y + c) % n
                y = (y*y + c) % n
                g = gcd(abs(x-y), n)
                #print("g",g)

            # If Pollard's Rho found a non-trivial factor, add it to the list of factors
            if g != n:
                factors += factorize(g)
                factors += factorize(n//g)
                break

            # If Pollard's Rho failed, increment d and try trial division again
            else:
                d += 1

    return sorted(factors)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def giris_komut():
 if y.get().isdigit():
    kullan = int(y.get())
    factors = factorize(kullan)
    
    result.config(text=str(factors),fg="red") 
 
kullanici = tk.Label(text="Enter an integer:")
kullanici.place(x=20,y=10)

y= tk.StringVar()
kullanici_girisi = tk.Entry(textvariable=y)
kullanici_girisi.place(x=130,y=10)

giris = tk.Button(text="Enter",command=giris_komut)
giris.place(x=150,y=55)


result = tk.Label(text="", font="Verdana 10 bold")
result.place(x=100,y=95)


arayüz.mainloop()
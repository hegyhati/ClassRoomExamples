import matplotlib.pyplot as plt

x=[]
y=[]
z=[]
for i in range(10):
    x.append(i)
    y.append(i*i-10)
    z.append(100-i**3/3)


f,a = plt.subplots(2)
a[0].plot(x,x, label="x", linewidth=0, marker="o")
a[0].plot(x,y, label="x^2-10", marker="^")
a[0].legend()

a[0].set_title("Harom szep fuggveny")
a[0].set_xlabel("x")
a[0].set_ylabel("fuggvenyertekek")



a[1].barh(["Barnabas", "Eszter", "Mirjam"], [172,168,161])
a[1].set_title("Testmagassagok")
a[1].set_ylabel("Testmagasag (cm)")

f.savefig('foobar.jpg')
a[0].autoscale(False)

a[0].plot(x,z, label="100-x^3/3", linewidth=5, linestyle="-.")
a[0].legend()

f.savefig('foobar2.jpg')



# Exercises

## `Fraction` class, so that this `main` will run:
```py
def input_fraction() -> Fraction:
   n = int(input("Numerator: "))
   while True:
      d = int(input("Denominator: "))
      if d!= 0: break
      print("The denominator cannot be 0.")
   return Fraction(d,n)

fr1 = input_fraction()
fr2 = input_fraction()

print(f"{fr1}+{fr2}={fr1.add(fr2)}")
print(f"{fr1}-{fr2}={fr1.sub(fr2)}")
print(f"{fr1}*{fr2}={fr1.mul(fr2)}")
if not fr2.is_zero():
   print(f"{fr1} / {fr2}={fr1.div(fr2)}")
```

## Necessary classes so that this `main` will work properly:

```py
def input_point() -> Point2D:
   x = float(input("X coordinate: "))
   y = float(input("Y coordinate: "))
   return Point2D(x,y)


print("Let's build a Polygon!")
polygon = Polyline()

print("Where should we start?")
start = input_point()
polygon.add_point(start)

while True:
   print(f"Your polyline so far: {polygon}")
   print("What should be the next point? (Give the starting point to complete the polygon!)")
   next_point = input_point()
   polygon.add_point(next_point)
   if next_point == start:
      break

print(f"The circumference of {polygon} is {polygon.circumference()}")
```

### SVG
Make a `polygon.export_to_svg(filename:str)` function. 
Useful helper functions: `minX`, `minY`, `maxX`, `maxY`. 

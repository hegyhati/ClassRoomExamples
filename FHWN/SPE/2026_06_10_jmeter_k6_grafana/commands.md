Simplest

```bash
k6 run test.js
```

Overwrite default/code-defined arguments:

```bash
-d 10s
-i 100
-u 30
--no-treshholds
```

Send data to prometheus:

```bash
k6 run -o experimental-prometheus-rw test.js
```

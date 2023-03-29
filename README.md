# Pyrom

Pyrom is a simple python module that allows you to generate ROMs, write in them and saved it into files.

In the `examples.py` you can find some examples and here you can see the properties and what they do:

```python
myROM = ROM(header, size, columns, data_sizes, show_addr_column)
```

### Header

---

The text of the first line in the file, can be empty.

### Size

---

The number of rows that the file will have, example size 8.

```
00: 0000 0000 0000 0000
04: 0000 0000 0000 0000
08: 0000 0000 0000 0000
```

### Columns

---

The nomber of columns of the file, example columns 2.

```
00: 0000 0000
02: 0000 0000
```

### Data_sizes

---

The size of each position in the ROM, example data_sizes 2.

```
00: 00 00
02: 00 00
```

### Show_addr_column

---

Is a boolean that indicates if you want to show the addr column, example false:

```
0000 0000 0000 0000
0000 0000 0000 0000
0000 0000 0000 0000
```

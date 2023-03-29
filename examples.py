from pyrom import ROM

myROM = ROM(header="Hex file", size=128, columns=4, data_sizes=4, show_addr_column=True)
# When you want to work with it, you need to init the ROM first
myROM.init_empty_ROM()

# The size indicates the number of rows no the number of data
# So if you have a ROM of size=128, the total data is 128+columns
# in this case is 131
myROM.in_rom_addr_write(0,"1111")
myROM.in_rom_addr_write(1,"1111")
myROM.in_rom_addr_write(2,"1111")
myROM.in_rom_addr_write(64,"1111")
myROM.in_rom_addr_write(131,"1111")
print(myROM)

# You can use the init_empty_ROM() method to reset the ROM object
myROM.init_empty_ROM()

for _ in range(0, 131, 2):
    myROM.in_rom_addr_write(_, "1111")

print(myROM)
myROM.save_into_file("example_rom")
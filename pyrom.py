"""This modules allows you to generate ROMs, write in them and saved it into files"""

class ROM:
    def __init__(self, header="", size=0x0, columns=1, data_sizes=0, show_addr_column=True):
        self.tittle = f"{header}\n"
        self.size = size
        self.columns = columns
        self.data_sizes = data_sizes
        self.show_addr_column = show_addr_column
        self.zfillForAddr = len(hex(self.size).replace("0x", ""))
        self.ROM = {}

    def init_empty_ROM(self):
        """Initializes an empty rom"""
        for addr in range(0, self.size+1, self.columns):
            addr = hex(addr).replace("0x", "")
            formatedAddr = addr.zfill(self.zfillForAddr)
            self.ROM[formatedAddr] = ["0"*self.data_sizes for _ in range(self.columns)]
        return self.ROM

    def in_rom_addr_write(self, tarjet_addr, data: str) -> bool:
        """Writes a value to a specific rom address"""
        addr_counter = 0
        for rom_addr in self.ROM:
            for index, line in enumerate(self.ROM[rom_addr]):
                if tarjet_addr == addr_counter:
                    self.ROM[rom_addr][index] = data
                    return True
                addr_counter += 1
        return False

    def rom_to_text(self) -> str:
        """Converts the rom data structure to text"""
        return_text = ""
        if len(self.tittle) > 1: return_text += self.tittle
        for addr in self.ROM:
            data_line = " ".join(self.ROM[addr])
            if self.show_addr_column:
                return_text += f"{addr}: {data_line}\n"
            else:
                return_text += f"{data_line}\n"
        return_text = return_text[:-1]
        return return_text

    def save_into_file(self, name="saved_rom"):
        """Saves the text of the rom to a file"""
        with open(name, "wb") as f:
            f.write(self.rom_to_text().encode("utf-8"))

    def __str__(self) -> str:
        return self.rom_to_text()
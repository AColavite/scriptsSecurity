import re
import lief
import subprocess
from capstone import *

# Extrair strings ASCII e Unicode #
def extract_strings(filepath, min_length=4):
    with open(filepath, "rb") as f:
        data = f.read()

        # Strings ASCII (32-126) #
    ascii_strings = re.findall(rb"[ -~]{%d,}" % min_length, data)

        # Strings unicode (utf 16)

    return [s.decode("utf-8", errors="ignore") for s in ascii_strings], \
           [s.decode("utf-16", errors="ignore") for s in unicode_strings]

    # String extration by sector #
    def extract_from_sections(binary_path):
        binary = lief.parse(binary_path)
        if not binary:
            return{}

        sections = {}
        for section in binary.sections:
            sec_name = section.name 
            raw_data = bytes(section.content)
            ascii_strings = re.findall(rb"[ -~]{4,}", raw_data) # ASCII
            sections[sec_name] = [s.decode("utf-8", errors="ignore") for s in ascii_strings]

        return sections

# Verify binary is in UPX #
def is_upx_packed(filepath):
    try:
        result = subprocess.run(["upx", "-t", filepath], capture_output=True, text=True)
        return "packed" in result.stdout.lower()
    except FileNotFoundError:
        print("[!] UPX not found. Install with 'apt install upx' or 'brew install upx'.")
        return False

# Decompac UPX #
def unpack_upx(filepath):
    if is_upx_packed(filepath):
        print("[!] Decompressing UPX. . .")
        subprocess.run(["upx", "-d", filepath])
        print("[!] Decompressing Concluded ")

# Disassemble binary and search references to strings #
def disassemble_binary(binary_path, max_instructions=30):
    with open(binary_path, "rb") as f:
        data = f.read()

    md = Cs(CS_ARCH_X86, CS_MODE_64)
    count = 0

    print("\n[+] Disassembly (Instruções ASM relevantes):")
    for i in md.disasm(data, 0x1000):
        print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
        count += 1
        if count >= max_instructions:
            break

# Principal #
def analyze_binary(binary_path):
    print(f"\n[+] Analyzing binary: {binary_path}")

    # verifica se tá UPX-pack e descompacta se necessário #
    if is_upx_packed(binary_path):
        print("[+] Binary is compacting with UPX")
        unpack_upx(binary_path)

    # String extraction #
    ascii_strings, unicode_strings = extract_strings(binary_path)
    print("\n".join(ascii_strings[:10])) # Mostra apenas 10

    print("\n[+] Strings Unicode found")
    print("\n".join(unicode_strings[:10]))

    # Extração por seção
    sections = extract_from_sections(binary_path)
    for sec, strings in sections.items():
        print(f"\n[+] Strings in section: {sec}")
        print("\n".join(strings[:10])) # Mostra as 10 Primeiras

    # Disassembly do binário
    disassemble_binary(binary_path)

    # rodando #
    if __name__ == "__main__":
        binary_file = "programa.exe" # Substitue pelo nome do binário
        analyze_binary(binary_file)
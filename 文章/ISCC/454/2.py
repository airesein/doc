def decrypt_ciphertext(encrypted_values, xor_key_list):
    encrypted_ints = [value & 0xffffffff for value in encrypted_values]
    decrypted_ints = [encrypted_ints[i] ^ xor_key_list[i] for i in range(len(encrypted_ints))]
    return decrypted_ints

def convert_ints_to_string(integer_list):
    try:
        return "".join([num.to_bytes(length=4, byteorder="little").decode() for num in integer_list])
    except UnicodeDecodeError:
        print("解码失败，可能密钥错误或数据损坏")
        return ""

def apply_custom_character_mapping(input_text, source_character_table, target_character_table):
    result = []
    for char in target_character_table:
        if char in source_character_table:
            position = source_character_table.index(char)
            if position < len(input_text):
                result.append(input_text[position])
    return ''.join(result)

def main():
    encrypted_data = [
        2025548301, -1806830254, -1580585371, -1007390782,
        1359709314, 672074166, 2062613310, -661606987, 1927004767
    ]
    
    decryption_key = [
        0x3ED6325B, 0xD709BF17, 0xE3F27E18, 0xA0870791,
        0x0146D6F9, 0x7C6140FF, 0x10B69406, 0x94DDE0F6, 0x40B2BB6C
    ]
    
    source_mapping_table = "5p6h7q8d9risbtjuevkwaxlyfzm0c1n2g3o4"
    target_mapping_table = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    decrypted_values = decrypt_ciphertext(encrypted_data, decryption_key)
    original_text = convert_ints_to_string(decrypted_values)
    
    print("解密后原始文本:", original_text)
    
    transformed_text = apply_custom_character_mapping(original_text, source_mapping_table, target_mapping_table)
    print("映射后文本:", transformed_text)

if __name__ == "__main__":
    main()
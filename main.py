from urllib.parse import urlparse, parse_qs


def decode_wordle(encoded_str):
    """Декодирует слово из Wordle"""
    if len(encoded_str) < 6:
        return "Ошибка: строка слишком короткая"

    core_str = encoded_str[3:-3].lower()

    reverse_map = {
        'f': 'а', '1': 'б', 'd': 'в', 'u': 'г', 'l': 'д',
        't': 'е', '`': 'ё', '2': 'ж', 'p': 'з', 'b': 'и',
        'q': 'й', 'r': 'к', 'k': 'л', 'v': 'м', 'y': 'н',
        'j': 'о', 'g': 'п', 'h': 'р', 'c': 'с', 'n': 'т',
        'e': 'у', 'a': 'ф', '3': 'х', 'w': 'ц', 'x': 'ч',
        'i': 'ш', 'o': 'щ', '4': 'ъ', 's': 'ы', 'm': 'ь',
        '5': 'э', '6': 'ю', 'z': 'я'
    }

    decoded_chars = [reverse_map.get(c, c) for c in core_str]
    decoded_str = ''.join(decoded_chars)

    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    shift = 5
    result = []
    for char in decoded_str:
        if char in alphabet:
            pos = (alphabet.index(char) - shift) % len(alphabet)
            result.append(alphabet[pos])
        else:
            result.append(char)

    return ''.join(result)


def extract_word_id(url):
    """Извлекает word_id из URL"""
    try:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        return query.get('word_id', [''])[0]
    except:
        return None


def main():
    print("=" * 60)

    while True:
        print("\nВставьте ссылку Wordle или word_id:")
        user_input = input().strip()

        # Проверка на выход
        if user_input.lower() in ('q', 'exit', 'quit'):
            print("Вы вышли. Но зачем? Вы же только начали побеждать!")
            break

        # Обработка ввода
        if user_input.startswith('http'):
            word_id = extract_word_id(user_input)
            if not word_id:
                print("Ошибка: ну и че ты мне скинул?")
                continue
        else:
            word_id = user_input

        # Декодирование и вывод
        decoded = decode_wordle(word_id)
        print("\nРезультат декодирования:")
        print(f"Закодировано: {word_id}")
        print(f"Декодировано: {decoded}\n")
        print("=" * 60)




if __name__ == "__main__":
    print("""
            ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
            ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
            ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
            ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░ 
     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
Декодер https://wordle.belousov.one/ (для выхода введите 'q' или 'exit')                                          
    """)
    main()
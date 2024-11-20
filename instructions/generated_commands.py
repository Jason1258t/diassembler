from instructions.instruction import AVRInstruction
from instructions.parameter import AVRParameter

# Полный список инструкций AVR
instructions = [
    # ADD - сложение регистров
    AVRInstruction(
        name="add Rd, Rr",
        mask="0000 11rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),

    # SUB - вычитание регистров
    AVRInstruction(
        name="sub Rd, Rr",
        mask="0001 10rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    AVRInstruction(
        name="subi Rd, K",
        mask="0101 KKKK dddd KKKK",
        parameters=[
            AVRParameter(name="Rd", constraints="16< <31"),
            AVRParameter(name="K", constraints="0< <255")
        ]
    ),
    AVRInstruction(
        name="sbci Rd, K",
        mask="0100 KKKK dddd KKKK",
        parameters=[
            AVRParameter(name="Rd", constraints="16< <31"),
            AVRParameter(name="K", constraints="0< <255")
        ]
    ),
    AVRInstruction(
        name="sbic P, b",
        mask="1001 1001 PPPP Pbbb",
        parameters=[
            AVRParameter(name="P"),
            AVRParameter(name="b")
        ]
    ),
    # LDI - загрузка немедленного значения в регистр
    AVRInstruction(
        name="ldi Rd, K",
        mask="1110 KKKK dddd KKKK",
        parameters=[
            AVRParameter(name="Rd", constraints="16< <32"),
            AVRParameter(name="K", constraints="0<= <=255")
        ]
    ),
    # JMP - переход на адрес
    AVRInstruction(
        name="jmp k",
        mask="1001 010k kkkk 110k kkkk kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="k", constraints="none", options="address")
        ]
    ),
    AVRInstruction(
        name="call k",
        mask="1001 010k kkkk 111k kkkk kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="k", constraints="none", options="address")
        ]
    ),
    # BRNE - условный переход
    AVRInstruction(
        name="brne k",
        mask="1111 01kk kkkk k001",
        parameters=[
            AVRParameter(name="k", options="signed")
        ]
    ),
    # BRNE - условный переход
    AVRInstruction(
        name="breq k",
        mask="1111 00kk kkkk k001",
        parameters=[
            AVRParameter(name="k", options="signed")
        ]
    ),
    # MOV - копирование значений между регистрами
    AVRInstruction(
        name="mov Rd, Rr",
        mask="0010 11rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # OUT - вывод в порт
    AVRInstruction(
        name="out P, Rr",
        mask="1011 1PPr rrrr PPPP",
        parameters=[
            AVRParameter(name="P", constraints="0<= <=63"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # IN - ввод из порта
    AVRInstruction(
        name="in Rd, P",
        mask="1011 0PPd dddd PPPP",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="P", constraints="0<= <=63")
        ]
    ),
    # IN - ввод из порта
    AVRInstruction(
        name="sts k, Rr",
        mask="1001 001r rrrr 0000 kkkk kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="Rr", constraints="0< <32"),
            AVRParameter(name="k", constraints="0< <=65535")
        ]
    ),
    # RJMP - относительный переход
    AVRInstruction(
        name="rjmp k",
        mask="1100 kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="k", options="signed")
        ]
    ),
    # SBC - вычитание с переносом
    AVRInstruction(
        name="sbc Rd, Rr",
        mask="0000 10rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # ADC - сложение с переносом
    AVRInstruction(
        name="adc Rd, Rr",
        mask="0001 11rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # LSR - логический сдвиг вправо
    AVRInstruction(
        name="lsr Rd",
        mask="1001 010d dddd 0110",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")]),
    # ROR - циклический сдвиг вправо
    AVRInstruction(
        name="ror Rd",
        mask="1001 010d dddd 0111",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # ASR - арифметический сдвиг вправо
    AVRInstruction(
        name="asr Rd",
        mask="1001 010d dddd 0101",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # COM - инвертирование регистра
    AVRInstruction(
        name="com Rd",
        mask="1001 010d dddd 0000",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # NEG - получение отрицания регистра
    AVRInstruction(
        name="neg Rd",
        mask="1001 010d dddd 0001",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # SWAP - обмен старшего и младшего полубайта
    AVRInstruction(
        name="swap Rd",
        mask="1001 010d dddd 0010",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # DEC - декремент регистра
    AVRInstruction(
        name="dec Rd",
        mask="1001 010d dddd 1010",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # INC - инкремент регистра
    AVRInstruction(
        name="inc Rd",
        mask="1001 010d dddd 0011",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # CPI - сравнение регистра с константой
    AVRInstruction(
        name="cpi Rd, K",
        mask="0011 KKKK dddd KKKK",
        parameters=[
            AVRParameter(name="Rd", constraints="16< <32", options="none"),
            AVRParameter(name="K", constraints="0<= <=255", options="none")
        ]
    ),
    # CP - сравнение двух регистров
    AVRInstruction(
        name="cp Rd, Rr",
        mask="0001 01rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # AND - логическое И между регистрами
    AVRInstruction(
        name="and Rd, Rr",
        mask="0010 00rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # OR - логическое ИЛИ между регистрами
    AVRInstruction(
        name="or Rd, Rr",
        mask="0010 10rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # EOR - логическое исключающее ИЛИ (XOR) между регистрами
    AVRInstruction(
        name="eor Rd, Rr",
        mask="0010 01rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),
    # SBR - установка битов в регистре
    AVRInstruction(
        name="sbr Rd, K",
        mask="0110 KKKK dddd KKKK",
        parameters=[
            AVRParameter(name="Rd", constraints="16< <32", options="none"),
            AVRParameter(name="K", constraints="0<= <=255", options="none")
        ]
    ),
    # SBR - установка битов в регистре
    AVRInstruction(
        name="sbrs Rr,b",
        mask="1111 111r rrrr obbb",
        parameters=[
            AVRParameter(name="Rr", constraints="0< <32", options="none"),
            AVRParameter(name="b", constraints="0<= <=7", options="none")
        ]
    ),
    # CPSE - сравнение регистров с пропуском следующей инструкции
    AVRInstruction(
        name="cpse Rd, Rr",
        mask="0001 00rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="Rr", constraints="0< <32")
        ]
    ),

    # LDS - загрузка данных из памяти в регистр
    AVRInstruction(
        name="lds Rd, k",
        mask="1001 000d dddd 0000 kkkk kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32"),
            AVRParameter(name="k", constraints="0<= <=65535")
        ]
    ),

    # BRCS - переход, если установлен флаг переноса (C = 1)
    AVRInstruction(
        name="brcs k",
        mask="1111 00kk kkkk k000",
        parameters=[
            AVRParameter(name="k", options="signed")
        ]
    ),

    # SBR - установка битов в регистре
    AVRInstruction(
        name="push Rr",
        mask="1001 001r rrrr 1111",
        parameters=[
            AVRParameter(name="Rr", constraints="0< <32", options="none"),
        ]
    ),
    # SBR - установка битов в регистре
    AVRInstruction(
        name="rcall k",
        mask="1101 kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="k", constraints="0< <32", options="address"),
        ]
    ),
    # CBR - очистка битов в регистре
    AVRInstruction(
        name="cbr Rd, K",
        mask="0111 KKKK dddd KKKK",
        parameters=[
            AVRParameter(name="Rd", constraints="16< <32", options="none"),
            AVRParameter(name="K", constraints="0<= <=255", options="none")
        ]
    ),
    # SBI - установка бита в I/O-регистре
    AVRInstruction(
        name="sbi A, b",
        mask="1001 1010 AAAA Abbb",
        parameters=[
            AVRParameter(name="A", constraints="0<= <=31", options="none"),
            AVRParameter(name="b", constraints="0<= <=7", options="none")
        ]
    ),
    # CBI - очистка бита в I/O-регистре
    AVRInstruction(
        name="cbi A, b",
        mask="1001 1000 AAAA Abbb",
        parameters=[
            AVRParameter(name="A", constraints="0<= <=31", options="none"),
            AVRParameter(name="b", constraints="0<= <=7", options="none")
        ]
    ),
    # LSR - логический сдвиг вправо
    AVRInstruction(
        name="lsr Rd",
        mask="1001 010d dddd 0110",
        parameters=[
            AVRParameter(name="Rd", constraints="0< <32", options="none")
        ]
    ),
    # RET - возврат из подпрограммы
    AVRInstruction(
        name="ret",
        mask="1001 0101 0000 1000",
        parameters=[]
    ),
    # SEI - установка флага прерываний
    AVRInstruction(
        name="sei",
        mask="1001 0100 0111 1000",
        parameters=[]
    ),
    # CLI - очистка флага прерываний
    AVRInstruction(
        name="cli",
        mask="1001 0100 1111 1000",
        parameters=[]
    ),
    AVRInstruction(
        name="nop",
        mask="0000 0000 0000 0000",
        parameters=[]
    ),
    AVRInstruction(
        name="mul Rd, Rr",
        mask="1001 11rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
            AVRParameter(name="Rr", constraints="0<= <32")
        ]
    ),
    AVRInstruction(
        name="lpm Rd, Z+",
        mask="1001 000d dddd 0101",
        parameters=[
            AVRParameter(name="Rd"),
        ]
    ),
    AVRInstruction(
        name="st X+, Rr",
        mask="1001 001r rrrr 1101",
        parameters=[
            AVRParameter(name="Rr"),
        ]
    ),
    AVRInstruction(
        name="cpc Rd, Rr",
        mask="0000 01rd dddd rrrr",
        parameters=[
            AVRParameter(name="Rr"),
            AVRParameter(name="Rd"),
        ]
    ),

    # MULS - умножение знаковых 8-битных значений
    AVRInstruction(
        name="muls Rd, Rr",
        mask="0000 0010 dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="16<= <32"),
            AVRParameter(name="Rr", constraints="16<= <32")
        ]
    ),

    # LSL - логический сдвиг влево
    AVRInstruction(
        name="lsl Rd",
        mask="0000 11dd dddd dddd",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32")
        ]
    ),

    # PUSH - сохранение регистра в стек
    AVRInstruction(
        name="push Rd",
        mask="1001 001d dddd 1111",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32")
        ]
    ),

    # POP - восстановление регистра из стека
    AVRInstruction(
        name="pop Rd",
        mask="1001 000d dddd 1111",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32")
        ]
    ),

    # BREAK - остановка программы
    AVRInstruction(
        name="break",
        mask="1001 0101 1001 1000",
        parameters=[]
    ),

    # SLEEP - режим сна
    AVRInstruction(
        name="sleep",
        mask="1001 0101 1000 1000",
        parameters=[]
    ),

    # WDR - сброс сторожевого таймера
    AVRInstruction(
        name="wdr",
        mask="1001 0101 1010 1000",
        parameters=[]
    ),
    # LD (X) - Загрузка из памяти по адресу регистра X
    AVRInstruction(
        name="ld Rd, X",
        mask="1001 000d dddd 1100",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),

    # ST (X) - Запись в память по адресу регистра X
    AVRInstruction(
        name="st X, Rr",
        mask="1001 001r rrrr 1100",
        parameters=[
            AVRParameter(name="Rr", constraints="0<= <32"),
        ]
    ),

    # LD (Y) с постинкрементом - Загрузка из памяти по адресу регистра Y с увеличением
    AVRInstruction(
        name="ld Rd, Y+",
        mask="1001 000d dddd 1001",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),
    AVRInstruction(
        name="ld Rd,Y",
        mask="1000 000d dddd 1000",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),
    AVRInstruction(
        name="ld Rd,Z",
        mask="1000 000d dddd 0000",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),

    # LDD (Z+) - Загрузка из памяти по адресу Z с увеличением
    AVRInstruction(
        name="ldd Rd, Z+",
        mask="1001 000d dddd 0001",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),
    # LDD (Z+) - Загрузка из памяти по адресу Z с увеличением
    AVRInstruction(
        name="ldd Rd, Z+q",
        mask="10q0 qq0d dddd 0qqq",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
            AVRParameter(name="q"),
        ]
    ),
    # LDD (Z+) - Загрузка из памяти по адресу Z с увеличением
    AVRInstruction(
        name="std Z+q, Rr",
        mask="10q0 qq1r rrrr 0qqq",
        parameters=[
            AVRParameter(name="Rr", constraints="0<= <32"),
            AVRParameter(name="q"),
        ]
    ),
    # LDD (Z+) - Загрузка из памяти по адресу Z с увеличением
    AVRInstruction(
        name="reti",
        mask="1001 0101 0001 1000",
        parameters=[]
    ),
    AVRInstruction(
        name="ld Rd,Z+",
        mask="1001 000d dddd 0001",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),
    # ST (Z+) - Запись в память по адресу Z с увеличением
    AVRInstruction(
        name="st Z+, Rr",
        mask="1001 001r rrrr 0001",
        parameters=[
            AVRParameter(name="Rr", constraints="0<= <32"),
        ]
    ),

    # ST (Z) - Запись в память по адресу регистра Z
    AVRInstruction(
        name="st Z, Rr",
        mask="1000 001r rrrr 0000",
        parameters=[
            AVRParameter(name="Rr", constraints="0<= <32"),
        ]
    ),

    # POP - восстановление регистра из стека
    AVRInstruction(
        name="pop Rd",
        mask="1001 000d dddd 1111",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),
    # ST (Y) с постинкрементом - Запись в память по адресу регистра Y с увеличением
    AVRInstruction(
        name="st Y+, Rr",
        mask="1001 001r rrrr 1001",
        parameters=[
            AVRParameter(name="Rr", constraints="0<= <32"),
        ]
    ),

    # LDD (Y+q) - Загрузка из памяти по адресу Y с добавлением смещения q
    AVRInstruction(
        name="ldd Rd, Y+q",
        mask="10q0 qq0d dddd 1qqq",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
            AVRParameter(name="q", constraints="0<= <63"),
        ]
    ),

    # STD (Y+q) - Запись в память по адресу Y с добавлением смещения q
    AVRInstruction(
        name="std Y+q, Rr",
        mask="10q0 qq1r rrrr 1qqq",
        parameters=[
            AVRParameter(name="Rr", constraints="0<= <32"),
            AVRParameter(name="q", constraints="0<= <63"),
        ]
    ),

    # MOVW - Копирование значений из пары регистров в пару регистров
    AVRInstruction(
        name="movw Rd, Rr",
        mask="0000 0001 dddd rrrr",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
            AVRParameter(name="Rr", constraints="0<= <32"),
        ]
    ),

    # ELPM (Z) - Загрузка из расширенной памяти по адресу Z
    AVRInstruction(
        name="elpm Rd, Z",
        mask="1001 000d dddd 0110",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),

    # ELPM (Z+) - Загрузка из расширенной памяти по адресу Z с увеличением
    AVRInstruction(
        name="elpm Rd, Z+",
        mask="1001 000d dddd 0111",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),

    # LPM (Z) - Загрузка из программной памяти по адресу Z
    AVRInstruction(
        name="lpm Rd, Z",
        mask="1001 000d dddd 0100",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),

    # LPM (Z+) - Загрузка из программной памяти по адресу Z с увеличением
    AVRInstruction(
        name="lpm Rd, Z+",
        mask="1001 000d dddd 0101",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),

    # XCH - Обмен содержимого регистра и адресуемой памяти
    AVRInstruction(
        name="xch Rd, Z",
        mask="1001 001d dddd 1010",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
        ]
    ),

    # LDS - Загрузка из абсолютного адреса SRAM
    AVRInstruction(
        name="lds Rd, k",
        mask="1001 000d dddd 0000 kkkk kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="Rd", constraints="0<= <32"),
            AVRParameter(name="k", constraints="0<= <65536"),
        ]
    ),

    # STS - Запись в абсолютный адрес SRAM
    AVRInstruction(
        name="sts k, Rr",
        mask="1001 001r rrrr 0000 kkkk kkkk kkkk kkkk",
        parameters=[
            AVRParameter(name="Rr", constraints="0<= <32"),
            AVRParameter(name="k", constraints="0<= <65536"),
        ]
    ),

]


def show_commands():
    for instruction in instructions:
        print(f"Instruction: {instruction.name}")
        print(f"Mask: {instruction.mask}")
        for param in instruction.parameters:
            print(f"  Param: {param.name}, Constraints: {param.constraints}, Options: {param.options}")
        print("\n")

colorMap={
'purple':'\033[95m',
'blue':'\033[94m',
'cyan':'\033[96m',
'green':'\033[92m',
'warning':'\033[93m',
'fail':'\033[91m',
'bold':'\033[1m',
'underline':'\033[4m',
}
#format: printc(text_to_print, color)
def printColor(text,color):
    print(colorMap[color]+text+'\033[0m')

    
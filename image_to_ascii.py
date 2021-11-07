from PIL import Image
import sys

BRIGHTNESS = 500  # seems good

def image_to_ascii(imageName, res):
    image = Image.open(imageName)

    textFile = open("imageToAscii.txt", 'w')

    for y in range(0, image.height - res, res):
        if y != 0:
            textFile.write('\n')
        for x in range(0, image.width - res, res):
            ave = ave_of_neighbors(image, x, y, res)
            char = determine_char(BRIGHTNESS, ave)

            textFile.write(char)


def ave_of_neighbors(image, x, y, res):
    ave = 0

    for i in range(res):
        for j in range(res):
            ave += sum(image.getpixel((x + i, y + j)))

    return ave / (res * res)


def determine_char(threshold, ave):

    # #Xx=+~-

    # magic numbers that ill fix at some point maybe idk
    if ave < threshold - 400:
        return '#'
    elif ave < threshold - 350:
        return 'X'
    elif ave < threshold - 300:
        return 'x'
    elif ave < threshold - 250:
        return '='
    elif ave < threshold - 200:
        return '+'
    elif ave < threshold - 150:
        return '~'
    elif ave < threshold - 100:
        return '-'
    elif ave < threshold - 50:
        return '-'
    else:
        return '.'


if __name__ == "__main__":
    try:
        if sys.argv[1] == "-h":
            print("argv: <filename> <sample size: bigger number means lower resolution Try 2 to 64>")
        else:
            file = sys.argv[1]
            sampleSize = int(sys.argv[2])

            image = Image.open(file)

            assert(sampleSize > 1 and sampleSize <= 64)

            image_to_ascii(file, sampleSize)
    except FileNotFoundError:
        print("File not found!")
    except IndexError:
        print("Not enough arguments given: <filename> <sample size: bigger number means lower resolution Try 2 to 64>")
    except AssertionError:
        print("Sample size must be greater than 1 and less than 65. Try 2 to 64")

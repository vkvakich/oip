import RPi.GPIO as IO

def decimal2binary(value):
     
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()

IO.setmode(IO.BCM)

IO.setup(dac, IO.OUT)

try:
    while(1):
        print("type digit in range[0:255]")
        val = input()
        if val == 'q':
            break
        else:
            if val.isdigit():

                val = int(val)
                if val < 0 or val > 255:
                    print("wrong range")
                else: 
                    binaryList = decimal2binary(val)
                    IO.output(dac, binaryList)
                    print(binaryList)
                    print("voltage: {:.2f}".format(val/256*3.3))
            else:
                print("not a digit")
finally:
    IO.output(dac, 0)
    IO.cleanup()

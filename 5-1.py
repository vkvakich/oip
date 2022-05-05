import RPi.GPIO as gpio
import time


dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
comp = 4
troyka = 17
Vref = 3.3
#outpin = 2
bdepth = 8 #хардкод разрядности

gpio.setmode( gpio.BCM )

gpio.setup( dac, gpio.OUT, initial=gpio.LOW )
gpio.setup( troyka, gpio.OUT, initial=gpio.HIGH )
gpio.setup( comp, gpio.IN )


def decimal2binary( value ):
    return [int(bit) for bit in bin( value ) [2:].zfill( bdepth )]

def adc():
    retvalue = 0
    for decVtest in range( 2 ** bdepth ):
        gpio.output( dac, decimal2binary( decVtest ) )
        time.sleep( 0.001 )
        compsignal = gpio.input( comp )

        if compsignal == 0: #если значение на ЦАП больше исследуемого
            retvalue = decVtest
            break

    return retvalue


try:
    while 1:
        decVfind = adc()
        binVfind = decimal2binary( decVfind )

        print('decimal V = {}'.format( decVfind ))
        print('binary V = {}'.format( binVfind ))
        print('V = {}'.format( decVfind / ( 2 ** bdepth ) * Vref ))
        print( '' )
        #time.sleep( 0.01 )


finally:
    gpio.output( dac, 0 )
    gpio.output( troyka, 0 )
    gpio.cleanup()

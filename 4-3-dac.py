import RPi.GPIO as gpio


Vref = 3.3
outpin = 2

gpio.setmode( gpio.BCM )
gpio.setup( outpin, gpio.OUT )
pwmctrl = gpio.PWM( outpin, 1000 )


try:
    pwmctrl.start( 0 )

    while True:
        inputval = float( input() )
        if inputval < 0 or inputval > 100:
            print( "Invalid value!" )
            continue

        Vout = Vref *( inputval / 100 )
        print( 'V = {}'.format( Vout ) )
        pwmctrl.ChangeDutyCycle( inputval )

finally:
    gpio.output( outpin, 0 )
    gpio.cleanup()

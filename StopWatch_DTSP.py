import tkinter as Tkinter

s = int(-1)
h = int(0)
m = int(0)

running = False


def counter_label(label):
    def count():

        if running:

            global s,h,m

            # To manage the intial delay.

            if s == -1:

                display = "Starting..."

            else:


                if (int(s) < 10):
                    s = str(0) + str(int(s))
                else:
                    s = str(s)

                if (int(m) < 10):
                    m = str(0) + str(int(m))
                else:
                    m = str(m)

                if (int(h) < 10):
                    h = str(0) + str(int(h))
                else:
                    h = str(h)

                display = h + ":" + m + ":" + s

            label['text'] = display  # Or label.config(text=display)

            # label.after(arg1, arg2) delays by

            # first argument given in milliseconds

            # and then calls the function given as second argument.

            # Generally like here we need to call the

            # function in which it is present repeatedly.

            # Delays by 1000ms=1 seconds and call count again.

            label.after(980, count)

            s = int(s)
            m = int(m)
            h = int(h)

            if s >= 59:
                s = 0
                if m >= int(59):
                    h = h + 1
                    m = 0
                else:
                    m = m + 1
            else:
                s = int(s)
                s += 1


    # Triggering the start of the counter.

    count()


# start function of the stopwatch

def Start(label):
    global running

    running = True

    counter_label(label)

    start['state'] = 'disabled'

    stop['state'] = 'normal'

    reset['state'] = 'normal'


# Stop function of the stopwatch

def Stop():
    global running,s,h,m

    start['state'] = 'normal'

    stop['state'] = 'disabled'

    reset['state'] = 'normal'

    running = False



# Reset function of the stopwatch

def Reset(label):
    global s,h,m

    s = -1
    m = 0
    h = 0
    # If rest is pressed after pressing stop

    if running == False:

        reset['state'] = 'disabled'

        label['text'] = 'Welcome!'



    # If reset is pressed while the stopwatch is running.

    else:

        label['text'] = 'Starting...'


root = Tkinter.Tk()

root.title("Stopwatch")

# Fixing the window size.

root.minsize(width=250, height=70)

label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()

start = Tkinter.Button(root, text='Start', width=15, command=lambda: Start(label))

stop = Tkinter.Button(root, text='Stop', width=15, state='disabled', command=Stop)

reset = Tkinter.Button(root, text='Reset', width=15, state='disabled', command=lambda: Reset(label))
start.pack()
stop.pack()
reset.pack()
root.mainloop()

"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jasmine Scott.
"""  # COMPLETED: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # COMPLETED: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window = tkinter.Tk()

    # ------------------------------------------------------------------
    # COMPLETED: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    window_frame = ttk.Frame(window, padding=20)
    window_frame.grid()
    # ------------------------------------------------------------------
    # COMPLETED: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    window_button = ttk.Button(window_frame, text='OOF')
    window_button.grid()
    # ------------------------------------------------------------------
    # COMPLETED: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    window_button['command'] = (lambda: words(['Jasmine', 3 // 2, 4, True, 'me'], 4))
    window_button.grid()
    # ------------------------------------------------------------------
    # COMPLETED: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    window_entry = ttk.Entry(window_frame)
    window_entry.grid()

    new_button = ttk.Button(window_frame, text='Print what you type')
    new_button['command'] = (lambda: print_entry(window_entry))

    new_button.grid()

    # ------------------------------------------------------------------
    # COMPLETED: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    new_window_entry = ttk.Entry(window_frame)
    new_window_entry.grid()

    third_button = ttk.Button(window_frame, text='Todo #7')
    third_button['command'] = (lambda: print_n_times(window_entry.get(), new_window_entry.get()))

    third_button.grid()
    # ------------------------------------------------------------------
    # COMPLETED: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    window.mainloop()


def print_n_times(s, n):
    """Prints words_typed n times"""
    total = ''
    for k in range(int(n)):
        total = total + s
    print(total)


def print_entry(words_typed):
    entry = words_typed.get()
    if entry == 'ok':
        print('Hello')
    else:
        print('Goodbye')


def words(sequence, n):
    """"Prints the nth index."""
    print(sequence[n])
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------


main()


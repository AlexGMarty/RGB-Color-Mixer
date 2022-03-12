# Developed for CIS156 at SMCC
# ASSIGNMENT 27 - RGB Color Mixer
# Developed by Alex Marty for CIS156 at SMCC (Fall 2021)

import tkinter


# decToHex method for converting decimal color values to hex
def decToHex(decimal):
    hexValues = "0123456789ABCDEF"
    sixteens = decimal // 16
    ones = decimal % 16
    return hexValues[sixteens] + hexValues[ones]


# setColor method for changing swatch color and hex code at bottom
def setColor(event):
    r = int(redSlider.get())
    g = int(greenSlider.get())
    b = int(blueSlider.get())
    hexColor = '#' + decToHex(r) + decToHex(g) + decToHex(b)
    swatch.configure(bg=hexColor)
    hexLabel.configure(text=hexColor)


swatchColor = '#000000'  # Set starting swatch color variable
bgColor = '#8888ff'  # Set background color variable

# Create main window
root = tkinter.Tk()
root.config(background=bgColor)
root.title("CIS156 RGB Color Mixer")

# Label for title and subtitle at the top
titleLabel = tkinter.Label(root, text="RGB Swatch",
                           width=14, anchor='center', borderwidth='3')
titleLabel.config(fg='black', bg=bgColor, font='Arial 24 bold italic')
titleLabel.pack(pady=5)
subtitleLabel = tkinter.Label(root, text="Program by Alex Marty",
                              anchor='center', borderwidth='3')
subtitleLabel.config(fg='black', bg=bgColor, font='Arial 14 bold underline')
subtitleLabel.pack()

# swatch Canvas to hold swatch square
swatch = tkinter.Canvas(root, width=200, height=200)
swatch.create_rectangle(0, 0, 203, 203)
swatch.configure(bg=swatchColor)
swatch.pack(pady=15)

# Frame sliderFrame to hold three sliders
sliderFrame = tkinter.Frame(root, bg=bgColor)
redSlider = tkinter.Scale(sliderFrame, bg='red', length=256,
                          tickinterval=32, from_=255, to_=0, command=setColor)
greenSlider = tkinter.Scale(sliderFrame, bg='green', length=256,
                            tickinterval=32, from_=255, to_=0, command=setColor)
blueSlider = tkinter.Scale(sliderFrame, bg='blue', length=256,
                           tickinterval=32, from_=255, to_=0, command=setColor)
sliderFrame.pack(pady=0)
redSlider.pack(side='left', padx=10)
greenSlider.pack(side='left', padx=10)
blueSlider.pack(side='left', padx=10)

# Label hexLabel to show hex value of swatch
hexLabel = tkinter.Label(root, text=swatchColor,
                         width=24, anchor='center', borderwidth='3')
hexLabel.config(fg='black', bg=bgColor, font='Arial 18 bold')
hexLabel.pack(pady=5)

# Run the application
root.mainloop()

import pywhatkit as pw
txt = input("Enter text to be converted:")
pw.text_to_handwriting(txt,"demo2.png",[255,0,0])
print("END")
# Exercise 6.5

text = "X-DSPAM-Confidence: 0.8475"

cfind = text.find("0")
print cfind

number = float(text[cfind:])

print number
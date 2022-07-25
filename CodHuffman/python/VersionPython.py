import math
import sys
global probabilities
probabilities = []

class HuffmanCode:
    def __init__(self,probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if(value >= self.probability[j]):
                return j
        return index-1

    def characteristics_huffman_code(self, code):
        
        length_of_code = [len(k) for k in code]

        mean_length = sum([a*b for a, b in zip(length_of_code, self.probability)])

        entropy_of_code = sum([-b*math.log2(b) for a, b in zip(length_of_code, self.probability)])

        print("Entropia: %f"% entropy_of_code)
        print("Average length of the code: %f" % mean_length)
        print("Efficiency of the code: %f" % (entropy_of_code/mean_length))

    def compute_code(self):
        LongitudPalabra = len(self.probability)
        huffman_code = ['']*LongitudPalabra

        for i in range(LongitudPalabra-2):
            val = self.probability[LongitudPalabra-i-1] + self.probability[LongitudPalabra-i-2]
            if(huffman_code[LongitudPalabra-i-1] != '' and huffman_code[LongitudPalabra-i-2] != ''):
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif(huffman_code[LongitudPalabra-i-1] != ''):
                huffman_code[LongitudPalabra-i-2] = '0'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif(huffman_code[LongitudPalabra-i-2] != ''):
                huffman_code[LongitudPalabra-i-1] = '1'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:
                huffman_code[LongitudPalabra-i-1] = '1'
                huffman_code[LongitudPalabra-i-2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if(isinstance(huffman_code[LongitudPalabra-i-2], list) and isinstance(huffman_code[LongitudPalabra-i-1], list)):
                complete_code = huffman_code[LongitudPalabra-i-1] + huffman_code[LongitudPalabra-i-2]
            elif(isinstance(huffman_code[LongitudPalabra-i-2], list)):
                complete_code = huffman_code[LongitudPalabra-i-2] + [huffman_code[LongitudPalabra-i-1]]
            elif(isinstance(huffman_code[LongitudPalabra-i-1], list)):
                complete_code = huffman_code[LongitudPalabra-i-1] + [huffman_code[LongitudPalabra-i-2]]
            else:
                complete_code = [huffman_code[LongitudPalabra-i-2], huffman_code[LongitudPalabra-i-1]]

            huffman_code = huffman_code[0:(len(huffman_code)-2)]
            huffman_code.insert(position, complete_code)

        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        if(len(huffman_code[1]) == 0):
            huffman_code[1] = '1'

        count = 0
        final_code = ['']*LongitudPalabra

        for i in range(2):
            for j in range(len(huffman_code[i])):
                final_code[count] = huffman_code[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code

string = input("Enter the string to compute Huffman Code: ")

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
length = len(string)

probabilities = [float("{:.2f}".format(frequency[1]/length)) for frequency in freq]
probabilities = sorted(probabilities, reverse=True) 

huffmanClassObject = HuffmanCode(probabilities)

huffman_code = huffmanClassObject.compute_code()

print(' Char | Huffman code ')
print('----------------------')

for id,char in enumerate(freq):
    if huffman_code[id]=='':
        print(' %-4r |%12s' % (char[0], 1))
        continue
    print(' %-4r |%12s' % (char[0], huffman_code[id])) 
print ("\n")
print('La trama total es: ')
for i in range(len(huffman_code)):  
    print(huffman_code[i],end='')
print ("\n")


huffmanClassObject.characteristics_huffman_code(huffman_code)
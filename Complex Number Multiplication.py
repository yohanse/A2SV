class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = num1.split('+')
        real2, imag2 = num2.split('+')
        imag1, imag2 = imag1[:-1], imag2[:-1]
        result_real = str(int(real1)*int(real2) - int(imag1)*int(imag2))
        result_imag = str(int(real1)*int(imag2) + int(imag1)*int(real2))
        return result_real + '+' + result_imag + 'i'
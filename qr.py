import qrcode


name = input('Enter your name: ')
n = int(input('Enter your Phone Number: '))

q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)

q.add_data(name)
q.add_data(n)
i = q.make_image(fill_color = 'cyan', back_color = 'red')


i.save('1.png')



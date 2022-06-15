import hashlib


hash32 = "5949e7111facd27cdb755252c342c1e8089277b6803142a7e08f71679528163c"
pincode = 0
request = "Bank SunBank. Src: 2445-5900-1167, Dest: 2445-5833-9378, Amount: 12000 $, PIN: " + str(pincode) + "."

while pincode <= 9999:
	request = "Bank SunBank. Src: 2445-5900-1167, Dest: 2445-5833-9378, Amount: 12000 $, PIN: " + str(pincode) + "."
	hashvalue = hashlib.sha256(str(request).encode())
	print(hashvalue.hexdigest())
	pincode +=1

	if hashvalue.hexdigest() == hash32:
		break


print('Пинкод взломан:' + str(pincode - 1) )

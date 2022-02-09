print("counting vowels and consonants in a string...");
mystr=input("Enter a string: ");
vow=0
cons=0
for i in mystr:
	if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or
i=='o' or i=='U' or i=='I'):
		vow=vow+1;
	else:
		cons=cons+1;
print('total letters counted: ', vow + cons);
print('vowels counted: ',vow);
print('consonants counted: ',cons);
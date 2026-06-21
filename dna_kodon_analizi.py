DNA= "ATGTAGATAATGTAAATGGTATGATAGTGATAA"
start_found = False
for i in range (0,len(DNA),3):
    codon =DNA[i:i+3]

    if codon =="ATG":
        print("başlangıç kodonu bulundu:")
        start_found = True
        continue
    if start_found:
         if codon in["TAA","TGA","TAG"]:
              print("stop kodonu bulundu:")

         else:
             print("devam:",codon)


else:
        print("geçerli bir codon giriniz")

DNA= "ATGTAGATAATGTAAATGGTATGATAGTGATAA"
start_found = False
for i in range (0,len(DNA),3):
    codon =DNA[i:i+3]

    if codon =="ATG":
        print("başlangıç kodonu bulundu:")
        start_found = True
        continue
    if start_found:
         if codon in["TAA","TGA","TAG"]:
              print("stop kodonu bulundu:")

         else:
             print("devam:",codon)


else:
        print("geçerli bir codon giriniz")

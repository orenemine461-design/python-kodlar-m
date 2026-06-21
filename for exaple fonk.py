

def gc_oranı(dna,ignore_case= True):
    if ignore_case:
        dna =dna.upper()

    for harf in dna:
        if harf not in "AGTC":
            print("Geçersiz dna")
            return

        if not set(dna).issubset({"A", "T", "G", "C"}):
            print("Geçersiz DNA")
            return
    g =dna.count("G")
    c =dna.count("C")
    toplam=len(dna)
    if toplam ==0:
        return


    return (g+c)/ toplam * 100
print(gc_oranı("GCGCCGTAgccA"))
print(gc_oranı("GCHGCAT"))

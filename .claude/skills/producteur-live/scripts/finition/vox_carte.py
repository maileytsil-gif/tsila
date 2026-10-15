"""Carte d'une voix (stem mono 16 bits) en doubles-croches : note détectée (YIN) ou « ~ » (souffle) ou « . » (silence), une ligne par mesure.
Usage : python3 vox_carte.py voix16mono.wav MESURE_DEBUT MESURE_FIN OFFSET_S TEMPS_REF BPM
Calage : seconde du fichier = OFFSET_S + (temps d'arrangement − TEMPS_REF) × 60/BPM  (relever un point commun fichier/arrangement).
Ex. Madame Gaspar : 3.43 8 120. Noms Ableton : C3 = 60."""
import wave,numpy as np,sys
f=wave.open(sys.argv[1]);sr=f.getframerate();x=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).astype(float)/32768
b0,b1=int(sys.argv[2]),int(sys.argv[3]);OFF,REF,BPM=float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]);SPB=60/BPM
ft=lambda B:OFF+(B-REF)*SPB;NAMES=['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
def pitch(seg):
    seg=seg-seg.mean();n=len(seg);lo,hi=int(sr/1000),int(sr/80)
    d=np.array([np.sum((seg[:n-hi]-seg[t:t+n-hi])**2) for t in range(hi+1)]);c=d.copy();c[1:]=d[1:]*np.arange(1,len(d))/np.maximum(np.cumsum(d[1:]),1e-12);c[0]=1
    t=lo+np.argmin(c[lo:hi]);return None if c[t]>0.25 else 69+12*np.log2(sr/t/440)
for bar in range(b0,b1+1):
    s=''
    for k in range(16):
        B=(bar-1)*4+k*0.25;a=int(ft(B)*sr);e=int(ft(B+0.25)*sr);db=20*np.log10(np.sqrt(np.mean(x[a:e]**2))+1e-9)
        m=pitch(x[a:a+2048]) if db>-35 else None
        s+=' .  ' if db<-40 else (' ~  ' if m is None else (NAMES[int(round(m))%12]+str(int(round(m))//12-2)).ljust(4))
    print(f'{bar:3d} |{s}')

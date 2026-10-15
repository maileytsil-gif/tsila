"""Qui remplit les aigus ? Niveau et largeur 3-8 kHz et 8-16 kHz de chaque piste d'un export « Toutes les pistes individuelles ».
Usage : python3 aigus_pistes.py <dossier des stems> [préfixe]   (trié par niveau 8-16k décroissant ; pistes post-fader, avant bus)
Comparer au Main du même export : la source la plus forte ET la plus centrée (corr > 0,85) est celle qui rétrécit l'image."""
import sys,glob,os,subprocess,tempfile,wave,numpy as np
D=sys.argv[1];pre=sys.argv[2] if len(sys.argv)>2 else '';tmp=os.path.join(tempfile.mkdtemp(),'s.wav');out=[]
for p in sorted(glob.glob(os.path.join(D,pre+'*.wav'))):
    subprocess.run(['afconvert','-f','WAVE','-d','LEI16@44100',p,tmp],check=True)
    f=wave.open(tmp);x=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).reshape(-1,2).astype(float)/32768
    L,R=x[:,0],x[:,1];N=1<<15;fr=np.fft.rfftfreq(N,1/44100);row=[]
    for lo,hi in [(3000,8000),(8000,16000)]:
        m=(fr>=lo)&(fr<hi);a=np.zeros(4);k=0
        for i in range(0,len(L)-N,N):
            Fl=np.fft.rfft(L[i:i+N]*np.hanning(N))[m];Fr=np.fft.rfft(R[i:i+N]*np.hanning(N))[m]
            a+=[np.sum(abs(Fl+Fr)**2/4),np.sum(abs(Fl-Fr)**2/4),np.real(np.sum(Fl*np.conj(Fr))),np.sqrt(np.sum(abs(Fl)**2)*np.sum(abs(Fr)**2))];k+=1
        row+=[10*np.log10((a[0]+a[1])/max(k,1)+1e-20),a[2]/(a[3]+1e-20)]
    out.append((os.path.basename(p)[len(pre):-4],row))
for n,r in sorted(out,key=lambda z:-z[1][2]):
    if r[2]>-150: print(f'{n[:26]:26} 3-8k {r[0]:6.1f} dB corr {r[1]:+.2f} | 8-16k {r[2]:6.1f} dB corr {r[3]:+.2f}')

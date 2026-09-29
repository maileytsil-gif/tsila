import sys,numpy as np,wave
def read24(p):
    w=wave.open(p); n=w.getnframes(); ch=w.getnchannels(); sr=w.getframerate(); b=w.readframes(n)
    a=np.frombuffer(b,dtype=np.uint8).reshape(-1,3)
    x=(a[:,0].astype(np.int32)|(a[:,1].astype(np.int32)<<8)|(a[:,2].astype(np.int32)<<16)); x=np.where(x>=1<<23,x-(1<<24),x)/float(1<<23)
    return x.reshape(-1,ch).mean(1),sr
x,sr=read24(sys.argv[1]); spb=60/128.
t0=48*4*spb; seg=x[int(t0*sr):int((t0+8*4*spb)*sr)]
db=lambda v:20*np.log10(max(v,1e-12))
# hits: every beat
L=int(0.4*sr); hits=np.array([seg[int(i*spb*sr):int(i*spb*sr)+L] for i in range(32) if int(i*spb*sr)+L<len(seg)])
h=hits.mean(0)
env=np.abs(h); pk=env.max(); ipk=env.argmax()
print('crête coup moyen %.1f dBFS à %.1f ms'%(db(pk),ipk/sr*1000))
sm=np.convolve(env,np.ones(int(sr*0.002))/int(sr*0.002),'same')
for th in (-6,-20,-40,-60):
    idx=np.where(sm>pk*10**(th/20))[0]; print('  durée au-dessus de %d dB : %.0f ms'%(th,(idx[-1])/sr*1000))
# pitch track via zero crossings windows
zc=np.where(np.diff(np.signbit(h)))[0]
for a,b in [(0,10),(10,20),(20,40),(40,80),(80,150),(150,250)]:
    z=zc[(zc>=a*sr/1000)&(zc<b*sr/1000)]
    if len(z)>2: print('  hauteur %3d–%3d ms : %.0f Hz'%(a,b,sr/(2*np.mean(np.diff(z)))))
S=np.abs(np.fft.rfft(hits*np.hanning(L),axis=1))**2; S=S.mean(0); f=np.fft.rfftfreq(L,1/sr)
tot=S[(f>20)&(f<20000)].sum()
for a,b in [(20,40),(40,60),(60,90),(90,130),(130,200),(200,400),(400,800),(800,2000),(2000,5000),(5000,10000),(10000,20000)]:
    e=S[(f>=a)&(f<b)].sum(); print('  %5d–%5d Hz : %5.1f dB rel. (%4.1f %%)'%(a,b,10*np.log10(e/tot),100*e/tot))
print('crête/RMS segment %.1f dB'%(db(np.abs(seg).max())-db(np.sqrt((seg**2).mean()))))

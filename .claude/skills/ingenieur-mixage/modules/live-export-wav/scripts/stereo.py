import sys, wave, numpy as np
def load(p):
    w=wave.open(p); n=w.getnframes(); sw=w.getsampwidth(); ch=w.getnchannels(); sr=w.getframerate()
    b=w.readframes(n)
    if sw==3:
        a=np.frombuffer(b,np.uint8).reshape(-1,3).astype(np.int32)
        x=(a[:,0]|(a[:,1]<<8)|(a[:,2]<<16)); x=np.where(x>=1<<23,x-(1<<24),x)/float(1<<23)
    elif sw==2: x=np.frombuffer(b,np.int16)/32768.
    else: x=np.frombuffer(b,np.int32)/2**31
    x=x.reshape(-1,ch)
    if ch==1: x=np.repeat(x,2,1)
    return x,sr
BANDS=[(20,120),(120,500),(500,2000),(2000,8000),(8000,20000)]
def stats(x,sr):
    N=8192; L=x[:,0]; R=x[:,1]
    nb=len(L)//N
    if nb==0: return None
    Lf=np.fft.rfft(L[:nb*N].reshape(nb,N)*np.hanning(N),axis=1); Rf=np.fft.rfft(R[:nb*N].reshape(nb,N)*np.hanning(N),axis=1)
    f=np.fft.rfftfreq(N,1/sr); out=[]
    for lo,hi in BANDS:
        k=(f>=lo)&(f<hi); l=Lf[:,k]; r=Rf[:,k]
        ll=(abs(l)**2).sum(); rr=(abs(r)**2).sum(); lr=(l*np.conj(r)).real.sum()
        m=((abs(l+r)/2)**2).sum(); s=((abs(l-r)/2)**2).sum()
        if ll+rr<1e-12: out.append(None); continue
        out.append((lr/np.sqrt(ll*rr+1e-30), 10*np.log10(s/m+1e-12), 10*np.log10(ll/rr+1e-12), 10*np.log10((ll+rr)/2+1e-30)))
    return out
if __name__=='__main__':
    p=sys.argv[1]; secs=[a.split(':') for a in sys.argv[2:]]
    x,sr=load(p); print(p.split('/')[-1], sr, 'Hz', round(len(x)/sr,1),'s')
    for name,a,b in secs:
        a=float(a);b=float(b); seg=x[int(a*sr):int(b*sr)]
        st=stats(seg,sr)
        if st is None: continue
        print(f'{name:<14}', ' | '.join('    —      ' if v is None else f'c{v[0]:+.2f} S/M{v[1]:+5.1f} G/D{v[2]:+4.1f}' for v in st))

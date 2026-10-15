import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/',1)[0]); from stereo import load
def biquad(x,b,a):
    y=np.zeros_like(x); x1=x2=y1=y2=np.zeros(x.shape[1])
    # vectorised per-sample loop is slow; use lfilter equivalent via direct form in chunks
    import numpy as _n
    for i in range(len(x)):
        xi=x[i]; yi=b[0]*xi+b[1]*x1+b[2]*x2-a[1]*y1-a[2]*y2
        x2=x1;x1=xi;y2=y1;y1=yi; y[i]=yi
    return y
def kcoef(fs):
    # pyloudnorm / BS.1770 coefficients recomputed for fs
    import math
    G=3.999843853973347; f0=1681.974450955533; Q=0.7071752369554196
    K=math.tan(math.pi*f0/fs); Vh=10**(G/20); Vb=Vh**0.4996667741545416
    a0=1+K/Q+K*K
    b1=[(Vh+Vb*K/Q+K*K)/a0, 2*(K*K-Vh)/a0, (Vh-Vb*K/Q+K*K)/a0]; a1=[1,2*(K*K-1)/a0,(1-K/Q+K*K)/a0]
    f0=38.13547087602444; Q=0.5003270373238773; K=math.tan(math.pi*f0/fs)
    a0=1+K/Q+K*K
    b2=[1,-2,1]; a2=[1,2*(K*K-1)/a0,(1-K/Q+K*K)/a0]
    return (b1,a1),(b2,a2)
def lfilter(b,a,x):
    try:
        from scipy.signal import lfilter as lf; return lf(b,a,x,axis=0)
    except ImportError: pass
    # fast IIR via numpy: process in float64 with python loop over samples is slow -> use recursive doubling not trivial; use loop with arrays of shape (n,2)
    return biquad(x,b,a)
def lufs(x,fs):
    (b1,a1),(b2,a2)=kcoef(fs)
    y=lfilter(b2,a2,lfilter(b1,a1,x))
    blk=int(0.4*fs); hop=int(0.1*fs)
    p=(y**2)
    cs=np.concatenate([np.zeros((1,2)),np.cumsum(p,0)])
    starts=np.arange(0,len(y)-blk+1,hop)
    z=(cs[starts+blk]-cs[starts])/blk
    lk=-0.691+10*np.log10(z.sum(1)+1e-20)
    g=z[lk>-70]; lg=-0.691+10*np.log10(g.mean(0).sum())
    g2=z[lk>lg-10]; return -0.691+10*np.log10(g2.mean(0).sum())
def truepeak(x,fs,up=4):
    m=0
    N=1<<16
    for s in range(0,len(x),N):
        seg=x[s:s+N+64]
        X=np.fft.rfft(seg,axis=0); n=len(seg)
        Y=np.zeros((n*up//2+1,2),complex); Y[:X.shape[0]]=X
        yy=np.fft.irfft(Y,n*up,axis=0)*up
        m=max(m,np.abs(yy[32*up:-32*up or None]).max() if n>128 else np.abs(yy).max())
    return 20*np.log10(m)
if __name__=='__main__':
    x,fs=load(sys.argv[1])
    print('LUFS intégré %.2f | true peak %.2f dBTP | crête sample %.2f dBFS'%(lufs(x,fs),truepeak(x,fs),20*np.log10(np.abs(x).max())))

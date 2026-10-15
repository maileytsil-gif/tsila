"""Transcription d'une voix (stem mono 16 bits) en notes JSON [[pitch, début, durée, dB]] (temps d'arrangement, C3 = 60), prête pour lom.py notes (soustraire le début du clip).
Usage : python3 vox_notes.py voix16mono.wav MESURE_DEBUT MESURE_FIN sortie.json OFFSET_S TEMPS_REF BPM   (même calage que vox_carte.py).
Erreurs d'octave et notes < 0,2 temps filtrées ; l'utilisateur corrige à l'oreille."""
import wave,numpy as np,sys,json
f=wave.open(sys.argv[1]);sr=f.getframerate();x=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).astype(float)/32768
b0,b1=float(sys.argv[2]),float(sys.argv[3])  # bars
OFF,REF,BPM=float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]);SPB=60/BPM;STEP=0.125  # triples-croches
def ft(B): return OFF+(B-REF)*SPB
def yin(seg):
    seg=seg-seg.mean();n=len(seg);lo,hi=int(sr/700),int(sr/90)
    W=n-hi
    d=np.array([np.sum((seg[:W]-seg[t:t+W])**2) for t in range(hi+1)])
    c=np.ones_like(d);cs=np.cumsum(d[1:]);c[1:]=d[1:]*np.arange(1,len(d))/np.maximum(cs,1e-12)
    cand=np.where(c[lo:hi]<0.2)[0]
    if len(cand)==0: return None
    t=lo+cand[0]
    while t+1<hi and c[t+1]<c[t]: t+=1
    return 69+12*np.log2(sr/t/440)
fr=[]
B=(b0-1)*4
while B<(b1-1)*4:
    a=int(ft(B)*sr);seg=x[a:a+1400]
    db=20*np.log10(np.sqrt(np.mean(x[a:int(ft(B+STEP)*sr)]**2))+1e-9)
    m=yin(seg) if db>-36 else None
    fr.append((B,db,m));B+=STEP
# median smoothing of pitch, fold octave errors toward neighbours
P=[None if m is None else m for _,_,m in fr]
notes=[];cur=None
for i,(B,db,m) in enumerate(fr):
    p=None if m is None else int(round(m))
    if p is not None and p<55: p=None   # sub-octave errors
    if cur and p is not None and abs(p-cur[0])<=0 : cur[2]=B+STEP-cur[1];cur[3]=max(cur[3],db);continue
    if cur and p is None and db>-30 and B-cur[1]-cur[2]<0.01 and i+1<len(fr): # unvoiced but loud: extend briefly
        cur[4]+=1
        if cur[4]<=2: cur[2]=B+STEP-cur[1];continue
    if cur: notes.append(cur);cur=None
    if p is not None: cur=[p,B,STEP,db,0]
if cur: notes.append(cur)
N=['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
out=[]
for p,s,d,db,_ in notes:
    if d<0.2: continue
    bar=int(s//4)+1;bt=s%4+1
    out.append([p,round(s,3),round(d,3),round(db,1)])
    print(f"{bar}|{bt:<6.3f} {N[p%12]}{p//12-2:<3} ({p}) dur {d:.3f}  {db:.0f} dB")
json.dump(out,open(sys.argv[4],'w'))

---
titre: "Gaku52/dj-skills-guide — lead-synth.md : supersaw et leads dans Ableton Wavetable (japonais)"
source: https://raw.githubusercontent.com/Gaku52/dj-skills-guide/3ae34b88ce1c7af67e527b576c05861fa2a7e722/docs/production/10-bass-melody/lead-synth.md
recupere_le: 2026-09-24
mode: texte integral
langue: ja
axe: cuivres électroniques ; Wavetable ; supersaw
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Fiche communautaire [HEUR-lu].

# リードシンセ

**楽曲の主役となる音色を完全マスター**

リードシンセは楽曲の「顔」であり、メロディを演奏する主役の音色です。Tranceのエピックなスーパーソー、Technoのアシッドリード、Progressive Houseの感動的なプラックまで、リードシンセの音色デザインが楽曲の個性を決定づけます。このガイドでは、Wavetableを使ったプロレベルのリードシンセ作成を完全マスターします。

---

## この章で学ぶこと

- ✅ Wavetableでのリード音色設計
- ✅ Supersawテクニック（Unison 8、Detune 30-50%）
- ✅ フィルターエンベロープ
- ✅ LFOモジュレーション
- ✅ ジャンル別リード音色（Trance、Techno、House、Progressive）
- ✅ エフェクトチェイン（EQ→Comp→Reverb→Delay）
- ✅ プリセット改変テクニック

**学習時間**: 4-6時間
**難易度**: ★★★☆☆ 中級

---

## なぜリードシンセが重要なのか

### DJの視点から

**DJとして**:
- リードシンセのドロップで**フロアが爆発**する瞬間を体感
- 音色の違いで**ジャンルが識別**できる
- エピックなリードで**観客の感情が高まる**

**プロデューサーとして**:
- その「魔法の瞬間」を**自分で作り出せる**
- 音色デザインで**楽曲の個性**を確立
- Wavetableだけで**無限のリード音色**を作成

### プロの意見

> "スーパーソーリードがなければTrancejゃない。Unisonで8-16ボイス、Detune 40%が黄金律。"
> — **Armin van Buuren**

> "リードシンセは楽曲の顔。音色が弱ければ、メロディがどんなに良くても埋もれる。"
> — **Deadmau5**

> "Progressive Houseではプラックリード。アタック10ms、リリース300msで完璧。"
> — **Eric Prydz**

### 数字で見る重要性

| ジャンル | リード重要度 | 制作時間配分 | 使用頻度 |
|---------|------------|-----------|---------|
| **Trance** | ★★★★★ (100%) | 4-5時間 / 20時間 | 90% |
| **Progressive House** | ★★★★★ (100%) | 3-4時間 / 20時間 | 80% |
| **Future Bass** | ★★★★★ (100%) | 4-5時間 / 20時間 | 95% |
| **Techno** | ★★★☆☆ (60%) | 1-2時間 / 20時間 | 40% |
| **Deep House** | ★★★☆☆ (60%) | 2-3時間 / 20時間 | 50% |

---

## 1. リードシンセの種類

### 1.1 Supersaw Lead（Trance、Future Bass）

**特徴**:
- 複数のSaw波を重ねる（Unison）
- わずかにDetuneして厚みを作る
- ステレオ幅が広い
- エピック、感動的

**音色イメージ**:
```
"Waaaaaaah" - 厚い、広がる、パワフル
```

**使用ジャンル**:
- Trance 90%
- Progressive House 70%
- Future Bass 80%
- Big Room House 60%

### 1.2 Pluck Lead（Progressive House）

**特徴**:
- 短いアタック（10-30 ms）
- 短いリリース（200-500 ms）
- 歯切れが良い
- リズミック

**音色イメージ**:
```
"Plink plink plink" - 明瞭、弾む
```

**使用ジャンル**:
- Progressive House 80%
- Melodic Techno 60%
- Tech House 50%

### 1.3 Acid Lead（Techno）

**特徴**:
- 303スタイル
- フィルターのレゾナンス高め
- モジュレーション激しい
- アグレッシブ

**音色イメージ**:
```
"Beeeow beeeow" - 鋭い、酸っぱい
```

**使用ジャンル**:
- Acid Techno 90%
- Tech House 40%
- Electro House 30%

### 1.4 Stab Lead（House）

**特徴**:
- コード全体を短く鳴らす
- アタック即座（0 ms）
- リリース短い（100-200 ms）
- パンチがある

**音色イメージ**:
```
"Stab! Stab!" - 突き刺すような
```

**使用ジャンル**:
- House 60%
- Disco 70%
- Funky House 80%

---

## 2. Wavetableでの作成（Supersaw）

### Step 1: 新規トラック作成

```
1. Cmd+Shift+T（新規MIDIトラック）
2. Browser → Instruments → Wavetable
3. ドラッグ&ドロップ
```

### Step 2: Oscillator設定

**Oscillator 1（メイン）**:
```
Category: Basic Shapes
Wavetable: Saw
Position: 0.00（完全なSaw波）
Level: 0.00 dB
```

**Oscillator 2（Detune用）**:
```
Category: Basic Shapes
Wavetable: Saw
Position: 0.00
Level: 0.00 dB
Detune: +7 cents（わずかにずらす）
```

**Sub Oscillator**:
```
Off（またはLevel -12 dB、低域補強用）
```

### Step 3: Unison設定（最重要）

**Oscillator 1 Unison**:
```
Unison: 8 voices
Detune: 40%
Stereo: 70%

効果:
  - 1音が8音に分裂
  - わずかにDetuneして厚み
  - ステレオ幅70%で広がり
```

**Oscillator 2 Unison**:
```
Unison: 8 voices
Detune: 35%（Osc 1と少し違う）
Stereo: 60%
```

**結果**:
```
合計16ボイス（Osc 1: 8 + Osc 2: 8）
→ 超厚いSupersaw
```

### Step 4: Filter設定

**Filter 1（Low Pass）**:
```
Type: Low Pass (Clean)
Cutoff: 3000 Hz（初期値）
Resonance: 10-20%
```

**Filter Envelope**:
```
Attack: 10 ms
Decay: 500 ms
Sustain: 60%
Release: 300 ms
Envelope Amount: +30%

効果:
  - アタック時にフィルターが開く
  - 徐々に閉じて落ち着く
```

### Step 5: Amp Envelope

```
Attack: 10 ms（わずかなフェードイン）
Decay: 0 ms
Sustain: 100%
Release: 500 ms（長めの余韻）
```

### Step 6: Global設定

```
Voices: 8（ポリフォニー、和音対応）
Glide: 0 ms（ポルタメント無効）
```

---

## 3. ジャンル別リードシンセ

### 3.1 Trance Supersaw

**目標**: エピック、感動的、ステレオ幅広い

**Wavetable設定**:
```
Oscillator 1:
  - Wavetable: Saw
  - Unison: 8
  - Detune: 45%
  - Stereo: 80%

Oscillator 2:
  - Wavetable: Saw
  - Detune: +10 cents
  - Unison: 8
  - Detune: 40%
  - Stereo: 70%

Filter:
  - Cutoff: 4000 Hz
  - Resonance: 20%
  - Envelope Amount: +40%

Amp Envelope:
  - Attack: 20 ms
  - Release: 800 ms（長い余韻）
```

**エフェクトチェイン**:
```
1. EQ Eight:
   - High Pass 200 Hz
   - Boost 4 kHz +3 dB（明瞭さ）
   - Air 12 kHz +2 dB（輝き）

2. Compressor:
   - Ratio: 3:1
   - Threshold: -12 dB
   - Attack: 10 ms
   - Release: 100 ms

3. Send A (Reverb):
   - Hall 3.0s
   - Send Level: 30%

4. Send B (Delay):
   - 1/8 Dotted
   - Feedback: 30%
   - Send Level: 20%

5. Utility:
   - Width: 100%（最大ステレオ幅）
```

### 3.2 Progressive House Pluck

**目標**: 歯切れ良い、リズミック、明瞭

**Wavetable設定**:
```
Oscillator 1:
  - Wavetable: Saw
  - Unison: 4（Tranceより少ない）
  - Detune: 30%
  - Stereo: 60%

Oscillator 2:
  - Off

Filter:
  - Cutoff: 2000 Hz
  - Resonance: 15%
  - Envelope Amount: +50%（大きめ）

Filter Envelope:
  - Attack: 0 ms（即座）
  - Decay: 300 ms（短い）
  - Sustain: 10%（ほぼゼロ）
  - Release: 100 ms（短い）

Amp Envelope:
  - Attack: 10 ms
  - Decay: 0 ms
  - Sustain: 100%
  - Release: 300 ms（Tranceより短い）
```

**エフェクトチェイン**:
```
1. EQ Eight:
   - High Pass 300 Hz
   - Boost 2 kHz +2 dB

2. Compressor (Sidechain to Kick):
   - Ratio: 6:1
   - Threshold: -20 dB
   - Attack: 10 ms
   - Release: 150 ms

3. Send A (Reverb):
   - Hall 2.0s
   - Send Level: 15%（控えめ）

4. Utility:
   - Width: 70%
```

### 3.3 Techno Acid Lead

**目標**: アグレッシブ、フィルターモジュレーション激しい

**Operator設定（FM合成）**:
```
Algorithm: 2
Operator A (Carrier):
  - Waveform: Saw
  - Coarse: 1.00
  - Level: 0.00 dB

Operator B (Modulator):
  - Waveform: Saw
  - Coarse: 1.00
  - Fine: 0.02（わずかにDetune）
  - Level: 30-60%（モジュレーション量）

Filter:
  - Type: Low Pass 12 dB
  - Cutoff: 500-2000 Hz（LFOで変化）
  - Resonance: 70%（高め、303スタイル）

Filter LFO:
  - Rate: 1/16（速い）
  - Amount: 80%
  - Waveform: Saw Up

または:

  - Rate: 1/8 Triplet
  - Amount: 60%
```

**エフェクトチェイン**:
```
1. Saturator:
   - Drive: 6 dB
   - Curve: A-Shape

2. EQ Eight:
   - High Pass 150 Hz
   - Boost 800 Hz +2 dB（酸味）

3. Send A (Reverb):
   - Room 1.0s（短い）
   - Send Level: 10%

4. Auto Filter (追加モジュレーション):
   - LFO Rate: 1/4
   - Amount: 30%
```

### 3.4 Future Bass Vocal Lead

**目標**: 人間的、感情的、ボーカル風

**Wavetable設定**:
```
Oscillator 1:
  - Wavetable: Vocal Formants（人間の声）
  - Position: 0.30（適度なフォルマント）
  - Unison: 8
  - Detune: 35%
  - Stereo: 80%

Oscillator 2:
  - Wavetable: Saw
  - Level: -6 dB（補助）
  - Unison: 4
  - Detune: 25%

Filter:
  - Cutoff: 3000 Hz
  - Resonance: 25%
  - Envelope Amount: +35%

LFO 1 → Filter Cutoff:
  - Rate: 1/2（遅い）
  - Amount: 20%
  - Waveform: Sine

→ ゆっくりとした「wah wah」効果
```

**エフェクトチェイン**:
```
1. Vocoder（オプション、より人間的に）:
   - Carrier: Lead Synth
   - Modulator: Vocal Sample

2. EQ Eight:
   - Boost 2-4 kHz +3 dB（人間の声の周波数）

3. Compressor:
   - Ratio: 4:1
   - Threshold: -15 dB

4. Send A (Reverb):
   - Hall 2.5s
   - Send Level: 35%

5. Send B (Chorus):
   - Rate: 0.5 Hz
   - Depth: 40%
   - Send Level: 25%（温かみ）
```

---

## 4. 高度なテクニック

### 4.1 LFOモジュレーション

**Filter Cutoff LFO（Wah効果）**:
```
LFO Settings:
  - Rate: 1/4（ビートに同期）
  - Waveform: Sine（滑らか）
  - Amount: 40%

効果:
  - フィルターが開閉
  - "Wah wah wah" サウンド
  - リズミック
```

**Pitch LFO（ビブラート）**:
```
LFO Settings:
  - Rate: 5 Hz（速い）
  - Waveform: Sine
  - Amount: 5%（わずか）

効果:
  - 音程が微妙に揺れる
  - 人間的、生命感
```

**Amp LFO（トレモロ）**:
```
LFO Settings:
  - Rate: 1/8（ビートに同期）
  - Waveform: Square（オン/オフ）
  - Amount: 50%

効果:
  - 音量が周期的に変化
  - ゲート効果
```

### 4.2 Macro Knob設定

**8つのMacro Knobで即座にコントロール**:

```
Macro 1: Filter Cutoff (300 - 8000 Hz)
  → 明るさ調整

Macro 2: Resonance (0 - 50%)
  → 音色の鋭さ

Macro 3: Unison Detune (0 - 100%)
  → 厚み調整

Macro 4: Stereo Width (0 - 100%)
  → 広がり調整

Macro 5: Amp Attack (0 - 100 ms)
  → アタックの鋭さ

Macro 6: Amp Release (100 - 2000 ms)
  → 余韻の長さ

Macro 7: LFO Rate (1/16 - 1 Bar)
  → モジュレーション速度

Macro 8: Reverb Send (0 - 50%)
  → 空間の深さ
```

**使い方**:
```
1. Wavetableのパラメーターを右クリック
2. "Map to Macro 1"
3. Range設定（Min/Max）
4. Macro Knobを回すだけで調整
```

### 4.3 レイヤリング

**複数のリードを重ねる**:

**Layer 1: メインリード**
```
音域: C4 - C5
Wavetable Supersaw
Unison 8
ステレオ幅: 80%
音量: 0 dB
```

**Layer 2: サブリード（1オクターブ下）**
```
音域: C3 - C4
同じMIDI、1オクターブ下
音量: -6 dB
ステレオ幅: 60%

効果: 厚み、低域補強
```

**Layer 3: ハイリード（1オクターブ上）**
```
音域: C5 - C6
音量: -12 dB
ステレオ幅: 100%

効果: 輝き、エアリー
```

**ミキシング**:
```
EQで周波数分離:
  - Layer 1: 500 Hz - 4 kHz（メイン）
  - Layer 2: 100 - 1000 Hz（Low Cut 500 Hz）
  - Layer 3: 2 kHz以上（High Pass 2 kHz）

→ お互いに干渉しない
```

---

## 5. エフェクトチェイン

### 5.1 完全エフェクトチェイン（Trance Lead）

**順序が重要**:

```
1. EQ Eight（前処理）:
   - High Pass 200 Hz
   - Low-Mid Cut 400 Hz -2 dB
   - Presence Boost 4 kHz +3 dB
   - Air Boost 12 kHz +2 dB

2. Compressor:
   - Ratio: 3:1
   - Threshold: -12 dB
   - Attack: 10 ms
   - Release: 100 ms
   - Makeup Gain: +3 dB

3. Saturator（倍音追加）:
   - Drive: 3 dB
   - Curve: Warm
   - Dry/Wet: 30%

4. Utility（ステレオ幅）:
   - Width: 100%

5. Send A - Reverb:
   - Hall 3.0s
   - Pre-Delay: 30 ms
   - Dry/Wet: 100%
   - Send Level: 30%

6. Send B - Delay:
   - Time: 1/8 Dotted
   - Feedback: 30%
   - Dry/Wet: 100%
   - Send Level: 20%
```

### 5.2 サイドチェイン（必須）

**Kickとの共存**:
```
Lead Track:
→ Compressor (2つ目、専用)
→ Audio From: 1-Kick

設定:
  - Ratio: 4:1
  - Threshold: -20 dB
  - Attack: 10 ms
  - Release: 150 ms

効果:
  - Kickが鳴る瞬間、リードが下がる
  - グルーヴ、ダンサビリティ
  - Progressive House必須
```

---

## 6. ミキシング

### 6.1 EQ処理

**リードシンセの基本EQ**:
```
EQ Eight:

1. High Pass 200-300 Hz
   （ベース領域回避）

2. Low-Mid Cut 400-600 Hz -2 to -3 dB
   （マッディネス除去）

3. Presence Boost 2-4 kHz +2 to +4 dB
   （明瞭さ、前に出す）

4. Air Boost 10-14 kHz +1 to +2 dB
   （輝き、エアリー）
```

**他のトラックとのスペース作り**:
```
Lead: 2-4 kHz +3 dB
Pad: 2-4 kHz -3 dB

→ お互いに干渉しない
```

### 6.2 ステレオ幅

**リードの最適幅**:
```
Trance Lead: 80-100%（広い）
Pluck Lead: 60-70%（中央寄り）
Mono Lead: 0%（完全中央、ボーカル風）

Utility:
  - Width: 80%

確認:
  - Mono互換性チェック
  - Correlation Meter: +0.3以上
```

### 6.3 音量バランス

**ミックス内での適切な音量**:
```
Kick: -6 dB (Peak)
Bass: -9 dB
Pad: -12 dB
Lead: -9 to -6 dB（ジャンルによる）

Trance: -6 dB（リードが主役）
Progressive House: -9 dB（控えめ）
Techno: -12 dB（背景）
```

---

## 7. プリセット改変テクニック

### 7.1 プリセットから始める

**Wavetable Factory Presets**:
```
Browser → Sounds → Wavetable
→ "Lead" フォルダ

推奨プリセット:
  - "Classic Lead"
  - "Supersaw Lead"
  - "Pluck Lead"
  - "Acid Lead"
```

### 7.2 改変の手順

**Step 1: Unisonを調整**
```
プリセット: Unison 4
自分: Unison 8
Detune: 30% → 45%

→ より厚く、広がる
```

**Step 2: Filterを調整**
```
Cutoff: 2000 Hz → 3500 Hz（明るく）
Resonance: 10% → 25%（鋭く）
```

**Step 3: Envelopeを調整**
```
Amp Attack: 50 ms → 10 ms（速く）
Amp Release: 200 ms → 500 ms（長く）
```

**Step 4: エフェクトを追加**
```
プリセットのエフェクト → 削除
自分のエフェクトチェイン → 適用
```

**Step 5: 保存**
```
Save Preset As:
  - "Supersaw Lead - My Style"
  - Favorites に追加
```

---

## 8. 練習方法

### 初級（Week 1-2）

**Week 1: プリセット使用**
```
Day 1-2: プリセット "Classic Lead" で曲作り
Day 3-4: プリセット "Pluck Lead" で曲作り
Day 5-7: 5つのプリセットを試す
```

**Week 2: 簡単な改変**
```
Day 1-2: Unison、Detune調整
Day 3-4: Filter Cutoff調整
Day 5-7: Envelope調整
```

---

### 中級（Week 3-4）

**Week 3: ゼロからSupersaw作成**
```
Day 1-2: Oscillator設定、Unison
Day 3-4: Filter、Envelope
Day 5-7: エフェクトチェイン完成
```

**Week 4: ジャンル別リード**
```
Day 1-2: Trance Supersaw
Day 3-4: Progressive Pluck
Day 5-7: Techno Acid
```

---

### 上級（Week 5-8）

**Week 5-6: リファレンストラック分析**
```
1. プロの楽曲のリード音色を耳で分析
2. Wavetableで完全再現
3. プリセット保存
4. 自分の楽曲に使用
```

**Week 7-8: オリジナル音色開発**
```
1. 完全オリジナルリード作成
2. Macro Knob設定
3. 10パターン保存
4. フル楽曲制作
```

---

## 9. よくある失敗と対処法

### 失敗1: リードが埋もれる

**対処法**:
```
1. EQ: 2-4 kHz +3 dB
2. Compressor: Threshold -15 dB
3. ステレオ幅: 80%
4. 他の楽器: 2-4 kHz -2 dB
```

---

### 失敗2: 音が薄い

**対処法**:
```
1. Unison: 4 → 8
2. Detune: 20% → 40%
3. Oscillator 2を追加（Detune +7 cents）
4. レイヤリング（1オクターブ下も追加）
```

---

### 失敗3: 音が汚い、ざらつく

**対処法**:
```
1. Unison Detune下げる: 60% → 30%
2. Resonance下げる: 40% → 15%
3. EQ: High Pass 200 Hz（低域ノイズ除去）
4. Filter Cutoff下げる: 5000 → 3000 Hz
```

---

### 失敗4: ステレオ幅が広すぎてMono互換性NG

**対処法**:
```
1. Utility Width: 100% → 70%
2. Unison Stereo: 80% → 60%
3. Mono互換性テスト（Utilityでmono化）
4. Correlation Meter: +0.3以上確認
```

---

## まとめ

### リードシンセの核心

1. **Supersaw**: Unison 8、Detune 40%が基本
2. **Filter Envelope**: Attack 10ms、Decay 500ms
3. **エフェクトチェイン**: EQ→Comp→Reverb→Delay
4. **ステレオ幅**: 60-80%（ジャンルによる）
5. **サイドチェイン**: Kickとの共存必須

### DJから制作者へ

**DJスキル**:
- フロアで効いたリード音色を分析
- ジャンル別の音色特性を理解
- エピックな瞬間を体感

**プロデューサーとして**:
- その「魔法」を自分で作り出せる
- 音色デザインで個性を確立
- 無限のバリエーションを創造

### 次のステップ

1. **[パッド](./pads.md)**: リードを補完する背景音
2. **[ミキシング](../05-mixing/)**: リードを完璧に仕上げる
3. **[サウンドデザイン](../08-sound-design/)**: 高度な音色設計

---

**次のステップ**: [パッド](./pads.md) へ進む

---

**🎵 楽曲の主役となるリードシンセを完全マスターして、エピックなトラックを作りましょう！**

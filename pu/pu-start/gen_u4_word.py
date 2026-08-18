#!/usr/bin/env python3
"""Generate PU Start U4 Word Game HTML"""

import re

# Read U2 template to extract the logo base64
with open('/app/data/所有对话/主对话/mona-woods-games/pu/pu-start/u2-word/index.html', 'rb') as f:
    u2_content = f.read().decode('utf-8', errors='replace')

# Extract logo base64
logo_match = re.search(r'src="(data:image/png;base64,[^"]+)"', u2_content)
logo_base64 = logo_match.group(1) if logo_match else ''

print(f"Logo extracted: {len(logo_base64)} chars")

# Now build the U4 word game HTML
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Power Up Start U4 单词闯关 - Mona单词游戏</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    background: #0F2B46;
    min-height: 100vh;
    color: #0F2B46;
    display: flex;
    flex-direction: column;
  }}
  /* 顶部 */
  .header {{
    background: #0F2B46;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 2px solid rgba(45, 212, 191, 0.2);
  }}
  .logo-area {{
    width: 44px;
    height: 44px;
    border-radius: 50%;
    overflow: hidden;
    flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }}
  .logo-area img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}
  .header-title {{
    color: white;
    flex: 1;
  }}
  .header-title h1 {{
    font-size: 18px;
    font-weight: 600;
  }}
  .header-title p {{
    font-size: 12px;
    color: rgba(255,255,255,0.6);
    margin-top: 2px;
  }}
  /* 返回主页按钮 */
  .home-btn {{
    background: rgba(255,255,255,0.15);
    color: white;
    border: 1px solid rgba(255,255,255,0.2);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
    flex-shrink: 0;
    display: none;
  }}
  .home-btn:hover {{ background: rgba(255,255,255,0.25); }}
  .home-btn:active {{ transform: scale(0.95); }}

  /* 主内容 */
  .main {{
    flex: 1;
    padding: 20px 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
  }}
  /* 关卡进度 */
  .level-progress {{
    width: 100%;
    max-width: 500px;
    display: none;
    justify-content: space-between;
    margin-bottom: 20px;
    position: relative;
  }}
  .level-dot {{
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: rgba(255,255,255,0.15);
    color: rgba(255,255,255,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 13px;
    position: relative;
    z-index: 2;
    transition: all 0.3s;
  }}
  .level-dot.active {{
    background: #2DD4BF;
    color: #0F2B46;
    box-shadow: 0 0 0 4px rgba(45, 212, 191, 0.25);
  }}
  .level-dot.done {{
    background: #2DD4BF;
    color: #0F2B46;
  }}
  .level-line {{
    position: absolute;
    top: 50%;
    left: 32px;
    right: 32px;
    height: 3px;
    background: rgba(255,255,255,0.15);
    transform: translateY(-50%);
    z-index: 1;
  }}
  .level-line-fill {{
    height: 100%;
    background: #2DD4BF;
    width: 0%;
    transition: width 0.5s;
  }}
  /* 卡片 */
  .card {{
    width: 100%;
    max-width: 500px;
    background: white;
    border-radius: 20px;
    padding: 28px 24px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
  }}
  .card-title {{
    font-size: 14px;
    color: #2DD4BF;
    font-weight: 600;
    margin-bottom: 4px;
  }}
  .question-progress {{
    font-size: 13px;
    color: #999;
    margin-bottom: 16px;
  }}
  .question-word {{
    text-align: center;
    margin: 20px 0;
  }}
  .question-word .word {{
    font-size: 38px;
    font-weight: 700;
    color: #0F2B46;
    margin-bottom: 12px;
  }}
  .question-word .chinese {{
    font-size: 24px;
    color: #0F2B46;
    font-weight: 600;
    margin-bottom: 12px;
  }}
  .sound-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #E6FFFA;
    color: #0F2B46;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .sound-btn:hover {{ background: #2DD4BF; color: white; }}
  .sound-btn:active {{ transform: scale(0.95); }}

  /* 图片选项（第一关） */
  .image-options {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 20px;
  }}
  .image-option {{
    background: #F7FAFC;
    border: 2px solid #E2E8F0;
    border-radius: 14px;
    padding: 16px 8px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    color: #0F2B46;
    font-weight: 500;
  }}
  .image-option:hover {{ border-color: #2DD4BF; background: #E6FFFA; }}
  .image-option.correct {{
    background: #DEF7EC;
    border-color: #2DD4BF;
    color: #0F2B46;
  }}
  .image-option.wrong {{
    background: #FED7D7;
    border-color: #FC8181;
    color: #742A2A;
  }}
  .image-option.disabled {{ pointer-events: none; }}
  .image-option .emoji {{
    font-size: 48px;
    margin-bottom: 8px;
  }}
  .image-option .label {{
    font-size: 14px;
    color: #718096;
  }}

  /* 选项 */
  .options {{
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 20px;
  }}
  .option {{
    background: #F7FAFC;
    border: 2px solid #E2E8F0;
    border-radius: 14px;
    padding: 16px;
    font-size: 18px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    color: #0F2B46;
    font-weight: 500;
  }}
  .option:hover {{ border-color: #2DD4BF; background: #E6FFFA; }}
  .option.correct {{
    background: #DEF7EC;
    border-color: #2DD4BF;
    color: #0F2B46;
  }}
  .option.wrong {{
    background: #FED7D7;
    border-color: #FC8181;
    color: #742A2A;
  }}
  .option.disabled {{ pointer-events: none; }}
  /* 反馈区 */
  .feedback {{
    margin-top: 16px;
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    display: none;
  }}
  .feedback.show {{ display: block; }}
  .feedback.correct {{
    background: #DEF7EC;
    color: #276749;
  }}
  .feedback.wrong {{
    background: #FED7D7;
    color: #742A2A;
  }}
  .feedback .title {{
    font-weight: 600;
    font-size: 16px;
    margin-bottom: 4px;
  }}
  .feedback .detail {{
    font-size: 14px;
  }}
  /* 按钮区 */
  .btn-row {{
    display: flex;
    gap: 12px;
    margin-top: 20px;
  }}
  .btn {{
    flex: 1;
    padding: 14px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
  }}
  .btn:active {{ transform: scale(0.97); }}
  .btn-primary {{
    background: #2DD4BF;
    color: #0F2B46;
  }}
  .btn-primary:hover {{ background: #1FB8A3; }}
  .btn-secondary {{
    background: #E2E8F0;
    color: #0F2B46;
  }}
  .btn-secondary:hover {{ background: #CBD5E0; }}
  .btn:disabled {{
    opacity: 0.5;
    cursor: not-allowed;
  }}

  /* 拼写关 - 字母块区 */
  .spell-area {{
    margin: 20px 0;
  }}
  .spell-answer {{
    min-height: 60px;
    background: #F7FAFC;
    border: 2px dashed #CBD5E0;
    border-radius: 14px;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    padding: 12px;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
  }}
  .spell-answer .letter {{
    min-width: 44px;
    height: 48px;
    background: #2DD4BF;
    color: #0F2B46;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    padding: 0 10px;
    text-transform: lowercase;
  }}
  .spell-answer .letter:active {{ transform: scale(0.9); }}
  .spell-answer .placeholder {{
    color: #A0AEC0;
    font-size: 14px;
  }}
  .spell-options {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
  }}
  .spell-options .letter {{
    min-width: 52px;
    height: 52px;
    background: #E6FFFA;
    color: #0F2B46;
    border: 2px solid #2DD4BF;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    padding: 0 12px;
    text-transform: lowercase;
  }}
  .spell-options .letter:hover {{ background: #2DD4BF; }}
  .spell-options .letter:active {{ transform: scale(0.9); }}
  .spell-options .letter.used {{
    opacity: 0.3;
    pointer-events: none;
  }}
  .spell-hint {{
    text-align: center;
    color: #718096;
    font-size: 13px;
    margin-bottom: 12px;
  }}
  .spell-count {{
    display: inline-block;
    background: #FEFCBF;
    color: #975A16;
    padding: 2px 10px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 600;
  }}

  /* 连词成句 */
  .sentence-area {{
    margin: 20px 0;
  }}
  .sentence-chinese {{
    text-align: center;
    font-size: 22px;
    color: #0F2B46;
    font-weight: 600;
    margin-bottom: 8px;
  }}
  .sentence-hint {{
    text-align: center;
    color: #718096;
    font-size: 13px;
    margin-bottom: 16px;
  }}
  .sentence-slots {{
    min-height: 60px;
    background: #F7FAFC;
    border: 2px dashed #CBD5E0;
    border-radius: 14px;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    padding: 12px;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
  }}
  .sentence-slots .word {{
    min-height: 44px;
    background: #2DD4BF;
    color: #0F2B46;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    padding: 6px 14px;
  }}
  .sentence-slots .word:active {{ transform: scale(0.9); }}
  .sentence-slots .placeholder {{
    color: #A0AEC0;
    font-size: 14px;
  }}
  .sentence-words {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }}
  .sentence-words .word {{
    min-height: 48px;
    background: #E6FFFA;
    color: #0F2B46;
    border: 2px solid #2DD4BF;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    padding: 6px 16px;
  }}
  .sentence-words .word:hover {{ background: #2DD4BF; }}
  .sentence-words .word:active {{ transform: scale(0.9); }}
  .sentence-words .word.used {{
    opacity: 0.3;
    pointer-events: none;
  }}

  /* 开始页（关卡选择） */
  .start-screen {{
    text-align: center;
  }}
  .start-screen .icon-logo {{
    width: 80px;
    height: 80px;
    margin: 0 auto 15px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  }}
  .start-screen .icon-logo img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}
  .start-screen h2 {{
    font-size: 26px;
    color: #0F2B46;
    margin-bottom: 8px;
  }}
  .start-screen p {{
    color: #718096;
    margin-bottom: 8px;
    font-size: 15px;
  }}
  .start-screen .word-count {{
    display: inline-block;
    background: #E6FFFA;
    color: #0F2B46;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    margin: 12px 0 20px;
  }}
  .level-select-title {{
    font-size: 16px;
    color: #0F2B46;
    font-weight: 600;
    margin-bottom: 14px;
    text-align: left;
  }}
  .level-buttons {{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 20px;
  }}
  .level-btn {{
    padding: 14px 18px;
    border: none;
    border-radius: 14px;
    font-size: 15px;
    cursor: pointer;
    transition: all 0.2s;
    font-weight: 600;
    color: white;
    text-align: left;
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: inherit;
  }}
  .level-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.15); }}
  .level-btn:active {{ transform: scale(0.98); }}
  .level-btn .level-num {{
    width: 34px;
    height: 34px;
    background: rgba(255,255,255,0.25);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 700;
    flex-shrink: 0;
  }}
  .level-btn .level-info {{
    flex: 1;
  }}
  .level-btn .level-name {{
    font-size: 15px;
    margin-bottom: 2px;
  }}
  .level-btn .level-desc {{
    font-size: 12px;
    opacity: 0.85;
    font-weight: 400;
  }}
  .level-btn.l1 {{ background: linear-gradient(135deg, #2DD4BF 0%, #1FB8A3 100%); }}
  .level-btn.l2 {{ background: linear-gradient(135deg, #0F2B46 0%, #2D4A6B 100%); }}
  .level-btn.l3 {{ background: linear-gradient(135deg, #4299E1 0%, #2B6CB0 100%); }}
  .level-btn.l4 {{ background: linear-gradient(135deg, #9F7AEA 0%, #6B46C1 100%); }}
  .level-btn.l5 {{ background: linear-gradient(135deg, #ED8936 0%, #C05621 100%); }}

  /* 结算页 */
  .result-screen {{
    text-align: center;
  }}
  .result-screen .trophy {{
    font-size: 72px;
    margin-bottom: 12px;
  }}
  .result-screen h2 {{
    font-size: 26px;
    color: #0F2B46;
    margin-bottom: 4px;
  }}
  .result-screen .subtitle {{
    color: #2DD4BF;
    font-weight: 600;
    margin-bottom: 20px;
  }}
  .result-stats {{
    display: flex;
    justify-content: center;
    gap: 24px;
    margin-bottom: 24px;
  }}
  .result-stat {{
    text-align: center;
  }}
  .result-stat .num {{
    font-size: 28px;
    font-weight: 700;
    color: #2DD4BF;
  }}
  .result-stat .label {{
    font-size: 13px;
    color: #718096;
  }}
  .wrong-words {{
    background: #F7FAFC;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 24px;
    text-align: left;
  }}
  .wrong-words h3 {{
    font-size: 15px;
    color: #E53E3E;
    margin-bottom: 10px;
  }}
  .wrong-words ul {{
    list-style: none;
  }}
  .wrong-words li {{
    padding: 6px 0;
    font-size: 14px;
    color: #2D3748;
    border-bottom: 1px solid #E2E8F0;
    display: flex;
    justify-content: space-between;
  }}
  .wrong-words li:last-child {{ border-bottom: none; }}
  .wrong-words li .en {{ font-weight: 600; }}
  .wrong-words li .cn {{ color: #718096; }}
  .all-correct {{
    background: #DEF7EC;
    color: #276749;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 24px;
    font-weight: 600;
  }}
  /* 底部 */
  .footer {{
    text-align: center;
    padding: 16px;
    color: rgba(255,255,255,0.4);
    font-size: 12px;
  }}
  /* 关卡过渡动画 */
  .fade-in {{
    animation: fadeIn 0.4s ease;
  }}
  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  .bounce {{
    animation: bounce 0.5s ease;
  }}
  @keyframes bounce {{
    0%, 100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.1); }}
  }}
  /* 小屏适配 */
  @media (max-width: 360px) {{
    .question-word .word {{ font-size: 30px; }}
    .question-word .chinese {{ font-size: 20px; }}
    .spell-options .letter {{ min-width: 44px; height: 46px; font-size: 18px; padding: 0 8px; }}
    .spell-answer .letter {{ min-width: 38px; height: 42px; font-size: 18px; padding: 0 8px; }}
    .sentence-words .word {{ font-size: 14px; padding: 6px 12px; }}
    .sentence-slots .word {{ font-size: 14px; padding: 6px 10px; }}
    .image-option .emoji {{ font-size: 40px; }}
  }}
</style>
</head>
<body>
  <div class="header">
    <div class="logo-area"><img src="{logo_base64}" alt="Mona Woods"></div>
    <div class="header-title">
      <h1>U4 单词闯关</h1>
      <p>My home 家居房间主题</p>
    </div>
    <button class="home-btn" id="homeBtn" onclick="goHome()">🏠 主页</button>
  </div>

  <div class="main">
    <!-- 关卡进度 -->
    <div class="level-progress" id="levelProgress">
      <div class="level-dot" id="dot1">1</div>
      <div class="level-dot" id="dot2">2</div>
      <div class="level-dot" id="dot3">3</div>
      <div class="level-dot" id="dot4">4</div>
      <div class="level-dot" id="dot5">5</div>
      <div class="level-line"><div class="level-line-fill" id="levelLineFill"></div></div>
    </div>

    <div class="card">
      <!-- 开始页 -->
      <div class="start-screen fade-in" id="startScreen">
        <div class="icon-logo"><img src="{logo_base64}" alt="Mona Woods"></div>
        <h2>Power Up Start U4</h2>
        <p>🏠 家居房间 · 单词闯关</p>
        <div class="word-count">5 个单词 · 18 个句子 · 五大关卡</div>
        <div class="level-select-title">🎯 选择关卡开始</div>
        <div class="level-buttons">
          <button class="level-btn l1" onclick="startGame(1)">
            <div class="level-num">1</div>
            <div class="level-info">
              <div class="level-name">听音指认</div>
              <div class="level-desc">听发音，点击对应房间图片</div>
            </div>
          </button>
          <button class="level-btn l2" onclick="startGame(2)">
            <div class="level-num">2</div>
            <div class="level-info">
              <div class="level-name">看英文选中文</div>
              <div class="level-desc">根据英文单词选择正确的中文意思</div>
            </div>
          </button>
          <button class="level-btn l3" onclick="startGame(3)">
            <div class="level-num">3</div>
            <div class="level-info">
              <div class="level-name">看中文选英文</div>
              <div class="level-desc">根据中文意思选择正确的英文单词</div>
            </div>
          </button>
          <button class="level-btn l4" onclick="startGame(4)">
            <div class="level-num">4</div>
            <div class="level-info">
              <div class="level-name">拼单词</div>
              <div class="level-desc">看图听发音，拖动字母拼出单词</div>
            </div>
          </button>
          <button class="level-btn l5" onclick="startGame(5)">
            <div class="level-num">5</div>
            <div class="level-info">
              <div class="level-name">连词成句</div>
              <div class="level-desc">打乱的单词，排列成完整句子</div>
            </div>
          </button>
        </div>
      </div>

      <!-- 游戏区 -->
      <div id="gameArea" style="display:none;"></div>

      <!-- 结算页 -->
      <div class="result-screen fade-in" id="resultScreen" style="display:none;">
        <div class="trophy" id="resultTrophy">🏆</div>
        <h2 id="resultTitle">闯关成功！</h2>
        <div class="subtitle" id="resultSubtitle">太棒了，你完成了本关！</div>
        <div class="result-stats">
          <div class="result-stat">
            <div class="num" id="totalWords">5</div>
            <div class="label">题目总数</div>
          </div>
          <div class="result-stat">
            <div class="num" id="wrongCount">0</div>
            <div class="label">错误次数</div>
          </div>
          <div class="result-stat">
            <div class="num" id="accuracy">100%</div>
            <div class="label">正确率</div>
          </div>
        </div>
        <div id="wrongWordsList"></div>
        <div class="btn-row">
          <button class="btn btn-secondary" onclick="restartLevel()">🔄 重玩本关</button>
          <button class="btn btn-primary" id="nextLevelBtn" onclick="nextLevel()">下一关 →</button>
        </div>
        <div style="margin-top: 10px;">
          <button class="btn btn-secondary" style="background:#E6FFFA;color:#0F2B46;" onclick="goHome()">🏠 返回主页</button>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">Provided by Mona</div>

  <audio id="audioPlayer" preload="auto"></audio>

<script>
// ====== 单词数据 ======
const words = [
  {{ en: 'bathroom', cn: '浴室', emoji: '🛁', letters: ['b','a','t','h','r','o','o','m'] }},
  {{ en: 'living room', cn: '客厅', emoji: '🛋️', letters: ['l','i','v','i','n','g',' ','r','o','o','m'] }},
  {{ en: 'bedroom', cn: '卧室', emoji: '🛏️', letters: ['b','e','d','r','o','o','m'] }},
  {{ en: 'kitchen', cn: '厨房', emoji: '🍳', letters: ['k','i','t','c','h','e','n'] }},
  {{ en: 'garden', cn: '花园', emoji: '🌻', letters: ['g','a','r','d','e','n'] }}
];

// ====== 连词成句数据（18句）======
// words: 单词数组（标点作为单独元素）
// answer: 空格连接的答案（含标点前空格，用于判对）
// chinese: 中文提示
const sentenceData = [
  // ① We've got a + 房间（5句）
  {{ chinese: '我们有一间浴室。', words: ["We've", 'got', 'a', 'bathroom', '.'], answer: "We've got a bathroom ." }},
  {{ chinese: '我们有一间客厅。', words: ["We've", 'got', 'a', 'living', 'room', '.'], answer: "We've got a living room ." }},
  {{ chinese: '我们有一间卧室。', words: ["We've", 'got', 'a', 'bedroom', '.'], answer: "We've got a bedroom ." }},
  {{ chinese: '我们有一间厨房。', words: ["We've", 'got', 'a', 'kitchen', '.'], answer: "We've got a kitchen ." }},
  {{ chinese: '我们有一个花园。', words: ["We've", 'got', 'a', 'garden', '.'], answer: "We've got a garden ." }},
  // ② There is / There are + 物品 + in + 房间（8句）
  {{ chinese: '卧室里有一张床。', words: ['There', 'is', 'a', 'bed', 'in', 'the', 'bedroom', '.'], answer: 'There is a bed in the bedroom .' }},
  {{ chinese: '卧室里有一盏灯。', words: ['There', 'is', 'a', 'lamp', 'in', 'the', 'bedroom', '.'], answer: 'There is a lamp in the bedroom .' }},
  {{ chinese: '客厅里有一个钟。', words: ['There', 'is', 'a', 'clock', 'in', 'the', 'living', 'room', '.'], answer: 'There is a clock in the living room .' }},
  {{ chinese: '客厅里有一台电脑。', words: ['There', 'is', 'a', 'computer', 'in', 'the', 'living', 'room', '.'], answer: 'There is a computer in the living room .' }},
  {{ chinese: '厨房里有一个橱柜。', words: ['There', 'is', 'a', 'cupboard', 'in', 'the', 'kitchen', '.'], answer: 'There is a cupboard in the kitchen .' }},
  {{ chinese: '浴室里有一面镜子。', words: ['There', 'is', 'a', 'mirror', 'in', 'the', 'bathroom', '.'], answer: 'There is a mirror in the bathroom .' }},
  {{ chinese: '花园里有一些胡萝卜。', words: ['There', 'are', 'some', 'carrots', 'in', 'the', 'garden', '.'], answer: 'There are some carrots in the garden .' }},
  {{ chinese: '花园里有一些苹果。', words: ['There', 'are', 'some', 'apples', 'in', 'the', 'garden', '.'], answer: 'There are some apples in the garden .' }},
  // ③ 某人 + is in + 房间（5句）
  {{ chinese: '妈妈在厨房里。', words: ['Mum', 'is', 'in', 'the', 'kitchen', '.'], answer: 'Mum is in the kitchen .' }},
  {{ chinese: '爸爸在花园里。', words: ['Dad', 'is', 'in', 'the', 'garden', '.'], answer: 'Dad is in the garden .' }},
  {{ chinese: '哥哥在卧室里。', words: ['Brother', 'is', 'in', 'the', 'bedroom', '.'], answer: 'Brother is in the bedroom .' }},
  {{ chinese: '姐姐在客厅里。', words: ['Sister', 'is', 'in', 'the', 'living', 'room', '.'], answer: 'Sister is in the living room .' }},
  {{ chinese: '猫在浴室里。', words: ['The', 'cat', 'is', 'in', 'the', 'bathroom', '.'], answer: 'The cat is in the bathroom .' }}
];

// ====== 游戏状态 ======
let currentLevel = 1;
let currentQuestion = 0;
let wrongItems = [];
let shuffledQuestions = [];
let answered = false;
let spellAnswer = [];
let spellLetterStatus = [];
let sentenceAnswer = [];
let sentenceWordStatus = [];

// ====== 三级语音兜底：有道 → 百度 → Web Speech ======
let audioEl = document.getElementById('audioPlayer');
let ttsFallbackIndex = 0;

function playSound(text) {{
  // 清理文本：去掉标点前的空格，让发音更自然
  const cleanText = text.replace(/ \./g, '.').replace(/ \?/g, '?').replace(/ !/g, '!');
  ttsFallbackIndex = 0;
  tryTTS(cleanText);
}}

function tryTTS(text) {{
  if (ttsFallbackIndex === 0) {{
    // 第一级：有道 TTS
    audioEl.onerror = function() {{
      ttsFallbackIndex = 1;
      tryTTS(text);
    }};
    audioEl.src = 'https://dict.youdao.com/dictvoice?audio=' + encodeURIComponent(text) + '&type=1';
    audioEl.play().catch(function() {{
      ttsFallbackIndex = 1;
      tryTTS(text);
    }});
  }} else if (ttsFallbackIndex === 1) {{
    // 第二级：百度 TTS
    audioEl.onerror = function() {{
      ttsFallbackIndex = 2;
      tryTTS(text);
    }};
    audioEl.src = 'https://fanyi.baidu.com/gettts?lan=uk&text=' + encodeURIComponent(text) + '&spd=3&source=web';
    audioEl.play().catch(function() {{
      ttsFallbackIndex = 2;
      tryTTS(text);
    }});
  }} else {{
    // 第三级：浏览器 Web Speech
    if ('speechSynthesis' in window) {{
      try {{
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = 0.9;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(utterance);
      }} catch(e) {{}}
    }}
  }}
}}

// ====== 工具函数 ======
function shuffle(arr) {{
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }}
  return a;
}}

// ====== 开始游戏 ======
function startGame(level) {{
  currentLevel = level;
  currentQuestion = 0;
  wrongItems = [];
  answered = false;
  
  document.getElementById('startScreen').style.display = 'none';
  document.getElementById('resultScreen').style.display = 'none';
  document.getElementById('levelProgress').style.display = 'flex';
  document.getElementById('gameArea').style.display = 'block';
  document.getElementById('homeBtn').style.display = 'block';
  
  updateLevelProgress();
  loadLevel();
}}

// ====== 更新关卡进度 ======
function updateLevelProgress() {{
  for (let i = 1; i <= 5; i++) {{
    const dot = document.getElementById('dot' + i);
    dot.classList.remove('active', 'done');
    if (i < currentLevel) dot.classList.add('done');
    else if (i === currentLevel) dot.classList.add('active');
  }}
  const fill = document.getElementById('levelLineFill');
  fill.style.width = ((currentLevel - 1) / 4 * 100) + '%';
}}

// ====== 加载关卡 ======
function loadLevel() {{
  if (currentLevel <= 4) {{
    // 前4关：单词题
    shuffledQuestions = shuffle(words);
  }} else {{
    // 第5关：连词成句，18句全部打乱
    shuffledQuestions = shuffle([...sentenceData]);
  }}
  currentQuestion = 0;
  renderQuestion();
}}

// ====== 渲染题目 ======
function renderQuestion() {{
  answered = false;
  spellAnswer = [];
  sentenceAnswer = [];
  
  const total = shuffledQuestions.length;
  const gameArea = document.getElementById('gameArea');
  
  if (currentLevel === 1) {{
    renderLevel1(total);
  }} else if (currentLevel === 2) {{
    renderLevel2(total);
  }} else if (currentLevel === 3) {{
    renderLevel3(total);
  }} else if (currentLevel === 4) {{
    renderLevel4(total);
  }} else if (currentLevel === 5) {{
    renderLevel5(total);
  }}
}}

// ========== 第一关：听音指认 ==========
function renderLevel1(total) {{
  const word = shuffledQuestions[currentQuestion];
  const gameArea = document.getElementById('gameArea');
  
  // 5个图片选项，全部显示
  const allOptions = shuffle([...words]);
  
  gameArea.innerHTML = `
    <div class="fade-in">
      <div class="card-title">第一关 · 听音指认</div>
      <div class="question-progress">第 ${{currentQuestion + 1}} / ${{total}} 题</div>
      <div class="question-word">
        <button class="sound-btn" onclick="playSound('${{word.en}}')">🔊 听发音</button>
      </div>
      <div class="image-options" id="options">
        ${{allOptions.map((opt, i) => `
          <div class="image-option" onclick="checkLevel1(${{i}}, '${{opt.en}}')">
            <div class="emoji">${{opt.emoji}}</div>
            <div class="label">${{opt.cn}}</div>
          </div>
        `).join('')}}
      </div>
      <div class="feedback" id="feedback"></div>
      <div class="btn-row" id="btnRow" style="display:none;">
        <button class="btn btn-secondary" onclick="retryQuestion()">再试一次</button>
        <button class="btn btn-primary" onclick="nextQuestion()">下一题 →</button>
      </div>
    </div>
  `;
  
  // 自动播放发音
  setTimeout(() => playSound(word.en), 500);
}}

function checkLevel1(index, answer) {{
  if (answered) return;
  answered = true;
  
  const word = shuffledQuestions[currentQuestion];
  const options = document.querySelectorAll('.image-option');
  const feedback = document.getElementById('feedback');
  const btnRow = document.getElementById('btnRow');
  const isCorrect = answer === word.en;
  
  options.forEach((opt, i) => {{
    opt.classList.add('disabled');
    const label = opt.querySelector('.label').textContent;
    const optWord = words.find(w => w.cn === label);
    if (optWord && optWord.en === word.en) {{
      opt.classList.add('correct');
    }}
  }});
  
  if (isCorrect) {{
    options[index].classList.add('correct');
    feedback.className = 'feedback show correct';
    feedback.innerHTML = `<div class="title">✅ 回答正确！</div><div class="detail">${{word.en}} — ${{word.cn}}</div>`;
    btnRow.style.display = 'flex';
    btnRow.querySelector('.btn-secondary').style.display = 'none';
  }} else {{
    options[index].classList.add('wrong');
    wrongItems.push({{ type: 'word', en: word.en, cn: word.cn }});
    feedback.className = 'feedback show wrong';
    feedback.innerHTML = `<div class="title">❌ 回答错误</div><div class="detail">正确答案：${{word.en}} — ${{word.cn}}</div>`;
    btnRow.style.display = 'flex';
    btnRow.querySelector('.btn-secondary').style.display = 'block';
  }}
  
  playSound(word.en);
}}

// ========== 第二关：看英文选中文 ==========
function renderLevel2(total) {{
  const word = shuffledQuestions[currentQuestion];
  const options = generateChineseOptions(word);
  const gameArea = document.getElementById('gameArea');
  
  gameArea.innerHTML = `
    <div class="fade-in">
      <div class="card-title">第二关 · 看英文选中文</div>
      <div class="question-progress">第 ${{currentQuestion + 1}} / ${{total}} 题</div>
      <div class="question-word">
        <div class="word">${{word.en}}</div>
        <button class="sound-btn" onclick="playSound('${{word.en}}')">🔊 听发音</button>
      </div>
      <div class="options" id="options">
        ${{options.map((opt, i) => `<div class="option" onclick="checkLevel2(${{i}}, '${{opt}}')">${{opt}}</div>`).join('')}}
      </div>
      <div class="feedback" id="feedback"></div>
      <div class="btn-row" id="btnRow" style="display:none;">
        <button class="btn btn-secondary" onclick="retryQuestion()">再试一次</button>
        <button class="btn btn-primary" onclick="nextQuestion()">下一题 →</button>
      </div>
    </div>
  `;
}}

function generateChineseOptions(correctWord) {{
  const wrongs = shuffle(words.filter(w => w.cn !== correctWord.cn)).slice(0, 3).map(w => w.cn);
  return shuffle([correctWord.cn, ...wrongs]);
}}

function checkLevel2(index, answer) {{
  if (answered) return;
  answered = true;
  
  const word = shuffledQuestions[currentQuestion];
  const options = document.querySelectorAll('.option');
  const feedback = document.getElementById('feedback');
  const btnRow = document.getElementById('btnRow');
  const isCorrect = answer === word.cn;
  
  options.forEach((opt, i) => {{
    opt.classList.add('disabled');
    if (opt.textContent.trim() === word.cn) {{
      opt.classList.add('correct');
    }}
  }});
  
  if (isCorrect) {{
    options[index].classList.add('correct');
    feedback.className = 'feedback show correct';
    feedback.innerHTML = `<div class="title">✅ 回答正确！</div><div class="detail">${{word.en}} — ${{word.cn}}</div>`;
    btnRow.style.display = 'flex';
    btnRow.querySelector('.btn-secondary').style.display = 'none';
  }} else {{
    options[index].classList.add('wrong');
    wrongItems.push({{ type: 'word', en: word.en, cn: word.cn }});
    feedback.className = 'feedback show wrong';
    feedback.innerHTML = `<div class="title">❌ 回答错误</div><div class="detail">正确答案：${{word.cn}}（${{word.en}} — ${{word.cn}}）</div>`;
    btnRow.style.display = 'flex';
    btnRow.querySelector('.btn-secondary').style.display = 'block';
  }}
  
  playSound(word.en);
}}

// ========== 第三关：看中文选英文 ==========
function renderLevel3(total) {{
  const word = shuffledQuestions[currentQuestion];
  const options = generateEnglishOptions(word);
  const gameArea = document.getElementById('gameArea');
  
  gameArea.innerHTML = `
    <div class="fade-in">
      <div class="card-title">第三关 · 看中文选英文</div>
      <div class="question-progress">第 ${{currentQuestion + 1}} / ${{total}} 题</div>
      <div class="question-word">
        <div class="chinese">${{word.cn}}</div>
      </div>
      <div class="options" id="options">
        ${{options.map((opt, i) => `
          <div class="option" onclick="checkLevel3(${{i}}, '${{opt.replace(/'/g, "\\\\'")}}')">
            ${{opt}}
            <span style="float:right;cursor:pointer;" onclick="event.stopPropagation();playSound('${{opt.replace(/'/g, "\\\\'")}}')">🔊</span>
          </div>
        `).join('')}}
      </div>
      <div class="feedback" id="feedback"></div>
      <div class="btn-row" id="btnRow" style="display:none;">
        <button class="btn btn-secondary" onclick="retryQuestion()">再试一次</button>
        <button class="btn btn-primary" onclick="nextQuestion()">下一题 →</button>
      </div>
    </div>
  `;
}}

function generateEnglishOptions(correctWord) {{
  const wrongs = shuffle(words.filter(w => w.en !== correctWord.en)).slice(0, 3).map(w => w.en);
  return shuffle([correctWord.en, ...wrongs]);
}}

function checkLevel3(index, answer) {{
  if (answered) return;
  answered = true;
  
  const word = shuffledQuestions[currentQuestion];
  const options = document.querySelectorAll('.option');
  const feedback = document.getElementById('feedback');
  const btnRow = document.getElementById('btnRow');
  const isCorrect = answer === word.en;
  
  options.forEach((opt, i) => {{
    opt.classList.add('disabled');
    const optText = opt.textContent.replace('🔊', '').trim();
    if (optText === word.en) {{
      opt.classList.add('correct');
    }}
  }});
  
  if (isCorrect) {{
    options[index].classList.add('correct');
    feedback.className = 'feedback show correct';
    feedback.innerHTML = `<div class="title">✅ 回答正确！</div><div class="detail">${{word.en}} — ${{word.cn}}</div>`;
    btnRow.style.display = 'flex';
    btnRow.querySelector('.btn-secondary').style.display = 'none';
  }} else {{
    options[index].classList.add('wrong');
    wrongItems.push({{ type: 'word', en: word.en, cn: word.cn }});
    feedback.className = 'feedback show wrong';
    feedback.innerHTML = `<div class="title">❌ 回答错误</div><div class="detail">正确答案：${{word.en}}（${{word.cn}}）</div>`;
    btnRow.style.display = 'flex';
    btnRow.querySelector('.btn-secondary').style.display = 'block';
  }}
  
  playSound(word.en);
}}

// ========== 第四关：拼单词 ==========
function renderLevel4(total) {{
  const word = shuffledQuestions[currentQuestion];
  const correctLetters = word.letters;
  
  // 打乱字母顺序
  let shuffled = shuffle([...correctLetters]);
  // 确保打乱后与原顺序不同
  if (shuffled.join('') === correctLetters.join('') && correctLetters.length > 1) {{
    shuffled = shuffle([...correctLetters]);
  }}
  
  spellAnswer = [];
  spellLetterStatus = shuffled.map(() => false);
  
  const gameArea = document.getElementById('gameArea');
  gameArea.innerHTML = `
    <div class="fade-in">
      <div class="card-title">第四关 · 拼单词</div>
      <div class="question-progress">第 ${{currentQuestion + 1}} / ${{total}} 题</div>
      <div class="question-word">
        <div style="font-size: 64px; margin-bottom: 12px;">${{word.emoji}}</div>
        <div class="chinese">${{word.cn}}</div>
        <button class="sound-btn" onclick="playSound('${{word.en}}')">🔊 听发音</button>
      </div>
      <div class="spell-hint">
        这个单词有 <span class="spell-count">${{correctLetters.filter(l => l !== ' ').length}} 个字母</span>，点击字母拼出单词
      </div>
      <div class="spell-area">
        <div class="spell-answer" id="spellAnswer">
          <span class="placeholder">点击字母拼出单词</span>
        </div>
        <div class="spell-options" id="spellOptions">
          ${{shuffled.map((s, i) => `<div class="letter" data-index="${{i}}" onclick="selectLetter(${{i}}, '${{s}}')">${{s === ' ' ? '⎵' : s}}</div>`).join('')}}
        </div>
      </div>
      <div class="feedback" id="feedback"></div>
      <div class="btn-row" id="btnRow">
        <button class="btn btn-secondary" onclick="clearSpell()">清空</button>
        <button class="btn btn-primary" onclick="checkSpell()">确认提交</button>
      </div>
    </div>
  `;
}}

function selectLetter(index, letter) {{
  if (spellLetterStatus[index]) return;
  spellLetterStatus[index] = true;
  spellAnswer.push({{ index, letter }});
  
  const answerEl = document.getElementById('spellAnswer');
  const placeholder = answerEl.querySelector('.placeholder');
  if (placeholder) placeholder.remove();
  
  const letterEl = document.createElement('div');
  letterEl.className = 'letter';
  letterEl.textContent = letter === ' ' ? '⎵' : letter;
  letterEl.onclick = () => removeLetter(spellAnswer.length - 1);
  answerEl.appendChild(letterEl);
  
  document.querySelectorAll('.spell-options .letter')[index].classList.add('used');
}}

function removeLetter(pos) {{
  const removed = spellAnswer.splice(pos, 1)[0];
  spellLetterStatus[removed.index] = false;
  document.querySelectorAll('.spell-options .letter')[removed.index].classList.remove('used');
  
  // 重新渲染答案区
  const answerEl = document.getElementById('spellAnswer');
  answerEl.innerHTML = '';
  if (spellAnswer.length === 0) {{
    answerEl.innerHTML = '<span class="placeholder">点击字母拼出单词</span>';
  }} else {{
    spellAnswer.forEach((item, i) => {{
      const letterEl = document.createElement('div');
      letterEl.className = 'letter';
      letterEl.textContent = item.letter === ' ' ? '⎵' : item.letter;
      letterEl.onclick = () => removeLetter(i);
      answerEl.appendChild(letterEl);
    }});
  }}
}}

function clearSpell() {{
  while (spellAnswer.length > 0) {{
    removeLetter(0);
  }}
}}

function checkSpell() {{
  const word = shuffledQuestions[currentQuestion];
  const answer = spellAnswer.map(a => a.letter).join('');
  const feedback = document.getElementById('feedback');
  const btnRow = document.getElementById('btnRow');
  
  if (answer.length === 0) return;
  
  if (answer === word.en) {{
    feedback.className = 'feedback show correct';
    feedback.innerHTML = `<div class="title">✅ 拼写正确！</div><div class="detail">${{word.en}} — ${{word.cn}}</div>`;
    // 禁用字母块
    document.querySelectorAll('.spell-options .letter').forEach(s => s.style.pointerEvents = 'none');
    // 禁用答案区点击
    document.querySelectorAll('.spell-answer .letter').forEach(s => s.style.pointerEvents = 'none');
    btnRow.innerHTML = `
      <button class="btn btn-secondary" style="display:none;">再试一次</button>
      <button class="btn btn-primary" onclick="nextQuestion()">下一题 →</button>
    `;
    playSound(word.en);
  }} else {{
    wrongItems.push({{ type: 'word', en: word.en, cn: word.cn }});
    feedback.className = 'feedback show wrong';
    feedback.innerHTML = `<div class="title">❌ 拼写错误</div><div class="detail">正确答案：${{word.en}}（${{word.cn}}）</div>`;
    btnRow.innerHTML = `
      <button class="btn btn-secondary" onclick="retryQuestion()">再试一次</button>
      <button class="btn btn-primary" onclick="nextQuestion()">下一题 →</button>
    `;
    playSound(word.en);
  }}
}}

// ========== 第五关：连词成句 ==========
function renderLevel5(total) {{
  const item = shuffledQuestions[currentQuestion];
  const allWords = shuffle([...item.words]);
  
  sentenceAnswer = [];
  sentenceWordStatus = allWords.map(() => false);
  
  const gameArea = document.getElementById('gameArea');
  gameArea.innerHTML = `
    <div class="fade-in">
      <div class="card-title">第五关 · 连词成句</div>
      <div class="question-progress">第 ${{currentQuestion + 1}} / ${{total}} 题</div>
      <div class="sentence-area">
        <div class="sentence-chinese">${{item.chinese}}</div>
        <div class="sentence-hint">点击下方单词，排列成正确的句子 👇</div>
        <div class="sentence-slots" id="sentenceSlots">
          <span class="placeholder">点击单词开始组句</span>
        </div>
        <div class="sentence-words" id="sentenceWords">
          ${{allWords.map((w, i) => `<div class="word" data-index="${{i}}" onclick="selectSentenceWord(${{i}}, '${{w.replace(/'/g, "\\\\'")}}')">${{w}}</div>`).join('')}}
        </div>
      </div>
      <div class="feedback" id="feedback"></div>
      <div class="btn-row" id="btnRow">
        <button class="btn btn-secondary" onclick="clearSentence()">重排🔄</button>
        <button class="btn btn-primary" onclick="checkSentence()">确认提交</button>
      </div>
    </div>
  `;
  
  // 保存当前题目打乱后的单词和答案
  sentenceAnswer = [];
  sentenceWordStatus = allWords.map(() => false);
  window._currentSentenceWords = allWords;
  window._currentSentenceAnswer = item.answer;
  window._currentSentenceChinese = item.chinese;
}}

function selectSentenceWord(index, word) {{
  if (sentenceWordStatus[index]) return;
  sentenceWordStatus[index] = true;
  sentenceAnswer.push({{ index, word }});
  
  const slotsEl = document.getElementById('sentenceSlots');
  const placeholder = slotsEl.querySelector('.placeholder');
  if (placeholder) placeholder.remove();
  
  const wordEl = document.createElement('div');
  wordEl.className = 'word';
  wordEl.textContent = word;
  wordEl.onclick = () => removeSentenceWord(sentenceAnswer.length - 1);
  slotsEl.appendChild(wordEl);
  
  document.querySelectorAll('.sentence-words .word')[index].classList.add('used');
}}

function removeSentenceWord(pos) {{
  const removed = sentenceAnswer.splice(pos, 1)[0];
  sentenceWordStatus[removed.index] = false;
  document.querySelectorAll('.sentence-words .word')[removed.index].classList.remove('used');
  
  // 重新渲染答案区
  const slotsEl = document.getElementById('sentenceSlots');
  slotsEl.innerHTML = '';
  if (sentenceAnswer.length === 0) {{
    slotsEl.innerHTML = '<span class="placeholder">点击单词开始组句</span>';
  }} else {{
    sentenceAnswer.forEach((item, i) => {{
      const wordEl = document.createElement('div');
      wordEl.className = 'word';
      wordEl.textContent = item.word;
      wordEl.onclick = () => removeSentenceWord(i);
      slotsEl.appendChild(wordEl);
    }});
  }}
}}

function clearSentence() {{
  while (sentenceAnswer.length > 0) {{
    removeSentenceWord(0);
  }}
}}

function checkSentence() {{
  const answer = sentenceAnswer.map(a => a.word).join(' ');
  const correctAnswer = window._currentSentenceAnswer;
  const chinese = window._currentSentenceChinese;
  const feedback = document.getElementById('feedback');
  const btnRow = document.getElementById('btnRow');
  
  if (answer.length === 0) return;
  
  // 播放句子发音（去掉标点前空格）
  const spoken = correctAnswer.replace(/ \./g, '.').replace(/ \?/g, '?');
  
  if (answer === correctAnswer) {{
    feedback.className = 'feedback show correct';
    feedback.innerHTML = `<div class="title">✅ 句子正确！</div><div class="detail">${{spoken}}</div>`;
    // 禁用单词
    document.querySelectorAll('.sentence-words .word').forEach(w => w.style.pointerEvents = 'none');
    document.querySelectorAll('.sentence-slots .word').forEach(w => w.style.pointerEvents = 'none');
    btnRow.innerHTML = `
      <button class="btn btn-secondary" style="display:none;">再试一次</button>
      <button class="btn btn-primary" onclick="nextQuestion()">下一题 →</button>
    `;
    playSound(spoken);
  }} else {{
    wrongItems.push({{ type: 'sentence', answer: correctAnswer, chinese: chinese }});
    feedback.className = 'feedback show wrong';
    feedback.innerHTML = `<div class="title">❌ 顺序不对哦</div><div class="detail">正确答案：${{spoken}}</div>`;
    btnRow.innerHTML = `
      <button class="btn btn-secondary" onclick="retryQuestion()">再试一次</button>
      <button class="btn btn-primary" onclick="nextQuestion()">下一题 →</button>
    `;
    playSound(spoken);
  }}
}}

// ====== 通用：重试当前题 ======
function retryQuestion() {{
  answered = false;
  spellAnswer = [];
  sentenceAnswer = [];
  renderQuestion();
}}

// ====== 下一题 ======
function nextQuestion() {{
  currentQuestion++;
  if (currentQuestion >= shuffledQuestions.length) {{
    showResult();
  }} else {{
    renderQuestion();
  }}
}}

// ====== 结算页 ======
function showResult() {{
  document.getElementById('gameArea').style.display = 'none';
  document.getElementById('resultScreen').style.display = 'block';
  
  const total = shuffledQuestions.length;
  const wrongCount = wrongItems.length;
  document.getElementById('totalWords').textContent = total;
  document.getElementById('wrongCount').textContent = wrongCount;
  
  // 正确率
  const accuracy = Math.round((total - wrongCount) / total * 100);
  document.getElementById('accuracy').textContent = Math.max(0, accuracy) + '%';
  
  // 标题
  const levelNames = ['', '第一关', '第二关', '第三关', '第四关', '第五关'];
  document.getElementById('resultTitle').textContent = levelNames[currentLevel] + '完成！';
  document.getElementById('resultSubtitle').textContent = wrongCount === 0 ? '🎉 全部正确！太棒了！' : '继续加油，你一定可以的！';
  document.getElementById('resultTrophy').textContent = wrongCount === 0 ? '🏆' : '💪';
  
  // 错题列表
  const wrongListEl = document.getElementById('wrongWordsList');
  if (wrongItems.length > 0) {{
    // 去重
    const uniqueWrong = [];
    const seen = new Set();
    wrongItems.forEach(item => {{
      const key = item.type + '|' + (item.en || item.answer);
      if (!seen.has(key)) {{
        seen.add(key);
        uniqueWrong.push(item);
      }}
    }});
    
    wrongListEl.innerHTML = `
      <div class="wrong-words">
        <h3>📝 需要复习（${{uniqueWrong.length}}个）</h3>
        <ul>
          ${{uniqueWrong.map(item => {{
            if (item.type === 'word') {{
              return `<li><span class="en">${{item.en}}</span><span class="cn">${{item.cn}}</span></li>`;
            }} else {{
              const cleanAns = item.answer.replace(/ \./g, '.').replace(/ \?/g, '?');
              return `<li><span class="en">${{cleanAns}}</span><span class="cn">${{item.chinese}}</span></li>`;
            }}
          }}).join('')}}
        </ul>
      </div>
    `;
  }} else {{
    wrongListEl.innerHTML = `<div class="all-correct">🎉 全部正确！你真是单词小达人！</div>`;
  }}
  
  // 下一关按钮
  const nextBtn = document.getElementById('nextLevelBtn');
  if (currentLevel < 5) {{
    nextBtn.style.display = 'block';
  }} else {{
    nextBtn.style.display = 'none';
  }}
}}

// ====== 返回主页 ======
function goHome() {{
  document.getElementById('gameArea').style.display = 'none';
  document.getElementById('resultScreen').style.display = 'none';
  document.getElementById('levelProgress').style.display = 'none';
  document.getElementById('homeBtn').style.display = 'none';
  document.getElementById('startScreen').style.display = 'block';
}}

// ====== 重玩本关 ======
function restartLevel() {{
  startGame(currentLevel);
}}

// ====== 下一关 ======
function nextLevel() {{
  if (currentLevel < 5) {{
    startGame(currentLevel + 1);
  }}
}}
</script>
</body>
</html>
'''

# Write output
output_path = '/app/data/所有对话/主对话/mona-woods-games/pu/pu-start/u4-word/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"File written: {output_path}")
print(f"File size: {len(html)} chars")

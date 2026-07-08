
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 新的题库
new_bank = """// 三关题库（每关20+题，随机抽取）
const questionBank = [
  // ========== 第一关：点餐对话 ==========
  {
    title: '第一关：点餐对对碰',
    type: 'choice',
    bank: [
      { scene: '🍞 情景：服务员问你要不要面包', text: '______ some bread?  — Yes, please.', options: ['Do you like', 'Would you like', 'Can I have'], answer: 1, explain: '提供食物给别人用 Would you like...?' },
      { scene: '🧃 情景：你想喝果汁', text: '______ some juice, please?  — Sure. Here you are.', options: ['Can I have', 'Do you like', 'Would you like'], answer: 0, explain: '自己想要某物用 Can I have...?' },
      { scene: '🍎 情景：问朋友喜不喜欢苹果', text: '______ apples?  — Yes, I do.', options: ['Would you like', 'Can I have', 'Do you like'], answer: 2, explain: '问喜好（喜欢什么）用 Do you like...?' },
      { scene: '🍰 情景：你去同学家做客，阿姨给你蛋糕', text: '______ some cake?  — No, thanks. I\\'m full.', options: ['Do you like', 'Would you like', 'Can I have'], answer: 1, explain: '主人给客人提供食物用 Would you like...?' },
      { scene: '🍗 情景：你在餐厅想点鸡肉', text: '______ some chicken, please?  — Sure.', options: ['Can I have', 'Do you like', 'Would you like'], answer: 0, explain: '点餐时自己要食物用 Can I have...?' },
      { scene: '🍌 情景：问同学喜不喜欢香蕉', text: '______ bananas?  — No, I don\\'t.', options: ['Would you like', 'Do you like', 'Can I have'], answer: 1, explain: '问喜好（喜欢不喜欢）用 Do you like...?' },
      { scene: '🥗 情景：你饿了，朋友问你吃不吃沙拉', text: '______ some salad?  — Yes, please. I\\'m hungry.', options: ['Can I have', 'Do you like', 'Would you like'], answer: 2, explain: '提供食物用 Would you like，回答是 Yes, please.' },
      { scene: '🍫 情景：你想吃巧克力', text: '______ some chocolate, please?  — Sorry, no.', options: ['Do you like', 'Would you like', 'Can I have'], answer: 2, explain: '请求要某物用 Can I have，否定回答是 Sorry, no.' },
      { scene: '🌭 情景：妈妈端来香肠，问你吃不吃', text: '______ some sausages?  — Yes, please.', options: ['Would you like', 'Do you like', 'Can I have'], answer: 0, explain: '提供食物用 Would you like...?' },
      { scene: '🍦 情景：你在冰淇淋店想要冰淇淋', text: '______ an ice cream, please?  — Here you are.', options: ['Do you like', 'Can I have', 'Would you like'], answer: 1, explain: '自己要某物用 Can I have...?' },
      { scene: '🥩 情景：问弟弟喜不喜欢肉丸', text: '______ meatballs?  — No, he doesn\\'t.', options: ['Does he like', 'Would he like', 'Can he have'], answer: 0, explain: '问第三人称喜好用 Does + 主语 + like...?' },
      { scene: '🫘 情景：招待客人，递上豆子', text: '______ some beans?  — No, thanks.', options: ['Do you like', 'Can I have', 'Would you like'], answer: 2, explain: '主人提供食物给客人用 Would you like...?' },
      { scene: '🍊 情景：你想再要些橙子', text: '______ some more oranges, please?  — Sure.', options: ['Can I have', 'Do you like', 'Would you like'], answer: 0, explain: '请求再要一些用 Can I have...?' },
      { scene: '🥛 情景：问同桌喜不喜欢牛奶', text: '______ milk?  — Yes, I do.', options: ['Would you like', 'Do you like', 'Can I have'], answer: 1, explain: '问喜好（喜不喜欢）用 Do you like...?' },
      { scene: '🍩 情景：店员问你要不要甜甜圈', text: '______ a donut?  — Yes, please.', options: ['Can I have', 'Do you like', 'Would you like'], answer: 2, explain: '店员提供食物用 Would you like...?' },
      { scene: '🥩 情景：你饿了，想向妈妈要些肉', text: '______ some meat, please?  — OK.', options: ['Do you like', 'Can I have', 'Would you like'], answer: 1, explain: '自己想要食物用 Can I have...?' },
      { scene: '🍇 情景：问好朋友喜不喜欢葡萄', text: '______ grapes?  — Yes, they are sweet.', options: ['Do you like', 'Would you like', 'Can I have'], answer: 0, explain: '问喜好（喜欢什么）用 Do you like...?' },
      { scene: '🧃 情景：看电影时朋友给你柠檬水', text: '______ some lemonade?  — No, thanks.', options: ['Can you have', 'Would you like', 'Do you like'], answer: 1, explain: '朋友给你提供饮料用 Would you like...?' },
      { scene: '🍔 情景：你在快餐店想点汉堡', text: '______ a burger, please?  — Here you are.', options: ['Do you like', 'Would you like', 'Can I have'], answer: 2, explain: '点餐时自己要食物用 Can I have...?' },
      { scene: '🌭 情景：问妹妹喜不喜欢香肠', text: '______ sausages?  — No, she doesn\\'t.', options: ['Does she like', 'Would she like', 'Can she have'], answer: 0, explain: '问第三人称（女生）喜好：Does she like...?' },
      { scene: '🍎 情景：生日派对上，有人问你吃不吃水果', text: '______ some fruit?  — Yes, please!', options: ['Would you like', 'Do you like', 'Can you have'], answer: 0, explain: '提供食物用 Would you like...?' },
      { scene: '🫘 情景：早餐你想要些豆子', text: '______ some beans, please?  — Sure.', options: ['Can I have', 'Do you like', 'Would you like'], answer: 0, explain: '自己要食物用 Can I have...?' }
    ]
  },
  // ========== 第二关：喜好调查（选择） ==========
  {
    title: '第二关：喜好大调查',
    type: 'choice',
    bank: [
      { scene: '📝 选择正确的形式', text: 'I ______ apples.', options: ['like', 'likes', 'am like'], answer: 0, explain: 'I 后面用原形 like' },
      { scene: '📝 选择正确的形式', text: 'She ______ chocolate.', options: ['like', 'likes', 'liking'], answer: 1, explain: 'she 是第三人称单数，like 要加 s' },
      { scene: '📝 选择正确的形式', text: 'He ______ bananas. (否定)', options: ['don\\'t like', 'doesn\\'t like', 'not like'], answer: 1, explain: 'he 三单否定用 doesn\\'t like，like 用原形' },
      { scene: '📝 选择正确的形式', text: 'We ______ grapes. (否定)', options: ['doesn\\'t like', 'don\\'t like', 'not like'], answer: 1, explain: 'we 是复数，否定用 don\\'t like' },
      { scene: '📝 选择正确的形式', text: 'Tom ______ meatballs.', options: ['like', 'likes', 'is like'], answer: 1, explain: 'Tom 是一个人，第三人称单数，用 likes' },
      { scene: '📝 选择正确的形式', text: 'They ______ bread.', options: ['like', 'likes', 'are like'], answer: 0, explain: 'they 是复数，用原形 like' },
      { scene: '📝 选择正确的形式', text: 'My sister ______ salad. (否定)', options: ['don\\'t like', 'doesn\\'t like', 'not like'], answer: 1, explain: 'my sister 是第三人称单数，否定用 doesn\\'t like' },
      { scene: '📝 选择正确的形式', text: 'The cat ______ fish.', options: ['like', 'likes', 'is like'], answer: 1, explain: 'the cat 是 it，三单，like 加 s' },
      { scene: '📝 选择正确的形式', text: 'You ______ milk.', options: ['like', 'likes', 'are like'], answer: 0, explain: 'you 后面用原形 like' },
      { scene: '📝 选择正确的形式', text: 'It ______ meat.', options: ['like', 'likes', 'is like'], answer: 1, explain: 'it 是第三人称单数，like 加 s' },
      { scene: '📝 选择正确的形式', text: 'My dad ______ juice.', options: ['like', 'likes', 'is like'], answer: 1, explain: 'my dad 是第三人称单数（he），用 likes' },
      { scene: '📝 选择正确的形式', text: 'Lily and Lucy ______ ice cream.', options: ['like', 'likes', 'are like'], answer: 0, explain: 'Lily and Lucy 是两个人，复数，用 like' },
      { scene: '📝 选择正确的形式', text: 'The dog ______ salad. (否定)', options: ['doesn\\'t like', 'don\\'t like', 'not like'], answer: 0, explain: 'the dog 是 it，三单否定用 doesn\\'t like' },
      { scene: '📝 选择正确的形式', text: 'I ______ oranges. They are sour. (否定)', options: ['don\\'t like', 'doesn\\'t like', 'am not like'], answer: 0, explain: 'I 后面否定用 don\\'t like' },
      { scene: '📝 选择正确的形式', text: 'My brother ______ chicken.', options: ['like', 'likes', 'is like'], answer: 1, explain: 'my brother 是第三人称单数（he），用 likes' },
      { scene: '📝 选择正确的形式', text: 'The students ______ burgers.', options: ['like', 'likes', 'are like'], answer: 0, explain: 'the students 是复数，用原形 like' },
      { scene: '📝 选择正确的形式', text: 'She ______ fish. She thinks it\\'s smelly. (否定)', options: ['don\\'t like', 'doesn\\'t like', 'not like'], answer: 1, explain: 'she 三单否定用 doesn\\'t like' },
      { scene: '📝 选择正确的形式', text: 'We ______ cake very much.', options: ['like', 'likes', 'are like'], answer: 0, explain: 'we 是复数，用原形 like' },
      { scene: '📝 选择正确的形式', text: 'He ______ eggs for breakfast.', options: ['like', 'likes', 'is like'], answer: 1, explain: 'he 是第三人称单数，like 加 s' },
      { scene: '📝 选择正确的形式', text: 'The bird ______ fruit. (否定)', options: ['don\\'t like', 'doesn\\'t like', 'not like'], answer: 1, explain: 'the bird 是 it，三单否定用 doesn\\'t like' },
      { scene: '📝 选择正确的形式', text: 'My grandma ______ milk.', options: ['like', 'likes', 'is like'], answer: 1, explain: 'my grandma 是第三人称单数（she），用 likes' },
      { scene: '📝 选择正确的形式', text: 'You ______ sausages. (否定)', options: ['don\\'t like', 'doesn\\'t like', 'not like'], answer: 0, explain: 'you 后面否定用 don\\'t like' }
    ]
  },
  // ========== 第三关：综合挑战 ==========
  {
    title: '第三关：综合大挑战',
    type: 'choice',
    bank: [
      { scene: '❓ 问句：Do you like apples?', text: '选择正确的回答：', options: ['Yes, please.', 'Yes, I do.', 'Sure.'], answer: 1, explain: 'Do you like 问喜好，回答用 Yes, I do. / No, I don\\'t.' },
      { scene: '❓ 问句：Would you like some cake?', text: '选择正确的回答：', options: ['Yes, I do.', 'Yes, please.', 'Yes, I can.'], answer: 1, explain: 'Would you like 提供食物，回答用 Yes, please. / No, thanks.' },
      { scene: '❓ 问句：Can I have some juice?', text: '选择正确的回答：', options: ['Yes, I do.', 'No, thanks.', 'Sure. Here you are.'], answer: 2, explain: 'Can I have 请求食物，回答用 Sure. / Here you are.' },
      { scene: '❓ 问句：Does she like chocolate?', text: '选择正确的回答：', options: ['No, she doesn\\'t.', 'No, thanks.', 'No, she don\\'t.'], answer: 0, explain: 'Does she 问三单喜好，否定回答 No, she doesn\\'t.' },
      { scene: '🍔 情景：你是服务员，给客人提供汉堡', text: '你应该说：', options: ['Do you like burgers?', 'Would you like a burger?', 'Can I have a burger?'], answer: 1, explain: '服务员提供食物用 Would you like...?' },
      { scene: '🍗 情景：你去朋友家，想吃鸡肉', text: '你应该说：', options: ['Do you like chicken?', 'Would you like some chicken?', 'Can I have some chicken?'], answer: 2, explain: '自己想吃，请求食物用 Can I have...?' },
      { scene: '👧 句子：She ______ ice cream.', text: '选择正确的词：', options: ['like', 'likes', 'don\\'t like'], answer: 1, explain: 'she 是第三人称单数，用 likes' },
      { scene: '🍌 情景：问同学喜不喜欢香蕉', text: '你应该说：', options: ['Do you like bananas?', 'Would you like bananas?', 'Can I have bananas?'], answer: 0, explain: '问喜好（喜欢不喜欢）用 Do you like...?' },
      { scene: '❓ 问句：Do they like bread?', text: '选择正确的回答：', options: ['Yes, they do.', 'Yes, please.', 'Sure.'], answer: 0, explain: 'Do they 问复数喜好，回答用 Yes, they do. / No, they don\\'t.' },
      { scene: '🍰 情景：店员给你提供蛋糕', text: '店员说：______  你回答：Yes, please.', options: ['Do you like cake?', 'Would you like some cake?', 'Can I have some cake?'], answer: 1, explain: '店员提供食物用 Would you like...?，回答是 Yes, please.' },
      { scene: '👦 句子：My brother ______ meatballs.', text: '选择正确的词：', options: ['don\\'t like', 'doesn\\'t like', 'not like'], answer: 1, explain: 'my brother 是三单（he），否定用 doesn\\'t like' },
      { scene: '🍊 情景：你在超市，想要些橙子', text: '你对店员说：', options: ['Do you like oranges?', 'Can I have some oranges?', 'Would you like oranges?'], answer: 1, explain: '自己要某物用 Can I have...?' },
      { scene: '❓ 问句：Would you like some milk?', text: '选择否定回答：', options: ['No, I don\\'t.', 'No, thanks.', 'No, I can\\'t.'], answer: 1, explain: 'Would you like 的否定回答是 No, thanks.' },
      { scene: '🐶 句子：The dog ______ meat.', text: '选择正确的词：', options: ['like', 'likes', 'don\\'t like'], answer: 1, explain: 'the dog 是 it，三单，用 likes' },
      { scene: '🥛 情景：早上妈妈问你喝不喝牛奶', text: '妈妈说：______', options: ['Do you like milk?', 'Would you like some milk?', 'Can I have some milk?'], answer: 1, explain: '提供给对方食物/饮料用 Would you like...?' },
      { scene: '❓ 问句：Can I have some bread?', text: '选择否定回答：', options: ['No, I don\\'t.', 'No, thanks.', 'Sorry, no.'], answer: 2, explain: 'Can I have 请求的否定回答是 Sorry, no.' },
      { scene: '👨‍👩‍👧 句子：My family ______ salad.', text: '选择正确的词：', options: ['like', 'likes', 'doesn\\'t like'], answer: 0, explain: 'my family 表示家人（复数含义），用 like' },
      { scene: '🍰 情景：你去餐厅，想点一块蛋糕', text: '你说：______', options: ['Can I have a piece of cake?', 'Do you like cake?', 'Would you like a piece of cake?'], answer: 0, explain: '点餐自己要食物用 Can I have...?' },
      { scene: '❓ 问句：Does he like chicken?', text: '选择肯定回答：', options: ['Yes, he is.', 'Yes, he does.', 'Yes, please.'], answer: 1, explain: 'Does he 问三单喜好，肯定回答 Yes, he does.' },
      { scene: '🍇 情景：问朋友喜不喜欢葡萄', text: '你说：______', options: ['Can I have grapes?', 'Would you like grapes?', 'Do you like grapes?'], answer: 2, explain: '问喜好（喜欢不喜欢）用 Do you like...?' },
      { scene: '👧 句子：Lily ______ sausages. They are tasty.', text: '选择正确的词：', options: ['like', 'likes', 'don\\'t like'], answer: 1, explain: 'Lily 是一个人，三单，用 likes' },
      { scene: '🍎 情景：朋友来家里，你拿水果招待', text: '你说：______', options: ['Do you like fruit?', 'Would you like some fruit?', 'Can I have some fruit?'], answer: 1, explain: '主人招待客人用 Would you like...?' }
    ]
  }
];"""

# 匹配从 "// 三关题库" 到 "];\n\nlet currentLevel" 的部分
pattern = r'// 三关题库.*?\];\n\nlet currentLevel'
replacement = new_bank + '\n\nlet currentLevel'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 同时修改第二关描述：动词形式填空 → 动词形式选择
new_content = new_content.replace(
    '<div class="level-desc">动词形式填空 · 8题</div>',
    '<div class="level-desc">动词形式选择 · 8题</div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("替换完成")
print("检查：第二关描述是否已修改？", '动词形式选择' in new_content)
print("检查：是否还有 dumpling？", 'dumpling' in new_content)
print("检查：是否还有 hamburger（非burger）？", 'hamburger' in new_content and 'burgers' not in new_content)
print("检查：是否还有 rice？", 'rice' in new_content)
print("检查：是否还有 pizza？", 'pizza' in new_content)
print("检查：第二关 type 是 choice？", "title: '第二关：喜好大调查',\n    type: 'choice'" in new_content)

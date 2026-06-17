// Cloudflare Pages Function: TTS 中转
// GET /api/tts?text=teacher&type=0
// - 调有道词典 TTS 公开端点（国内免 key，单词级）
// - type=0 美音, type=1 英音
// - 返回 audio/mpeg，供前端 <audio> 播放

export async function onRequestGet(context) {
  const { request } = context;
  const url = new URL(request.url);
  const text = url.searchParams.get('text') || '';
  const type = url.searchParams.get('type') || '0';

  // 参数校验：单词（短字符串），有道不支持长句
  if (!text || text.length > 50) {
    return new Response(JSON.stringify({ error: 'text required, max 50 chars' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // type 校验
  const safeType = (type === '1') ? '1' : '0';

  const youdaoUrl = `https://dict.youdao.com/dictvoice?type=${safeType}&audio=${encodeURIComponent(text)}`;

  try {
    const resp = await fetch(youdaoUrl, {
      headers: {
        // 有道会校验 referer，模拟浏览器
        'Referer': 'https://dict.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      },
      cf: {
        // 缓存 24 小时，单词 TTS 不会变
        cacheTtl: 86400,
        cacheEverything: true
      }
    });

    if (!resp.ok) {
      return new Response(JSON.stringify({ error: `youdao ${resp.status}` }), {
        status: 502,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const audio = await resp.arrayBuffer();

    return new Response(audio, {
      status: 200,
      headers: {
        'Content-Type': 'audio/mpeg',
        'Content-Length': String(audio.byteLength),
        'Cache-Control': 'public, max-age=86400',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type'
      }
    });
  } catch (e) {
    return new Response(JSON.stringify({ error: e.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}

// 兼容 OPTIONS 预检
export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '86400'
    }
  });
}

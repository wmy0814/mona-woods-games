// Netlify Function: 接收前端 POST，转发到飞书 Open API 写入 base
// 部署在: https://mona-woods-games.netlify.app/.netlify/functions/sync
// 用法: POST JSON { nickname, classCode, gameName, currentLevel, score, wrongWords, lastUpdate }
// 鉴权: 简单固定 token（前端在请求头带 X-Api-Key，校验通过才转发飞书 API）

const FEISHU_APP_ID = process.env.LARK_APP_ID || 'cli_aaad75690d351cb3';
const FEISHU_APP_SECRET = process.env.FEISHU_APP_SECRET || 'h8HvIr0U2PwIYdBwpr3W2gBwePhXgRYq';
const BASE_TOKEN = 'F3oWbtQK8atcMdskYYdcA4RTnhg';
const TABLE_ID = 'tblPtsZ9cm6vdlOb';
const API_TOKEN = process.env.SYNC_API_TOKEN || 'pep-exam-2026';

// 字段映射：前端传入的 key -> 飞书 base 字段名
const FIELD_MAP = {
  nickname: '昵称',
  classCode: '班级',
  gameName: '游戏',
  currentLevel: '当前关',
  score: '通关分',
  wrongWords: '错词',
  lastUpdate: '更新时间'
};

// 允许的班级（防止垃圾数据）
const ALLOWED_CLASSES = ['PU1班', 'PU2班', 'PU3班', 'PU4班', 'NCE1班'];

// 缓存 token（避免每次请求都拿）
let cachedToken = null;
let cachedTokenExpire = 0;

async function getTenantAccessToken() {
  const now = Date.now();
  if (cachedToken && cachedTokenExpire > now + 60_000) {
    return cachedToken;
  }
  const resp = await fetch('https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ app_id: FEISHU_APP_ID, app_secret: FEISHU_APP_SECRET })
  });
  const data = await resp.json();
  if (data.code !== 0) {
    throw new Error('飞书 token 获取失败: ' + data.msg);
  }
  cachedToken = data.tenant_access_token;
  cachedTokenExpire = now + (data.expire - 120) * 1000;
  return cachedToken;
}

function buildFields(body) {
  const fields = {};
  for (const [key, target] of Object.entries(FIELD_MAP)) {
    if (body[key] === undefined || body[key] === null) continue;
    let value = body[key];
    if (key === 'currentLevel') value = String(value);
    if (key === 'classCode' && !ALLOWED_CLASSES.includes(value)) {
      throw new Error('非法班级: ' + value);
    }
    if (key === 'wrongWords' && typeof value === 'string' && value.length > 5000) {
      value = value.slice(0, 5000);
    }
    fields[target] = value;
  }
  return fields;
}

function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, X-Api-Key',
    'Access-Control-Max-Age': '86400',
    'Content-Type': 'application/json'
  };
}

exports.handler = async (event) => {
  // CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers: corsHeaders(), body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers: corsHeaders(),
      body: JSON.stringify({ ok: false, error: 'method_not_allowed' })
    };
  }

  // 鉴权
  const apiKey = event.headers['x-api-key'] || event.headers['X-Api-Key'];
  if (apiKey !== API_TOKEN) {
    return {
      statusCode: 401,
      headers: corsHeaders(),
      body: JSON.stringify({ ok: false, error: 'unauthorized' })
    };
  }

  // 解析 body
  let body;
  try {
    body = JSON.parse(event.body || '{}');
  } catch (e) {
    return {
      statusCode: 400,
      headers: corsHeaders(),
      body: JSON.stringify({ ok: false, error: 'invalid_json' })
    };
  }

  // 必填字段
  if (!body.nickname || !body.classCode || !body.gameName) {
    return {
      statusCode: 400,
      headers: corsHeaders(),
      body: JSON.stringify({ ok: false, error: 'missing_required', need: ['nickname', 'classCode', 'gameName'] })
    };
  }

  // 构造飞书 fields
  let fields;
  try {
    fields = buildFields(body);
  } catch (e) {
    return {
      statusCode: 400,
      headers: corsHeaders(),
      body: JSON.stringify({ ok: false, error: e.message })
    };
  }

  // 调飞书 Open API 写入
  try {
    const token = await getTenantAccessToken();
    const url = `https://open.feishu.cn/open-apis/base/v3/bases/${BASE_TOKEN}/tables/${TABLE_ID}/records`;
    const resp = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
      },
      body: JSON.stringify(fields)
    });
    const data = await resp.json();
    if (data.code !== 0) {
      return {
        statusCode: 502,
        headers: corsHeaders(),
        body: JSON.stringify({ ok: false, error: 'feishu_api_error', detail: data })
      };
    }
    return {
      statusCode: 200,
      headers: corsHeaders(),
      body: JSON.stringify({ ok: true, record_id: data.data?.record_id_list?.[0] })
    };
  } catch (e) {
    return {
      statusCode: 500,
      headers: corsHeaders(),
      body: JSON.stringify({ ok: false, error: 'internal', message: e.message })
    };
  }
};

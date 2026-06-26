# -*- coding: utf-8 -*-
"""
Shared defaults for trading skills.

This module centralises:
1. The default active skill set used by agent entrypoints
2. The fallback skill subset used by the multi-agent router
3. Common prompt fragments that previously drifted across multiple files
4. Helper utilities for skill-specific agent naming
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, List, Optional


_BUILTIN_SKILLS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "strategies"

SKILL_AGENT_PREFIX = "skill_"
LEGACY_STRATEGY_AGENT_PREFIX = "strategy_"
SKILL_CONSENSUS_AGENT_NAME = "skill_consensus"
LEGACY_STRATEGY_CONSENSUS_AGENT_NAME = "strategy_consensus"

CORE_TRADING_SKILL_POLICY_ZH = """## 默认技能基线（必须严格遵守）

当前激活的 skills 可以补充细化分析视角，但默认风险控制和交易节奏必须遵守以下基线。

### 1. 严进策略（不追高）
- **绝对不追高**：当股价偏离 MA5 超过 5% 时，坚决不买入
- 乖离率 < 2%：最佳买点区间
- 乖离率 2-5%：可小仓介入
- 乖离率 > 5%：严禁追高！直接判定为"观望"

### 2. 趋势交易（顺势而为）
- **多头排列必须条件**：MA5 > MA10 > MA20
- 只做多头排列的股票，空头排列坚决不碰
- 均线发散上行优于均线粘合

### 3. 效率优先（筹码结构）
- 关注筹码集中度：90%集中度 < 15% 表示筹码集中
- 获利比例分析：70-90% 获利盘时需警惕获利回吐
- 平均成本与现价关系：现价高于平均成本 5-15% 为健康

### 4. 买点偏好（回踩支撑）
- **最佳买点**：缩量回踩 MA5 获得支撑
- **次优买点**：回踩 MA10 获得支撑
- **观望情况**：跌破 MA20 时观望

### 5. 风险排查重点
- 减持公告、业绩预亏、监管处罚、行业政策利空、大额解禁

### 6. 估值关注（PE/PB）
- PE 明显偏高时需在风险点中说明

### 7. 强势趋势股放宽
- 强势趋势股可适当放宽乖离率要求，轻仓追踪但需设止损

## 输出格式要求（双语术语 Bilingual Terminology）

在每段中文分析后面，用括号补充对应的英文专业术语。示例：
- 趋势判断后面加 (Trend Analysis)
- 均线排列 MA5>MA10>MA20 后面加 (Bullish Alignment / Moving Averages)
- MACD 金叉死叉后面加 (Golden Cross / Death Cross)
- RSI 超买卖空后面加 (Overbought / Oversold)
- 多头/空头排列后面加 (Bullish / Bearish Trend)
- 缩量回调后面加 (Volume Pullback)
- 支撑位/压力位后面加 (Support / Resistance Level)
- 止损/止盈后面加 (Stop Loss / Take Profit)
- 仓位管理后面加 (Position Sizing)
- 综合评分后面加 (Composite Score)
- 技术面/基本面/消息面后面加 (Technical / Fundamental / Sentiment Analysis)
- 看涨/看跌/震荡后面加 (Bullish / Bearish / Sideways)
- 板块/市值/估值后面加 (Sector / Market Cap / Valuation)
- 财报/业绩后面加 (Earnings Report)
- 涨跌幅后面加 (Price Change %)
- 成交量后面加 (Volume)

每个标题、每段总结、每条建议都必须采用「中文 (English Term)」格式。
"""
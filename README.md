# AI Agent 架构演进与自我进化

> Harness 框架本质 · Self-Evolution 机制 · Multi-Agent 协作原理 · 中国 AI 生态分析

## 这是什么

一个面向 **AI Agent 产品设计与工程选型** 的知识型 Skill：把 Agent 的技术演进拆成可复用的三层模型（模型 = 大脑 / Harness = 手脚 / 真实世界 = 环境），并给出自我进化与多智能体协作的机制设计与决策框架。

## 核心内容

**三层架构认知**
- 模型层：智力来源，决定单轮上限
- Harness 层：工具、记忆、上下文管理——决定能力留存
- 真实世界层：验证闭环的最终裁判

**Self-Evolution 三阶段**：探索 → 压缩 → 固化（经验如何变成可复用资产）

**Multi-Agent 协作**：拓扑选择、信息流设计与过早终止判据

**中国 AI 生态分析**：Agent Infra 层创业机会识别、生态位判断

## 仓库结构

```
├── SKILL.md          # 技能入口：触发条件 + 完整知识体（573 行，YAML frontmatter）
├── QUICKREF.md       # 快速参考：核心概念速查表 + 决策树（281 行）
├── TEST.md           # 5 组测试案例：Harness 选型 / 自进化设计 / 多Agent拓扑（458 行）
├── README.md         # 本文件
├── LICENSE           # MIT
├── .harness/         # 校验子目录（config/router/memory/templates）
└── references/
    └── asset-metadata.json
```

## 典型用法

```yaml
# Harness 选型决策
输入: 团队规模、任务类型、现有工具链
输出: 三层拆解 + Harness 职责边界 + 选型建议

# Self-Evolution 机制设计
输入: 业务场景、经验来源、验证手段
输出: 探索-压缩-固化三阶段落地方案

# 多 Agent 拓扑设计
输入: 任务依赖关系、信息共享需求
输出: 协作拓扑 + 信息流设计 + 终止条件
```

## 适用场景

- Agent 产品设计：三层架构拆解、能力边界界定
- Harness 框架选型：职责划分、工具链评估
- Self-Evolution 机制设计：经验沉淀路径、验证闭环
- Multi-Agent 架构：协作拓扑、信息流、失败恢复
- 中国 AI 生态分析：Infra 层机会、生态位判断

## 许可证

MIT License

# StepFun Harness 本地记忆存储

## 存储结构

```
.harness/memory/
├── feedback.json      # 执行反馈记录
├── patterns.json      # 学习到的模式
└── optimization.json  # 优化策略
```

## 数据格式

### feedback.json
```json
{
  "version": "1.0.0",
  "entries": [
    {
      "timestamp": "2026-06-07T10:00:00Z",
      "task": {
        "user_input": "...",
        "task_type": "analysis|content|code|research|career",
        "complexity": "simple|medium|complex"
      },
      "execution": {
        "skills_used": ["skill1", "skill2"],
        "execution_steps": 5,
        "total_time": 45,
        "token_usage": 12000
      },
      "outcome": {
        "success": true,
        "quality_score": 0.9,
        "user_feedback": "..."
      }
    }
  ]
}
```

### patterns.json
```json
{
  "version": "1.0.0",
  "patterns": {
    "stock_analysis_excel": {
      "frequency": 15,
      "success_rate": 0.95,
      "avg_time": 35,
      "recommended_skills": ["stock-deep-analysis", "xlsx"]
    }
  }
}
```

### optimization.json
```json
{
  "version": "1.0.0",
  "routing_weights": {
    "stock-deep-analysis": 0.95,
    "xlsx": 0.98
  },
  "context_rules": {
    "max_skills_loaded": 5,
    "skill_description_max_length": 500
  }
}
```
